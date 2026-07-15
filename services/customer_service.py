from decimal import Decimal, ROUND_HALF_EVEN
from numbers import Number
import re

from repositories.customer_repository import CustomerRepository
from models.customer import Customer
from exceptions import CustomerNotFoundError, DuplicateCustomerError


class CustomerService:
    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    def create_customer(self, customer: Customer) -> Customer:

        if not self.is_valid_email(customer.email):
            raise CustomerNotFoundError(
                f"Customer with ID '{customer.id}' has an invalid email format."
            )

        if not self.is_unique_email(customer.email):
            raise DuplicateCustomerError(
                f"Customer with email '{customer.email}' already exists."
            )

        return self._repository.add(customer)

    def get_all_customers(self) -> list[Customer]:
        return self._repository.get_all()
    
    def get_by_email(self, email: str) -> Customer | None:
        return self._repository.get_by_email(email)

    def get_by_id(self, id: Number) -> Customer:
        return self._repository.get_by_id(id)

    def add_customer(self, customer: Customer) -> Customer:
        return self._repository.add(customer)

    def update_customer(self, customer: Customer) -> Customer:
        # Make sure the customer exists
        existing_customer = self._repository.get_by_id(customer.id)

        if existing_customer is None:
            raise CustomerNotFoundError(
                f"Customer with ID '{customer.id}' does not exist."
            )

        # Validate email format
        if not self.is_valid_email(customer.email):
            raise CustomerNotFoundError(
                f"Customer with ID '{customer.id}' has an invalid email format."
            )

        # Check that another customer doesn't already have this email
        customer_with_email = self._repository.get_by_email(customer.email)

        if (
            customer_with_email is not None
            and customer_with_email.id != customer.id
        ):
            raise DuplicateCustomerError(
                f"Customer with email '{customer.email}' already exists.")

        customer.lifetime_spend = Decimal(
            str(customer.lifetime_spend)
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_EVEN
        )
 
        return self._repository.update(customer.id, customer)

    def add_to_lifetime_spent(self, email: str, amount: Decimal) -> Customer | None:
        customer = self.get_by_email(email)
        if customer is None:
            return None
            
        if customer.lifetime_spend is None:
            customer.lifetime_spend = Decimal("0.00")

        customer.lifetime_spend = (
            Decimal(str(customer.lifetime_spend))
            + Decimal(str(amount))
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_EVEN
        )
        
        return self.update_customer(customer)

    def delete_customer(self, id: Number) -> None:
        self._repository.delete(id)

    def is_valid_email(self, email: str) -> bool:
        pattern = r"^[A-Za-z0-9._%+-]{1,30}@[A-Za-z0-9-]{1,30}\.[A-Za-z]{2,15}$"
        return re.match(pattern, email) is not None

    def is_unique_email(self, email: str) -> bool:
        existing_customer = self._repository.get_by_email(email)
        return existing_customer is None

    def _calculate_sale_price(
        self, customer: Customer, price: Decimal
    ) -> Decimal:
        baked_goods_total = sum(
            baked_good.price for baked_good in customer.baked_goods
        )

        drink_total = sum(
            drink.price for drink in customer.drinks
        )

        lifetime_spend_total = (
            customer.lifetime_spend
            + baked_goods_total
            + drink_total
        )

        return lifetime_spend_total.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_EVEN
        )