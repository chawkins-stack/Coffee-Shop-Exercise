# models/ingredient.py
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    purchasing_cost: float
    unit_amount: float
    unit_of_measure: str