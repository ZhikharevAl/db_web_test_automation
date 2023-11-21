from datetime import datetime

from data.data import PersonData
from pages.base_page import BasePage
from pages.locators import PlaceOrderPageLocators


class PlaceOrderPage(BasePage):
    """
    Класс PlaceOrderPage наследует от BasePage и представляет собой страницу
    оформления заказа.
    """

    def click_place_order(self):
        """
        Метод для нажатия на кнопку "Оформить заказ".
        """
        self.click_button(PlaceOrderPageLocators.PLACE_ORDER_BUTTON)

    def fill_form(self, person: PersonData):
        """
        Метод для заполнения формы данными из объекта PersonData.
        """
        self.fill_name(person.name)
        self.fill_country(person.country)
        self.fill_city(person.city)
        self.fill_credit_card(person.credit_card)
        self.fill_month(person.month)
        self.fill_year(person.year)

    def fill_name(self, name):
        """
        Метод для заполнения поле "Имя".
        """
        self.fill(PlaceOrderPageLocators.NAME, name)

    def fill_country(self, country):
        """
        Метод для заполнения поле "Страна".
        """
        self.fill(PlaceOrderPageLocators.COUNTRY, country)

    def fill_city(self, city):
        """
        Метод для заполнения поле "Город".
        """
        self.fill(PlaceOrderPageLocators.CITY, city)

    def fill_credit_card(self, credit_card):
        """
        Метод для заполнения поле "Номер карты".
        """
        self.fill(PlaceOrderPageLocators.CREDIT_CARD, credit_card)

    def fill_month(self, month):
        """
        Метод для заполнения поле "Месяц".
        """
        self.fill(PlaceOrderPageLocators.MONTH, month)

    def fill_year(self, year):
        """
        Метод для заполнения поле "Год".
        """
        self.fill(PlaceOrderPageLocators.YEAR, year)

    def scroll_down(self):
        """
        Метод для прокрутки страницы вниз.
        """
        self.scroll_down()

    def click_purchase(self):
        """
        Метод для нажатия на кнопку "Купить".
        """
        self.click_button(PlaceOrderPageLocators.PURCHASE)

    def place_order(self):
        """
        Метод для оформления заказа.
        """
        self.bring_to_front()
        self.click_button_by_role("Purchase")

    def place_order_screenshot(self):
        """
        Метод для снимка экрана.
        """
        current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.screenshot(f'docs/artifacts/screenshots/'
                        f'place_order_screenshot_{current_datetime}.png')

    def message_thank_you(self):
        """
        Метод для получения сообщения "Спасибо за покупку".
        """
        return self.inner_text(PlaceOrderPageLocators.THANK_YOU)
