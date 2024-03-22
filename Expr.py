class Expr:
    def __str__(self):
        return "Generic Expr"
    
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class Visitor:
    def visitBinaryExpr(self, expr):
        pass

    def visitGroupingExpr(self, expr):
        pass

    def visitLiteralExpr(self, expr):
        pass

    def visitUnaryExpr(self, expr):
        pass

class Binary(Expr):
    def __str__(self):
        return f"Binary Expr: {self.left} {self.operator} {self.right}"
    
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinaryExpr(self)
    
class Assign(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Assign Expr: {self.name.lexeme} = {self.value}"

    def accept(self, visitor):
        return visitor.visitAssignExpr(self)
    
class Grouping(Expr):
    def __str__(self):
        return f"Grouping Expr: {self.expression}"
    
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitGroupingExpr(self)

class Literal(Expr):
    def __str__(self):
        return f"Literal: {self.value}"
    
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitLiteralExpr(self)

class Unary(Expr):
    def __str__(self):
        return f"Unary Expr: {self.operator} {self.right}"
    
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visitUnaryExpr(self)
    
class Variable(Expr):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        """ Create a accept method that calls the visitor. """
        return visitor.visitVariableExpr(self)
    
class If(Expr):
    def __init__(self, condition, thenBranch, elseBranch):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

    def __str__(self):
        return f"If: {self.condition}, {self.thenBranch}, {self.elseBranch}"

    def accept(self, visitor):
        return visitor.visitIfExpr(self)
    
class Logical(Expr):
        def __init__(self, left, operator, right):
            self.left = left
            self.operator = operator
            self.right = right

        def accept(self, visitor):
            return visitor.visitLogicalExpr(self)
        
class Call(Expr):
    def __init__(self, callee, paren, arguments):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

    def accept(self, visitor):
        return visitor.visitCallExpr(self)
    
class Function:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def accept(self, visitor):
        return visitor.visitFunctionStmt(self)

    def __str__(self):
        return f"<fn {self.name.lexeme}>"
