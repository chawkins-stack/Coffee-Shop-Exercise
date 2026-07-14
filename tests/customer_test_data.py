from models.customer import Customer
from repositories.customer_repository import CustomerRepository

c_00 = Customer(
    2000,
    "Chamar",
    "chawkins@catalyte.io",
    212.56
)
c_01 = Customer(
    2001,
    "Ciera",
    "cwatts@catalyte.io",
    78.32
)
c_02 = Customer(
    2002,
    "Brennan",
    "bidor@catalyte.io",
    42.35
)
c_03 = Customer(
    2003,
    "Arlette",
    "adiaz@catalyte.io",
    676.81
)
c_04 = Customer(
    2004,
    "Hayes",
    "hmccardell@catalyte.io",
    94.56
)
c_05 = Customer(
    2005,
    "Mike",
    "mirodriguez@catalyte.io",
    112.09
)
c_06 = Customer(
    2006,
    "Jarquetta",
    "jarquetta@xchangechicago.org",
    777.77
)
c_07 = Customer(
    2007,
    "Omowale",
    "ocasselle@sdipresence.com",
    999.99
)
c_08 = Customer(
    2008,
    "Nicholas",
    "nrobinson@catalyte.io",
    345.67
)
c_09 = Customer(
    2009,
    "Adeyemi",
    "aoshodi@catalyte.io",
    76.20
)

def customer_dataset():
    customers = CustomerRepository()
    customer_instances = [globals()[f"c_{index:02d}"] for index in range(10)]
    for customer in customer_instances:
        customers.add(customer)
    return customers