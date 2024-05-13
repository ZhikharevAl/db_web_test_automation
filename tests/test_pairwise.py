import allure
import pytest
from allure_commons.types import Severity

from conftest import TestFixtures
from generator.generator_person_data import generate_person_data
from logging_config import configure_logger
from pages.base_pages.base_test import BaseTest

logger = configure_logger(__name__, "test.log")


class TestPairwise(TestFixtures, BaseTest):

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование функциональности просмотра продукта.")
    def test_click_smartphone_button(self, page, base_url, user_account_authorized):
        """
        Test the functionality of viewing a product.

        Args:
            self: The test class instance.
            page: The page object.
            base_url: The base URL of the website.
            user_account_authorized: A flag indicating whether the
            user account is authorized.

        """

        try:
            if user_account_authorized:
                with allure.step("Нажимаем кнопку смартфона"):
                    self.pairwise_page.click_button_smartphone()
                    logger.info("Кнопка смартфона нажата.")
            else:
                with allure.step("Открываем страницу магазина"):
                    self.pairwise_page.go_to(base_url)
                    logger.info("Страница магазина открыта.")

                    with allure.step("Нажимаем кнопку смартфона"):
                        self.pairwise_page.click_button_smartphone()
                        logger.info("Кнопка смартфона нажата.")

                    with allure.step("Нажимаем кнопку телефона"):
                        self.pairwise_page.click_button_phone()
                        logger.info("Кнопка телефона нажата.")

                    with allure.step("Проверяем текст названия телефона"):
                        assert self.pairwise_page.name_text_phone() == (
                            "Sony " "xperia z5"
                        )
                        logger.info(
                            "Текст названия телефона проверен и "
                            "соответствует ожидаемому."
                        )

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование функциональности добавления " "ноутбука в корзину.")
    def test_add_notebook_to_cart(self, page, base_url, user_account_authorized):
        """
        Test the functionality of adding a notebook to the cart.

        Args:
            page: The page object representing the current page.
            base_url: The base URL of the website.
            user_account_authorized: A boolean indicating
            whether the user account is authorized.
        """

        try:
            if user_account_authorized:
                with allure.step("Нажимаем кнопку ноутбука"):
                    self.pairwise_page.click_button_laptop()
                    logger.info("Кнопка ноутбука нажата.")
            else:
                with allure.step("Открываем страницу магазина"):
                    self.pairwise_page.go_to(base_url)
                    logger.info("Страница магазина открыта.")

                with allure.step("Нажимаем кнопку ноутбука"):
                    self.pairwise_page.click_button_laptop()
                    logger.info("Кнопка ноутбука нажата.")

            with allure.step("Нажимаем карточку ноутбука"):
                self.pairwise_page.click_button_notebook()
                logger.info("Страница ноутбука открыта.")

            with allure.step("Нажимаем кнопку 'Добавить в корзину'"):
                self.pairwise_page.click_add_to_cart()
                logger.info("Кнопка 'Добавить в корзину' нажата.")

            with allure.step("Нажимаем кнопку корзины"):
                self.pairwise_page.click_button_cart()
                logger.info("Кнопка корзины нажата.")

            with allure.step("Проверяем текст названия ноутбука"):
                assert self.pairwise_page.name_text_laptop() == "2017 Dell 15.6 Inch"
                logger.info(
                    "Текст названия ноутбука проверен и " "соответствует ожидаемому."
                )

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование просмотра товара ноутбука.")
    def test_notebook_view(self, page, base_url):
        """
        Test for viewing a notebook product.

        Args:
            page (Page): The page object for interacting with the web page.
            base_url (str): The base URL of the online store.

        Raises:
            Exception: If there is an error during the test execution.

        """

        try:
            # Open the store page
            with allure.step("Открываем страницу магазина"):
                self.pairwise_page.go_to(base_url)
                logger.info("Страница магазина открыта.")

            # Click on the laptop button
            with allure.step("Нажимаем кнопку ноутбука"):
                self.pairwise_page.click_button_laptop()
                logger.info("Кнопка ноутбука нажата.")

            # Click on the notebook card
            with allure.step("Нажимаем карточку ноутбука"):
                self.pairwise_page.click_button_notebook()
                logger.info("Страница ноутбука открыта.")

            with allure.step("Проверяем текст названия ноутбука"):
                assert self.pairwise_page.name_text_notebook() == "2017 Dell 15.6 Inch"
                logger.info(
                    "Текст названия ноутбука проверен и " "соответствует ожидаемому."
                )

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")

            # Attach a screenshot to the allure report
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )

            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование добавления телефона в корзину.")
    def test_add_phone_to_cart(self, page, base_url):
        """
        Test the functionality of adding a phone to the cart.

        Args:
            self: The instance of the test class.
            page: The page object representing the web page.
            base_url: The base URL of the web page.
        """
        try:
            with allure.step("Открываем страницу магазина"):
                self.pairwise_page.go_to(base_url)
                logger.info("Страница магазина открыта.")
            with allure.step("Нажимаем кнопку смартфона"):
                self.pairwise_page.click_button_smartphone()
                logger.info("Кнопка смартфона нажата.")
            with allure.step("Нажимаем карточку смартфона"):
                self.pairwise_page.click_button_phone()
                logger.info("Кнопка смартфона нажата.")
            with allure.step("Нажимаем кнопку 'Добавить в корзину'"):
                self.pairwise_page.click_add_to_cart()
                logger.info("Кнопка 'Добавить в корзину' нажата.")
            with allure.step("Нажимаем кнопку корзины"):
                self.pairwise_page.click_button_cart()
                logger.info("Кнопка корзины нажата.")
            with allure.step("Проверяем текст названия смартфона"):
                assert self.pairwise_page.name_text_phone_cart() == "Sony xperia z5"
                logger.info(
                    "Текст названия смартфона проверен и " "соответствует ожидаемому."
                )

        except Exception as e:
            logger.error(f"Ошибка при выполнении теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование оформления заказа для смартфона.")
    def test_smartphone_making_order(self, page, user_account):
        """
        Тест функциональности оформления заказа для смартфона.

        Args:
            page: Объект страницы, представляющий текущую веб-страницу.
            Base_url: Базовый URL веб-сайта.
            User_account: Объект учетной записи пользователя,
                          представляющий текущего пользователя.

        Raises:
            Exception: Если происходит ошибка во время выполнения теста.
        """
        # Генерируем случайные данные для заказа
        person_order = generate_person_data()

        try:
            # Щелкнуть кнопку 'Smartphone'
            with allure.step("Щелкнуть кнопку 'Smartphone'"):
                self.pairwise_page.click_button_smartphone()
                logger.info("Кнопка 'Smartphone' нажата.")

            # Щелкнуть карточку смартфона
            with allure.step("Щелкнуть карточку смартфона"):
                self.pairwise_page.click_button_phone()
                logger.info("Карточка смартфона нажата.")

            # Щелкнуть кнопку 'Add to Cart'
            with allure.step("Щелкнуть кнопку 'Add to Cart'"):
                self.pairwise_page.click_add_to_cart()
                logger.info("Кнопка 'Add to Cart' нажата.")

            # Щелкнуть кнопку 'Cart'
            with allure.step("Щелкнуть кнопку 'Cart'"):
                self.pairwise_page.click_button_cart()
                logger.info("Кнопка 'Cart' нажата.")

            # Щелкнуть кнопку 'Place Order'
            with allure.step("Щелкнуть кнопку 'Place Order'"):
                self.pairwise_page.click_button_place_order()

            # Заполнить форму данными пользователя
            with allure.step("Заполнить форму"):
                self.pairwise_page.fill_form(person_order)

            # Щелкнуть кнопку 'Submit'
            with allure.step("Щелкнуть кнопку 'Submit'"):
                self.pairwise_page.click_button_purchase()
                logger.info("Кнопка 'Submit' нажата.")

                # Проверить, подтвержден ли заказ
            with allure.step("Проверить, подтвержден ли заказ"):
                assert (
                    self.pairwise_page.text_thank_you()
                    == "Thank you for your purchase!"
                )
                logger.info("Заказ подтвержден.")

        # Прикрепить снимок экрана к отчету Allure в случае ошибки
        except Exception as e:
            logger.error(f"Ошибка во время выполнения теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование оформления заказа для монитора.")
    def test_monitor_making_order(self, page, base_url, user_account_authorized):
        """
        Тест функциональности оформления заказа для монитора.

        Args:
            page: Объект страницы, представляющий текущую веб-страницу.
            Base_url: Базовый URL веб-сайта.

        Raises:
            Exception: Если происходит ошибка во время выполнения теста.
        """
        # Генерируем случайные данные для заказа
        person_order = generate_person_data()

        try:
            if user_account_authorized:
                with allure.step("Щелкнуть кнопку 'Monitor'"):
                    self.pairwise_page.click_button_monitor()
                    logger.info("Кнопка 'Monitor' нажата.")
            else:
                with allure.step("Открываем страницу магазина"):
                    self.pairwise_page.go_to(base_url)
                    logger.info("Страница магазина открыта.")

                with allure.step("Щелкнуть кнопку 'Monitor'"):
                    self.pairwise_page.click_button_monitor()
                    logger.info("Кнопка 'Monitor' нажата.")

                with allure.step("Щелкнуть карточку монитора"):
                    self.pairwise_page.click_button_asus_monitor()
                    logger.info("Карточка монитора нажата.")

                with allure.step("Нажать 'Add to Cart'"):
                    self.pairwise_page.click_add_to_cart()
                    logger.info("Кнопка 'Add to Cart' нажата.")

                with allure.step("Щелкнуть кнопку 'Cart'"):
                    self.pairwise_page.click_button_cart()
                    logger.info("Кнопка 'Cart' нажата.")

                with allure.step("Щелкнуть кнопку 'Place Order'"):
                    self.pairwise_page.click_button_place_order()

                with allure.step("Заполнить форму"):
                    self.pairwise_page.fill_form(person_order)

                with allure.step("Щелкнуть кнопку 'Submit'"):
                    self.pairwise_page.click_button_purchase()

                with allure.step("Проверить, подтвержден ли заказ"):
                    assert (
                        self.pairwise_page.text_thank_you()
                        == "Thank you for your purchase!"
                    )
                    logger.info("Заказ подтвержден.")

        # Прикрепить снимок экрана к отчету Allure в случае ошибки
        except Exception as e:
            logger.error(f"Ошибка во время выполнения теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @pytest.mark.smoke
    @pytest.mark.pairwise
    @allure.severity(Severity.CRITICAL)
    @allure.title("Тестирование добавления монитора в корзину.")
    def test_monitor_add_to_cart(self, page, user_account):
        """
        Тест функциональности добавления монитора в корзину.

        Args:
            page: Объект страницы, представляющий текущую веб-страницу.
            Base_url: Базовый URL веб-сайта.
            User_account: Объект учетной записи пользователя,
                          представляющий текущего пользователя.

        Raises:
            Exception: Если происходит ошибка во время выполнения теста.
        """

        try:
            with allure.step("Нажать на кнопку 'Monitor'"):
                self.pairwise_page.click_button_monitor()
                logger.info("Кнопка 'Monitor' нажата.")

            with allure.step("Выбрать монитор"):
                self.pairwise_page.click_button_asus_monitor()
                logger.info("Карточка монитора нажата.")

            with allure.step("Щелкнуть кнопку 'Add to Cart'"):
                self.pairwise_page.click_add_to_cart()
                logger.info("Кнопка 'Add to Cart' нажата.")

            with allure.step("Щелкнуть кнопку 'Cart'"):
                self.pairwise_page.click_button_cart()
                logger.info("Кнопка 'Cart' нажата.")

            with allure.step("Проверить текст названия монитора"):
                assert self.pairwise_page.text_by_monitor() == "ASUS Full HD"
                logger.info("Текст названия монитора верен.")
        except Exception as e:
            logger.error(f"Ошибка во время выполнения теста: {e}")
            allure.attach(
                name="screenshot",
                body=page.screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise
