from dataclasses import dataclass
from numbers import Number
from models.ingredients import Ingredient

@dataclass
class Drink:
    id: Number
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: float
    markup_percentage: float
    sale_price: float