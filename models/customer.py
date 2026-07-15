from dataclasses import dataclass
from numbers import Number
from decimal import Decimal

@dataclass
class Customer:
  def __init__(self, id: int, name:str,email: str):
    self.id = id
    self.name = name
    self.email = email
