''' Custom Drink Exception Handeling '''
class DuplicateDrinkError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' already exists.")

class DrinkNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' was not found.")

class InvalidDrinkError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

''' Custom Ingredient Exception Handeling '''
class DuplicateIngredientError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Ingredient '{name}' already exists.")

class IngredientNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Ingredient '{name}' was not found.")

''' Custom Customer Exception Handeling '''
class DuplicateCustomerError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Customer '{name}' already exists.")

class CustomerNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Customer '{name}' was not found.")

''' Custom BakedGood Exception Handeling '''

''' Custom Purchase Exception Handeling '''