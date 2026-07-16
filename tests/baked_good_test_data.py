from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository

bg_00 = BakedGood(
    "Chocolate Croissant", 
    1.20,
    0.65,
    "Golden Wheat Bakers Co.",
    ["Wheat", "Milk", "Eggs", "Soy"],
)
bg_01 = BakedGood(
    "Blueberry Muffin", 
    0.95,
    0.80,
    "Riverside Pastry Supply",
    ["Wheat", "Milk", "Eggs"],
)
bg_02 = BakedGood(
    "Cinnamon Roll", 
    1.50,
    0.55,
    "Sweet Harvest Baking Co.",
    ["Wheat", "Milk", "Eggs"],
)
bg_03 = BakedGood(
    "Almond Biscotti", 
    0.85,
    0.90,
    "Whisk & Wonder Bakeshop",
    ["Wheat", "Eggs", "Tree Nuts (Almonds)"],
)
bg_04 = BakedGood(
    "Peanut Butter Cookie", 
    0.60,
    1.00,
    "Hearth & Home Bakery Supply",
    ["Wheat", "Eggs", "Peanuts"],
)
bg_05 = BakedGood(
    "Sourdough Baguette", 
    1.80,
    0.45,
    "Millstone Artisan Breads",
    ["Wheat"],
)
bg_06 = BakedGood(
    "Red Velvet Cupcake", 
    1.10,
    0.70,
    "Sugarplum Dessert Distributors",
    ["Wheat", "Milk", "Eggs"],
)
bg_07 = BakedGood(
    "Pecan Danish", 
    1.65,
    0.60,
    "Golden Wheat Bakers Co.",
    ["Wheat", "Milk", "Eggs", "Tree Nuts (Pecans)"],
)
bg_08 = BakedGood(
    "Sesame Bagel", 
    0.75,
    0.75,
    "Riverside Pastry Supply",
    ["Wheat", "Sesame"],
)
bg_09 = BakedGood(
    "Coconut Macaron", 
    1.05,
    0.85,
    "Whisk & Wonder Bakeshop",
    ["Eggs", "Tree Nuts (Coconut)"],
)

def baked_goods_dataset():
    baked_goods = BakedGoodRepository()
    baked_good_instances = [globals()[f"bg_{index:02d}"] for index in range(10)]
    for baked_good in baked_good_instances:
        baked_goods.add(baked_good)
    return baked_goods