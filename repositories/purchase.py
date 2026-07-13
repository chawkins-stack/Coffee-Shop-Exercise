
from datetime import datetime

from models.purchase import Purchase 

class Purchase_repository:
    def __init__(self):
        self._purchases: list[Purchase] = []

    def get_all(self) -> list[Purchase]:
        return self._purchases 
    
    def get_by_id(self, timestamp: datetime) -> Purchase | None:
        return next((purchase for purchase in self._purchases if purchase.timestamp == timestamp), None)
    
    
    def add(self, purchase: Purchase) -> Purchase:
        self._purchases.append(purchase)
        return purchase
    
    def update (self, timestamp: datetime, purchase: Purchase) -> Purchase | None:
        existing_purchase = self.get_by_id(timestamp)
        if existing_purchase:
            existing_purchase.timestamp = purchase.timestamp
            return existing_purchase
        return None

    

    def delete(self, timestamp: datetime) -> bool:
        purchase = self.get_by_id(timestamp)
        if purchase:
            self._purchases.remove(purchase)
            return True
        return False
    