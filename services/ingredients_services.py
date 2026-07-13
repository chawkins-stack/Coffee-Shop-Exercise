# services/ingredients_service.py
from repositories.drink_repository import DrinkRepository
from models.drink import Drink
from exceptions import DuplicateDrinkError

class IngredientService:
    def __init__(self, repository: IngredientRepository):
        self._repository = repository

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        if self._repository.get_by_id(ingredient.name) is not None:
            raise DuplicateIngredientError(f"Ingredient '{ingredient.name}' already exists.")
        return self._repository.add(ingredient)