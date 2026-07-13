from dataclasses import dataclass

@dataclass
class Purchase:
    timestamp: datetime
    items: []
    total_cost: float
    Customer: Customer
    
