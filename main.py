from datetime import datetime, timezone
from decimal import Decimal

# Import models
from models.customer import Customer
from models.baked_good import BakedGood
from models.purchase import Purchase
from models.drink import Drink
from models.ingredients import Ingredient

# Import repositories
from repositories.customer_repository import CustomerRepository
from repositories.baked_good_repository import BakedGoodRepository
from repositories.purchase_repository import PurchaseRepository
from repositories.drink_repository import DrinkRepository
from repositories.ingredients_repository import IngredientRepository

# Import services
from services.customer_service import CustomerService
from services.purchase_service import PurchaseService
from services.drink_service import DrinkService
from services.baked_good_service import BakedGoodService
from services.ingredients_services import IngredientService

# Initialize repos
customer_repo = CustomerRepository()
purchase_repo = PurchaseRepository()
drink_repo = DrinkRepository()
baked_good_repo = BakedGoodRepository()
ingredient_repo = IngredientRepository()

# Initialize services
customer_service = CustomerService(customer_repo)
purchase_service = PurchaseService(purchase_repo, customer_service)
drink_service = DrinkService(drink_repo)
baked_good_service = BakedGoodService(baked_good_repo)
ingredient_service = IngredientService(ingredient_repo)


def create_customer_ui():
    print("\n--- Create Customer ---")
    name = input("Name: ")
    email = input("Email: ")

    customer = Customer(name=name, email=email, lifetime_spent=0)
    customer_service.create_customer(customer)

    print(f"Customer '{name}' created.\n")


def create_drink_ui():
    print("\n--- Create Drink ---")
    name = input("Drink name: ")
    raw_ingredients = input("List ingredients (comma-separated): ")
    ingredients = [
        Ingredient(name=i.strip(), purchasing_cost=0, unit_amount=0, unit_of_measure=0)
        for i in raw_ingredients.split(",") if i.strip()
    ]

    cost_to_produce = Decimal(input("Cost to produce: "))
    markup_percentage = Decimal(input("Markup percentage (e.g., 0.25 for 25%): "))

    drink = Drink(
        name=name,
        ingredients=ingredients,
        cost_to_produce=cost_to_produce,
        markup_percentage=markup_percentage
    )

    drink_service.create_drink(drink)

    print(f"Drink '{name}' created.\n")


def create_baked_good_ui():
    print("\n--- Create Baked Good ---")

    name = input("Item name: ")
    purchasing_cost = Decimal(input("Cost to purchase: "))
    markup_percentage = Decimal(input("Markup percentage (e.g., 0.25 for 25%): "))
    vendor_name = input("Vendor name: ")

    raw_allergens = input("List allergens (comma-separated): ")
    allergens = [ a.strip() for a in raw_allergens.split(",") if a.strip()]

    baked_good = BakedGood(
        name=name,
        purchasing_cost=purchasing_cost,
        marking_percentage=markup_percentage,
        vendor_name=vendor_name,
        allergens=allergens
    )
    baked_good_service.create_baked_good(baked_good)

    print(f"Baked good '{name}' created.\n")


def add_ingredient_ui():
    print("\n--- Add Ingredient ---")
    name = input("Ingredient name: ")

    purchase_cost = Decimal(input("Purchase Cost: "))
    unit_amount = Decimal(input("Unit amount (e.g., 1.5): "))
    unit_of_measure = input("Unit of measure (e.g., kg, ml, oz): ")

    ingredient = Ingredient(
        name=name,
        purchasing_cost=purchase_cost,
        unit_amount=unit_amount,
        unit_of_measure=unit_of_measure
    )

    ingredient_service.create_ingredient(ingredient)

    print(f"Ingredient '{name}' added.\n")


def create_purchase_ui():
    print("\n--- Create Purchase ---")

    # Select customer
    customers = customer_service.get_all_customers()
    print("Customers:")
    for c in customers:
        print(f"{c.id}. {c.name}")

    customer_id = int(input("Choose customer ID: "))
    customer = customer_service.get_by_id(customer_id)

    # Select items
    print("\nDrinks:")
    drinks = drink_service.get_all_drinks()
    for d in drinks:
        print(f"{d.id}. {d.name} - ${d.sale_price}")

    print("\nBaked Goods:")
    baked_goods = baked_good_service.get_all_baked_goods()
    for b in baked_goods:
        print(f"{b.id}. {b.name} - ${b.sale_price}")

    item_ids = input("Enter item IDs separated by commas: ")
    item_ids = [int(x.strip()) for x in item_ids.split(",")]

    purchase = Purchase(
        Customer=customer_service.get_by_id(customer_id),
        items=item_ids,
        timestamp=datetime.now(timezone.utc)
    )

    purchase_service.create_purchase(purchase)
    print("Purchase created.\n")


def view_customers_ui():
    print("\n--- Customers ---")
    for c in customer_service.get_all_customers():
        print(f"{c.id}: {c.name} ({c.email}) - Spent: ${c.lifetime_spent}")
    print()


def view_drinks_ui():
    print("\n--- Drinks ---")
    for d in drink_service.get_all_drinks():
        print(f"{d.id}: {d.name} - ${d.sale_price}")
    print()


def view_ingredients_ui():
    print("\n--- Ingredients ---")
    for i in ingredient_service.get_all_ingredients():
        print(f"{i.id}: {i.name}")
    print()


def view_baked_goods_ui():
    print("\n--- Baked Goods ---")
    for b in baked_good_service.get_all_baked_goods():
        print(f"{b.id}: {b.name} - ${b.sale_price}")
    print()


def view_purchases_ui():
    print("\n--- Purchases ---")
    for p in purchase_service.get_all_purchases():
        print(f"Purchase {p.id} by Customer {p.customer_id} at {p.timestamp}")
    print()


def main_menu():
    while True:
        print("""
-----------------------------------
        CAFE MANAGEMENT SYSTEM
-----------------------------------
1. Create Customer
2. Create Drink
3. Create Baked Good
4. Add Ingredient
5. Create Purchase
6. View Customers
7. View Drinks
8. View Ingredients
9. View Baked Goods
10. View Purchases
0. Exit
-----------------------------------
""")

        choice = input("Choose an option: ")

        if choice == "1":
            create_customer_ui()
        elif choice == "2":
            create_drink_ui()
        elif choice == "3":
            create_baked_good_ui()
        elif choice == "4":
            add_ingredient_ui()
        elif choice == "5":
            create_purchase_ui()
        elif choice == "6":
            view_customers_ui()
        elif choice == "7":
            view_drinks_ui()
        elif choice == "8":
            view_ingredients_ui()
        elif choice == "9":
            view_baked_goods_ui()
        elif choice == "10":
            view_purchases_ui()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main_menu()
