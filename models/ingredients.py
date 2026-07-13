# models/ingredient.py
from dataclasses import dataclass
from numbers import Number

@dataclass
class Ingredient:
    id: Number
    name: str
    purchasing_cost: float
    unit_amount: float
    unit_of_measure: str