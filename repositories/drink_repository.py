from models.drink import Drink
from numbers import Number

class DrinkRepository:
    def __init__(self):
        self._drinks: list[Drink] = []
        self._next_id = 1301

    def get_all(self) -> list[Drink]:
        return self._drinks

    def get_by_id(self, id: Number) -> Drink | None:
        return next((d for d in self._drinks if d.id == id), None)

    def get_by_name(self, name: str) -> Drink | None:
        name = name.lower()
        for drink in self._drinks:
            if drink.name.lower() == name:
                return drink
        return None

    def add(self, drink: Drink) -> Drink:
        drink.id = self._next_id
        self._next_id += 1
        self._drinks.append(drink)
        return drink

    def update(self, id: Number, drink: Drink) -> Drink | None:
        for i, d in enumerate(self._drinks):
            if d.id == id:
                self._drinks[i] = drink
                return drink
        return None

    def delete(self, name: str) -> bool:
        drink = self.get_by_id(name)
        if drink:
            self._drinks.remove(drink)
            return True

        return False
