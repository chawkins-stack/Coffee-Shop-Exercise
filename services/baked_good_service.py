from numbers import Number
from unicodedata import decimal
from models import purchase
from models import baked_good
from repositories.baked_good_repository import Baked_good_repository
from models.baked_good import Baked_good
from exceptions import DuplicateBakedGoodError
from decimal import Decimal, ROUND_HALF_EVEN

baked_good.price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

class BakedGoodService:
    def __init__(self, repository: Baked_good_repository):
        self._repository = repository

    def create_baked_good(self, baked_good: Baked_good) -> Baked_good:
        if self._repository.get_by_id(baked_good.id) is not None:
            raise DuplicateBakedGoodError(f"Baked good '{baked_good.name}' already exists.")
        baked_good.price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

        return self._repository.add(baked_good)

    def get_all_baked_goods(self) -> list[Baked_good]:
        return self._repository.get_all()

    def get_by_id(self, id: Number) -> Baked_good:
        return self._repository.get_by_id(id)

    def get_by_name(self, name: str) -> Baked_good:
        return self._repository.get_by_name(name) 

    def add_baked_good(self, baked_good: Baked_good) -> Baked_good:
        baked_good.price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.add(baked_good)

    def update_baked_good(self, baked_good: Baked_good) -> Baked_good:
        baked_good.price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.update(baked_good)

    def delete_baked_good(self, name: str) -> None:
        self._repository.delete(name)

    def _calculate_sale_price(self, price: Decimal) -> Decimal:
        discount = Decimal("0.10")
        sale_price = price * (Decimal("1.00") - discount)
        return sale_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
