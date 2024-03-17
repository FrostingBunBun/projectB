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


