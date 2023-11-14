import logging

import allure
import pytest
from allure_commons.types import Severity

from pages.resgister_and_login_page import RegisterAndLoginPage
from pages.locators import LoginPageLocators


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
def test_register_and_login_functionality(page, caplog):
    caplog.set_level(logging.INFO)
    register_and_login_page = RegisterAndLoginPage(page)
    selector = LoginPageLocators.USERNAME_DISPLAY_SELECTOR
    with allure.step("Открываем страницу регистрации"):
        register_and_login_page.go_to()
    with allure.step("Регистрируем нового пользователя"):
        username = 'username'
        password = 'password'
        register_and_login_page.register_and_login(username, password)
    page.wait_for_selector(selector)
    with (allure.step("Проверяем правильность регистрации")):
        assert register_and_login_page.is_logged_in(username) is True, \
            f"Неправильный результат для {username} и {password}"
