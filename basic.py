#Constants
DIGITS="0123456789"

#Tokens

TT_INT        ="INT"
TT_FLOAT      ="FLOAT"
TT_MULT       ="MULT"
TT_PLUS       ="PLUS"
TT_DIV        ="DIV"
TT_MIN        ="MIN"
TT_LPAREN     ="LPAREN"
TT_RPAREN     ="RPAREN"

class Token:
  def __init__(self, type_, value=None):
    self.type=type_
    self.value=value
  
  def __repr__(self):
    if self.value: return f"{self.type}: {self.value}"
    return f"{self.type}"

#Lexer
class Lexer:
  def __init__(self, fn, text):
    self.fn=fn
    self.text=text
    self.pos=-1
    self.current_char=None
    self.advance()

  def advance(self):
    self.pos+=1
    self.current_char=self.text[self.pos] if self.pos < len(self.text) else None
  
  def make_tokens(self):
    tokens=[]

    while self.current_char!=None:
      if self.current_char in " \t":
        self.advance()
      elif self.current_char=="+":
        tokens.append(Token(TT_PLUS))
        self.advance()
      elif self.current_char=="-":
        tokens.append(Token(TT_MIN))
        self.advance()
      elif self.current_char=="*":
        tokens.append(Token(TT_MULT))
        self.advance()
      elif self.current_char=="/":
        tokens.appens(Token(TT_DIV))
        self.advance()
      elif self.current_char in DIGITS:
        tokens.append(self.make_number(self.current_char))
        self.advance()

    return tokens
  def make_number(self, number):
    pass