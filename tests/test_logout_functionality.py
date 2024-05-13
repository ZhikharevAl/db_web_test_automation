import allure
import pytest
from allure_commons.types import Severity

from conftest import TestFixtures
from pages.base_pages.base_test import BaseTest
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")


class TestLogoutFunctionality(TestFixtures, BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Тестирование функциональности выхода из системы.")
    def test_logout_functionality(self, page, user_account):
        """
        Тестирование функциональности выхода из системы.

        :param page: Экземпляр страницы для тестирования.
        :param user_account: Fixture для регистрации и авторизации.
        """

        try:
            self.logout_page.log_out()

            with allure.step("Проверяем, что вышли из системы"):
                is_logged_out = self.logout_page.is_logged_out()

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
