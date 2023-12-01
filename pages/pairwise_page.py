from data.data import PersonData
from pages.base_page import BasePage
from pages.locators import PairwisePageLocators


class PairwisePage(BasePage):
    def click_button_smartphone(self):
        """
           Clicks the smartphone button on the webpage.
           This function uses the `click_get_by_role`
           method to click the smartphone button.
           """
        self.click_get_by_role(*PairwisePageLocators.PHONES)

    def click_button_phone(self):
        """
            Clicks the phone button on the webpage.
            This function uses the `click_get_by_role`
            method to click the phone button.
            """
        self.click_get_by_role(*PairwisePageLocators.SONYXPERIAZ5)

    def name_text_phone(self):
        """
            Returns the text of the phone's name on the webpage.
            Returns:
                str: The text of the phone's name.
            """
        return self.text_by_role(*PairwisePageLocators.SONYXPERIAZ5_TEXT)

    def name_text_phone_cart(self):
        """
            Returns the text of the phone's name in the cart on the webpage.
            Returns:
                str: The text of the phone's name in the cart.
            """
        return self.text_by_role(*PairwisePageLocators.SONYXPERIAZ5_TEXT_CART)

    def click_button_laptop(self):
        """
            Clicks the laptop button on the webpage.

            This function uses the `click_get_by_role`
            method to click the laptop button.
            """
        self.click_get_by_role(*PairwisePageLocators.LAPTOPS)

    def click_button_monitor(self):
        """
            Clicks the monitor button on the webpage.
            This function uses the `click_get_by_role`
            method to click the monitor button.
            """
        self.click_get_by_role(*PairwisePageLocators.MONITORS)

    def click_button_notebook(self):
        """
           Clicks the notebook button on the webpage.
           This function uses the `click_get_by_role`
           method to click the notebook button.
           """
        self.click_get_by_role(*PairwisePageLocators.DELL)

    def click_add_to_cart(self):
        """
            Clicks the 'Add to Cart' button on the webpage.
            This function uses the `click_get_by_role`
            method to click the 'Add to Cart' button.
            """
        self.click_get_by_role(*PairwisePageLocators.ADD_TO_CART)

    def click_button_cart(self):
        """
            Clicks the 'Cart' button on the webpage.
            This function uses the `click_button`
            method to click the 'Cart' button.
            """
        self.click_button(PairwisePageLocators.CART)

    def name_text_laptop(self):
        """
            Retrieve the name text of the laptop from the page.
            Returns:
                str: The name text of the laptop.
            """
        return self.inner_text(PairwisePageLocators.DELL_NAME)

    def name_text_notebook(self):
        """
            Retrieve the name text from the notebook.

            Returns:
                str: The name text from the notebook.
            """
        return self.text_by_role(*PairwisePageLocators.DELL_NAME_TEXT)

    def click_button_place_order(self):
        """
            Clicks the 'Place Order' button on the webpage.

            This function uses the `click_get_by_role`
            method to click the 'Place Order' button.
            """
        self.click_get_by_role(*PairwisePageLocators.PLACE_ORDER)

    def fill_name(self, name):
        """
            Fills the name field on the webpage with the specified name.
            Args:
                name (str): The name to be filled in the name field.
            """
        self.get_by_label(PairwisePageLocators.NAME).fill(name)

    def fill_country(self, country):
        """
            Fills the country field on the webpage with the specified country.
            Args:
                country (str): The country to be filled in the country field.
            """
        self.get_by_label(PairwisePageLocators.COUNTRY).fill(country)

    def fill_city(self, city):
        """
            Fills the city input field with the given city name.
            Args:
                city (str): The name of the city to fill.
            Returns:
                None
            """
        self.get_by_label(PairwisePageLocators.CITY).fill(city)

    def fill_credit_card(self, credit_card):
        """
        Fill the credit card input field with the
        provided credit card number.

        Args:
            credit_card (int): The credit card number to fill.

        Returns:
            None
        """
        # Find the credit card input field by its label and
        # fill it with the provided credit card number
        self.get_by_label(PairwisePageLocators.CREDIT_CARD).fill(credit_card)

    def fill_month(self, month):
        """
        Fill the month field with the given value.

        Args:
            month (int): The value to fill the month field with.
        """
        # Find the month field element by label
        # and fill it with the given value
        self.get_by_label(PairwisePageLocators.MONTH).fill(month)

    def fill_year(self, year):
        """
        Fill the year field with the given value.

        Args:
            year (int): The value to fill the year field with.
        """
        # Find the year field element by label and fill it with the given value
        self.get_by_label(PairwisePageLocators.YEAR).fill(year)

    def fill_form(self, person: PersonData):
        """
        Fills the form with the given person's data.

        Args:
            person (PersonData): The person's data.

        Returns:
            None
        """
        # Fill name
        self.fill_name(person.name)

        # Fill country
        self.fill_country(person.country)

        # Fill city
        self.fill_city(person.city)

        # Fill credit card
        self.fill_credit_card(person.credit_card)

        # Fill month
        self.fill_month(person.month)

        # Fill year
        self.fill_year(person.year)

    def click_button_purchase(self):
        """
        Clicks the 'Purchase' button on the webpage.

        This function uses the `click_get_by_role`
        method to click the 'Purchase' button.
        """
        self.click_get_by_role(*PairwisePageLocators.PURCHASE)

    def text_thank_you(self):
        """
        Returns the text of the thank-you message on the page.

        Returns:
            str: The text of the thank-you message.
        """
        return self.text_by_role(*PairwisePageLocators.THANK_YOU)

    def click_button_asus_monitor(self):
        """
        Clicks the 'ASUS Monitor' button on the webpage.

        This function uses the `click_get_by_role`
        method to click the 'ASUS Monitor' button.
        """
        self.click_get_by_role(*PairwisePageLocators.ASUS_MONITOR)

    def text_by_monitor(self):
        """
        Get the inner text of the ASUS monitor element.

        Returns:
            str: The inner text of the ASUS monitor element.
        """
        return self.inner_text(PairwisePageLocators.ASUS_MONITOR_TEXT)
