
import allure
import pytest
from allure_commons.types import Severity

from generator.generator_person_data import generate_person_data
from logging_config import configure_logger
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrderPage

logger = configure_logger(__name__, 'test.log')


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.title("Тестирование функциональности оформления заказа")
def test_place_order(page, base_url, user_account, add_to_cart):
    """
    Тестирование функциональности оформления заказа.
    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param user_account: Фикстура для регистрации и входа в систему.
    :param add_to_cart: Фикстура для добавления карточки в корзину.
    """
    person = generate_person_data()
    place_order_page = PlaceOrderPage(page, base_url)
    cart_page = CartPage(page, base_url)

    try:
        with allure.step("Добавляем товар в корзину"):
            cart_page.click_add_to_cart()
            cart_page.click_cart_button()
            logger.info("Товар добавлен в корзину.")

        with allure.step("Открываем страницу оформления заказа"):
            place_order_page.click_place_order()
            logger.info("Страница оформления заказа открыта.")

        with allure.step("Заполняем форму оформления заказа"):
            place_order_page.fill_form(person)
            place_order_page.place_order_screenshot()
            logger.info("Форма оформления заказа заполнена.")

        with allure.step("Оформляем заказ"):
            place_order_page.place_order()
            logger.info("Заказ оформлен.")

        with (allure.step("Проверяем, что заказ успешно оформлен")):
            assert place_order_page.message_thank_you() == \
                   "Thank you for your purchase!"
            logger.info("Заказ успешно оформлен.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
