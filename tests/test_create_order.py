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

        response = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=payload)

        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}. Response: {response.text}"
        assert 'track' in response.json(), f"The 'track' key is missing in the response: {response.text}"
        track = response.json()['track']
        assert isinstance(track, int) and track > 0, f"'track' value should be a positive integer, but got {track}"
