from repositories.drink_repository import DrinkRepository
from models.drink import Drink
from exceptions import DuplicateDrinkError, DrinkNotFoundError

class DrinkService:
    def __init__(self, repository: DrinkRepository):
        self._repository = repository

    def create_drink(self, drink: Drink) -> Drink:
        if self._repository.get_by_id(drink.name) is not None:
            raise DuplicateDrinkError(drink.name)
        return self._repository.add(drink)
    
    def get_all_drinks(self) -> list[Drink]:
        return self._repository.get_all()
    
    def get_drink(self, name: str) -> Drink:
        drink = self._repository.get_by_id(name)
        if drink is None:
            raise DrinkNotFoundError(name)
        return drink

    def update_drink(self, name: str, updated: Drink) -> Drink:
        drink = self._repository.update(name, updated)
        if drink is None:
            raise DrinkNotFoundError(name)
        return drink

    def delete_drink(self, name: str) -> bool:
        if not self._repository.delete(name):
            raise DrinkNotFoundError(name)
        return True