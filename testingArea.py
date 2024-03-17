from scanner import Scanner
import Expr
from bunToken import Token
from tokenType import TokenType
from astPrinter import AstPrinter
from bunParser import Parser

test_code = """
// Sample test code
var x = 10;
print("Hello, world!");
// testing
if (x > 5) {
    print("Value is greater than five.");
} else if (x == 5) {
    print("Value is exactly five.");
"""
scanner = Scanner(test_code)

tokens = scanner.scanTokens()

for token in tokens:
    print(token)



# Example input tokens
# tokens = [
#     Token(TokenType.NUMBER, "3"),
#     Token(TokenType.PLUS, "+"),
#     Token(TokenType.NUMBER, "4"),
#     Token(TokenType.STAR, "*"),
#     Token(TokenType.NUMBER, "2"),
#     Token(TokenType.EOF, "")
# ]

# # Create a parser instance
# parser = Parser(tokens)

# # Parse the input
# syntax_tree = parser.expression()

# # Print the syntax tree
# print(syntax_tree)
