from tests.ingredient_test_data import Ingredient, ingredient_dataset, i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16

def test_get_all_ingredient_dataset():
    assert ingredient_dataset().get_all() == [i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16]

def test_get_by_id_is_i_07():
    assert ingredient_dataset().get_by_id(4007) is i_07

def test_get_by_id_is_i_09():
    assert ingredient_dataset().get_by_id(4009) is i_09

def test_get_by_id_nonexistent_id():
    assert ingredient_dataset().get_by_id(9797) is None

def test_get_by_name_is_i_06():
    assert ingredient_dataset().get_by_name("Matcha Powder") is i_06

def test_get_by_name_is_i_10():
    assert ingredient_dataset().get_by_name("Whipped Cream") is i_10

def test_get_by_name_nonexistent_name():
    assert ingredient_dataset().get_by_name("Soy Milk") is None