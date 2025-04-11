import pytest
from generators import generate_courier_body
from methods.auth_methods import AuthMethods
from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def auth_methods():
    return AuthMethods()


@pytest.fixture()
def generate_courier_data():
    courier_body = generate_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    firstName = courier_body['firstName']
    yield [courier_body, login, password, firstName]  # отдаем данные в тесты

@pytest.fixture(scope="function", autouse=True)
def delete_courier_data(generate_courier_data, auth_methods, courier_methods):
    #Фикстура для удаления курьера после тестов
    courier_body, login, password, _ = generate_courier_data
    yield
    courier_id = auth_methods.login(login, password)
    if courier_id.status_code == 200:
        return courier_id.json()["id"] and courier_methods.delete_courier(courier_id)
    else:
        return None
