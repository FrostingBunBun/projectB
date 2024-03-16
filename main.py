import bunInterpreter
import bunParser
import bunTokenizer

def print_ast(node, indent=0):
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

def main():
    interpreter = bunInterpreter.Interpreter()

    while True:
        try:
            # Read user input
            expression = input(">> ")

            # Tokenize and parse input
            tokens = bunTokenizer.tokenize(expression)
            ast = bunParser.parse(tokens)

            # Interpret AST and display result
            result = interpreter.interpret(ast)
            print_ast(ast)
            print("=====================")
            print("Result:", result)
        except KeyboardInterrupt:
            # Handle Ctrl+C to exit the loop
            print("\nExiting.")
            break
        except SyntaxError as e:
            print("Syntax Error:", e)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
