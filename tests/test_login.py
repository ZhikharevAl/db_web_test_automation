import pytest
import allure
import logging

from allure_commons.types import Severity

from pages.login_page import LoginPage
from tests.test_signup import test_signup_functionality


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('username, password, test_type', [
    ('valid_username', 'valid_password', 'positive'),
    ('invalid_username', 'valid_password', 'negative'),
    ('valid_username', 'invalid_password', 'negative'),
    ('invalid_username', 'invalid_password', 'negative'),
])
def test_login_functionality(page, username, password, test_type, caplog):
    caplog.set_level(logging.INFO)
    login_page = LoginPage(page)
    username = 'username'
    password = 'password'

    with allure.step("Открываем страницу входа"):
        login_page.go_to()
    with (allure.step("Регистрируем нового пользователя")):
        signup_successful = \
            test_signup_functionality(page, username,
                                      password, test_type='positive',
                                      caplog=caplog)
    if signup_successful:
        with allure.step("Вводим логин и пароль"):
            login_page.login(username, password)
        with allure.step("Проверяем правильность входа"):
            if test_type == 'positive':
                assert login_page.is_logged_in(username) is True, \
                    f"Wrong result for {username} and {password}"
                logging.info(f"Login is successful for {username}")
            elif test_type == 'negative':
                assert login_page.is_logged_in(
                    username) is False, \
                    (f"Login should not be successful for "
                     f"{username} and {password}")
                logging.info(f"Login is not successful as expected "
                             f"for {username}")
