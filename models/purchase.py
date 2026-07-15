from dataclasses import dataclass
import datetime
from decimal import Decimal
from numbers import Number
from typing import Optional
from models.customer import Customer
from models.drink import Drink
from models.baked_good import BakedGood

@dataclass
class Purchase:
    timestamp: datetime
    items: list[object]
    Customer: Customer
    total_cost: Optional[Decimal] = None
    id: Optional[Number] = None
