from faker import Faker
fake = Faker('ru_RU')
import random
import string
from datetime import date, timedelta

# Генерируем данные для курьера
def generate_login(min_length=2, max_length=10):
    length = random.randint(min_length, max_length)
    login = ''.join(random.choices(string.ascii_letters, k=length))
    return login

def generate_first_name():
    name = fake.first_name()
    while len(name) < 2 or len(name) > 10:
        name = fake.first_name()
    return name

def generate_courier_body():
    return {
        "login": generate_login(),
        "password": random.randint(0000, 9999),
        "firstName": generate_first_name()
    }
