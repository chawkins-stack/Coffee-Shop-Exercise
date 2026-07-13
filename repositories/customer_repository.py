# repositories/customer_repository.py
from models.customer import Customer
from models.drink import Drink

class CustomerRepository:
    def __init__(self):
        self._customers: list[Customer] = []

    def get_all(self) -> list[Customer]:
        return self._customers

    def get_by_id(self, name: str) -> Customer | None:
        return next((c for c in self._customers if c.name == name), None)

    def add(self, customer: Customer) -> Customer:
        self._customers.append(customer)
        return customer

    def update(self, name: str, customer: Customer) -> Customer | None:
        ...

    def delete(self, name: str) -> bool:
        ...