import allure
import pytest
import logging

from allure_commons.types import Severity

from pages.signup_page import SignUpPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description('Тестирование функциональности регистрации')
@pytest.mark.parametrize('username, password, test_type', [
    ('valid_username', 'valid_password', 'positive'),
    ('invalid_username', 'valid_password', 'negative'),
    ('valid_username', 'invalid_password', 'negative'),
    ('invalid_username', 'invalid_password', 'negative'),
])
def test_signup_functionality(page, username, password, test_type, caplog):
    """
    Тестирование функциональности регистрации.

    :param page: Экземпляр страницы для тестирования.
    :param username: Имя пользователя для регистрации.
    :param password: Пароль для регистрации.
    :param test_type: Тип теста ('positive' или 'negative').
    :param caplog: Журнал для записи результатов теста.
    """
    caplog.set_level(logging.INFO)
    signup_page = SignUpPage(page)

    with allure.step("Открываем страницу регистрации"):
        signup_page.go_to()
        logging.info("Страница регистрации открыта.")
    with allure.step("Вводим логин и пароль"):
        signup_page.sign_up(username, password)
        logging.info(f"Введены данные для регистрации: {username}, {password}")
    with allure.step("Проверяем правильность регистрации"):
        is_logged_in = signup_page.is_logged_in(username, test_type)
        assert is_logged_in == (test_type == 'positive'), \
            f"Неправильный результат для {username} и {password}"
        if is_logged_in:
            logging.info(f"Пользователь {username} успешно "
                         f"зарегистрирован и вошел в систему.")
        else:
            logging.error(f"Регистрация или вход в систему "
                          f"не удался для пользователя {username}.")
