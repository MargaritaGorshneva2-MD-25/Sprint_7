import allure
import pytest
import helper
from data import ErrorMessages
from methods.courier_methods import CourierMethods

class TestCreateCourier:
    @allure.title('Проверка успешного создания нового курьера')
    def test_success_created_courier(self, generate_courier_data):
        courier_methods = CourierMethods()
        courier_data = generate_courier_data[0]
        response = courier_methods.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_impossibility_creating_two_same_couriers(self, generate_courier_data):
        courier_methods = CourierMethods()
        courier_data = generate_courier_data[0]
        first_response = courier_methods.create_courier(courier_data)
        second_response = courier_methods.create_courier(courier_data)
        assert first_response.status_code == 201 and first_response.json() == {"ok": True}
        assert second_response.status_code == 409 and second_response.json() == ErrorMessages.LOGIN_ALREADY_USED_MESSAGE
        # Баг: Фактический результат: тело ответа: {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}, в теле содержится код и несоответствие message


    @allure.title('Проверка невозможности создания курьера без обязательных полей')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_impossibility_creating_courier_without_required_field(self, generate_courier_data, missing_field):
        courier_methods = CourierMethods()
        courier_data = generate_courier_data[0].copy()
        courier_data.pop(missing_field, None)
        response = courier_methods.create_courier(courier_data)
        assert response.status_code == 400 and response.json() == ErrorMessages.INSUFFICIENT_DATA_CREATE_MESSAGE
        # Баг: Фактический результат: тело ответа: {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, в теле содержится код
