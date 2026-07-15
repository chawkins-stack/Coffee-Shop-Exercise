from datetime import datetime
from numbers import Number
from models.purchase import Purchase
from datetime import datetime, timezone

class PurchaseRepository:
    def __init__(self):
        self._purchases: list[Purchase] = []
        self._next_id = 7001

    def get_all(self) -> list[Purchase]:
        return self._purchases 

    def get_by_date(self, date: datetime) -> list[Purchase]:
        return [purchase for purchase in self._purchases if purchase.timestamp.date() == date.date()]

    def get_by_id(self, timestamp: datetime) -> Purchase | None:
        return next((purchase for purchase in self._purchases if purchase.timestamp == timestamp), None)

    def add(self, purchase: Purchase) -> Purchase:
        purchase.id = self._next_id
        self._next_id += 1
        purchase.timestamp = purchase.timestamp.astimezone(timezone.utc)

        self._purchases.append(purchase)
        return purchase

    def update (self, timestamp: datetime, purchase: Purchase) -> Purchase | None:
        existing_purchase = self.get_by_id(timestamp)
        if existing_purchase:
            existing_purchase.timestamp = purchase.timestamp.astimezone(datetime.timezone.utc)
            return existing_purchase
        return None

    def delete(self, timestamp: datetime) -> bool:
        purchase = self.get_by_id(timestamp)
        if purchase:
            self._purchases.remove(purchase)
            return True
        return False
