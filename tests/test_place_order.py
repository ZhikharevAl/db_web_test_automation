import logging

import allure
import pytest
from allure_commons.types import Severity

from generator.generator_person_data import generate_person_data
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrderPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.title("Тестирование функциональности оформления заказа")
def test_place_order(page, user_account, add_to_cart, caplog):
    """
    Тестирование функциональности оформления заказа.
    :param page: Экземпляр страницы для тестирования.
    :param user_account: Фикстура для регистрации и входа в систему.
    :param add_to_cart: Фикстура для добавления карточки в корзину.
    :param caplog: Журнал для записи результатов теста.
    """
    caplog.set_level(logging.INFO)
    person = generate_person_data()
    place_order_page = PlaceOrderPage(page)
    cart_page = CartPage(page)

    with allure.step("Добавляем товар в корзину"):
        cart_page.click_add_to_cart()
        cart_page.click_cart_button()
        logging.info("Товар добавлен в корзину.")

    with allure.step("Открываем страницу оформления заказа"):
        place_order_page.click_place_order()
        logging.info("Страница оформления заказа открыта.")

    with allure.step("Заполняем форму оформления заказа"):
        place_order_page.fill_form(person)
        place_order_page.place_order_screenshot()
        logging.info("Форма оформления заказа заполнена.")

    with allure.step("Оформляем заказ"):
        place_order_page.place_order()
        logging.info("Заказ оформлен.")

    with (allure.step("Проверяем, что заказ успешно оформлен")):
        assert place_order_page.message_thank_you() == \
                "Thank you for your purchase!"
        logging.info("Заказ успешно оформлен.")
