from repositories.ingredients_repository import IngredientRepository
from models.ingredients import Ingredient
from exceptions import DuplicateIngredientError

class IngredientService:
    def __init__(self, repository: IngredientRepository):
        self._repository = repository

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        if self._repository.get_by_name(ingredient.name) is not None:
            raise DuplicateIngredientError(f"Ingredient '{ingredient.name}' already exists.")
        return self._repository.add(ingredient)
    
    def get_all_ingredients(self) -> list[Ingredient]:
        return self._repository.get_all()
    
    def get_by_id(self, name: str) -> Ingredient:
        return self._repository.get_by_id(name)
    
    def get_by_name(self, name: str) -> Ingredient:
        return self._repository.get_by_name(name)

    def validate_ingredient(self, ingredient: Ingredient) -> bool:
        if not ingredient.name or not ingredient.name.strip():
            raise ValueError("Ingredient name cannot be empty.")
        if ingredient.cost_to_produce is None or ingredient.cost_to_produce <= 0:
            raise ValueError("Ingredient cost to produce must be greater than 0.")
        return True
    
    def add_ingredient(self, ingredient: Ingredient) -> Ingredient:
        return self._repository.add(ingredient)
    
    def update_ingredient(self, ingredient: Ingredient) -> Ingredient:
        return self._repository.update(ingredient)
    
    def delete_ingredient(self, name: str) -> None:
        self._repository.delete(name)
