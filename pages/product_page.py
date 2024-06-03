from pages.base_pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Класс ProductPage наследуется от BasePage и представляет
            собой страницу продукта.
    """

    def click_on_the_product(self):
        """
        Метод для клика по продукту на странице.
        """
        self.click_button(ProductPageLocators.PRODUCTNAME)

    def get_product_name(self):
        """
        Метод для получения имени продукта на странице.
        """
        return self.inner_text(ProductPageLocators.NAMEPRODUCT)

    def click_product_samsung(self):
        self.click_button(ProductPageLocators.PRODUCTNAMESAMSUNG)
