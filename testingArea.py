from scanner import Scanner
import Expr
from bunToken import Token
from tokenType import TokenType
from astPrinter import AstPrinter
from bunParser import Parser

test_code = """
-123 * -45.67
"""
scanner = Scanner(test_code)

tokens = scanner.scanTokens()

for token in tokens:
    print(token)

