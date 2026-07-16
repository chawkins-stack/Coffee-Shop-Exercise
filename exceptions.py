''' Custom Drink Exception Handeling '''
from numbers import Number

from models.customer import Customer


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


''' Custom Purchase Exception Handeling '''
class DuplicateBakedGoodError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Baked good '{name}' already exists.")

class BakedGoodNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Baked good '{name}' was not found.")

    
''' Custom Purchase Exception Handeling '''
class DuplicatePurchaseError(Exception):
    def __init__(self, timestamp: str):
        super().__init__(f"Purchase with timestamp '{timestamp}' already exists.")

class PurchaseNotFoundError(Exception):
    def __init__(self, timestamp: str):
        super().__init__(f"Purchase with timestamp '{timestamp}' was not found.")
