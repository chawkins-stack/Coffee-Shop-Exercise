# repositories/customer_repository.py
from numbers import Number

from models.customer import Customer
from models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self._customers: list[Customer] = []

    def get_all(self) -> list[Customer]:
        return self._customers

    def get_by_id(self, id: Number ) -> Customer | None:
        return next((c for c in self._customers if c.id == id), None)

    def get_by_name(self, name: str) -> Customer | None:
        return next((c for c in self._customers if c.name == name), None)

    def add(self, customer: Customer) -> Customer:
        self._customers.append(customer)
        return customer

    def update(self, id: Number, customer: Customer) -> Customer | None:
        for i, c in enumerate(self._customers):
            if c.id == id:
                self._customers[i] = customer
                return customer

    def delete(self, id: Number) -> bool:
        customer = self.get_by_id(id)
        if customer:
            self._customers.remove(customer)
            return True
        return False
