from selene import browser, have
import allure


class MainPage:
    @staticmethod
    def check_auth_is_success(login):
        with allure.step('Проверка авторизации'):
            browser.element('.account').should(have.text(login))

    @staticmethod
    def go_to_cart():
        with allure.step('Переход в корзину'):
            browser.element('#topcartlink').click()


main_page = MainPage()
