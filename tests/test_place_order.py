import allure
import pytest
from allure_commons.types import Severity

from generator.generator_person_data import generate_person_data
from logging_config import configure_logger
from pages.base_pages.base_test import BaseTest

logger = configure_logger(__name__, "test.log")


class PlaceOrder(BaseTest):
    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование функциональности оформления заказа")
    def test_place_order(self, page):
        """
        Тестирование функциональности оформления заказа.
        :param page: Экземпляр страницы для тестирования.
        """
        person = generate_person_data()

        try:
            with allure.step("Добавляем товар в корзину"):
                self.cart_page.click_add_to_cart()
                self.cart_page.click_cart_button()
                logger.info("Товар добавлен в корзину.")

            with allure.step("Открываем страницу оформления заказа"):
                self.place_order_page.click_place_order()
                logger.info("Страница оформления заказа открыта.")

            with allure.step("Заполняем форму оформления заказа"):
                self.place_order_page.fill_form(person)
                self.place_order_page.place_order_screenshot()
                logger.info("Форма оформления заказа заполнена.")

            with allure.step("Оформляем заказ"):
                self.place_order_page.place_order()
                logger.info("Заказ оформлен.")

            with allure.step("Проверяем, что заказ успешно оформлен"):
                assert (
                    self.place_order_page.message_thank_you()
                    == "Thank you for your purchase!"
                )
                logger.info("Заказ успешно оформлен.")

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise
