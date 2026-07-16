from models.purchase import Purchase
from models.drink import Drink
from models.baked_good import BakedGood

from repositories.purchase_repository import PurchaseRepository
from services.customer_service import CustomerService
from exceptions import DuplicatePurchaseError, PurchaseNotFoundError
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN


class PurchaseService:
    def __init__(self, purchase_repository: PurchaseRepository, customer_service: CustomerService):
        self._customer_service = customer_service
        self._repository = purchase_repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        purchase.timestamp = datetime.now(timezone.utc)
        purchase.total_cost = self._calculate_total_cost(purchase)

        if self._repository.get_by_id(purchase.timestamp) is not None:
            raise DuplicatePurchaseError(f"Purchase with timestamp '{purchase.timestamp}' already exists.")

        if purchase.Customer is not None:
            self._customer_service.add_to_lifetime_spent(
                purchase.Customer.email,
                purchase.total_cost,
            )

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
 
    def _calculate_total_cost(self, purchase: Purchase) -> Decimal:
        drinks_total = Decimal("0")
        baked_goods_total = Decimal("0")

        for item in purchase.items:
            if isinstance(item, Drink):
                drinks_total += item.sale_price
            elif isinstance(item, BakedGood):
                baked_goods_total += item.sale_price

        return drinks_total + baked_goods_total

    def format_receipt(self, purchase: Purchase) -> str:
        lines = []
        lines.append("====================================")
        lines.append("            PURCHASE RECEIPT        ")
        lines.append("====================================")
        lines.append(f"Purchase ID: {purchase.id}")
        lines.append(f"Customer: {purchase.Customer.name}")
        lines.append(f"Timestamp: {purchase.timestamp.isoformat()}")
        lines.append("------------------------------------")
        lines.append("Items:")

        total = Decimal("0")

        for item in purchase.items:
            item_type = item.__class__.__name__
            price = item.sale_price
            total += price
            lines.append(f"  {item_type:<12} {item.name:<20} ${price}")

        lines.append("------------------------------------")
        lines.append(f"TOTAL: ${total}")
        lines.append("====================================")

        return "\n".join(lines)