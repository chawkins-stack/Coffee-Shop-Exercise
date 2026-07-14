from dataclasses import dataclass
from numbers import Number
from decimal import Decimal

@dataclass
class Customer:
    id: Number
    name: str
    email: str
    lifetime_spent: Decimal
    
