from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER    =0
    PLUS      =1
    MINUS     =2
    MULT      =3
    DIV       =4
    LPAREN    =5
    RPAREN    =6
    RCURL     =7
    LCURL     =8
    EQ        =9

@dataclass
class Token:
    type: TokenType
    value: any = None
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")