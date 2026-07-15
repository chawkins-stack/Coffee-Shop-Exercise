from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository

bg_00 = BakedGood(
    1000,
    "Chocolate Croissant", 
    1.20,
    0.65,
    "Golden Wheat Bakers Co.",
    ["Wheat", "Milk", "Eggs", "Soy"],
    1.98
)
bg_01 = BakedGood(
    1001,
    "Blueberry Muffin", 
    0.95,
    0.80,
    "Riverside Pastry Supply",
    ["Wheat", "Milk", "Eggs"],
    1.71
)
bg_02 = BakedGood(
    1002,
    "Cinnamon Roll", 
    1.50,
    0.55,
    "Sweet Harvest Baking Co.",
    ["Wheat", "Milk", "Eggs"],
    2.33
)
bg_03 = BakedGood(
    1003,
    "Almond Biscotti", 
    0.85,
    0.90,
    "Whisk & Wonder Bakeshop",
    ["Wheat", "Eggs", "Tree Nuts (Almonds)"],
    1.62
)
bg_04 = BakedGood(
    1004,
    "Peanut Butter Cookie", 
    0.60,
    1.00,
    "Hearth & Home Bakery Supply",
    ["Wheat", "Eggs", "Peanuts"],
    1.20
)
bg_05 = BakedGood(
    1005,
    "Sourdough Baguette", 
    1.80,
    0.45,
    "Millstone Artisan Breads",
    ["Wheat"],
    2.61
)
bg_06 = BakedGood(
    1006,
    "Red Velvet Cupcake", 
    1.10,
    0.70,
    "Sugarplum Dessert Distributors",
    ["Wheat", "Milk", "Eggs"],
    1.87
)
bg_07 = BakedGood(
    1007,
    "Pecan Danish", 
    1.65,
    0.60,
    "Golden Wheat Bakers Co.",
    ["Wheat", "Milk", "Eggs", "Tree Nuts (Pecans)"],
    2.64
)
bg_08 = BakedGood(
    1008,
    "Sesame Bagel", 
    0.75,
    0.75,
    "Riverside Pastry Supply",
    ["Wheat", "Sesame"],
    1.31
)
bg_09 = BakedGood(
    1009,
    "Coconut Macaron", 
    1.05,
    0.85,
    "Whisk & Wonder Bakeshop",
    ["Eggs", "Tree Nuts (Coconut)"],
    1.94
)

def baked_goods_dataset():
    baked_goods = BakedGoodRepository()
    baked_good_instances = [globals()[f"bg_{index:02d}"] for index in range(10)]
    for baked_good in baked_good_instances:
        baked_goods.add(baked_good)
    return baked_goods