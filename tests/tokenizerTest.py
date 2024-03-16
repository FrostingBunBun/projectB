import os
import sys

# Add the directory of the bunTokenizer module to the sys.path
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_dir)

import unittest
from bunTokenizer import tokenize


class TestTokenizer(unittest.TestCase):
    def test_basic_expression(self):
        input_string = "x = 10 + 20"
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', '='),
            ('NUMBER', '10'),
            ('PLUS', '+'),
            ('NUMBER', '20'),
            ('EOF', '')
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
            ('NUMBER', '2'),
            ('EOF', '')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            tokenize("x = 10 + @EOF")

    def test_whitespace_ignored(self):
        input_string = " x = 10 + 20 "
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', '='),
            ('NUMBER', '10'),
            ('PLUS', '+'),
            ('NUMBER', '20'),
            ('EOF', '')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_identifier_starting_with_underscore(self):
        input_string = "_var = 5"
        expected_tokens = [
            ('IDENTIFIER', '_var'),
            ('ASSIGN', '='),
            ('NUMBER', '5'),
            ('EOF', '')
        ]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_empty_input_string(self):
        input_string = ""
        self.assertEqual(tokenize(input_string), [('EOF', '')])

    def test_single_number(self):
        input_string = "42"
        expected_tokens = [('NUMBER', '42'), ('EOF', '')]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_assignment_only(self):
        input_string = "="
        expected_tokens = [('ASSIGN', '='), ('EOF', '')]
        self.assertEqual(tokenize(input_string), expected_tokens)

    def test_single_identifier(self):
        input_string = "variable"
        expected_tokens = [('IDENTIFIER', 'variable'), ('EOF', '')]
        self.assertEqual(tokenize(input_string), expected_tokens)

if __name__ == '__main__':
    unittest.main()
