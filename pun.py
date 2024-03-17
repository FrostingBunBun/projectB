import sys

class Pun:

    had_error = False
    
    @staticmethod
    def main(args):
        if len(args) > 1:
            print("Usage: python pun.py [script]")
            sys.exit(64)
        elif len(args) == 1:
            Pun.run_file(args[0])
        else:
            Pun.run_prompt()

    @staticmethod
    def run_file(path):
        with open(path, 'r') as file:
            source = file.read()
        if Pun.had_error:
            sys.exit(65)
        Pun.run(source)

    @staticmethod
    def run_prompt():
        while True:
            try:
                line = input("> ")
                Pun.run(line)
                Pun.had_error = False
            except EOFError:
                break

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
    
        # For now, just print the tokens.
        for token in tokens:
            print(token)

    @staticmethod
    def error(line, message):
        Pun.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print("[line " + str(line) + "] Error" + where + ": " + message, file=sys.stderr)
        Pun.had_error = True


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []

    def scan_tokens(self):
        # Tokenization logic
        pass

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

if __name__ == "__main__":
    Pun.main(sys.argv)
