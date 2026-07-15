from dataclasses import dataclass
import datetime
from decimal import Decimal
from numbers import Number
from models.customer import Customer
from models.drink import Drink
from models.baked_good import BakedGood

@dataclass
class Purchase:
    id: Number
    timestamp: datetime
    items: list[Drink, BakedGood]
    total_cost: Decimal
    Customer: Customer
 