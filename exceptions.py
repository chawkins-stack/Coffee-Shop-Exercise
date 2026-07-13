class DuplicateDrinkError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' already exists.")

class DrinkNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' was not found.")

class DuplicateIngredientError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Ingredient '{name}' already exists.")

class IngredientNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Ingredient '{name}' was not found.")

class DuplicateCustomerError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Customer '{name}' already exists.")

class CustomerNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Customer '{name}' was not found.")
