from typing import List, Dict
from interpreter import Interpreter
from Expr import Expr, Visitor, Variable, Assign, Function, Binary, Call, Grouping, Literal, Logical, If, Unary
from stmt import Stmt, StmtVisitor, Block, Var, Expression, Print, Return, While
from bunToken import Token


class Resolver(Visitor, StmtVisitor):
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter
        self.scopes: List[Dict[str, bool]] = []

    def visitBlockStmt(self, stmt: Block):
        self.beginScope()
        self.resolve(stmt.statements)
        self.endScope()
        return None

    def resolve(self, statements):
        if isinstance(statements, list):
            for statement in statements:
                self.resolve(statement)
        else:
            statements.accept(self)

    def beginScope(self):
        self.scopes.append({})

    def endScope(self):
        self.scopes.pop()

    def declare(self, name: Token):
        if not self.scopes:
            return
        scope = self.scopes[-1]
        scope[name.lexeme] = False

    def define(self, name: Token):
        if not self.scopes:
            return
        self.scopes[-1][name.lexeme] = True

    def visitVarStmt(self, stmt: Var):
        self.declare(stmt.name)
        if stmt.initializer:
            self.resolve(stmt.initializer)
        self.define(stmt.name)
        return None

    def visitVariableExpr(self, expr: Variable):
        if self.scopes and expr.name.lexeme in self.scopes[-1] and not self.scopes[-1][expr.name.lexeme]:
            raise RuntimeError(expr.name, "Can't read local variable in its own initializer.")
        self.resolveLocal(expr, expr.name)
        return None

    def resolveLocal(self, expr: Expr, name: Token):
        for i in range(len(self.scopes) - 1, -1, -1):
            if name.lexeme in self.scopes[i]:
                self.interpreter.resolve(expr, len(self.scopes) - 1 - i)
                return

    def visitAssignExpr(self, expr: Assign):
        self.resolve(expr.value)
        self.resolveLocal(expr, expr.name)
        return None

    def visitFunctionStmt(self, stmt: Function):
        self.declare(stmt.name)
        self.define(stmt.name)
        self.resolveFunction(stmt)
        return None

    def resolveFunction(self, function: Function):
        self.beginScope()
        for param in function.params:
            self.declare(param)
            self.define(param)
        self.resolve(function.body)
        self.endScope()

    def visitExpressionStmt(self, stmt: Expression):
        self.resolve(stmt.expression)
        return None

    def visitIfStmt(self, stmt: If):
        self.resolve(stmt.condition)
        self.resolve(stmt.thenBranch)
        if stmt.elseBranch:
            self.resolve(stmt.elseBranch)
        return None

    def visitPrintStmt(self, stmt: Print):
        self.resolve(stmt.expression)
        return None

    def visitReturnStmt(self, stmt: Return):
        if stmt.value:
            self.resolve(stmt.value)
        return None

    def visitWhileStmt(self, stmt: While):
        self.resolve(stmt.condition)
        self.resolve(stmt.body)
        return None

    def visitBinaryExpr(self, expr: Binary):
        self.resolve(expr.left)
        self.resolve(expr.right)
        return None

    def visitCallExpr(self, expr: Call):
        self.resolve(expr.callee)
        for argument in expr.arguments:
            self.resolve(argument)
        return None

    def visitGroupingExpr(self, expr: Grouping):
        self.resolve(expr.expression)
        return None

    def visitLiteralExpr(self, expr: Literal):
        return None

    def visitLogicalExpr(self, expr: Logical):
        self.resolve(expr.left)
        self.resolve(expr.right)
        return None

    def visitUnaryExpr(self, expr: Unary):
        self.resolve(expr.right)
        return None
