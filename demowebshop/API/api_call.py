import allure
from utils.data import API_URL, ADD_TO_CART_URL
from utils.logger import send_request_logger
from utils.tools import get_auth_cookie


class ApiCall:

    @staticmethod
    def add_item_to_cart(item):
        with allure.step(f'Добавить в корзину {item}'):
            send_request_logger('POST', f'{API_URL}{ADD_TO_CART_URL}{item}',
                                cookies={'NOPCOMMERCE.AUTH': get_auth_cookie()})


api_call = ApiCall()
