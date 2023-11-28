import logging
import allure
import pytest

from generator.generator_person_data import generate_person_data
from pages.e2e_page import E2EPage


class TestE2E:
    @pytest.mark.e2e
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Тестирование happy path E2E.")
    @allure.feature('E2E Testing')
    @allure.story('Happy Path')
    def test_e2e(self, page, base_url, caplog):
        """
            Тестирование happy path E2E.
            :param page: Экземпляр страницы для тестирования.
            :param base_url: URL-адрес домашней страницы.
            :param caplog: Журнал для записи результатов теста.
        """
        caplog.set_level(logging.INFO)
        person = generate_person_data()
        page_e2e = E2EPage(page, base_url)

        with allure.step("Открываем страницу"):
            allure.dynamic.link(base_url,
                                name='Link_OpenPage')
            page_e2e.go_to(base_url)
            logging.info("Страница открыта.")

        with allure.step("Проверяем логотип"):
            allure.dynamic.link(base_url,
                                name='Link_CheckLogo')
            assert page_e2e.title() == "STORE", (f"Логотип "
                                                 f"{page_e2e.title()} "
                                                 f"не верен")
            logging.info("Логотип проверен.")

        with allure.step("Регистрируем нового пользователя"):
            allure.dynamic.link(base_url,
                                name='Link_RegisterUser')
            page_e2e.register()
            logging.info("Новый пользователь зарегистрирован.")

        with allure.step("Авторизоваться"):
            allure.dynamic.link(base_url,
                                name='Link_LoginUser')
            page_e2e.login_happy_path()
            logging.info("Пользователь авторизован.")

        with allure.step("Проверяем, что пользователь авторизован"):
            allure.dynamic.link(base_url,
                                name='Link_AuthorizationCheck')
            page_e2e.authorization_check()
            logging.info("Пользователь авторизован.")

        with allure.step("Добавляем продукт в корзину"):
            product_url = f"{base_url}/prod.html?idp_=8"
            allure.dynamic.link(product_url, name='Link_AddToCart')
            page_e2e.add_product_to_cart()
            logging.info("Продукт добавлен в корзину.")

        with allure.step("Оформляем заказ"):
            cart_url = f"{base_url}/cart.html"
            allure.dynamic.link(cart_url, name='Link_PlaceOrder')
            page_e2e.order()
            page_e2e.fill_form(person)
            logging.info("Заказ оформлен.")

        with allure.step("Проверяем, что заказ оформлен"):
            order_check_url = f"{base_url}/cart.html"
            allure.dynamic.link(order_check_url, name='Link_OrderCheck')
            page_e2e.order_check()
            logging.info("Заказ оформлен.")
