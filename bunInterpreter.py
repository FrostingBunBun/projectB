class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        return self.visit(ast)

    def visit(self, node):
        node_type = node['Node Type']
        if node_type == 'NumLiteral':
            return node['Value']
        elif node_type == 'BinaryExpr':
            operator = node['Operation']
            left_result = self.visit(node['Children'][0])
            right_result = self.visit(node['Children'][1])
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
            name = node['Name']
            if name not in self.variables:
                raise RuntimeError(f"Variable '{name}' is not defined.")
            return self.variables[name]
        elif node_type == 'Assignment':
            name = node['Name']
            value = self.visit(node['Value'])
            self.variables[name] = value
            return value
        else:
            raise RuntimeError(f"Unknown node type: {node_type}")