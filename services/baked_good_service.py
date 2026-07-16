from numbers import Number
from models import baked_good
from repositories.baked_good_repository import BakedGoodRepository
from models.baked_good import BakedGood
from exceptions import DuplicateBakedGoodError, BakedGoodNotFoundError, InvalidBakedGoodError 
from decimal import Decimal, ROUND_HALF_EVEN

# sales_price = BakedGood.sales_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)

class BakedGoodService:
    def __init__(self, repository: BakedGoodRepository):
        self._repository = repository

    def create_baked_good(self, baked_good: BakedGood) -> BakedGood:
        if self._repository.get_by_id(baked_good.id) is not None:
            raise DuplicateBakedGoodError(f"Baked good '{baked_good.name}' already exists.")
        baked_good.sale_price = self._calculate_sales_price(baked_good)
        return self._repository.add(baked_good)

    def get_baked_good(self, id: Number) -> BakedGood:
        baked_good = self._repository.get_by_id(id)
        if baked_good is None:
            raise BakedGoodNotFoundError(f"Baked good with ID '{id}' was not found.")
        return baked_good
    
    def validate_baked_good(self, baked_good: BakedGood) -> None:
        if not baked_good.name or len(baked_good.name) == 0:
            raise InvalidBakedGoodError(f"Baked good '{baked_good.name}' is invalid.")
        
        if baked_good.purchasing_cost <= 0:
            raise InvalidBakedGoodError(f"Baked good '{baked_good.name}' is invalid.")
        
        if baked_good.marking_percentage <= 0:
            raise InvalidBakedGoodError(f"Baked good '{baked_good.name}' is invalid.")
        
        if not baked_good.vendor_name:
            raise InvalidBakedGoodError(f"Baked good '{baked_good.name}' is invalid.")
        
        if not isinstance(baked_good.allergens, list):
            raise InvalidBakedGoodError(f"Baked good '{baked_good.name}' is invalid.")
    
    def get_all_baked_goods(self) -> list[BakedGood]:
        return self._repository.get_all()

    def get_by_id(self, id: Number) -> BakedGood:
        return self._repository.get_by_id(id)

    def get_by_name(self, name: str) -> BakedGood:
        return self._repository.get_by_name(name) 

    def add_baked_good(self, baked_good: BakedGood) -> BakedGood:
        baked_good.sales_price = self._calculate_sales_price(baked_good.sales_price)
        return self._repository.add(baked_good)

    def update_baked_good(self, baked_good: BakedGood) -> BakedGood:
       baked_good.sales_price = self._calculate_sales_price(baked_good)
       
       baked_good = self._repository.update(baked_good.id, baked_good)
       if baked_good is None:
            raise BakedGoodNotFoundError(name)
       return baked_good

    def delete_baked_good(self, name: str) -> None:
        self._repository.delete(name)

    def _calculate_sales_price(self, baked_good: BakedGood) -> Decimal:
        purchasing_cost = baked_good.purchasing_cost
        markup = baked_good.marking_percentage
        sales_price = purchasing_cost * (1 + markup)

        return sales_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
