from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    email:str
    lifetime_spent:float
    