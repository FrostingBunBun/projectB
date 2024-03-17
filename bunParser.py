from typing import List
from tokenType import TokenType
from bunToken import Token
from Expr import Expr

class Parser:
    class ParseError(RuntimeError):
        pass

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        """
        equality → comparison ( ( "!=" | "==" ) comparison )* ;
        """
        expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Expr.Binary(expr, operator, right)

        return expr

    # Methods for other grammar rules can be added similarly

    def match(self, *types: TokenType) -> bool:
        """
        Check if the current token matches any of the given types.
        """
        for tokenType in types:
            if self.check(tokenType):
                self.advance()
                return True
        return False

    def check(self, tokenType: TokenType) -> bool:
        """
        Check if the current token is of the given type.
        """
        if self.is_at_end():
            return False
        return self.peek().type == tokenType

    def advance(self) -> Token:
        """
        Consume the current token and return it.
        """
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        """
        Check if we have reached the end of input.
        """
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        """
        Return the current token.
        """
        return self.tokens[self.current]

    def previous(self) -> Token:
        """
        Return the previous token.
        """
        return self.tokens[self.current - 1]

    def comparison(self) -> Expr:
        """
        comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
        """
        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def term(self) -> Expr:
        """
        term → factor ( ( "-" | "+" ) factor )* ;
        """
        expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def factor(self) -> Expr:
        """
        factor → unary ( ( "/" | "*" ) unary )* ;
        """
        expr = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def unary(self) -> Expr:
        """
        unary → ( "!" | "-" ) unary | primary ;
        """
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Expr.Unary(operator, right)

        return self.primary()

    def primary(self) -> Expr:
        """
        primary → NUMBER | STRING | "true" | "false" | "nil"
                | "(" expression ")" ;
        """
        if self.match(TokenType.FALSE):
            return Expr.Literal(False)
        if self.match(TokenType.TRUE):
            return Expr.Literal(True)
        if self.match(TokenType.NIL):
            return Expr.Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Expr.Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Expr.Grouping(expr)
        raise self.error(self.peek(), "Expect expression.")


    def consume(self, tokenType: TokenType, message: str) -> Token:
        """
        Consume the current token if it matches the given type,
        otherwise raise a syntax error with the provided message.
        """
        if self.check(tokenType):
            return self.advance()

        # Raise SyntaxError with the given message
        raise SyntaxError(self.peek(), message)

    def error(self, token: Token, message: str) -> ParseError:
        """
        Raise a ParseError with the given message and token.
        """
        # Custom error reporting can be added here if needed
        raise self.ParseError(message)

    def synchronize(self):
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return

            # Check if the current token indicates the start of a new statement
            if self.peek().type in [TokenType.CLASS, TokenType.FUN, TokenType.VAR, TokenType.FOR,
                                          TokenType.IF, TokenType.WHILE, TokenType.PRINT, TokenType.RETURN]:
                return

            self.advance()

    def parse(self):
        try:
            return self.expression()
        except self.ParseError as error:
            return None
