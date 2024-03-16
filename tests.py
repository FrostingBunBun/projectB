import unittest
from bunTokenizer import tokenize  # Import your tokenizer function from your module

class TestTokenizer(unittest.TestCase):
    def test_basic_expression(self):
        input_string = "x = 10 + 20"
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', '='),
            ('NUMBER', '10'),
            ('PLUS', '+'),
            ('NUMBER', '20')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_complex_expression(self):
        input_string = "(5 * 3) - 2 / 2"
        expected_tokens = [
            ('LPAREN', '('),
            ('NUMBER', '5'),
            ('MULTIPLY', '*'),
            ('NUMBER', '3'),
            ('RPAREN', ')'),
            ('MINUS', '-'),
            ('NUMBER', '2'),
            ('DIVIDE', '/'),
            ('NUMBER', '2')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            tokenize("x = 10 + @")

    def test_whitespace_ignored(self):
        input_string = " x = 10 + 20 "
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', '='),
            ('NUMBER', '10'),
            ('PLUS', '+'),
            ('NUMBER', '20')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

if __name__ == '__main__':
    unittest.main()
