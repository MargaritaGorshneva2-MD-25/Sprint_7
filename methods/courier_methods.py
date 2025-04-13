import requests
import allure
from data import Url

class CourierMethods:
    @allure.step("Создание курьера")
    def create_courier(self, body):
        with allure.step(f"Отправка POST запроса на {Url.CREATE_COURIER_URL}"):
            response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=body)
            allure.attach(response.request.method, "Method", allure.attachment_type.TEXT)
            allure.attach(response.request.url, "URL", allure.attachment_type.TEXT)
            allure.attach(str(response.request.body), "Request Body", allure.attachment_type.TEXT)
            allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
            allure.attach(response.text, "Response", allure.attachment_type.TEXT)
            return response

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        with allure.step(f"Отправка DELETE запроса на {Url.CREATE_COURIER_URL}/{courier_id}"):
            response = requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}/{courier_id}')
            allure.attach(response.request.method, "Method", allure.attachment_type.TEXT)
            allure.attach(response.request.url, "URL", allure.attachment_type.TEXT)
            allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
            allure.attach(response.text, "Response", allure.attachment_type.TEXT)
            return response
