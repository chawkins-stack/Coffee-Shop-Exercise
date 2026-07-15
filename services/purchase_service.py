
from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from services.customer_service import CustomerService
from exceptions import DuplicatePurchaseError, PurchaseNotFoundError
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN

# purchase.BakedGood.sales_price = Decimal(purchase.BakedGood.sales_price).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

class PurchaseService:
    def __init__(self, purchase_repository: PurchaseRepository, customer_service: CustomerService):
        self._customer_service = customer_service
        self._repository = purchase_repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        purchase.timestamp = datetime.now(timezone.utc)

        if self._repository.get_by_id(purchase.timestamp) is not None:
            raise DuplicatePurchaseError(f"Purchase with timestamp '{purchase.timestamp}' already exists.")
        
        purchase.baked_good.price = Decimal(purchase.baked_good.price).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

        if purchase.customer_email is not None:
            self._customer_service.add_to_lifetime_spending(purchase.customer_email, purchase.baked_good.price)
            return self._repository.add(purchase)

    def get_all_purchases(self) -> list[Purchase]:
        return self._repository.get_all()

    def get_purchase_by_timestamp(self, timestamp: datetime) -> Purchase | None:
        return self._repository.get_by_id(timestamp.astimezone(timezone.utc))

    def get_purchase_by_timestamp_not_found(self, timestamp: datetime) -> Purchase:
        purchase = self._repository.get_by_id(timestamp.astimezone(timezone.utc))

        if purchase is None:
            raise PurchaseNotFoundError(f"Purchase with timestamp '{timestamp}' was not found.")
        
        return purchase

    def update_purchase(self, timestamp: datetime, purchase: Purchase) -> Purchase | None:
        purchase.timestamp = purchase.timestamp.astimezone(timezone.utc)
        purchase.baked_good.price = Decimal(purchase.baked_good.price).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.update(timestamp.astimezone(timezone.utc), purchase)

    def delete_purchase(self, timestamp: datetime) -> bool:
        timestamp = timestamp.astimezone(timezone.utc)
        return self._repository.delete(timestamp)
 


