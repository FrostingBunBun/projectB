import re

# Define token types using regular expressions
token_regex = [
    ('NUMBER', r'\d+(\.\d+)?'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('DATATYPE', r'int|float|char|bool'),  # Data types
    ('EOF', r'$'),  # End of file token
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifier token
    ('ASSIGN', r'='),  # Assignment operator
]

# Tokenize input string
def tokenize(input_string):
    tokens = []
    while input_string:
        matched = False
        for token_type, regex_pattern in token_regex:
            match = re.match(regex_pattern, input_string)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                input_string = input_string[match.end():].strip()
                matched = True
                break
        if not matched:
            raise ValueError('Invalid character: ' + input_string[0])
    tokens.append(('EOF', ''))  # Add EOF token at the end
    return tokens
