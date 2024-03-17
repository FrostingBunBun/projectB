from scanner import Scanner

test_code = """
// Sample test code
var x = 10;
print("Hello, world!");
"""
scanner = Scanner(test_code)

tokens = scanner.scanTokens()

for token in tokens:
    print(token)
