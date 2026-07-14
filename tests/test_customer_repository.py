from tests.customer_test_data import Customer, customer_dataset, c_00, c_01, c_02, c_03, c_04, c_05, c_06, c_07, c_08, c_09

def test_get_all_customer_dataset():
    assert customer_dataset().get_all() == [c_00, c_01, c_02, c_03, c_04, c_05, c_06, c_07, c_08, c_09]

def test_get_by_id_is_c_04():
    assert customer_dataset().get_by_id(2004) == c_04

def test_get_by_id_is_c_05():
    assert customer_dataset().get_by_id(2005) == c_05

def test_get_by_id_is_none():
    assert customer_dataset().get_by_id(9898) is None