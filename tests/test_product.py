import logging

import allure
import pytest
from allure_commons.types import Severity
from pages.product_page import ProductPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.description("Тестирование функциональности продукта.")
def test_product(page, base_url, user_account, caplog):
    """
    Тестирование функциональности продукта.

    :param page: Экземпляр страницы для тестирования.
    :param user_account: Фикстура для регистрации и авторизации.
    :param caplog: Журнал для записи результатов теста.
    """
    caplog.set_level(logging.INFO)
    product_page = ProductPage(page, base_url)

    with allure.step("Нажимаем на продукт"):
        product_page.click_on_the_product()
        logging.info("Нажали на продукт.")
    with allure.step("Проверяем имя продукта"):
        product_name = product_page.get_product_name()
        assert product_name, f"{product_name} не отображается."
        if product_name:
            logging.info(f"Имя продукта отображается корректно: "
                         f"{product_name}")
        else:
            logging.error("Имя продукта не отображается.")
