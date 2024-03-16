import os
import sys

# Add the directory of the bunTokenizer module to the sys.path
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_dir)

import unittest
from bunInterpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.interpreter = Interpreter()

    def test_num_literal(self):
        ast = {'Node Type': 'NumLiteral', 'Value': 5}
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 5)

    def test_binary_expr_addition(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '+',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 5},
                         {'Node Type': 'NumLiteral', 'Value': 3}]
        }
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 8)

    def test_binary_expr_subtraction(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '-',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 5},
                         {'Node Type': 'NumLiteral', 'Value': 3}]
        }
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 2)

    def test_binary_expr_multiplication(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '*',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 5},
                         {'Node Type': 'NumLiteral', 'Value': 3}]
        }
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 15)

    def test_binary_expr_division(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '/',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 6},
                         {'Node Type': 'NumLiteral', 'Value': 2}]
        }
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 3)

    def test_identifier_not_defined(self):
        ast = {'Node Type': 'Identifier', 'Name': 'x'}
        with self.assertRaises(RuntimeError):
            self.interpreter.interpret(ast)

    def test_assignment_and_identifier(self):
        ast_assign = {'Node Type': 'Assignment', 'Identifier': 'x', 'Value': {'Node Type': 'NumLiteral', 'Value': 10}}
        self.interpreter.interpret(ast_assign)
        ast_identifier = {'Node Type': 'Identifier', 'Name': 'x'}
        result = self.interpreter.interpret(ast_identifier)
        self.assertEqual(result, 10)

    def test_string_literal(self):
        ast = {'Node Type': 'StringLiteral', 'Value': 'hello'}
        result = self.interpreter.interpret(ast)
        self.assertEqual(result, 'hello')

    def test_division_by_zero(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '/',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 6},
                         {'Node Type': 'NumLiteral', 'Value': 0}]
        }
        with self.assertRaises(ZeroDivisionError):
            self.interpreter.interpret(ast)

    def test_unknown_operator(self):
        ast = {
            'Node Type': 'BinaryExpr',
            'Operation': '%',
            'Children': [{'Node Type': 'NumLiteral', 'Value': 6},
                         {'Node Type': 'NumLiteral', 'Value': 2}]
        }
        with self.assertRaises(RuntimeError):
            self.interpreter.interpret(ast)

if __name__ == '__main__':
    unittest.main()
