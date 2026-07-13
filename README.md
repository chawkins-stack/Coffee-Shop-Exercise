# Coffee Shop Exercise

This repository models a small coffee shop domain using Python classes, repositories, and service-layer abstractions. It is organized around customers, drinks, baked goods, ingredients, and purchases.

## Project Goals

The project is designed to demonstrate:

- domain modeling with Python dataclasses
- repository patterns for data access
- service-layer orchestration for business logic
- exception handling for duplicate or missing resources

## Main Domain Models

- Customer: stores customer identity and lifetime spending information
- Drink: represents a drink with ingredients, production cost, markup, and sale price
- Baked_good: represents a baked item with cost, markup, vendor, allergens, and sale price
- Purchase: tracks purchases, associated items, timestamp, and total cost
- Ingredient: models the ingredients used by drinks

## Project Structure

- models/: domain entities and data models
- repositories/: persistence-style classes for each model
- services/: business logic and operations over the repository layer
- exceptions.py: custom exceptions for duplicate and missing entities

## Example Concepts Covered

- creating and managing customers
- tracking drink and baked good inventory concepts
- building purchase records from product selections
- handling duplicate or missing item scenarios with custom exceptions

## Getting Started

Run the project from the repository root with Python:

```bash
python main.py
```

If a main entry point is not yet present, you can still explore the models and services directly from the Python modules in the project.

## Notes

This is an exercise repository, so the implementation focuses on structure and object-oriented design rather than a full production-ready application.
