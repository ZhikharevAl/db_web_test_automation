import allure
import pytest
from logging_config import configure_logger
from pages.base_pages.base_test import BaseTest

logger = configure_logger(__name__, "test.log")


@pytest.mark.skip
@pytest.mark.broken
@allure.description("Тестирование некорректного названия домашней страницы.")
class TestHomePageBroken(BaseTest):
    def test_homepage_loads(self, page, base_url):
        try:
            with allure.step("Открываем страницу входа"):
                self.home_page.go_to(base_url)
                logger.info("Страница входа открыта.")

            with allure.step("Проверка заголовка"):
                assert self.home_page.get_title() == "STOR"
                logger.info("Некорректный заголовок страницы.")

        except Exception as e:
            logger.error(e)
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

        finally:
            logger.info("Тест завершен.")
