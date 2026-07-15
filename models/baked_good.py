from dataclasses import dataclass
from numbers import Number
from decimal import Decimal
from typing import Optional

@dataclass
class BakedGood:
    name: str
    purchasing_cost: Decimal
    marking_percentage: Decimal
    vendor_name: str
    allergens: list[str]
    sale_price: Optional[Decimal] = None
    id: Optional[Number] = None