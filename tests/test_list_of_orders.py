import requests
import allure
import pytest
from data import Url, OrderData

class TestGetListOrders:


    @allure.title('Получение списка заказов')
    def test_get_list_of_orders(self):
        payload = OrderData.DEFAULT_ORDER_PAYLOAD.copy()
        requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=payload)
        list_orders = requests.get(f'{Url.BASE_URL}{Url.LIST_ORDER_URL}')
        assert list_orders.status_code == 200
        assert "orders" in list_orders.json()
        assert isinstance(list_orders.json()["orders"], list), "Ответ должен содержать список заказов"
