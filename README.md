---

# Coffee Shop Exercise — Python Small Group Project (Express‑O)

A small-group Python project simulating a simple drink‑management system for a coffee shop.  
This application demonstrates clean architecture principles using:

- Repository pattern  
- Service layer  
- Custom exceptions  
- Domain models  
- In‑memory data storage  

It is designed for educational purposes and follows the structure outlined in the project’s Google Doc.

---

## Project Structure

```
Coffee-Shop-Exercise/
│
├── models/
│   └── drink.py              # Drink domain model
│
├── repositories/
│   └── drink_repository.py   # In‑memory CRUD repository
│
├── services/
│   └── drink_service.py      # Business logic + validation
│
├── exceptions.py             # Custom exception classes
│
└── main.py                   # (Optional) Entry point for testing
```

---

## Components Overview

### **Drink Model**
Represents a drink in the system.  
Typical fields include:

- `name`
- `size`
- `price`
- `ingredients`

---

### **DrinkRepository**
Handles **low‑level data operations** using an in‑memory list.

Supported operations:

- `get_all()` — return all drinks  
- `get_by_id(name)` — lookup by drink name  
- `add(drink)` — insert new drink  
- `update(name, drink)` — replace existing drink  
- `delete(name)` — remove drink  

This class contains **no business logic** — only raw data manipulation.

---

### **DrinkService**
Implements **business rules**, including:

- Preventing duplicate drinks  
- Validating existence before update/delete  
- Raising custom exceptions  
- Delegating storage to the repository  

Supported service methods:

- `create_drink(drink)`
- `get_all_drinks()`
- `get_drink(name)`
- `update_drink(name, updated)`
- `delete_drink(name)`

---

### **Custom Exceptions**
Located in `exceptions.py`:

```python
class DuplicateDrinkError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' already exists.")

class DrinkNotFoundError(Exception):
    def __init__(self, name: str):
        super().__init__(f"Drink '{name}' was not found.")
```

These ensure clean error handling and readable API responses.

---

## Getting Started

### **1. Clone the repository**

```bash
git clone https://github.com/chawkins-stack/Coffee-Shop-Excercise
cd Coffee-Shop-Excercise
```

### **2. Run the project**

If you have a `main.py`:

```bash
python main.py
```

Or run your own tests/interactions in a Python shell:

```python
from models.drink import Drink
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService

repo = DrinkRepository()
service = DrinkService(repo)

service.create_drink(Drink(name="Latte", size="Medium", price=4.50))
print(service.get_all_drinks())
```

---

## Testing

You can test the system by:

- Creating drinks  
- Attempting duplicates  
- Updating existing drinks  
- Deleting drinks  
- Triggering exceptions intentionally  

Example:

```python
try:
    service.create_drink(Drink("Latte"))
    service.create_drink(Drink("Latte"))  # Will raise DuplicateDrinkError
except DuplicateDrinkError as e:
    print(e)
```

---

## Learning Objectives

This project demonstrates:

- Clean separation of concerns  
- Repository pattern  
- Service layer validation  
- Custom exception handling  
- Python OOP fundamentals  
- Simple domain modeling  

Perfect for small‑group learning or introductory backend architecture.

---

## License

This project is for educational use.  

---