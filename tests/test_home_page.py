import pytest
import allure

from allure_commons.types import Severity

from pages.base_pages.base_test import BaseTest
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")


class TestHomePage(BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Тестирование заголовка домашней страницы.")
    @pytest.mark.parametrize(
        "expected_title, test_type",
        [
            ("STORE", "positive"),
            ("Wrong Title", "negative"),
        ],
    )
    def test_home_page_title(self, page, base_url, expected_title, test_type):
        """
        Тестирование заголовка домашней страницы.

        :param page: Экземпляр страницы для тестирования.
        :param base_url: URL-адрес домашней страницы.
        :param expected_title: Ожидаемый заголовок страницы.
        :param test_type: Тип теста ('positive' или 'negative').
        """

        try:
            with allure.step("Открываем страницу входа"):
                self.home_page.go_to(base_url)
                logger.info("Страница входа открыта")

            with allure.step("Проверка заголовка"):
                if test_type == "positive":
                    assert (
                        self.home_page.get_title() == expected_title
                    ), f"Неверный заголовок для {base_url}"
                    logger.info(f"Заголовок верен для {base_url}")
                elif test_type == "negative":
                    assert (
                        self.home_page.get_title() != expected_title
                    ), f"Заголовок не должен быть {expected_title}"
                    logger.info(
                        f"Заголовок не {expected_title}, "
                        f"как и ожидалось для {base_url}"
                    )

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise
