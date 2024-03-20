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
