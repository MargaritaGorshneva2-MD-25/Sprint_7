class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDER_URL = '/api/v1/orders'
    CREATE_COURIER_URL ='/api/v1/courier'
    LOGIN_URL = '/api/v1/courier/login'
    LIST_ORDER_URL = '/api/v1/orders'

class DataForCourier:
    CREATE_COURIER = {
        "login": "gay",
        "password": "1234",
        "firstName": "aelo"
    }

class DataForAuth:
    CREATE_ID = {
        "login": "typ",
        "password": "1234"
}

class DataForOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Kiarra",
        "lastName": "Achav",
        "address": "Arial str., 13",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-04-04",
        "comment": "Brother? where are you?",
        "color": [
            "BLACK"
        ]
    }
class ErrorMessages:
    INSUFFICIENT_DATA_CREATE_MESSAGE = {'message': 'Недостаточно данных для создания учетной записи'}
    LOGIN_ALREADY_USED_MESSAGE = {'message': 'Этот логин уже используется. Попробуйте другой.'}
    NOT_FOUND_MESSAGE = {'message': 'Учетная запись не найдена'}
    INSUFFICIENT_DATA_LOGIN_MESSAGE = {'message':  'Недостаточно данных для входа'}

class OrderData:
    DEFAULT_ORDER_PAYLOAD = {
        "firstName": "Беллион",
        "lastName": "Ахав",
        "address": "Церковная, д. 42",
        "metroStation": 25,
        "phone": "+79998887766",
        "rentTime": 3,
        "deliveryDate": "2025-01-30",
        "comment": "Хочу новую гитару",
    }