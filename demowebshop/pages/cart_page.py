from selene import browser, have
import allure


class CartPage:

    @staticmethod
    def check_item_in_cart(item):
        with allure.step(f'Проверка {item} в корзине'):
            browser.element('.product-name').should(have.text(item))

    @staticmethod
    def clean_cart():
        with allure.step('Очистка корзины'):
            browser.element('.qty-input').set_value(0)
            browser.element('[name=updatecart]').click()


cart_page = CartPage()
