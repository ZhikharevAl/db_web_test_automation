import allure
import pytest
import logging

from allure_commons.types import Severity

from pages.signup_page import SignUpPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('username, password, test_type', [
    ('valid_username', 'valid_password', 'positive'),
    ('invalid_username', 'valid_password', 'negative'),
    ('valid_username', 'invalid_password', 'negative'),
    ('invalid_username', 'invalid_password', 'negative'),

])
def test_signup_functionality(page, username, password, test_type, caplog):
    caplog.set_level(logging.INFO)
    signup_page = SignUpPage(page)
    with allure.step("Открываем страницу регистрации"):
        signup_page.go_to()
    with allure.step("Вводим логин и пароль"):
        signup_page.sign_up(username, password)
    with allure.step("Проверяем правильность регистрации"):
        assert signup_page.is_logged_in(username, test_type) == (test_type == 'positive'), \
            f"Неправильный результат для {username} и {password}"


