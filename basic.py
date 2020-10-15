##########################################
#TOKENS
##########################################

TT_INT        ="INT"
TT_PLUS       ="PLUS"
TT_MINUS      ="MINUS"
TT_MULT       ="MULT"
TT_DIV        ="DIV"
TT_EQ         ="EQ"
TT_FLOAT      ="FLOAT"
TT_LPAREN     ="LPAREN"
TT_RPAREN     ="RPAREN"

class Token:
  def __init__(self, type_, value):
    self.type=type_
    self.value=value
  
  def __repr__(self):
    if self.value: return f'{self.type}:{self.value}'
    return f'{self.type}'