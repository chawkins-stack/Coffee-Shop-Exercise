from tests.drink_test_data import Drink, drink_dataset, d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09, i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16

def test_get_all_drink_dataset():
    assert drink_dataset().get_all() == [d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09]

def test_get_by_id_is_d_00():
    assert drink_dataset().get_by_id(1301) is d_00

def test_get_by_id_is_d_09():
    assert drink_dataset().get_by_id(1310) is d_09

def test_get_by_id_nonexistent_drink():
    assert drink_dataset().get_by_id(9696) is None

def test_get_by_name_is_d_01():
    assert drink_dataset().get_by_name("Vanilla Latte") is d_01

def test_get_by_name_is_d_08():
    assert drink_dataset().get_by_name("Iced Americano") is d_08

def test_get_by_name_nonexistent_drink():
    assert drink_dataset().get_by_name("Pistachio Rose Latte") is None

def test_add_drink():
    d_10 = Drink(
        "Iced Vanilla Cold Brew",
        [i_02, i_03, i_05, i_09],
        0.85,
        2.53,
        3.00,
    )
    data = drink_dataset()
    data.add(d_10)
    assert data.get_by_id(1311) is d_10

def test_update_existing_drink():
    d_11 = Drink(
        "Honey Cinnamon Oat Latte",
        [i_00, i_07, i_12, i_15],
        1.20,
        2.42,
        4.10,
    )
    data = drink_dataset()
    data.update(1303, d_11)
    assert data.get_by_name("Honey Cinnamon Oat Latte") and not data.get_by_name("Caramel Macchiato")

def test_update_nonexistent_drink():
    d_12 = Drink(
        "Caramel Mocha",
        [i_00, i_02, i_04, i_08, i_10],
        1.45,
        2.31,
        4.80,
    )
    data = drink_dataset()
    assert data.update(9901, d_12) is None

def test_delete_existing_drink():
    assert drink_dataset().delete(1304)

def test_delete_nonexistent_drink():
    assert drink_dataset().delete(9909) is False