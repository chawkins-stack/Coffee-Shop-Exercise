from models import baked_good
from models.baked_good import BakedGood
from numbers import Number

class BakedGoodRepository:
    def __init__(self):
        self._baked_goods: list[BakedGood] = []
        self._next_id = 6701

    def get_all(self) -> list[BakedGood]:
        return self._baked_goods

    def get_by_name(self, name: str) -> BakedGood | None:
        return next((baked_good for baked_good in self._baked_goods if baked_good.name == name), None)

    def get_by_id(self, id: Number) -> BakedGood | None:
        return next((baked_good for baked_good in self._baked_goods if baked_good.id == id), None)

    def add(self, baked_good: BakedGood) -> BakedGood:
        baked_good.id = self._next_id
        self._next_id += 1
        self._baked_goods.append(baked_good)
        return baked_good
    
    def update(self, id: Number, baked_good: BakedGood) -> BakedGood | None:
        for index, existing_baked_good in enumerate(self._baked_goods):
            if existing_baked_good.id == id:
                self._baked_goods[index] = baked_good
                return baked_good
            
        return None


    def delete(self, id: Number) -> bool:
        baked_good = self.get_by_id(id)
        if baked_good:
            self._baked_goods.remove(baked_good)
            return True
        return False
