from numbers import Number
import re

from repositories.customer_repository import Customer_Repository
from models.customer import Customer
from exceptions import DuplicateCustomerError, DuplicateCutomerError

class CustomerService:
    def __init__(self, repository: Customer_Repository):
        self._repository = repository

    def create_customer(self, customer: Customer) -> Customer:
        if self._repository.get_by_id(customer.id) is not None:
            raise DuplicateCustomerError(f"Customer with ID '{customer.id}' already exists.")

        if not self.is_valid_email(customer.email):
            raise ValueError(f"Invalid email format: '{customer.email}'")

        if not self.is_unique_email(customer.email):
            raise DuplicateCustomerError(f"Customer with email '{customer.email}' already exists.")

        return self._repository.add(customer)

    def get_all_customers(self) -> list[Customer]:
        return self._repository.get_all()

    def get_by_id(self, id: Number) -> Customer:
        return self._repository.get_by_id(id)

    def add_customer(self, customer: Customer) -> Customer:
        return self._repository.add(customer)

    def update_customer(self, customer: Customer) -> Customer:
        return self._repository.update(customer)

    def delete_customer(self, id: Number) -> None:
        self._repository.delete(id)

    def is_valid_email(self, email: str) -> bool:
        pattern = r"^[A-Za-z0-9._%+-]{1,30}@[A-Za-z0-9-]{1,30}\.[A-Za-z]{2,15}$"
        return re.match(pattern, email) is not None

    def is_unique_email(self, email: str) -> bool:
        existing_customer = self._repository.get_by_email(email)
        return existing_customer is None
