from punCallable import PunCallable
from enviroment import Environment
from _return import ReturnException

class PunFunction(PunCallable):
    def __init__(self, declaration, closure):
        self.declaration = declaration
        self.closure = closure

    def arity(self):
        return len(self.declaration.params)
    
    def __str__(self):
        return "<fn " + self.declaration.name.lexeme + ">"

    def call(self, interpreter, arguments):
        enviroment = Environment(self.closure)
        for i in range(len(self.declaration.params)):
            enviroment.define(self.declaration.params[i].lexeme, arguments[i])

        try:
            interpreter.executeBlock(self.declaration.body, enviroment)
        except ReturnException as return_value:
            return return_value.value

        return None
