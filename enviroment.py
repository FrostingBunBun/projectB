class Environment:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.values = {}

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]
        elif self.enclosing is not None:
            return self.enclosing.get(name)
        else:
            raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
        elif self.enclosing is not None:
            self.enclosing.assign(name, value)
        else:
            raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")

    def define(self, name, value):
        self.values[name] = value
