from datetime import datetime, timezone
from decimal import Decimal

# Import models
from exceptions import BakedGoodNotFoundError, CustomerNotFoundError, DrinkNotFoundError, DuplicateBakedGoodError, DuplicateCustomerError, DuplicateDrinkError, DuplicateIngredientError, DuplicatePurchaseError, IngredientNotFoundError, InvalidBakedGoodError, InvalidDrinkError, PurchaseNotFoundError
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

def update_customer_ui():
    print("\n--- Update Customer ---")

    customers = customer_service.get_all_customers()
    for c in customers:
        print(f"{c.id}. {c.name} - {c.email}")

    try:
        customer_id = int(input("Enter customer ID: "))
        customer = customer_service.get_by_id(customer_id)
    except CustomerNotFoundError as e:
        print(e)
        return

    print("Leave fields blank to keep current values.")

    new_name = input(f"New name ({customer.name}): ").strip() or customer.name
    new_email = input(f"New email ({customer.email}): ").strip() or customer.email

    customer.name = new_name
    customer.email = new_email

    customer_service.update_customer(customer)
    print("Customer updated.\n")

def delete_customer_ui():
    print("\n--- Delete Customer ---")

    customers = customer_service.get_all_customers()
    for c in customers:
        print(f"{c.id}. {c.name} - {c.email}")

    try:
        customer_id = int(input("Enter customer ID to delete: "))
        customer = customer_service.get_by_id(customer_id)
    except CustomerNotFoundError as e:
        print(e)
        return

    confirm = input(f"Delete customer '{customer.name}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    customer_service.delete_customer(customer_id)
    print("Customer deleted.\n")

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

def update_drink_ui():
    print("\n--- Update Drink ---")
    drinks = drink_service.get_all_drinks()

    for d in drinks:
        print(f"{d.id}. {d.name} - ${d.sale_price}")

    try:
        drink_id = int(input("Enter drink ID to update: "))
        drink = drink_service.get_drink(drink_id)
    except DrinkNotFoundError as e:
        print(e)
        return

    print("Leave fields blank to keep current values.")

    new_name = input(f"New name ({drink.name}): ").strip() or drink.name
    new_markup = input(f"New markup ({drink.markup_percentage}): ").strip()
    new_markup = Decimal(new_markup) if new_markup else drink.markup_percentage

    drink.name = new_name
    drink.markup_percentage = new_markup

    try:
        drink_service.update_drink(drink)
        print("Drink updated.\n")
    except DuplicateDrinkError as e:
        print(e)

def delete_drink_ui():
    print("\n--- Delete Drink ---")

    drinks = drink_service.get_all_drinks()
    for d in drinks:
        print(f"{d.id}. {d.name} - ${d.sale_price}")

    try:
        drink_id = int(input("Enter drink ID to delete: "))
        drink = drink_service.get_drink(drink_id)
    except DrinkNotFoundError as e:
        print(e)
        return

    confirm = input(f"Delete drink '{drink.name}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    drink_service.delete_drink(drink_id)
    print("Drink deleted.\n")

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

def update_baked_good_ui():
    print("\n--- Update Baked Good ---")

    baked_goods = baked_good_service.get_all_baked_goods()
    for b in baked_goods:
        print(f"{b.id}. {b.name} - ${b.sale_price}")

    try:
        bg_id = int(input("Enter baked good ID: "))
        baked_good = baked_good_service.get_baked_good(bg_id)
    except BakedGoodNotFoundError as e:
        print(e)
        return

    print("Leave fields blank to keep current values.")

    new_name = input(f"New name ({baked_good.name}): ").strip() or baked_good.name
    new_markup = input(f"New markup ({baked_good.marking_percentage}): ").strip()
    new_markup = Decimal(new_markup) if new_markup else baked_good.marking_percentage

    baked_good.name = new_name
    baked_good.marking_percentage = new_markup

    try:
        baked_good_service.update_baked_good(baked_good)
        print("Baked good updated.\n")
    except DuplicateBakedGoodError as e:
        print(e)

def delete_baked_good_ui():
    print("\n--- Delete Baked Good ---")

    baked_goods = baked_good_service.get_all_baked_goods()
    for b in baked_goods:
        print(f"{b.id}. {b.name} - ${b.sale_price}")

    try:
        bg_id = int(input("Enter baked good ID to delete: "))
        baked_good = baked_good_service.get_baked_good(bg_id)
    except BakedGoodNotFoundError as e:
        print(e)
        return

    confirm = input(f"Delete baked good '{baked_good.name}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    baked_good_service.delete_baked_good(bg_id)
    print("Baked good deleted.\n")

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

def delete_ingredient_ui():
    print("\n--- Delete Ingredient ---")

    ingredients = ingredient_service.get_all_ingredients()
    for i in ingredients:
        print(f"{i.id}. {i.name} - {i.unit_amount}{i.unit_of_measure} @ ${i.purchasing_cost}")

    try:
        ing_id = int(input("Enter ingredient ID to delete: "))
        ingredient = ingredient_service.get_by_id(ing_id)
    except IngredientNotFoundError as e:
        print(e)
        return

    confirm = input(f"Delete ingredient '{ingredient.name}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    ingredient_service.delete_ingredient(ing_id)
    print("Ingredient deleted.\n")

def update_ingredient_ui():
    print("\n--- Update Ingredient ---")

    ingredients = ingredient_service.get_all_ingredients()
    for i in ingredients:
        print(f"{i.id}. {i.name} - {i.unit_amount}{i.unit_of_measure} @ ${i.purchasing_cost}")

    try:
        ing_id = int(input("Enter ingredient ID: "))
        ingredient = ingredient_service.get_by_id(ing_id)
    except IngredientNotFoundError as e:
        print(e)
        return

    print("Leave fields blank to keep current values.")

    new_name = input(f"New name ({ingredient.name}): ").strip() or ingredient.name
    new_cost = input(f"New cost ({ingredient.purchasing_cost}): ").strip()
    new_cost = Decimal(new_cost) if new_cost else ingredient.purchasing_cost

    ingredient.name = new_name
    ingredient.purchasing_cost = new_cost

    ingredient_service.update_ingredient(ingredient)
    print("Ingredient updated.\n")

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

def update_purchase_ui():
    print("\n--- Update Purchase ---")

    purchases = purchase_service.get_all_purchases()
    for p in purchases:
        print(f"{p.id}. {p.Customer.name} - {len(p.items)} items - {p.timestamp}")

    try:
        purchase_id = int(input("Enter purchase ID: "))
        purchase = purchase_service.get_purchase(purchase_id)
    except PurchaseNotFoundError as e:
        print(e)
        return

    print("Leave fields blank to keep current values.")

    customers = customer_service.get_all_customers()
    for c in customers:
        print(f"{c.id}. {c.name}")

    new_customer_id = input(f"New customer ID ({purchase.Customer.id}): ").strip()
    if new_customer_id:
        try:
            purchase.Customer = customer_service.get_by_id(int(new_customer_id))
        except CustomerNotFoundError as e:
            print(e)
            return

    purchase_service.update_purchase(purchase)
    print("Purchase updated.\n")

def delete_purchase_ui():
    print("\n--- Delete Purchase ---")

    purchases = purchase_service.get_all_purchases()
    for p in purchases:
        print(f"{p.id}. {p.Customer.name} - {len(p.items)} items - {p.timestamp}")

    try:
        purchase_id = int(input("Enter purchase ID to delete: "))
        purchase = purchase_service.get_purchase(purchase_id)
    except PurchaseNotFoundError as e:
        print(e)
        return

    confirm = input(f"Delete purchase #{purchase.id}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    purchase_service.delete_purchase(purchase_id)
    print("Purchase deleted.\n")

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
        print("3. Update Customer")
        print("4. Delete Customer")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_customer_ui()
        elif choice == "2":
            view_customers_ui()
        elif choice == "3":
            update_customer_ui()
        elif choice == "4":
            delete_customer_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def drink_menu():
    while True:
        print("\n--- Drink Menu ---")
        print("1. Create Drink")
        print("2. View Drinks")
        print("3. Update Drink")
        print("4. Delete Drink")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_drink_ui()
        elif choice == "2":
            view_drinks_ui()
        elif choice == "3":
            update_drink_ui()
        elif choice == "4":
            delete_drink_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


def baked_good_menu():
    while True:
        print("\n--- Baked Goods Menu ---")
        print("1. Create Baked Good")
        print("2. View Baked Goods")
        print("3. Update Baked Good")
        print("4. Delete Baked Good")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_baked_good_ui()
        elif choice == "2":
            view_baked_goods_ui()
        elif choice == "3":
            update_baked_good_ui()
        elif choice == "4":
            delete_baked_good_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def ingredient_menu():
    while True:
        print("\n--- Ingredient Menu ---")
        print("1. Add Ingredient")
        print("2. View Ingredients")
        print("3. Update Ingredient")
        print("4. Delete Ingredient")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_ingredient_ui()
        elif choice == "2":
            view_ingredients_ui()
        elif choice == "3":
            update_ingredient_ui()
        elif choice == "4":
            delete_ingredient_ui()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


def purchase_menu():
    while True:
        print("\n--- Purchase Menu ---")
        print("1. Create Purchase")
        print("2. View Purchases")
        print("3. Update Purchase")
        print("4. Delete Purchase")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_purchase_ui()
        elif choice == "2":
            view_purchases_ui()
        elif choice == "3":
            update_purchase_ui()
        elif choice == "4":
            delete_purchase_ui()
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
