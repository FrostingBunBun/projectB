import unittest
from Expr import Literal, Unary, Binary
from tokenType import TokenType
from interpreter import Interpreter
from bunToken import Token

class TestInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = Interpreter()
        
    def test_addition(self):
        expression = Binary(
            Literal(5),
            Token(TokenType.PLUS, "+", None, 1),
            Literal(7)
        )
        self.assertEqual(self.interpreter.evaluate(expression), 12)
    
    def test_subtraction(self):
        expression = Binary(
            Literal(10),
            Token(TokenType.MINUS, "-", None, 1),
            Literal(7)
        )
        self.assertEqual(self.interpreter.evaluate(expression), 3)
    
    def test_multiplication(self):
        expression = Binary(
            Literal(5),
            Token(TokenType.STAR, "*", None, 1),
            Literal(7)
        )
        self.assertEqual(self.interpreter.evaluate(expression), 35)
    
    def test_division(self):
        expression = Binary(
            Literal(20),
            Token(TokenType.SLASH, "/", None, 1),
            Literal(5)
        )
        self.assertEqual(self.interpreter.evaluate(expression), 4)
    
    def test_negative_number(self):
        expression = Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(10)
        )
        self.assertEqual(self.interpreter.evaluate(expression), -10)
    
    def test_negative_result(self):
        expression = Binary(
            Literal(5),
            Token(TokenType.MINUS, "-", None, 1),
            Literal(10)
        )
        self.assertEqual(self.interpreter.evaluate(expression), -5)
    
    def test_boolean_operators(self):
        expression = Unary(
            Token(TokenType.BANG, "!", None, 1),
            Literal(True)
        )
        self.assertEqual(self.interpreter.evaluate(expression), False)
    
    def test_string_concatenation(self):
        expression = Binary(
            Literal("hello"),
            Token(TokenType.PLUS, "+", None, 1),
            Literal(" world")
        )
        self.assertEqual(self.interpreter.evaluate(expression), "hello world")
    
    def test_invalid_operation(self):
        expression = Binary(
            Literal("hello"),
            Token(TokenType.PLUS, "+", None, 1),
            Literal(10)
        )
        with self.assertRaises(RuntimeError):
            self.interpreter.evaluate(expression)
    
    def test_invalid_unary_operation(self):
        expression = Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal("hello")
        )
        with self.assertRaises(RuntimeError):
            self.interpreter.evaluate(expression)
    
    def test_divide_by_zero(self):
        expression = Binary(
            Literal(5),
            Token(TokenType.SLASH, "/", None, 1),
            Literal(0)
        )
        with self.assertRaises(RuntimeError):
            self.interpreter.evaluate(expression)

    def test_complex_expression(self):
        # Test a complex expression involving multiple operations
        expression = Binary(
            Literal(5),
            Token(TokenType.PLUS, "+", None, 1),
            Unary(
                Token(TokenType.MINUS, "-", None, 1),
                Binary(
                    Literal(10),
                    Token(TokenType.STAR, "*", None, 1),
                    Literal(2)
                )
            )
        )
        self.assertEqual(self.interpreter.evaluate(expression), -15)

    def test_chained_operations(self):
        # Test chained operations (e.g., 5 + 3 - 2 * 4)
        expression = Binary(
            Binary(
                Literal(5),
                Token(TokenType.PLUS, "+", None, 1),
                Literal(3)
            ),
            Token(TokenType.MINUS, "-", None, 1),
            Binary(
                Literal(2),
                Token(TokenType.STAR, "*", None, 1),
                Literal(4)
            )
        )
        self.assertEqual(self.interpreter.evaluate(expression), 0)

    def test_mixed_types(self):
        # Test expressions with mixed data types (e.g., 5 + "hello")
        expression = Binary(
            Literal(5),
            Token(TokenType.PLUS, "+", None, 1),
            Literal("hello")
        )
        with self.assertRaises(RuntimeError):
            self.interpreter.evaluate(expression)

    def test_empty_expression(self):
        # Test an empty expression
        expression = Literal(None)
        self.assertIsNone(self.interpreter.evaluate(expression))

    def test_grouping_expression(self):
        expression = Binary(
            Unary(
                Token(TokenType.MINUS, "-", None, 1),
                Literal(10)
            ),
            Token(TokenType.STAR, "*", None, 1),
            Unary(
                Token(TokenType.MINUS, "-", None, 1),
                Literal(2)
            )
        )
        self.assertEqual(self.interpreter.evaluate(expression), 20)


if __name__ == '__main__':
    unittest.main()
