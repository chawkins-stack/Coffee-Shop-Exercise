# models/ingredient.py
from dataclasses import dataclass
from numbers import Number
from decimal import Decimal

@dataclass
class Ingredient:
    id: Number
    name: str
    purchasing_cost: Decimal
    unit_amount: Decimal
    unit_of_measure: str
