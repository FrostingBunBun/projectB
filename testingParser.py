from tokenType import TokenType
from bunToken import Token
from bunParser import Parser
from scanner import Scanner
print("======================")



def test_parser(input_expr):
    # Tokenize the input expression
    tokens = tokenize(input_expr)
    
    # Create a parser instance
    parser = Parser(tokens)
    
    # Parse the expression
    parsed_expr = parser.parse()
    
    # Print the result of parsing
    if parsed_expr:
        print(f"Input: {input_expr}")
        print(f"Parsed Expression: {parsed_expr}")
        print()
    else:
        print(f"Input: {input_expr}")
        print("Parsing failed.")
        print()

def tokenize(input_expr):

    scanner = Scanner(input_expr)
    print(f"SCANNER:\n{scanner}")
    tokens = scanner.scanTokens()
    print(f"TOKENS:\n{tokens}")
    return tokens

# Test cases

# test_parser("5 * (3 - 2) / 4")
test_parser("-123 * -45.67")
print("============")
# test_parser("1- 10;")
