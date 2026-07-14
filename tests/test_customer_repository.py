from tests.customer_test_data import Customer, customer_dataset, c_00, c_01, c_02, c_03, c_04, c_05, c_06, c_07, c_08, c_09

def test_get_all_customer_dataset():
    assert customer_dataset().get_all() == [c_00, c_01, c_02, c_03, c_04, c_05, c_06, c_07, c_08, c_09]

def test_get_by_id_is_c_04():
    assert customer_dataset().get_by_id(2004) is c_04

def test_get_by_id_is_c_05():
    assert customer_dataset().get_by_id(2005) is c_05

def test_get_by_id_nonexistent_id():
    assert customer_dataset().get_by_id(9898) is None

def test_get_by_name_is_c_03():
    assert customer_dataset().get_by_name("Arlette") is c_03

def test_get_by_name_is_c_06():
    assert customer_dataset().get_by_name("Jarquetta") is c_06

def test_get_by_name_nonexistent_name():
    assert customer_dataset().get_by_name("LeBron James") is None

def test_get_by_email_is_c_02():
    assert customer_dataset().get_by_email("bidor@catalyte.io") is c_02

def test_get_by_email_is_c_07():
    assert customer_dataset().get_by_email("ocasselle@sdipresence.com") is c_07

def test_get_by_email_nonexistent_email():
    assert customer_dataset().get_by_email("johnny.appleseed@gmail.com") is None

def test_add_customer():
    c_10 = Customer(
        2010,
        "Michael Jordan",
        "mjordan@gmail.com",
        23.23
    )
    data = customer_dataset()
    data.add(c_10)
    assert data.get_by_id(2010) is c_10

# def test_update_existing_id():
