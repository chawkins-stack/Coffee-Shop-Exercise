from dataclasses import dataclass

@dataclass
class Baked_good:
    name: str
    purchasing_cost: float
    marking_percentage: float
    vendor_name: str
    allergens: list[str]
    sales_price: float 
    