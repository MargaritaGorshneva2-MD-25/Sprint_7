from data import DataForOrder, DataForCourier, DataForAuth


def modify_crate_courier_body(key, value):
    body = DataForCourier.CREATE_COURIER.copy()
    body[key] = value
    return body

def modify_crate_login_body(key, value):
    body = DataForAuth.CREATE_ID.copy()
    body[key] = value
    return body

def modify_crate_order_body(key, value):
    body = DataForOrder.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body