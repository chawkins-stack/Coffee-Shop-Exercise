# services/customer_service.py
from models import drink
from repositories.customer_repository import customerRepository
from models.customer import Customer
from models.customer import customer
from exceptions import DuplicateDrinkError

class CustomerService:
    def __init__(self, repository: customerRepository):
        self._repository = repository

    def create_customer(self, customer: Customer) -> Customer:
        if self._repository.get_by_id(customer.name) is not None:
            raise DuplicateDrinkError(f"Customer '{customer.name}' already exists.")
        return self._repository.add(customer)
    
    def get_all_customers(self) -> list[Customer]:
        return self._repository.get_all()
    
    def get_customer(self, name: str) -> Customer:
        customer = self._repository.get_by_id(name)
        if customer is None:
            raise CustomerNotFoundError(name)
        return customer

    def update_customer(self, name: str, updated: Customer) -> Customer:
        customer = self._repository.update(name, updated)
        if customer is None:
            raise CustomerNotFoundError(name)
        return customer

    def delete_customer(self, name: str) -> bool:
        if not self._repository.delete(name):
            raise CustomerNotFoundError(name)
        return True