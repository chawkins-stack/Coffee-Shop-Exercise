# services/ingredients_service.py
from models.ingredients import Ingredient
from repositories.drink_repository import DrinkRepository
from models.drink import Drink
from exceptions import DuplicateDrinkError, DuplicateIngredientError, IngredientNotFoundError
from repositories.ingredients_repository import IngredientRepository

class IngredientService:
    def __init__(self, repository: IngredientRepository):
        self._repository = repository

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        if self._repository.get_by_id(ingredient.name) is not None:
            raise DuplicateIngredientError(f"Ingredient '{ingredient.name}' already exists.")
        return self._repository.add(ingredient)
    
    def get_all_ingredients(self) -> list[Ingredient]:
        return self._repository.get_all()
    
    def get_ingredient(self, name: str) -> Ingredient:
        ingredient = self._repository.get_by_id(name)
        if ingredient is None:
            raise IngredientNotFoundError(name)
        return ingredient

    def update_ingredient(self, name: str, updated: Ingredient) -> Ingredient:
        ingredient = self._repository.update(name, updated)
        if ingredient is None:
            raise IngredientNotFoundError(name)
        return ingredient

    def delete_ingredient(self, name: str) -> bool:
        if not self._repository.delete(name):
            raise IngredientNotFoundError(name)
        return True