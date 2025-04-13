import requests
import allure
import pytest
from data import Url

class TestGetListOrders:

    @allure.title('Получение списка заказов')
    def test_get_list_of_orders(self):
        list_orders_response = requests.get(f'{Url.BASE_URL}{Url.LIST_ORDER_URL}')
        assert list_orders_response.status_code == 200, f"Failed to get list of orders: {list_orders_response.text}"

        data = list_orders_response.json()
        assert "orders" in data, f"The 'orders' key is missing in the response: {data}"
        assert isinstance(data["orders"], list), f"'orders' should be a list, but got {type(data['orders'])}"

