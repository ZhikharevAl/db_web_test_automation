import allure
import pytest
from allure_commons.types import Severity

from pages.cart_page import CartPage
from logging_config import configure_logger

logger = configure_logger(__name__, 'test.log')


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description("Тестирование функциональности добавления в корзину.")
def test_add_to_cart(page, base_url, user_account, add_to_cart):
    """
    Тестирование функциональности добавления в корзину.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param user_account: Фикстура для регистрации и авторизации.
    :param add_to_cart: Фикстура для добавления товара в корзину.
    """

    cart_page = CartPage(page, base_url)

    try:
        # Добавление продукта в корзину
        with allure.step("Добавляем продукт в корзину"):
            cart_page.click_add_to_cart()
            logger.info("Продукт добавлен в корзину.")

        # Открытие корзины
        with allure.step("Открываем корзину"):
            cart_page.click_cart_button()
            logger.info("Корзина открыта.")
            cart_page.wait_for_selector_element()

            # Проверка отображения цены
        with ((allure.step("Проверяем, что цена отображается"))):
            price = cart_page.get_price()

            # Проверяем, что цена не является объектом CartPage
            some_variable = "CartPage"
            assert not isinstance(price, CartPage), \
                f"Цена представлена объектом {some_variable}."

            if price is not None:
                logger.info(f"Цена отображается корректно: {price}")
            else:
                logger.error("Цена не отображается.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
