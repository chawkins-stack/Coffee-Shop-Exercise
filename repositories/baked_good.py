from models.baked_good import BakedGood
from numbers import Number

class Baked_good_repository:
    def __init__(self):
        self._baked_goods: list[BakedGood] = []

    def get_all(self) -> list[BakedGood]:
        return self._baked_goods 
    
    def get_by_id(self,: str) -> BakedGood | None:
        return next((baked_good for baked_good in self._baked_goods if baked_good.name == name), None)
    
    def add(self, baked_good: BakedGood) -> BakedGood:
        self._baked_goods.append(baked_good)
        return baked_good
    
    def update (self, id: Number: str, baked_good: BakedGood) -> BakedGood | None:
        existing_baked_good = self.get_by_id(name)
        if existing_baked_good:
            existing_baked_good.name = baked_good.name
            return existing_baked_good
        return None

    

    def delete(self, name: str) -> bool:
        baked_good = self.get_by_id(name)
        if baked_good:
            self._baked_goods.remove(baked_good)
            return True
        return False
    