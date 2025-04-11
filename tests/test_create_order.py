import requests
import allure
import pytest
from data import Url, OrderData

class TestCreateOrder:

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GRAY'],
        []
    ])
    @allure.title('Создание заказа')
    def test_create_order(self, color):
        payload = OrderData.DEFAULT_ORDER_PAYLOAD.copy()
        payload['color'] = color

        r = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=payload)
        assert r.status_code == 201
        assert 'track' in r.json()
