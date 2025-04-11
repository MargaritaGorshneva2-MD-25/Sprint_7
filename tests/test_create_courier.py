import allure
import pytest
import helper
from data import ErrorMessages


class TestCreateCourier:
    @allure.title('Проверка успешного создания нового курьера')
    def test_success_created_courier(self, generate_courier_data, courier_methods):
        courier_data = generate_courier_data[0]
        courier = courier_methods.create_courier(courier_data)
        assert courier.status_code == 201
        assert courier.json() == {"ok": True}

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_impossibility_creating_two_same_couriers(self, generate_courier_data, courier_methods):
        first_courier = courier_methods.create_courier(generate_courier_data[0])
        second_courier = courier_methods.create_courier(generate_courier_data[0])
        assert first_courier.status_code == 201 and first_courier.json() == {"ok": True}
        assert second_courier.status_code == 409 and second_courier.json() == ErrorMessages.LOGIN_ALREADY_USED_MESSAGE
        # Баг: Фактический результат: тело ответа: {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}, в теле содержится код и несоответствие message

    @allure.title('Проверка невозможности создания курьера без обязательных полей') # Согласно требованиям, обязательные поля: логин и пароль
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_impossibility_creating_courier_without_required_field(self, generate_courier_data, courier_methods, missing_field):
        courier_data = generate_courier_data[0]
        courier_data[missing_field] = None
        response = courier_methods.create_courier(courier_data)
        assert response.status_code == 400 and response.json() == ErrorMessages.INSUFFICIENT_DATA_CREATE_MESSAGE
        # Баг: Фактический результат: тело ответа: {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, в теле содержится код
