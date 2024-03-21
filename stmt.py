class Stmt:
    pass

class StmtVisitor:
    def visitExpression(self, stmt):
        pass
    
    def visitPrint(self, stmt):
        value = self.evaluate(stmt.expression)
        print(value)
    

    def visit(stmt):
        pass

class Expression(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitExpression(self)

class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitPrint(self)
    
class Var(Stmt):
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer
        
    def accept(self, visitor):
        return visitor.visitVarStmt(self)

class Block(Stmt):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitBlock(self)