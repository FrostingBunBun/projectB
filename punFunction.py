from punCallable import PunCallable
from enviroment import Environment

class PunFunction(PunCallable):
    def __init__(self, declaration):
        self.declaration = declaration

    def arity(self):
        return len(self.declaration.params)
    
    def __str__(self):
        return "<fn " + self.declaration.name.lexeme + ">"

    def call(self, interpreter, arguments):
        environment = Environment(interpreter.globals)
        for i in range(len(self.declaration.params)):
            environment.define(self.declaration.params[i].lexeme, arguments[i])

        interpreter.executeBlock(self.declaration.body, environment)
        return None
