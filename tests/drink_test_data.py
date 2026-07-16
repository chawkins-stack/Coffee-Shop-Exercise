from models.drink import Drink
from repositories.drink_repository import DrinkRepository
from ingredient_test_data import i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16, i_17

d_00 = Drink(
    3000,
    "Classic Espresso",
    [i_00, i_01],
    0.45,
    2.33,
    1.50,
)
d_01 = Drink(
    3001,
    "Vanilla Latte",
    [i_00, i_02, i_03],
    0.95,
    2.89,
    3.70,
)
d_02 = Drink(
    3002,
    "Caramel Macchiato",
    [i_00, i_02, i_03, i_04],
    1.10,
    2.64,
    4.00,
)
d_03 = Drink(
    3003,
    "Cold Brew",
    [i_01, i_05],
    0.60,
    3.17,
    2.50,
)
d_04 = Drink(
    3004,
    "Matcha Green Tea Latte",
    [i_02, i_06, i_08],
    1.35,
    2.26,
    4.40,
)
d_05 = Drink(
    3005,
    "Mocha Frappe",
    [i_00, i_02, i_08, i_09, i_10],
    1.50,
    2.00,
    4.50,
)
d_06 = Drink(
    3006,
    "Chai Tea Latte",
    [i_02, i_11, i_12],
    1.05,
    2.71,
    3.90,
)
d_07 = Drink(
    3007,
    "Hot Chocolate",
    [i_02, i_10, i_13, i_14],
    0.80,
    2.50,
    2.80,
)
d_08 = Drink(
    3008,
    "Iced Americano",
    [i_00, i_01, i_09],
    0.50,
    2.40,
    1.70,
)
d_09 = Drink(
    3009,
    "Lavender Honey Oat Milk Latte",
    [i_00, i_07, i_15, i_16],
    1.60,
    2.19,
    5.10,
)

def drink_dataset():
    drinks = DrinkRepository()
    drink_instances = [globals()[f"d_{index:02d}"] for index in range (10)]
    for drink in drink_instances:
        drinks.add(drink)
    return drinks
