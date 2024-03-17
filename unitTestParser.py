from bunToken import Token
from tokenType import TokenType
from Expr import Expr
from bunParser import Parser

# Test for the expression method
def test_expression():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.PLUS, "+", None, 1),
              Token(TokenType.NUMBER, "3", 3, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.expression()
    assert isinstance(result, Expr)
    print("Expression method test passed.")

# Test for the equality method
def test_equality():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.EQUAL_EQUAL, "==", None, 1),
              Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.equality()
    assert isinstance(result, Expr)
    print("Equality method test passed.")

# Test for the comparison method
def test_comparison():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.GREATER, ">", None, 1),
              Token(TokenType.NUMBER, "3", 3, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.comparison()
    assert isinstance(result, Expr)
    print("Comparison method test passed.")

# Test for the term method
def test_term():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.PLUS, "+", None, 1),
              Token(TokenType.NUMBER, "3", 3, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.term()
    assert isinstance(result, Expr)
    print("Term method test passed.")

# Test for the factor method
def test_factor():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.STAR, "*", None, 1),
              Token(TokenType.NUMBER, "3", 3, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.factor()
    assert isinstance(result, Expr)
    print("Factor method test passed.")

# Test for the unary method
def test_unary():
    tokens = [Token(TokenType.MINUS, "-", None, 1),
              Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.unary()
    assert isinstance(result, Expr)
    print("Unary method test passed.")

# Test for the primary method
def test_primary():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    result = parser.primary()
    assert isinstance(result, Expr)
    print("Primary method test passed.")



# Test for the error method
def test_error():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    try:
        parser.error(tokens[0], "Test error")
    except Parser.ParseError:
        print("Error method test passed.")
        return
    assert False, "Error method test failed."

# Test for the synchronize method
def test_synchronize():
    tokens = [Token(TokenType.NUMBER, "5", 5, 1),
              Token(TokenType.SEMICOLON, ";", None, 1),
              Token(TokenType.NUMBER, "10", 10, 1),
              Token(TokenType.EOF, "", None, 1)]
    parser = Parser(tokens)
    parser.synchronize()
    assert parser.peek().type == TokenType.NUMBER
    print("Synchronize method test passed.")

# Main test function to run all tests
def test_all():
    test_expression()
    test_equality()
    test_comparison()
    test_term()
    test_factor()
    test_unary()
    test_primary()

    test_error()
    test_synchronize()

if __name__ == "__main__":
    test_all()
