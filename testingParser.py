from tokenType import TokenType
from bunToken import Token
from Expr import Expr
from bunParser import Parser

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
    # Dummy function to tokenize the input expression
    # Replace it with your actual tokenization logic
    # For simplicity, we assume the input expression is already tokenized
    return [Token(TokenType.NUMBER, "5", 5, 1),
            Token(TokenType.PLUS, "+", None, 1),
            Token(TokenType.NUMBER, "3", 3, 1),
            Token(TokenType.EOF, "", None, 1)]

# Test cases
# test_parser("5 + 3")
# test_parser("5 * (3 - 2) / 4")
# test_parser("3 > 2")
# test_parser("true != false")
# test_parser("-5")
# test_parser("3 * (2 + 4)")
# test_parser("5 + 3 * (7 - 2) == 20")
# test_parser("5 *+")  # Invalid expression
# test_parser("")
test_parser("true and nil")