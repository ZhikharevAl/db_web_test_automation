from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    """
    Класс CartPage наследуется от BasePage и
            представляет собой страницу корзины.
    """

    def click_add_to_cart(self):
        """
        Метод для добавления продукта в корзину.
        """
        self.click_button(CartPageLocators.CART_BUTTON)

    def click_cart_button(self):
        """
        Метод для перехода к корзине.
        """
        self.click_button(CartPageLocators.CART)

    def wait_for_selector_element(self):
        """
        Метод ожидания появления элемента на странице.
        """
        self.wait_for_selector(CartPageLocators.PRICE)

    def get_price(self):
        """
        Метод для получения цены продукта в корзине.
        """
        return self.inner_text(CartPageLocators.PRICE)
