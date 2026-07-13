from dataclasses import dataclass
from numbers import Number

@dataclass
class Customer:
    id: Number
    name: str
    email: str
    lifetime_spent: float
    