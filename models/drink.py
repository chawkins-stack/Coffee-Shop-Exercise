from dataclasses import dataclass
from numbers import Number
from decimal import Decimal
from typing import Optional
from models.ingredients import Ingredient

@dataclass
class Drink:
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: Decimal
    markup_percentage: Decimal
    sale_price: Optional[Decimal] = None
    id: Optional[Number] = None
    