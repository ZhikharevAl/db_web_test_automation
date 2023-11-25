import logging

import allure
import pytest
from allure_commons.types import Severity

from generator.generator_person_data import generate_person_data
from pages.e2e_page import E2EPage


class TestE2E:
    @pytest.mark.e2e
    @allure.severity(Severity.BLOCKER)
    def test_e2e(self, page, caplog):
        """
        Тестирование happy path E2E.
        :param page: Экземпляр страницы для тестирования.
        :param caplog: Журнал для записи результатов теста.
        """

        caplog.set_level(logging.INFO)
        person = generate_person_data()
        page_e2e = E2EPage(page)

        with allure.step("Открываем страницу"):
            allure.dynamic.link(url='https://www.demoblaze.com/', name='Link')
            page_e2e.go_to_e2e()
            logging.info("Страница открыта.")
        with allure.step("Проверяем логотип"):
            allure.dynamic.link(url='https://www.demoblaze.com/', name='Link')
            assert page_e2e.title() == "STORE", (f"Логотип "
                                                 f"{page_e2e.title()} "
                                                 f"не верен")
            logging.info("Логотип проверен.")
        with allure.step("Регистрируем нового пользователя"):
            allure.dynamic.link(url='https://www.demoblaze.com/', name='Link')
            page_e2e.register()
            logging.info("Новый пользователь зарегистрирован.")
        with allure.step("Авторизоваться"):
            allure.dynamic.link(url='https://www.demoblaze.com/', name='Link')
            page_e2e.login_happy_path()
            logging.info("Пользователь авторизован.")
        with allure.step("Проверяем, что пользователь авторизован"):
            allure.dynamic.link(url='https://www.demoblaze.com/', name='Link')
            page_e2e.authorization_check()
            logging.info("Пользователь авторизован.")
        with allure.step("Добавляем продукт в корзину"):
            allure.dynamic.link(
                url='https://www.demoblaze.com/prod.html?idp_=8', name='Link')
            page_e2e.add_product_to_cart()
            logging.info("Продукт добавлен в корзину.")
        with allure.step("Оформляем заказ"):
            allure.dynamic.link(
                url='https://www.demoblaze.com/cart.html', name='Link')
            page_e2e.order()
            page_e2e.fill_form(person)
            logging.info("Заказ оформлен.")
        with allure.step("Проверяем, что заказ оформлен"):
            allure.dynamic.link(
                url='https://www.demoblaze.com/cart.html', name='Link')
            page_e2e.order_check()
            logging.info("Заказ оформлен.")
