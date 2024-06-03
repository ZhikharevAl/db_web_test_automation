import pytest
import allure

from allure_commons.types import Severity

from logging_config import configure_logger
from pages.signup_page import SignUpPage

logger = configure_logger(__name__, "test.log")


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description("Тестирование функциональности регистрации")
@pytest.mark.parametrize(
    "username, password, test_type",
    [
        ("valid_username", "valid_password", "positive"),
        ("invalid_username", "valid_password", "negative"),
        ("valid_username", "invalid_password", "negative"),
        ("invalid_username", "invalid_password", "negative"),
    ],
)
def test_signup_functionality(page, base_url, username, password, test_type):
    """
    Тестирование функциональности регистрации.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param username: Имя пользователя для регистрации.
    :param password: Пароль для регистрации.
    :param test_type: Тип теста ('positive' или 'negative').
    """
    signup_page = SignUpPage(page, base_url)

    try:
        with allure.step("Открываем страницу регистрации"):
            signup_page.go_to(base_url)
            logger.info("Страница регистрации открыта.")

        with allure.step("Вводим логин и пароль"):
            signup_page.sign_up(username, password)
            logger.info(f"Введены данные для регистрации: " f"{username}, {password}")

        with allure.step("Проверяем правильность регистрации"):
            is_logged_in = signup_page.is_logged_in(username, test_type)
            assert is_logged_in == (
                test_type == "positive"
            ), f"Неправильный результат для {username} и {password}"

            if is_logged_in:
                logger.info(
                    f"Пользователь {username} "
                    f"успешно зарегистрирован и вошел в систему."
                )
            else:
                logger.error(
                    f"Регистрация или вход в "
                    f"систему не удался для пользователя {username}."
                )

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise

    finally:
        logger.info("Тест завершен.")
