from tests.drink_test_data import Drink, drink_dataset, d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09

def test_get_all_drink_dataset():
    assert drink_dataset().get_all() == [d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09]

def test_get_by_id_is_d_00():
    assert drink_dataset().get_by_id(1301) is d_00

def test_get_by_id_is_d_09():
    assert drink_dataset().get_by_id(1310) is d_09

def test_get_by_id_nonexistent_drink():
    assert drink_dataset().get_by_id(9696) is None