from tests.ingredient_test_data import Ingredient, ingredient_dataset, i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16

def test_get_all_ingredient_dataset():
    assert ingredient_dataset().get_all() == [i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16]