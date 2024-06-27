import pytest
import allure

from allure_commons.types import Severity

from pages.base_pages.base_test import BaseTest
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")


class TestHomePage(BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Позитивное тестирование заголовка домашней страницы.")
    def test_home_page_title_positive(self, page, base_url):
        expected_title = "STORE"
        self._check_home_page_title(page, base_url, expected_title, should_match=True)

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Негативное тестирование заголовка домашней страницы.")
    def test_home_page_title_negative(self, page, base_url):
        wrong_title = "Wrong Title"
        self._check_home_page_title(page, base_url, wrong_title, should_match=False)

    def _check_home_page_title(self, page, base_url, expected_title, should_match):
        try:
            with allure.step("Открываем домашнюю страницу"):
                self.home_page.go_to(base_url)
                logger.info("Домашняя страница открыта")

            with allure.step(f"Проверка заголовка {'соответствует' if should_match else
                                                   'не соответствует'} ожидаемому"):
                actual_title = self.home_page.get_title()
                if should_match:
                    assert actual_title == expected_title, (
                        f"Неверный заголовок для "
                        f"{base_url}. Ожидалось: {expected_title}, Получено: {actual_title}"
                    )
                    logger.info(f"Заголовок верен для {base_url}")
                else:
                    assert (
                        actual_title != expected_title
                    ), f"Заголовок не должен быть '{expected_title}' для {base_url}"
                    logger.info(
                        f"Заголовок не '{expected_title}', как и ожидалось для {base_url}"
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
