from dataclasses import dataclass
from numbers import Number
from decimal import Decimal

@dataclass
class BakedGood:
    id: Number
    name: str
    purchasing_cost: Decimal
    marking_percentage: Decimal
    vendor_name: str
    allergens: list[str]
    sales_price: Decimal
    