from dataclasses import dataclass
from numbers import Number

@dataclass
class Baked_good:
    id: Number
    name: str
    purchasing_cost: float
    marking_percentage: float
    vendor_name: str
    allergens: list[str]
    sales_price: float 
    