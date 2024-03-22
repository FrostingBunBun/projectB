from punCallable import PunCallable
from enviroment import Environment
from _return import ReturnException

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

        try:
            interpreter.executeBlock(self.declaration.body, environment)
        except ReturnException as return_value:
            return return_value.value

        return None
