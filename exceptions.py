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

def update(self, number: Number, customer: Customer) -> Customer:
    for i, c in enumerate(self._customers):
        if c.number == number:
            self._customers[i] = customer
            return customer

    raise CustomerNotFoundError(number)


''' Custom BakedGood Exception Handeling '''

''' Custom Purchase Exception Handeling '''