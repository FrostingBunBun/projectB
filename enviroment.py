class Environment:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.values = {}

    def get(self, name):
        # print("self: ", self)
        # print("self values: ", self.values)
        # print("name: ", name)
        # print("name lexeme: ", name.lexeme)

        if name.lexeme in self.values:
            return self.values[name.lexeme]
        elif self.enclosing is not None:
            return self.enclosing.get(name)
        else:
            raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")

    def assign(self, name, value):
        # print("self: ", self)
        # print("name: ", name)
        # print("value: ", value)
        if name in self.values:
            self.values[name] = value
        elif self.enclosing is not None:
            self.enclosing.assign(name, value)
        else:
            raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")

    def define(self, name, value):
        self.values[name] = value
