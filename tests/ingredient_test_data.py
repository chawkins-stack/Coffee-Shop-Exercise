from models.ingredients import Ingredient
from repositories.ingredients_repository import IngredientRepository

i_00 = Ingredient(
    4000,
    "Espresso Beans",
    18.00,
    2,
    "lb"
)
i_01 = Ingredient(
    4001,
    "Water",
    1.20,
    1,
    "gallon"
)
i_02 = Ingredient(
    4002,
    "Whole Milk",
    4.10,
    1,
    "gallon"
)
i_03 = Ingredient(
    4003,
    "Vanilla Syrup",
    9.50,
    750,
    "ml"
)
i_04 = Ingredient(
    4004,
    "Caramel Drizzle",
    8.75,
    500,
    "ml"
)
i_05 = Ingredient(
    4005,
    "Coarse Ground Coffee",
    16.50,
    2,
    "lb"
)
i_06 = Ingredient(
    4006,
    "Matcha Powder",
    22.00,
    1,
    "lb"
)
i_07 = Ingredient(
    4007,
    "Honey",
    7.25,
    24,
    "oz"
)
i_08 = Ingredient(
    4008,
    "Chocolate Syrup",
    6.90,
    750,
    "ml"
)
i_09 = Ingredient(
    4009,
    "Ice",
    2.00,
    10,
    "lb"
)
i_10 = Ingredient(
    4010,
    "Whipped Cream",
    5.40,
    32,
    "oz"
)
i_11 = Ingredient(
    4011,
    "Chai Concentrate",
    11.00,
    32,
    "oz"
)
i_12 = Ingredient(
    4012,
    "Cinnamon",
    4.50,
    12,
    "oz"
)
i_13 = Ingredient(
    4013,
    "Cocoa Powder",
    6.75,
    16,
    "oz"
)
i_14 = Ingredient(
    4014,
    "Sugar",
    3.20,
    4,
    "lb"
)
i_15 = Ingredient(
    4015,
    "Oat Milk",
    5.60,
    64,
    "fl oz"
)
i_16 = Ingredient(
    4016,
    "Lavendar Syrup",
    10.25,
    750,
    "ml"
)

def ingredient_dataset():
    ingredients = IngredientRepository()
    ingredient_instances = [globals()[f"i_{index:02d}"] for index in range (17)]
    for ingredient in ingredient_instances:
        ingredients.add(ingredient)
    return ingredients
