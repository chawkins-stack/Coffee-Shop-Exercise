# repositories/ingredients_repository.py
from numbers import Number

from models.ingredient import Ingredient


class IngredientRepository:
    def __init__(self):
        self._ingredient: list[Ingredient] = []
        self._next_id = 4901

    def get_all(self) -> list[Ingredient]:
        return self._ingredient

    def get_by_id(self, id: Number) -> Ingredient | None:
        return next((ingredient for ingredient in self._ingredient if ingredient.id == id), None)

    def get_by_name(self, name: str) -> Ingredient | None:
        return next((ingredient for ingredient in self._ingredient if ingredient.name == name), None)

    def add(self, ingredient: Ingredient) -> Ingredient:
        ingredient.id = self._next_id
        self._next_id += 1
        
        self._ingredients.append(ingredient)
        return ingredient

    def update(self, id: Number, ingredient: Ingredient) -> Ingredient | None:
        for i, existing_ingredient in enumerate(self._ingredients):
            if existing_ingredient.id == id:
                ingredient.id = id
                self._ingredients[i] = ingredient
                return ingredient
            return None

    def delete(self, id: Number) -> bool:
        ingredient = self.get_by_id(id)

        if ingredient:
            self._ingredients.remove(ingredient)
            return True

        return False
