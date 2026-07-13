# repositories/ingredients_repository.py
from models.baked_good import Ingredient
from models.ingredients import Ingredient

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
        for i, d in enumerate(self._ingredients):
            if d.name == name:
                self._ingredients[i] = ingredient
                return ingredient

    def delete(self, name: str) -> bool:
        ingredient = self.get_by_id(name)
        if ingredient:
            self._ingredients.remove(ingredient)
            return True
        return False