from repositories.baked_good import Baked_good_repository
from models.baked_good import Baked_good
from exceptions import DuplicateBakedGoodError

class Baked_goodService:
    def __init__(self, repository: Baked_good_repository):
        self._repository = repository

    def create_baked_good(self, baked_good: Baked_good) -> Baked_good:
        if self._repository.get_by_id(baked_good.name) is not None:
            raise DuplicateBakedGoodError(f"Baked good '{baked_good.name}' already exists.")
        return self._repository.add(baked_good)
    
    def get_all_baked_goods(self) -> list[Baked_good]:
        return self._repository.get_all()
    
    def get_by_id(self, name: str) -> Baked_good:
        return self._repository.get_by_id(name)
    
    def add_baked_good(self, baked_good: Baked_good) -> Baked_good:
        return self._repository.add(baked_good)
    
    def update_baked_good(self, baked_good: Baked_good) -> Baked_good:
        return self._repository.update(baked_good)
    
    def delete_baked_good(self, name: str) -> None:
        self._repository.delete(name)
    
 
