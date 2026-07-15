from models.customer import Customer
from repositories.customer_repository import CustomerRepository

c_00 = Customer(
    "Chamar",
    "chawkins@catalyte.io",
    212.56,
)
c_01 = Customer(
    "Ciera",
    "cwatts@catalyte.io",
    78.32,
)
c_02 = Customer(
    "Brennan",
    "bidor@catalyte.io",
    42.35,
)
c_03 = Customer(
    "Arlette",
    "adiaz@catalyte.io",
    676.81,
)
c_04 = Customer(
    "Hayes",
    "hmccardell@catalyte.io",
    94.56,
)
c_05 = Customer(
    "Mike",
    "mirodriguez@catalyte.io",
    112.09,
)
c_06 = Customer(
    "Jarquetta",
    "jarquetta@xchangechicago.org",
    777.77,
)
c_07 = Customer(
    "Omowale",
    "ocasselle@sdipresence.com",
    999.99,
)
c_08 = Customer(
    "Nicholas",
    "nrobinson@catalyte.io",
    345.67,
)
c_09 = Customer(
    "Adeyemi",
    "aoshodi@catalyte.io",
    76.20,
)

def customer_dataset():
    customers = CustomerRepository()
    customer_instances = [globals()[f"c_{index:02d}"] for index in range(10)]
    for customer in customer_instances:
        customers.add(customer)
    return customers