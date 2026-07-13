from repositories.purchase import Purchase_repository
from models.purchase import Purchase
from exceptions import DuplicatePurchaseError
from datetime import datetime

class PurchaseService:
    def __init__(self, repository: Purchase_repository):
        self._repository = repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        if self._repository.get_by_id(purchase.timestamp) is not None:
            raise DuplicatePurchaseError(f"Purchase with timestamp '{purchase.timestamp}' already exists.")
        return self._repository.add(purchase)
    
    def get_all_purchases(self) -> list[Purchase]:
        return self._repository.get_all()
    
    def get_purchase_by_timestamp(self, timestamp: datetime) -> Purchase | None:
        return self._repository.get_by_id(timestamp)
    
    def update_purchase(self, timestamp: datetime, purchase: Purchase) -> Purchase | None:
        return self._repository.update(timestamp, purchase)
    
    def delete_purchase(self, timestamp: datetime) -> bool:
        return self._repository.delete(timestamp)
    
