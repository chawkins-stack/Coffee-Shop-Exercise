from datetime import datetime, timezone
from decimal import Decimal

# Import models
from exceptions import BakedGoodNotFoundError, DrinkNotFoundError, DuplicateBakedGoodError, DuplicateCustomerError, DuplicateDrinkError, DuplicateIngredientError, DuplicatePurchaseError, InvalidBakedGoodError, InvalidDrinkError
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

    try:
        name = input("Name: ")
        email = input("Email: ")

        customer = Customer(name=name, email=email, lifetime_spent=0)
        customer_service.create_customer(customer)

        print(f"Customer '{name}' created.\n")

    except DuplicateCustomerError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}\n")

def create_drink_ui():
    print("\n--- Create Drink ---")

    try:
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

    except DuplicateDrinkError as e:
        print(e)

    except InvalidDrinkError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}\n")

def create_baked_good_ui():
    print("\n--- Create Baked Good ---")

    try:
        name = input("Item name: ")
        purchasing_cost = Decimal(input("Cost to purchase: "))
        markup_percentage = Decimal(input("Markup percentage (e.g., 0.25 for 25%): "))
        vendor_name = input("Vendor name: ")

        raw_allergens = input("List allergens (comma-separated): ")
        allergens = [a.strip() for a in raw_allergens.split(",") if a.strip()]

        baked_good = BakedGood(
            name=name,
            purchasing_cost=purchasing_cost,
            marking_percentage=markup_percentage,
            vendor_name=vendor_name,
            allergens=allergens
        )

        baked_good_service.create_baked_good(baked_good)
        print(f"Baked good '{name}' created.\n")

    except DuplicateBakedGoodError as e:
        print(e)

    except InvalidBakedGoodError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}\n")

def add_ingredient_ui():
    print("\n--- Add Ingredient ---")

    try:
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

    except DuplicateIngredientError as e:
        print(e)

    except InvalidDrinkError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}\n")

def create_purchase_ui():
    print("\n--- Create Purchase ---")

    try:
        customers = customer_service.get_all_customers()
        print("Customers:")
        for c in customers:
            print(f"{c.id}. {c.name}")

        customer_id = int(input("Choose customer ID: "))
        customer = customer_service.get_by_id(customer_id)

        print("\nDrinks:")
        drinks = drink_service.get_all_drinks()
        for d in drinks:
            print(f"{d.id}. {d.name} - ${d.sale_price}")

        print("\nBaked Goods:")
        baked_goods = baked_good_service.get_all_baked_goods()
        for b in baked_goods:
            print(f"{b.id}. {b.name} - ${b.sale_price}")

        item_ids = [int(x.strip()) for x in input("Enter item IDs separated by commas: ").split(",")]

        items = []
        for item_id in item_ids:
            try:
                items.append(drink_service.get_drink(item_id))
                continue
            except DrinkNotFoundError:
                pass

            try:
                items.append(baked_good_service.get_baked_good(item_id))
                continue
            except BakedGoodNotFoundError:
                pass

            print(f"Item ID {item_id} was not found.")

        purchase = Purchase(
            Customer=customer,
            items=items,
            timestamp=datetime.now(timezone.utc)
        )

        created = purchase_service.create_purchase(purchase)
        receipt = purchase_service.format_receipt(created)
        print(receipt)
        print("Purchase created.\n")

    except DuplicatePurchaseError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}\n")

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
        print(f"Purchase {p.id} by Customer {p.Customer.id} at {p.timestamp}")
    print()

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create Customer")
        print("2. View Customers")
        print("0. Back")
        print("-----------------------\n")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_customer_ui()
        elif choice == "2":
            view_customers_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def drink_menu():
    while True:
        print("\n--- Drink Menu ---")
        print("1. Create Drink")
        print("2. View Drinks")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_drink_ui()
        elif choice == "2":
            view_drinks_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def baked_good_menu():
    while True:
        print("\n--- Baked Goods Menu ---")
        print("1. Create Baked Good")
        print("2. View Baked Goods")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_baked_good_ui()
        elif choice == "2":
            view_baked_goods_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def ingredient_menu():
    while True:
        print("\n--- Ingredient Menu ---")
        print("1. Add Ingredient")
        print("2. View Ingredients")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_ingredient_ui()
        elif choice == "2":
            view_ingredients_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def purchase_menu():
    while True:
        print("\n--- Purchase Menu ---")
        print("1. Create Purchase")
        print("2. View Purchases")
        print("0. Back")
        print("-----------------------------------")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_purchase_ui()
        elif choice == "2":
            view_purchases_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


def seed_demo_data():
    print("\nLoading demo data...")

    # --- Customers ---
    try:
        customer_service.create_customer(Customer("Arlette Diaz", "adiaz@gmail.com", 0))
        customer_service.create_customer(Customer("Ciera Watts", "cwatts@gmail.com", 0))
        customer_service.create_customer(Customer("Chamar Hawkins", "chawkins@gmail.com", 0))
        customer_service.create_customer(Customer("Brennan Idor", "bidor@gmail.com", 0))
    except Exception as e:
        print(f"Customer seed error: {e}")

    # --- Ingredients ---
    try:
        ingredient_service.create_ingredient(Ingredient("Milk", Decimal("1.00"), 1, "cup"))
        ingredient_service.create_ingredient(Ingredient("Espresso", Decimal("0.50"), 1, "shot"))
        ingredient_service.create_ingredient(Ingredient("Chocolate", Decimal("0.75"), 1, "tbsp"))
    except Exception as e:
        print(f"Ingredient seed error: {e}")

    # --- Drinks ---
    try:
        latte = Drink(
            name="Latte",
            ingredients=[
                Ingredient("Milk", 1, 1, "cup"),
                Ingredient("Espresso", 0.5, 1, "shot")
            ],
            cost_to_produce=Decimal("1.50"),
            markup_percentage=Decimal("0.50")
        )
        drink_service.create_drink(latte)

        mocha = Drink(
            name="Mocha",
            ingredients=[
                Ingredient("Milk", 1, 1, "cup"),
                Ingredient("Espresso", 0.5, 1, "shot"),
                Ingredient("Chocolate", 0.75, 1, "tbsp")
            ],
            cost_to_produce=Decimal("2.00"),
            markup_percentage=Decimal("0.50")
        )
        drink_service.create_drink(mocha)

    except Exception as e:
        print(f"Drink seed error: {e}")

    # --- Baked Goods ---
    try:
        baked_good_service.create_baked_good(BakedGood(
            name="Croissant",
            purchasing_cost=Decimal("1.50"),
            marking_percentage=Decimal("0.50"),
            vendor_name="Bakery Co",
            allergens=["gluten", "dairy"]
        ))

        baked_good_service.create_baked_good(BakedGood(
            name="Blueberry Muffin",
            purchasing_cost=Decimal("2.25"),
            marking_percentage=Decimal("0.50"),
            vendor_name="Bakery Co",
            allergens=["gluten", "eggs"]
        ))
    except Exception as e:
        print(f"Baked good seed error: {e}")

    print("Demo data loaded.\n")

def main_menu():
    while True:
        print("""
-----------------------------------
        CAFE MANAGEMENT SYSTEM
-----------------------------------
1. Customers
2. Drinks
3. Baked Goods
4. Ingredients
5. Purchases
0. Exit
-----------------------------------
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            customer_menu()
        elif choice == "2":
            drink_menu()
        elif choice == "3":
            baked_good_menu()
        elif choice == "4":
            ingredient_menu()
        elif choice == "5":
            purchase_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    seed_demo_data()
    main_menu()
