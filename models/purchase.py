from dataclasses import dataclass
import datetime
from models.customer import Customer


@dataclass
class Purchase:
    timestamp: datetime
    items: list[]
    total_cost: float
    Customer: Customer
    
