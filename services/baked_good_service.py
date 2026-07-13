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
    
    def 

 
