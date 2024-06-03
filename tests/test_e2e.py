import allure
import pytest

from data.data import PersonData
from pages.base_pages.base_test import BaseTest
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")


class TestE2E(BaseTest):
    @pytest.mark.e2e
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Тестирование happy path E2E.")
    @allure.feature("E2E Testing")
    @allure.story("Happy Path")
    def test_e2e(self, page, base_url):
        """
        Тестирование happy path E2E.
        :param page: Экземпляр страницы для тестирования.
        :param base_url: URL-адрес домашней страницы.
        """
        person = PersonData()

        try:
            with allure.step("Открываем страницу"):
                allure.dynamic.link(base_url, name="Link_OpenPage")
                self.e2e_page.go_to(base_url)
                logger.info("Страница открыта.")

            with allure.step("Проверяем логотип"):
                allure.dynamic.link(base_url, name="Link_CheckLogo")
                assert self.e2e_page.title() == "STORE", (
                    f"Логотип " f"{self.e2e_page.title()} " f"не верен"
                )
                logger.info("Логотип проверен.")

            with allure.step("Регистрируем нового пользователя"):
                allure.dynamic.link(base_url, name="Link_RegisterUser")
                self.e2e_page.register()
                logger.info("Новый пользователь зарегистрирован.")

            with allure.step("Авторизоваться"):
                allure.dynamic.link(base_url, name="Link_LoginUser")
                self.e2e_page.login_happy_path()
                logger.info("Пользователь авторизован.")

            with allure.step("Проверяем, что пользователь авторизован"):
                allure.dynamic.link(base_url, name="Link_AuthorizationCheck")
                self.e2e_page.authorization_check()
                logger.info("Пользователь авторизован.")

            with allure.step("Добавляем продукт в корзину"):
                product_url = f"{base_url}/prod.html?idp_=8"
                allure.dynamic.link(product_url, name="Link_AddToCart")
                self.e2e_page.add_product_to_cart()
                logger.info("Продукт добавлен в корзину.")

            with allure.step("Оформляем заказ"):
                cart_url = f"{base_url}/cart.html"
                allure.dynamic.link(cart_url, name="Link_PlaceOrder")
                self.e2e_page.order()
                self.e2e_page.fill_form(person)
                logger.info("Заказ оформлен.")

            with allure.step("Проверяем, что заказ оформлен"):
                order_check_url = f"{base_url}/cart.html"
                allure.dynamic.link(order_check_url, name="Link_OrderCheck")
                self.e2e_page.order_check()
                logger.info("Заказ оформлен.")
        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            raise

        finally:
            logger.info("Тест завершен.")
