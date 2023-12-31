import collections
##########################################
# TOKENS
##########################################

IDENTIFICATOR = "identifikator"
KEY_WORD = "kljucna rijec"
SEPARATOR = "separator"
OPERATOR = "operator"
CONSTANT = "konstanta"
COMMENT = "komentar"

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value : return f'{self.type}:{self.value}'
        return f'{self.type}'


##########################################
# LEXER
##########################################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        operators = {}
        identificators = {}
        comments = {}
        separators = {}
        constans = {}

        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char == '+' or self.current_char == '-' or self.current_char == '*' or self.current_char == '/' or self.current_char == '=':
                tokens.append(f"('{self.current_char}',{Token(OPERATOR)})")
                if self.current_char in operators:
                    operators[self.current_char] += 1
                else:
                    operators[self.current_char] = 1
                self.advance()
            elif self.current_char >= 'a' and self.current_char <= 'z':
                tokens.append(f"('{self.current_char}',{Token(IDENTIFICATOR)})")
                if self.current_char in identificators:
                    identificators[self.current_char] += 1
                else:
                    identificators[self.current_char] = 1
                self.advance()
            elif self.current_char == ' ' or self.current_char == ';':
                tokens.append(f"('{self.current_char}',{Token(SEPARATOR)})")
                if self.current_char in separators:
                    separators[self.current_char] += 1
                else:
                    separators[self.current_char] = 1
                self.advance()
            elif self.current_char == '#':
                tokens.append(f"('{self.current_char}',{Token(COMMENT)})")
                if self.current_char in comments:
                    comments[self.current_char] += 1
                else:
                    comments[self.current_char] = 1
                self.advance()
            elif self.current_char >= '0' and self.current_char <= '9':
                tokens.append(f"('{self.current_char}',{Token(CONSTANT)})")
                if self.current_char in constans:
                    constans[self.current_char] += 1
                else:
                    constans[self.current_char] = 1
                self.advance()
            
        return tokens, separators, identificators, operators, comments, constans

    
##########################################
# RUN
##########################################

def run(text):
    lexer = Lexer(text)
    tokens, separators, identifiators, operators, comments, constants = lexer.make_tokens()

    return tokens, separators, identifiators, operators, comments, constants


