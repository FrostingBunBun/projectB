from Expr import Visitor
from tokenType import TokenType
from stmt import StmtVisitor
from enviroment import Environment
from punCallable import PunCallable
from punFunction import PunFunction
from _return import ReturnException


class Interpreter(Visitor, StmtVisitor):

    def __init__(self):
        self.globals = Environment()
        self.globals.define("clock", PunCallable())
        self.enviroment = self.globals

    

    def evaluate(self, expr):
        return expr.accept(self)
    
    def execute(self, stmt):
        if isinstance(stmt, list):
            for statement in stmt:
                self.execute(statement)
        else:
            stmt.accept(self)


    def executeBlock(self, statements, environment):
        previous = self.enviroment
        try:
            self.enviroment = environment

            for statement in statements:
                self.execute(statement)
        finally:
            self.enviroment = previous


    def visitBlockStmt(self, stmt):
        self.executeBlock(stmt.statements, Environment(self.enviroment))
        return None

    
    
    def visitExpressionStmt(self, stmt):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))
        return None
    
    def visitFunctionStmt(self, stmt):
        function = PunFunction(stmt, self.enviroment)
        self.enviroment.define(stmt.name.lexeme, function)
        return None

    
    def visitIfExpr(self, stmt):
        if self.isTruthy(self.evaluate(stmt.condition)):
            self.execute(stmt.thenBranch)
        elif stmt.elseBranch is not None:
            self.execute(stmt.elseBranch)
        return None

    
    def visitPrintStmt(self, stmt):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))
        return None
    
    def visitReturnStmt(self, stmt):
        value = None
        if stmt.value is not None:
            value = self.evaluate(stmt.value)

        raise ReturnException(value)

    
    # def visitVarStmt(self, stmt):
    #     value = None
    #     # if stmt.initializer is not None:
    #     value = self.evaluate(stmt.initializer)

    #     self.enviroment.define(stmt.name.lexeme, value)
    #     return None

    def visitVarStmt(self, stmt):
        if stmt.initializer is not None:
            value = self.evaluate(stmt.initializer)
        else:
            value = None  # Set value to None if no initializer is provided

        self.enviroment.define(stmt.name.lexeme, value)
        return None


    def visitWhileStmt(self, stmt):
        while self.isTruthy(self.evaluate(stmt.condition)):
            self.execute(stmt.body)
        
        return None


    
    # def visitAssignExpr(self, expr):
    #     value = self.evaluate(expr.value)
    #     self.enviroment.assign(expr.name, value)
    #     return value

    def visitAssignExpr(self, expr):
        value = self.evaluate(expr.value)
        self.enviroment.assign(expr.name.lexeme, value)  # Update the environment with the new value
        return value
    
    
    # @staticmethod
    # def isTruthy(obj):
    #     if obj is None:
    #         return False
    #     if isinstance(obj, bool):
    #         return obj
    #     return True

    @staticmethod
    def isTruthy(obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return obj
        return True

    @staticmethod
    def isEqual(object1, object2):
        if object1 is None and object2 is None:
            return True
        if object1 is None:
            return False
        return object1 == object2

    @staticmethod
    def stringify(object):
        if object is None:
            return "nil"
        if isinstance(object, (float, int)):
            text = str(object)
            if text.endswith(".0"):
                text = text[:-2]
            return text
        return str(object)


    @staticmethod
    def checkNumberOperands(operator, left, right):
        if isinstance(left, (float, int)) and isinstance(right, (float, int)):
            return
        raise RuntimeError(operator, "Operands must be numbers.")

    def visitLiteralExpr(self, expr):
        return expr.value
    
    def visitLogicalExpr(self, expr):
        left = self.evaluate(expr.left)

        if expr.operator.token_type == TokenType.OR:
            if self.isTruthy(left):
                return left
        else:
            if not self.isTruthy(left):
                return left

        return self.evaluate(expr.right)



    def visitGroupingExpr(self, expr):
        return self.evaluate(expr.expression)
    
    @staticmethod
    def checkNumberOperand(operator, operand):
        if isinstance(operand, (float, int)):
            return
        raise RuntimeError(operator, "Operand must be a number.")

    def visitUnaryExpr(self, expr):
        right = self.evaluate(expr.right)
        # print("Unary Expr - Operator:", expr.operator.token_type)
        # print("Unary Expr - Right:", right)

        if expr.operator.token_type == TokenType.MINUS:
            self.checkNumberOperand(expr.operator.token_type, right)
            return -float(right)
        elif expr.operator.token_type == TokenType.BANG:
            return not self.isTruthy(right)

        # Unreachable.
        return None
    
    def visitVariableExpr(self, expr):
        return self.enviroment.get(expr.name)

    def visitBinaryExpr(self, expr):

        
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

       
        # print("Unary Expr - Left:", left)
        # print("Unary Expr - Right:", right)
        # print("\n")
        # print("Unary Expr - Operator:", expr.operator)
        # print("TEST: ", TokenType.PLUS)
        # print("OPERATOR type: ", expr.operator.token_type)

        # print("ACTUAL1: ", type(TokenType.PLUS))
        # print("ACTUAL2: ", type(expr.operator))
        # print("ACTUAL2: ", type(expr.operator.token_type))
        # print("\n")
        

        if expr.operator.token_type == TokenType.MINUS:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) - float(right)
        elif expr.operator.token_type == TokenType.SLASH:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            if right == 0:
                raise RuntimeError(expr.operator.token_type, "Division by zero")
            return float(left) / float(right)
        elif expr.operator.token_type == TokenType.STAR:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) * float(right)
        
        elif expr.operator.token_type == TokenType.PLUS:
            if isinstance(left, (float, int)) and isinstance(right, (float, int)) or isinstance(left, int) and isinstance(right, int):
                return float(left) + float(right)
            if isinstance(left, str) and isinstance(right, str):
                return str(left) + str(right)
            raise RuntimeError(expr.operator.token_type, "Operands must be two numbers or two strings.")
        
        elif expr.operator.token_type == TokenType.GREATER:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) > float(right)
        elif expr.operator.token_type == TokenType.GREATER_EQUAL:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) >= float(right)
        elif expr.operator.token_type == TokenType.LESS:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) < float(right)
        elif expr.operator.token_type == TokenType.LESS_EQUAL:
            self.checkNumberOperands(expr.operator.token_type, left, right)
            return float(left) <= float(right)
        elif expr.operator.token_type == TokenType.BANG_EQUAL:
            return not self.isEqual(left, right)
        elif expr.operator.token_type == TokenType.EQUAL_EQUAL:
            return self.isEqual(left, right)
    
        # Unreachable.
        return None
    

    def visitCallExpr(self, expr):

        callee = self.evaluate(expr.callee)
        arguments = [self.evaluate(argument) for argument in expr.arguments] # faaaancy

        if not isinstance(callee, PunCallable):
            raise RuntimeError(f"Can only call functions and classes at line {expr.paren.line}.")
        function = callee

        if len(arguments) != function.arity():
            raise RuntimeError(f"Expected {function.arity()} arguments but got {len(arguments)} at line {expr.paren.line}.")

        return function.call(self, arguments)

    

    



    def interpret(self, statements):
        try:
            for statement in statements:
                self.execute(statement)
        except RuntimeError as error:
            print(error)
