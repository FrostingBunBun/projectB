import Expr
from bunToken import Token
from tokenType import TokenType

class AstPrinter:
    def print(self, expr):
        return expr.accept(self)

    def visitBinaryExpr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr):
        return self.parenthesize("group", expr.expression)

    def visitLiteralExpr(self, expr):
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visitUnaryExpr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        result = f"({name}"
        for expr in exprs:
            result += " "
            result += expr.accept(self)
        result += ")"
        return result

# if __name__ == "__main__":
#     expression = Expr.Binary(
#         Expr.Unary(
#             Token(TokenType.MINUS, "-", None, 1),
#             Expr.Literal(123)),
#         Token(TokenType.STAR, "*", None, 1),
#         Expr.Grouping(
#             Expr.Literal(45.67)))

#     print(AstPrinter().print(expression))
