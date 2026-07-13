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