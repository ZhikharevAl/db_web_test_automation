import time

import allure
import pytest
from allure_commons.types import Severity

from conftest import TestFixtures
from logging_config import configure_logger
from pages.base_pages.base_test import BaseTest

logger = configure_logger(__name__, "test.log")


class TestProduct(TestFixtures, BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.description("Тестирование функциональности продукта.")
    def test_product(self, page, user_account):
        """
        Тестирование функциональности продукта.

        :param page: Экземпляр страницы для тестирования.
        :param user_account: Фикстура для регистрации и авторизации.
        """

        try:
            with allure.step("Нажимаем на продукт"):
                start_time = time.time()
                self.product_page.click_on_the_product()
                end_time = time.time()
                logger.info(
                    f"Нажали на продукт за " f"{end_time - start_time:.2f} секунд."
                )

            with allure.step("Получаем имя продукта"):
                start_time = time.time()
                product_name_element = self.product_page.get_product_name()
                product_name = isinstance(product_name_element, str)
                end_time = time.time()
                logger.info(
                    f"Имя продукта получено за " f"{end_time - start_time:.2f} секунд."
                )
                end_time = time.time()

                if product_name:
                    logger.info(
                        f"Имя продукта отображается корректно: "
                        f"{product_name_element} "
                        f"за {end_time - start_time:.2f} секунд."
                    )
                else:
                    raise AssertionError("Имя продукта не отображается.")

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
