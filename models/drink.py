from dataclasses import dataclass
from models.ingredients import Ingredient

@dataclass
class Drink:
    name : str
    ingredients : list[Ingredient]
    cost_to_produce : float
    markup_percentage : float
    sale_price : float