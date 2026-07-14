# Coffee Shop Exercise — Python Small Group Project

This repository is a small educational Python project for modeling a coffee shop domain using dataclasses, repositories, services, and custom exceptions. It is organized around a layered design to demonstrate object-oriented programming concepts.

## What the project includes

- Customer records with basic validation
- Drink models with ingredients and pricing
- Baked good models with vendor and allergen information
- Purchase models for grouping items together
- In-memory repositories for storing data
- Service classes for create, read, update, and delete-style operations
- Custom exceptions for duplicate or missing records

## Project structure

```text
Coffee-Shop-Exercise/
├── models/
│   ├── baked_good.py
│   ├── customer.py
│   ├── drink.py
│   ├── ingredients.py
│   └── purchase.py
├── repositories/
│   ├── baked_good_repository.py
│   ├── customer_repository.py
│   ├── drink_repository.py
│   ├── ingredients_repository.py
│   └── purchase_repository.py
├── services/
│   ├── baked_good_service.py
│   ├── customer_service.py
│   ├── drink_service.py
│   ├── ingredients_services.py
│   └── purchase_service.py
├── exceptions.py
├── requirements.txt
└── tests/
```

## Getting started

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest
```

## Example usage

```python
from models.customer import Customer
from repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService

repo = CustomerRepository()
service = CustomerService(repo)

customer = Customer(id=1, name="Ada", email="ada@example.com", lifetime_spent=0)
service.create_customer(customer)
```

## Contributors
<a href="https://github.com/wshepelak-catalyte/Patient-Intake-Console-App/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=chawkins-stack/Coffee-Shop-Excercise"/>
</a>
