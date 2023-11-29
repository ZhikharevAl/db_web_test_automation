import allure
import pytest
from allure_commons.types import Severity

from logging_config import configure_logger
from pages.register_and_login_page import RegisterAndLoginPage

logger = configure_logger(__name__, 'test.log')


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description("Тестирование функциональности "
                    "регистрации и входа в систему")
def test_register_and_login_functionality(page, base_url):
    """
    Тестирование функциональности регистрации и входа в систему.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    """
    register_and_login_page = RegisterAndLoginPage(page, base_url)

    try:
        with allure.step(f"Открываем страницу регистрации ({base_url})"):
            register_and_login_page.go_to(base_url)
            logger.info("Страница регистрации открыта.")

        with allure.step("Регистрируем нового пользователя"):
            username = 'username'
            password = 'password'
            register_and_login_page.register_and_login(username, password)
            logger.info(f"Зарегистрирован новый пользователь: {username}")

        with (allure.step("Проверяем правильность регистрации")):
            is_logged_in = register_and_login_page.is_logged_in(username)
            assert is_logged_in is True, \
                f"Неправильный результат для {username} и {password}"

            if is_logged_in:
                logger.info(f"Пользователь {username} "
                            f"успешно зарегистрирован и вошел в систему.")
            else:
                logger.error(f"Регистрация или вход в систему "
                             f"не удался для пользователя {username}.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
