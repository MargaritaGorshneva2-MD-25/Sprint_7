import requests
import allure
from data import Url

class AuthMethods:
    @allure.step("Авторизация пользователя") # Декоратор allure.step
    def login(self, login, password):
        with allure.step(f"Отправка POST запроса на {Url.LOGIN_URL}"): # Контекстный менеджер для более детальной информации
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json={"login": login, "password": password})
            allure.attach(response.request.method, "Method", allure.attachment_type.TEXT) # Добавим метод запроса
            allure.attach(response.request.url, "URL", allure.attachment_type.TEXT) # Добавим URL запроса
            allure.attach(str(response.request.body), "Request Body", allure.attachment_type.TEXT) # Добавим тело запроса
            allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT) # Добавим статус код
            allure.attach(response.text, "Response", allure.attachment_type.TEXT) # Добавим ответ
            return response


