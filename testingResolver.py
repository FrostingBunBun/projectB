from interpreter import Interpreter
from Expr import Variable, Literal
from stmt import Var, Print, Block
from bunToken import Token
from resolver import Resolver

# Mock class for Interpreter
class MockInterpreter:
    def resolve(self, expr, scope_distance):
        print(f"Resolved {expr} at scope distance {scope_distance}")

# Create a mock interpreter
interpreter = MockInterpreter()

# Create a resolver instance
resolver = Resolver(interpreter)

# Create statements for testing
stmt1 = Var(Token("IDENTIFIER", "x", None, 1), None)
stmt2 = Print(Literal(5))
stmt3 = Var(Token("IDENTIFIER", "y", None, 2), None)
stmt4 = Block([stmt1, stmt2, stmt3])

# Resolve the statements
resolver.resolve([stmt4])

# Expected output:
# Resolved Variable(Token(IDENTIFIER, 'x', None, 1)) at scope distance 0
# Resolved Literal: 5 at scope distance 0
# Resolved Variable(Token(IDENTIFIER, 'y', None, 2)) at scope distance 0
