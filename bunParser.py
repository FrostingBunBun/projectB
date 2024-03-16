class Node:
    def __init__(self, node_type, **kwargs):
        self.node_type = node_type
        self.attributes = kwargs
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def to_json(self):
        json_dict = {"Node Type": self.node_type}
        if self.attributes:
            json_dict.update(self.attributes)
        if self.children:
            json_dict["Children"] = [child.to_json() for child in self.children]  # Convert child nodes to JSON
        return json_dict


class NumberNode(Node):
    pass


class StringNode(Node):
    pass


class IdentifierNode(Node):
    pass


class VariableNode(Node):
    pass


class BinaryOperationNode(Node):
    pass


class AssignmentNode(Node):
    def to_json(self):
        json_dict = super().to_json()  # Call the parent class method to get the base JSON
        # Convert the Value field to JSON if it's a Node instance
        if isinstance(self.attributes['Value'], Node):
            json_dict['Value'] = self.attributes['Value'].to_json()
        return json_dict
        



def parse_assignment(tokens):
    identifier = parse_factor(tokens)  # Get the left-hand side identifier
    if tokens.pop(0)[0] != 'ASSIGN':  # Consume the '=' token
        raise SyntaxError("Expected '='")
    value = parse_expression(tokens)  # Get the right-hand side expression
    return AssignmentNode("Assignment", Identifier=_get_token_text(identifier), Value=value)


def parse_factor(tokens):
    if tokens[0][0] == 'NUMBER':
        return NumberNode("NumLiteral", Value=float(tokens.pop(0)[1]))  # Consume and return the number token
    elif tokens[0][0] == 'STRING':
        return StringNode("StringLiteral", Value=tokens.pop(0)[1])  # Consume and return the string token
    elif tokens[0][0] == 'IDENTIFIER':
        return IdentifierNode("Identifier", Name=tokens.pop(0)[1])  # Consume and return the identifier token
    elif tokens[0][0] == 'VARIABLE':
        return VariableNode("Variable", Name=tokens.pop(0)[1])  # Consume and return the variable token
    elif tokens[0][0] == 'LPAREN':
        tokens.pop(0)  # Consume the left parenthesis token
        expression = parse_expression(tokens)
        if tokens.pop(0)[0] != 'RPAREN':
            raise SyntaxError('Expected closing parenthesis')
        return expression
    else:
        raise SyntaxError('Expected number, string, identifier, variable, or left parenthesis')


def parse_term(tokens):
    left = parse_factor(tokens)
    while tokens and tokens[0][0] in ('MULTIPLY', 'DIVIDE'):
        operator = tokens.pop(0)[1]  # Consume the operator token
        right = parse_factor(tokens)
        binary_node = BinaryOperationNode("BinaryExpr", Operation=operator)
        binary_node.add_child(left)
        binary_node.add_child(right)
        left = binary_node
    return left


def parse_expression(tokens):
    if tokens[0][0] == 'IDENTIFIER' and len(tokens) > 1 and tokens[1][0] == 'ASSIGN':
        return parse_assignment(tokens)  # Parse assignment if '=' follows an identifier
    else:
        left = parse_term(tokens)
        while tokens and tokens[0][0] in ('PLUS', 'MINUS'):
            operator = tokens.pop(0)[1]  # Consume the operator token
            right = parse_term(tokens)
            binary_node = BinaryOperationNode("BinaryExpr", Operation=operator)
            binary_node.add_child(left)
            binary_node.add_child(right)
            left = binary_node
        return left


def _get_token_text(node):
    if isinstance(node, NumberNode):
        return node.attributes['Value']  # Access the 'Value' attribute of the NumberNode
    elif isinstance(node, StringNode):
        return node.attributes['Value']  # Access the 'Value' attribute of the StringNode
    elif isinstance(node, IdentifierNode):
        return node.attributes['Name']  # Access the 'Name' attribute of the IdentifierNode
    elif isinstance(node, VariableNode):
        return node.attributes['Name']  # Access the 'Name' attribute of the VariableNode
    else:
        raise ValueError("Unsupported node type")


def parse(tokens):
    return parse_expression(tokens).to_json()



# # TESTS

# # Define your tokens representing expressions or assignments
# tokens = [
#     ('IDENTIFIER', 'x'),
#     ('ASSIGN', '='),
#     ('NUMBER', '10'),
#     ('PLUS', '+'),
#     ('NUMBER', '5'),
#     ('MULTIPLY', '*'),
#     ('NUMBER', '2'),
#     ('ASSIGN', '='),
#     ('NUMBER', '15'),
#     ('ASSIGN', '='),
#     ('STRING', 'hello'),
#     ('ASSIGN', '='),
#     ('IDENTIFIER', 'x'),
#     ('PLUS', '+'),
#     ('NUMBER', '5'),
# ]

# # Call the parse function with the tokens
# result = parse(tokens)

# # Print the result
# print(result)
