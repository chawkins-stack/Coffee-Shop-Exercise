from dataclasses import dataclass
from numbers import Number
from typing import Optional
from decimal import Decimal

@dataclass
class Customer:
    name: str
    email: str
    lifetime_spent: Decimal
    id: Optional[Number] = None
