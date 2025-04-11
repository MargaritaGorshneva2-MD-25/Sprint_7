import requests
from data import Url

class AuthMethods:
    def login(self, login, password):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json={"login": login, "password": password})
