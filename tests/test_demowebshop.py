import allure
from demowebshop.API.api_call import api_call
from demowebshop.pages.cart_page import cart_page
from demowebshop.pages.main_page import main_page
from utils.data import LOGIN, SMARTPHONE_API, SMARTPHONE_NAME, NOTEBOOK_API, NOTEBOOK_NAME


def test_login_api():
    with allure.step('Авторизация '):
        main_page.check_auth_is_success(LOGIN)


def test_add_smartphone_to_cart():
    with allure.step('Добавление телефона в корзину'):
        api_call.add_item_to_cart(SMARTPHONE_API)
        main_page.go_to_cart()
        cart_page.check_item_in_cart(SMARTPHONE_NAME)
        cart_page.clean_cart()


def test_add_notebook_add_to_cart():
    with allure.step('Добавление ноутбука в корзину'):
        api_call.add_item_to_cart(NOTEBOOK_API)
        main_page.go_to_cart()
        cart_page.check_item_in_cart(NOTEBOOK_NAME)
        cart_page.clean_cart()
