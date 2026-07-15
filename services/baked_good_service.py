from numbers import Number
from repositories.baked_good_repository import BakedGoodRepository
from models.baked_good import BakedGood
from exceptions import DuplicateBakedGoodError, BakedGoodNotFoundError 
from decimal import Decimal, ROUND_HALF_EVEN

# sales_price = BakedGood.sales_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

class BakedGoodService:
    def __init__(self, repository: BakedGoodRepository):
        self._repository = repository

    def create_baked_good(self, baked_good: BakedGood) -> BakedGood:
        if self._repository.get_by_id(baked_good.id) is not None:
            raise DuplicateBakedGoodError(f"Baked good '{baked_good.name}' already exists.")
        sales_price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.add(baked_good)

    def get_baked_good(self, id: Number) -> BakedGood:
        baked_good = self._repository.get_by_id(id)
        if baked_good is None:
            raise BakedGoodNotFoundError(f"Baked good with ID '{id}' was not found.")
        return baked_good
    
    def get_all_baked_goods(self) -> list[BakedGood]:
        return self._repository.get_all()

    def get_by_id(self, id: Number) -> BakedGood:
        return self._repository.get_by_id(id)

    def get_by_name(self, name: str) -> BakedGood:
        return self._repository.get_by_name(name) 

    def add_baked_good(self, baked_good: BakedGood) -> BakedGood:
        sales_price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.add(baked_good)

    def update_baked_good(self, baked_good: BakedGood) -> BakedGood:
        sales_price = baked_good.price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        return self._repository.update(baked_good)

    def delete_baked_good(self, name: str) -> None:
        self._repository.delete(name)

    def _calculate_sale_price(self, price: Decimal) -> Decimal:
        discount = Decimal("0.10")
        sale_price = price * (Decimal("1.00") - discount)
        return sale_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
