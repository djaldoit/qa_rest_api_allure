import pytest
from selene import browser
import allure
from utils.tools import get_auth_cookie, add_auth_cookie


@pytest.fixture(scope='session', autouse=True)
def set_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    get_auth_cookie()
    add_auth_cookie()

    yield browser

    browser.quit()
