import allure
import pytest
from allure_commons.types import Severity

from pages.logout_page import LogOutPage
from logging_config import configure_logger

logger = configure_logger(__name__, 'test.log')


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description("Тестирование функциональности выхода из системы.")
def test_logout_functionality(page, base_url, user_account):
    """
    Тестирование функциональности выхода из системы.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param user_account: Fixture для регистрации и авторизации.
    """
    logout_page = LogOutPage(page, base_url)

    try:
        logout_page.log_out()

        with allure.step("Проверяем, что вышли из системы"):
            is_logged_out = logout_page.is_logged_out()

        assert is_logged_out

        if is_logged_out:
            logger.info("Выход из системы выполнен успешно.")
        else:
            logger.error("Выход из системы не выполнен.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
