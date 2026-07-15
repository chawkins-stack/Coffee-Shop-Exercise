# models/ingredient.py
from dataclasses import dataclass
from numbers import Number
from decimal import Decimal
from typing import Optional

@dataclass
class Ingredient:
    name: str
    purchasing_cost: Decimal
    unit_amount: Decimal
    unit_of_measure: str
    id: Optional[Number] = None
