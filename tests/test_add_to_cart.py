import logging
import allure
import pytest
from allure_commons.types import Severity

from pages.cart_page import CartPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
def test_add_to_cart(page, caplog, user_account, add_to_cart):
    """
    Тестирование функциональности добавления в корзину.

    :param page: Экземпляр страницы для тестирования.
    :param user_account: Фикстура для регистрации и авторизации.
    :param add_to_cart: Фикстура для добавления товара в корзину.
    """
    caplog.set_level(logging.INFO)
    cart_page = CartPage(page)
    with allure.step("Добавляем продукт в корзину"):
        cart_page.click_add_to_cart()
        logging.info("Продукт добавлен в корзину.")
    with allure.step("Открываем корзину"):
        cart_page.click_cart_button()
        logging.info("Корзина открыта.")
    with allure.step("Проверяем, что цена отображается"):
        price = cart_page.get_price()
        assert price is not None, "Цена не отображается."
        if price is not None:
            logging.info(f"Цена отображается корректно: {price}")
        else:
            logging.error("Цена не отображается.")
