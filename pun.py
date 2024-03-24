import sys
import os
from scanner import Scanner
from bunParser import Parser
from astPrinter import AstPrinter
from tokenType import TokenType
from interpreter import Interpreter
from resolver import Resolver

class Pun:

    interpreter = Interpreter()

    __slots__ = ('had_error')

    hadRuntimeError = False

    def __init__(self):
        self.had_error = False

    def error(self, token, message):
        if token.token_type == TokenType.EOF:
            self.report_error(token.line, " at end", message)
        else:
            self.report_error(token.line, f" at '{token.lexeme}'", message)

    def runtimeError(self, error):
        print(error.message)
        print(f"\n[line {error.token.line}]")
        self.hadRuntimeError = True


    def run_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.run(f.read())
            if self.had_error:
                SystemExit(65)
            if self.hadRuntimeError:
                sys.exit(70)
        else:
            print('File does not exist')

    def run(self, line):
        scanner = Scanner(line)
        # print(f"SCANNER: \n{scanner}")
        tokens = scanner.scanTokens()
        # print(f"TOKENS: \n{tokens}")
        parser = Parser(tokens)
        # print(f"PARSER: \n{parser}")
        statements = parser.parse()
        # print("EXPRESSIONS: ", statements)
        if self.had_error:
            return
        
        resolver = Resolver(self.interpreter)
        # resolver.resolve(statements) ??????????????????????????????????

        self.interpreter.interpret(statements)
        # print(AstPrinter().print(expression))
        

    def run_prompt(self):
        line = input('> ')
        while (len(line) > 0 and line != None and line != TokenType.EOF):
        # while (len(line) > 0 and line != None):
            self.run(line)
            line = input('> ')

    def report_error(self, line, where, message):
        print(f"line {line} Error{where}: {message}")
        self.had_error = True

if __name__ == '__main__':
    pun = Pun()

    if len(sys.argv) > 2:
        print('Usage: python3 pun.py [script]')
    elif len(sys.argv) == 2:
        pun.run_file(sys.argv[1])
        if pun.had_error:
            sys.exit(65)
    else:
        pun.run_prompt()
        pun.had_error = False