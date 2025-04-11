import allure
import pytest
import helper
import requests
from data import Url
from data import ErrorMessages

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_successful_courier_login(self, generate_courier_data, auth_methods):
        courier_body, login, password, _ = generate_courier_data  # Распаковка списка
        courier_id = auth_methods.login(login, password)  # Пытаемся залогиниться
        assert courier_id is not None

    @allure.title('Проверка невозможности авторизации курьера без обязательного поля')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_impossibility_login_courier_without_required_field(self, generate_courier_data, auth_methods, missing_field):
        courier_body, login, password, _ = generate_courier_data
        login_data = {"login": login, "password": password}
        login_data[missing_field] = None
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=login_data)
        assert response.status_code == 400 and response.json() == ErrorMessages.INSUFFICIENT_DATA_LOGIN_MESSAGE


    @allure.title('Проверка невозможности авторизации курьера с неверными учетными данными')
    def test_impossibility_login_courier_with_incorrect_credentials(self, generate_courier_data, auth_methods):
        courier_body, login, password, _ = generate_courier_data
        incorrect_login = login + "incorrect"
        incorrect_password = str(int(password) + 1)
        response = auth_methods.login(incorrect_login, incorrect_password)
        assert response.status_code == 404 and response.json() == ErrorMessages.NOT_FOUND_MESSAGE

    @allure.title('Проверка невозможности авторизации курьера с несуществующим логином и паролем')
    def test_impossibility_login_courier_with_nonexistent_user(self, auth_methods):
        login_data = {"login": "nonexistent_login", "password": "wrong_password"}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=login_data)
        assert response.status_code == 404 and response.json() == ErrorMessages.NOT_FOUND_MESSAGE
