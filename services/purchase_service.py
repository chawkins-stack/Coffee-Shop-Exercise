from unicodedata import decimal

from models import baked_good
from models import purchase
from repositories.purchase_repository import Purchase_repository
from models.purchase import Purchase
from exceptions import DuplicatePurchaseError, PurchaseNotFoundError
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN

purchase.baked_good.price = Decimal(purchase.baked_good.price).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

class PurchaseService:
    def __init__(self, repository: Purchase_repository):
        self._repository = repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        purchase.timestamp = datetime.now(timezone.utc)

        if self._repository.get_by_id(purchase.timestamp) is not None:
            raise DuplicatePurchaseError(f"Purchase with timestamp '{purchase.timestamp}' already exists.")
        purchase.baked_good.price = Decimal(purchase.baked_good.price).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

        return self._repository.add(purchase)

    def get_all_purchases(self) -> list[Purchase]:
        return self._repository.get_all()

    def get_purchase_by_timestamp(self, timestamp: datetime) -> Purchase | None:
        return self._repository.get_by_id(timestamp.astimezone(timezone.utc))

    def get_purchase_by_timestamp_not_found(self, timestamp: datetime) -> Purchase | None:
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
