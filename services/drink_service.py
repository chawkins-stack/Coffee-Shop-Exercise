from decimal import ROUND_HALF_EVEN, Decimal

from repositories.drink_repository import DrinkRepository
from models.drink import Drink
from exceptions import DuplicateDrinkError, DrinkNotFoundError, InvalidDrinkError

class DrinkService:
    def __init__(self, repository: DrinkRepository):
        self._repository = repository

    def create_drink(self, drink: Drink) -> Drink:
        # Duplicate name check
        if self._repository.get_by_name(drink.name) is not None:
            raise DuplicateDrinkError(drink.name)

        # Validation
        self._validate_drink(drink)

        # Calculate sale price
        drink.sale_price = self._calculate_sale_price(drink.price)

        return self._repository.add(drink)

    def get_all_drinks(self) -> list[Drink]:
        return self._repository.get_all()

    def get_drink(self, name: str) -> Drink:
        drink = self._repository.get_by_name(name)
        if drink is None:
            raise DrinkNotFoundError(name)
        return drink

    def update_drink(self, name: str, updated: Drink) -> Drink:
        # Validate updated drink
        self._validate_drink(updated)

        # Recalculate sale price
        updated.sale_price = self._calculate_sale_price(updated.price)

        drink = self._repository.update(name, updated)
        if drink is None:
            raise DrinkNotFoundError(name)
        return drink

    def delete_drink(self, name: str) -> bool:
        if not self._repository.delete(name):
            raise DrinkNotFoundError(name)
        return True

    # -------------------------
    # Validation Helpers
    # -------------------------

    def _validate_drink(self, drink: Drink):
        # Must contain ingredient
        if not drink.ingredients or len(drink.ingredients) == 0:
            raise InvalidDrinkError("Drink must contain at least one ingredient.")

        # Price must be valid
        if drink.price is None or drink.price <= 0:
            raise InvalidDrinkError("Drink must have a valid price greater than 0.")

        # Ingredients must be strings
        if any(not isinstance(i, str) for i in drink.ingredients):
            raise InvalidDrinkError("All ingredients must be strings.")

    # -------------------------
    # Sale Price Logic
    # -------------------------

    def _calculate_sale_price(self, drink: Drink, price: Decimal) -> Decimal:
        cost_to_produce = drink.cost_to_produce
        markup = drink.markup_percentage
        sale_price = cost_to_produce + (cost_to_produce * markup )

        return sale_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
