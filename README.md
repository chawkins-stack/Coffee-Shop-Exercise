# Coffee Shop Exercise — Python Small Group Project (Express‑O)

This repository is a small Python exercise that models a coffee shop domain using object-oriented programming. It is organized around domain models, repositories, services, and custom exceptions to demonstrate a layered design.

## What the project covers

The project includes concepts for:

- customers and customer records
- drinks with ingredients and pricing
- baked goods with vendor and allergen details
- purchases that group items into an order
- simple in-memory storage with repository-style classes

## Project structure

```text
Coffee-Shop-Exercise/
├── models/
│   ├── customer.py
│   ├── drink.py
│   ├── baked_good.py
│   ├── purchase.py
│   └── ingredients.py
├── repositories/
│   ├── customer_repository.py
│   ├── drink_repository.py
│   ├── ingredients_repository.py
│   ├── baked_good.py
│   └── purchase.py
├── services/
│   ├── customer_service.py
│   ├── drink_service.py
│   ├── ingredients_services.py
│   ├── baked_good_service.py
│   └── purchase_service.py
├── exceptions.py
└── README.md
```

## Core domain models

- Customer: stores an ID, name, email, and lifetime spending information
- Drink: represents a drink with ingredients, production cost, markup, and sale price
- Baked_good: represents a baked item with purchasing cost, markup, vendor, allergens, and sale price
- Purchase: tracks a purchase with a timestamp, items, total cost, and customer
- Ingredient: models the ingredient used in drinks

## Repositories and services

The repository layer provides in-memory storage and basic CRUD-style operations such as add, lookup, update, and delete. The service layer builds on top of that by adding business rules and error handling.

## Exceptions

The project includes custom exceptions for common situations such as:

- DuplicateDrinkError
- DrinkNotFoundError
- CustomerNotFoundError

## Getting started

You can explore the project directly from Python by importing the models, repositories, and services:

```python
from models.drink import Drink
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService

repo = DrinkRepository()
service = DrinkService(repo)

drink = Drink(
    id=1,
    name="Latte",
    ingredients=[],
    cost_to_produce=2.0,
    markup_percentage=0.5,
    sale_price=3.0,
)

service.create_drink(drink)
print(service.get_all_drinks())
```

This project is for educational use.  

This is an educational repository focused on object-oriented design and layered architecture rather than a full production-ready application.

## Contributors
<a href="[https://github.com/wshepelak-catalyte/Patient-Intake-Console-App/graphs/contributors]">
  <img src="https://contrib.rocks/image?repo=chawkins-stack/Coffee-Shop-Excercise"/>
</a>
