from repositories.drink_repository import DrinkRepository
from models.drink import Drink
from exceptions import DuplicateDrinkError

class DrinkService:
    def __init__(self, repository: DrinkRepository):
        self._repository = repository

    def create_drink(self, drink: Drink) -> Drink:
        if self._repository.get_by_id(drink.name) is not None:
            raise DuplicateDrinkError(f"Drink '{drink.name}' already exisits.")
        return self._repository.add(drink)