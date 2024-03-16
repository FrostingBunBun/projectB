from bunTokenizer import tokenize
from bunParser import parse

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        return self.visit(ast)

    def visit(self, node):
        if isinstance(node, str):
            return node
        elif isinstance(node, dict):
            node_type = node.get('Node Type')
            if node_type == 'NumLiteral':
                return node.get('Value')
            elif node_type == 'BinaryExpr':
                operator = node.get('Operation')
                left_result = float(self.visit(node.get('Children')[0]))
                right_result = float(self.visit(node.get('Children')[1]))
                if operator == '+':
                    return left_result + right_result
                elif operator == '-':
                    return left_result - right_result
                elif operator == '*':
                    return left_result * right_result
                elif operator == '/':
                    return left_result / right_result
                else:
                    raise RuntimeError(f"Unknown operator: {operator}")
            elif node_type == 'Identifier':
                name = node.get('Name')
                if name not in self.variables:
                    raise RuntimeError(f"Variable '{name}' is not defined.")
                return self.variables[name]
            elif node_type == 'Assignment':
                identifier = node.get('Identifier')  # Access the identifier from the assignment node
                value = self.visit(node.get('Value'))  # Visit the value node
                self.variables[identifier] = value  # Assign the value to the identifier
                return value
            else:
                raise RuntimeError(f"Unknown node type: {node_type}")
        else:
            raise RuntimeError("Invalid AST node type")


        



# tests
interpreter = Interpreter() 
def print_ast(node, indent=4):
    """
    Recursively print the abstract syntax tree with proper indentation.
    """
    if isinstance(node, dict):
        operation = node.get('Operation', '')
        if operation:
            print(" " * indent + "{'Node Type': '" + node['Node Type'] + "', 'Operation': '" + str(operation) + "', 'Children': [")
        else:
            print(" " * indent + "{'Node Type': '" + node['Node Type'] + "', 'Value': " + str(node.get('Value', '')) + "}")

        if 'Children' in node:
            for child in node['Children']:
                print_ast(child, indent + 4)
        print(" " * indent + "]}")
    else:
        print(" " * indent + str(node))

# expression = "test = 5"
# print("EXPRESSION: ", expression)
# tokens = tokenize(expression)
# ast = parse(tokens)
# print_ast(ast)

# result = interpreter.interpret(ast)
# print("RESULT: ", result)
        

