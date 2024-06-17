import pytest
import allure

from allure_commons.types import Severity

from data.data import PersonData
from pages.base_pages.base_test import BaseTest
from tests.test_signup import test_signup_functionality
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")


class TestLoginPage(BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Тестирование функциональности входа.")
    @pytest.mark.parametrize(
        "username, password, test_type",
        [
            ("valid_username", "valid_password", "positive"),
            ("invalid_username", "valid_password", "negative"),
            ("valid_username", "invalid_password", "negative"),
            ("invalid_username", "invalid_password", "negative"),
        ],
    )
    def test_login_functionality(self, page, base_url, username, password, test_type):
        """
        Тестирование функциональности входа.
        :param page: Экземпляр страницы для тестирования.
        :param base_url: URL-адрес домашней страницы.
        :param username: Имя пользователя для регистрации.
        :param password: Пароль для регистрации.
        :param test_type: Тип теста ('positive' или 'negative').
        """
        person = PersonData()
        username = person.name
        password = person.password

        try:
            with allure.step("Открываем страницу входа"):
                self.login_page.go_to(base_url)

            with allure.step("Регистрируем нового пользователя"):
                signup_successful = test_signup_functionality(
                    page, base_url, username, password, test_type="positive"
                )

            if signup_successful:
                with allure.step("Вводим логин и пароль"):
                    self.login_page.login(username, password)

                with allure.step("Проверяем правильность входа"):
                    if test_type == "positive":
                        assert (
                            self.login_page.is_logged_in(username) is True
                        ), f"Wrong result for {username} and {password}"
                        logger.info(f"Login is successful for {username}")
                    elif test_type == "negative":
                        assert self.login_page.is_logged_in(username) is False, (
                            f"Login should not be successful for "
                            f"{username} and {password}"
                        )
                        logger.info(
                            f"Login is not successful as expected " f"for {username}"
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
            logger.info("Тест завершен")
