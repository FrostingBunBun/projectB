class Environment:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]
        elif self.enclosing is not None:
            return self.enclosing.get(name)
        else:
            raise RuntimeError(name, f"Undefined variable '{name}'.")
        
    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
            return
        elif self.enclosing is not None:
            self.enclosing.assign(name, value)
            return
        else:
            raise RuntimeError(name, f"Undefined variable '{name}'.")