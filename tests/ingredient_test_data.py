from models.ingredients import Ingredient
from repositories.ingredients_repository import IngredientRepository

i_00 = Ingredient(
    "Espresso Beans",
    18.00,
    2,
    "lb"
)
i_01 = Ingredient(
    "Water",
    1.20,
    1,
    "gallon"
)
i_02 = Ingredient(
    "Whole Milk",
    4.10,
    1,
    "gallon"
)
i_03 = Ingredient(
    "Vanilla Syrup",
    9.50,
    750,
    "ml"
)
i_04 = Ingredient(
    "Caramel Drizzle",
    8.75,
    500,
    "ml"
)
i_05 = Ingredient(
    "Coarse Ground Coffee",
    16.50,
    2,
    "lb"
)
i_06 = Ingredient(
    "Matcha Powder",
    22.00,
    1,
    "lb"
)
i_07 = Ingredient(
    "Honey",
    7.25,
    24,
    "oz"
)
i_08 = Ingredient(
    "Chocolate Syrup",
    6.90,
    750,
    "ml"
)
i_09 = Ingredient(
    "Ice",
    2.00,
    10,
    "lb"
)
i_10 = Ingredient(
    "Whipped Cream",
    5.40,
    32,
    "oz"
)
i_11 = Ingredient(
    "Chai Concentrate",
    11.00,
    32,
    "oz"
)
i_12 = Ingredient(
    "Cinnamon",
    4.50,
    12,
    "oz"
)
i_13 = Ingredient(
    "Cocoa Powder",
    6.75,
    16,
    "oz"
)
i_14 = Ingredient(
    "Sugar",
    3.20,
    4,
    "lb"
)
i_15 = Ingredient(
    "Oat Milk",
    5.60,
    64,
    "fl oz"
)
i_16 = Ingredient(
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
