class Interpreter:
    def __init__(self):
        self.variables = {}
        self.node_handlers = {
            'NumLiteral': self.handle_num_literal,
            'BinaryExpr': self.handle_binary_expr,
            'Identifier': self.handle_identifier,
            'Assignment': self.handle_assignment,
            'StringLiteral': self.handle_string_literal,
        }

    def interpret(self, ast):
        return self.visit(ast)

    def visit(self, node):
        if isinstance(node, str):
            return node
        elif isinstance(node, dict):
            node_type = node.get('Node Type')
            if node_type in self.node_handlers:
                return self.node_handlers[node_type](node)
            else:
                raise RuntimeError(f"Unknown node type: {node_type}")
        else:
            raise RuntimeError("Invalid AST node type")

    def handle_num_literal(self, node):
        return node.get('Value')

    def handle_binary_expr(self, node):
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

    def handle_identifier(self, node):
        name = node.get('Name')
        if name not in self.variables:
            raise RuntimeError(f"Variable '{name}' is not defined.")
        return self.variables[name]

    def handle_assignment(self, node):
        identifier = node.get('Identifier')
        value_node = node.get('Value')
        value = self.visit(value_node)
        self.variables[identifier] = value
        return None

    def handle_string_literal(self, node):
        return node.get('Value')  # Return the value of the StringLiteral node directly



# if __name__ == "__main__":
#     print("==========================")
#     from bunTokenizer import tokenize
#     from bunParser import parse
#     from bunInterpreter import Interpreter

#     # Sample input program
#     input_program = "x = 'niggers'"

#     print("\nINPUT:\n", input_program)

#     # Tokenize the input program
#     tokens = tokenize(input_program)
#     print("\ntokens:\n", tokens)

#     # Parse the tokens into an AST
#     ast = parse(tokens)
#     print("\nAST:\n", ast)

#     # Create an interpreter instance
#     interpreter = Interpreter()

#     # Interpret the AST
#     interpreter.interpret(ast)

#     # Print the value of variable x
#     print("\nVALUE:\n", interpreter.variables.get('x'))
