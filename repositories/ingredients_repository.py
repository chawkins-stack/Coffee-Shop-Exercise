from models.ingredients import Ingredient


class IngredientRepository:
    def __init__(self):
        self._ingredients: list[Ingredient] = []

    def get_all(self) -> list[Ingredient]:
        return self._ingredients

    def get_by_id(self, name: str) -> Ingredient | None:
        return next((ingredient for ingredient in self._ingredients if ingredient.name == name), None)

    def get_by_name(self, name: str) -> Ingredient | None:
        return next((ingredient for ingredient in self._ingredients if ingredient.name == name), None)

    def add(self, ingredient: Ingredient) -> Ingredient:
        self._ingredients.append(ingredient)
        return ingredient

    def update(self, name: str, ingredient: Ingredient) -> Ingredient | None:
        for i, existing_ingredient in enumerate(self._ingredients):
            if existing_ingredient.name == name:
                self._ingredients[i] = ingredient
                return ingredient

    def delete(self, name: str) -> bool:
        ingredient = self.get_by_id(name)

        if ingredient:
            self._ingredients.remove(ingredient)
            return True

        return False
