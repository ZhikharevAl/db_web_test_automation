import logging

import allure
import pytest
from allure_commons.types import Severity

from pages.register_and_login_page import RegisterAndLoginPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
def test_register_and_login_functionality(page, caplog):
    caplog.set_level(logging.INFO)
    register_and_login_page = RegisterAndLoginPage(page)

    with allure.step("Открываем страницу регистрации"):
        register_and_login_page.go_to()
        logging.info("Страница регистрации открыта.")
    with allure.step("Регистрируем нового пользователя"):
        username = 'username'
        password = 'password'
        register_and_login_page.register_and_login(username, password)
        logging.info(f"Зарегистрирован новый пользователь: {username}")
    with allure.step("Проверяем правильность регистрации"):
        is_logged_in = register_and_login_page.is_logged_in(username)
        assert is_logged_in is True, \
            f"Неправильный результат для {username} и {password}"
        if is_logged_in:
            logging.info(f"Пользователь {username} успешно "
                         f"зарегистрирован и вошел в систему.")
        else:
            logging.error(f"Регистрация или вход в систему "
                          f"не удался для пользователя {username}.")
