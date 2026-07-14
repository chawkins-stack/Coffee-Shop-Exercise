from dataclasses import dataclass
from numbers import Number
from decimal import Decimal
from models.ingredients import Ingredient

@dataclass
class Drink:
    id: Number
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: Decimal
    markup_percentage: float
    sale_price: Decimal