# repositories/customer_repository.py
from numbers import Number
from models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self._customers: list[Customer] = []
        self._next_id = 1201

    def get_all(self) -> list[Customer]:
        return self._customers

    def get_by_id(self, id: Number ) -> Customer | None:
        return next((customer for customer in self._customers if customer.id == id), None)

    def get_by_name(self, name: str) -> Customer | None:
        return next((customer for customer in self._customers if customer.name == name), None)
    
    def get_by_email(self, email: str) -> Customer | None:
        return next((customer for customer in self._customers if customer.email == email), None)

    def add(self, customer: Customer) -> Customer:
        customer.id = self._next_id
        self._next_id += 1
        self._customers.append(customer)
        return customer

    def update(self, id: Number, customer: Customer) -> Customer | None:
        for i, existing_customer in enumerate(self._customers):
            if existing_customer.id == id:
                self._customers[i] = customer
                return customer

    def delete(self, id: Number) -> bool:
        customer = self.get_by_id(id)
        if customer:
            self._customers.remove(customer)
            return True
        return False
    
