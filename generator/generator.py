import random
from data.data import Customer
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en')
Faker.seed()


def generated_new_customer():
    yield Customer(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        postcode=faker_ru.postcode(),
    )


def generated_customer():
    customers = ["Hermoine Granger", "Harry Potter", "Ron Weasly", "Albus Dumbledore", "Neville Longbottom"]
    return customers[random.randrange(len(customers))]
