# repositories/ingredients_repository.py
from models.baked_good import Ingredient
from models.drink import Drink

class IngredientRepository:
    def __init__(self):
        self._ingredients: list[Ingredient] = []

    def get_all(self) -> list[Ingredient]:
        return self._ingredients

    def get_by_id(self, name: str) -> Ingredient | None:
        return next((d for d in self._ingredients if d.name == name), None)

    def add(self, ingredient: Ingredient) -> Ingredient:
        self._ingredients.append(ingredient)
        return ingredient

    def update(self, name: str, ingredient: Ingredient) -> Ingredient | None:
        ...

    def delete(self, name: str) -> bool:
        ...