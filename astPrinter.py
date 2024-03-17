from Expr import Binary, Unary, Literal, Grouping, Visitor
from bunToken import Token
from tokenType import TokenType

class AstPrinter(Visitor):
    def print(self, expr):
        return expr.accept(self)

    def visitBinaryExpr(self, expr_instance):
        return self.parenthesize(expr_instance.operator.lexeme, expr_instance.left, expr_instance.right)

    def visitGroupingExpr(self, expr_instance):
        return self.parenthesize('group', expr_instance.expression);

    def visitLiteralExpr(self, expr_instance):
        if expr_instance.value == None:
            return 'nil'
        else:
            return str(expr_instance.value)

    def visitUnaryExpr(self, expr_instance):
        return self.parenthesize(expr_instance.operator, expr_instance.right)

    def parenthesize(self, name, *expressions):
        output = ''
        output += f'({name}'
        for expression in expressions:
            output += ' '
            output += expression.accept(self)
        output += ')'

        return output
    
    
# if __name__ == "__main__":
#     expression = Binary(
#         Unary(
#             Token(TokenType.MINUS, "-", None, 1),
#             Literal(123)),
#         Token(TokenType.STAR, "*", None, 1),
#         Grouping(
#             Literal(45.67)))

#     print(AstPrinter().print(expression))
