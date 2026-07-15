from tests.baked_good_test_data import BakedGood, baked_goods_dataset, bg_00, bg_01, bg_02, bg_03, bg_04, bg_05, bg_06, bg_07, bg_08, bg_09

def test_get_all_baked_goods_dataset():
    assert baked_goods_dataset().get_all() == [bg_00, bg_01, bg_02, bg_03, bg_04, bg_05, bg_06, bg_07, bg_08, bg_09]

def test_get_by_name_is_bg_00():
    assert baked_goods_dataset().get_by_name("Chocolate Croissant") == bg_00

def test_get_by_name_is_bg_09():
    assert baked_goods_dataset().get_by_name("Coconut Macaron") == bg_09

def test_get_by_name_is_none():
    assert baked_goods_dataset().get_by_name("Mooncake") is None

def test_get_by_id_is_bg_01():
    assert baked_goods_dataset().get_by_id(6702) == bg_01

def test_get_by_id_is_bg_08():
    assert baked_goods_dataset().get_by_id(6709) == bg_08

def test_get_by_id_is_none():
    assert baked_goods_dataset().get_by_id(9999) is None

def test_add_baked_good():
    bg_10 = BakedGood(
        "Almond Croissant",
        1.50,
        0.65,
        "Sweet Harvest Baking Co.",
        ["Wheat", "Milk", "Eggs", "Tree Nuts (Almonds)"],
    )
    data = baked_goods_dataset()
    data.add(bg_10)
    assert data.get_by_id(6711) == bg_10

def test_update_existing_baked_good():
    data = baked_goods_dataset()
    bg_11 = BakedGood(
        "Brioche Cinnamon Roll",
        1.65,
        0.60,
        "Hearth & Home Bakery Supply",
        ["Wheat", "Milk", "Eggs"]
    )
    data.update(6703, bg_11)
    print(data.get_by_id(6703))
    assert data.get_by_name("Brioche Cinnamon Roll") and not data.get_by_name("Cinnamon Roll")

def test_delete_existing_baked_good():
    data = baked_goods_dataset()
    data.delete(6704)
    assert data.get_by_id(6704) is None

def test_delete_nonexistent_baked_good():
    assert baked_goods_dataset().delete(9998) is False