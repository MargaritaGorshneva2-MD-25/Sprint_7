import allure
import pytest
import requests
from data import Url
from methods.auth_methods import AuthMethods
from methods.courier_methods import CourierMethods
from generators import generate_courier_body

@pytest.fixture
def existing_courier():
    courier_body = generate_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    courier_methods = CourierMethods()
    response_create = courier_methods.create_courier(courier_body)
    assert response_create.status_code == 201
    yield courier_body, login, password

@pytest.fixture
def existing_courier_id(existing_courier):
    courier_body, login, password = existing_courier
    auth_methods = AuthMethods()
    response_login = auth_methods.login(login, password)
    assert response_login.status_code == 200
    courier_id = response_login.json()['id']
    yield courier_id

class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_successful_courier_login(self, existing_courier):
        courier_body, login, password = existing_courier
        auth_methods = AuthMethods()
        response = auth_methods.login(login, password)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Ошибка при авторизации без обязательных полей')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_missing_field_login(self, missing_field):
        courier_body = generate_courier_body()
        login = courier_body['login']
        password = courier_body['password']
        login_data = {"login": login, "password": password}
        del login_data[missing_field]
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=login_data, timeout=60)
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Ошибка при неверном логине или пароле')
    def test_incorrect_credentials(self, existing_courier):
        courier_body, login, password = existing_courier

        incorrect_login_data = {"login": login + "incorrect", "password": password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=incorrect_login_data)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

        incorrect_password_data = {"login": login, "password": "wrong_password"}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=incorrect_password_data)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Ошибка при авторизации несуществующего пользователя')
    def test_nonexistent_user(self):
        nonexistent_data = {"login": "nonexistent_user", "password": "some_password"}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=nonexistent_data)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
