from dataclasses import dataclass
from numbers import Number
from decimal import Decimal
from typing import Optional

@dataclass
class BakedGood:
    id: Number
    name: str
    purchasing_cost: Decimal
    marking_percentage: Decimal
    vendor_name: str
    allergens: list[str]
    sales_price: Decimal
    id: Optional[Number] = None