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
            json_dict["Children"] = [child.to_json() for child in self.children]
        return json_dict

class NumberNode(Node):
    pass

class BinaryOperationNode(Node):
    pass

class IdentifierNode(Node):
    pass

class AssignmentNode(Node):
    pass
class VariableDeclarationNode(Node):
    pass

def _get_token_text(node):
    return node[1]

def parse_assignment(tokens):
    identifier = parse_factor(tokens)  # Get the left-hand side identifier
    if tokens.pop(0)[0] != 'ASSIGN':  # Consume the '=' token
        raise SyntaxError("Expected '='")
    value = parse_expression(tokens)  # Get the right-hand side expression
    return AssignmentNode("Assignment", Name=_get_token_text(identifier), Value=value)

def parse_factor(tokens):
    if tokens[0][0] == 'NUMBER':
        return NumberNode("NumLiteral", Value=float(tokens.pop(0)[1]))  # Consume and return the number token
    elif tokens[0][0] == 'IDENTIFIER':
        return IdentifierNode("Identifier", Name=tokens.pop(0)[1])  # Consume and return the identifier token
    elif tokens[0][0] == 'LPAREN':
        tokens.pop(0)  # Consume the left parenthesis token
        expression = parse_expression(tokens)
        if tokens.pop(0)[0] != 'RPAREN':
            raise SyntaxError('Expected closing parenthesis')
        return expression
    else:
        raise SyntaxError('Expected number, identifier, or left parenthesis')

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

def parse(tokens):
    return parse_expression(tokens).to_json()