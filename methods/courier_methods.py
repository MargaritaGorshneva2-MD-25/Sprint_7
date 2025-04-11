import requests
from data import Url


class CourierMethods:
    def create_courier(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=body)

    def delete_courier(self, courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}/{courier_id}')
