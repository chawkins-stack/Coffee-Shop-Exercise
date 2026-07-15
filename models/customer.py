from dataclasses import dataclass
from numbers import Number
from typing import Optional
from decimal import Decimal

@dataclass
class Customer:
<<<<<<< HEAD
  def __init__(self, id: int, name:str,email: str):
    self.id = id
    self.name = name
    self.email = email
=======
    name: str
    email: str
    lifetime_spent: Decimal
    id: Optional[Number] = None
>>>>>>> 0b92d7e6288b7a66ad6aca09cead5697d29845c8
