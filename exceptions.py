class DuplicateDrinkError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' already exists.")

class DrinkNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' was not found.")
