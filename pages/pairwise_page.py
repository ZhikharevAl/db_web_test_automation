from pages.base_page import BasePage
from pages.locators import PairwisePageLocators


class PairwisePage(BasePage):

    def click_button_smartphone(self):
        self.click_get_by_role(*PairwisePageLocators.PHONES)

    def click_button_phone(self):
        self.click_get_by_role(*PairwisePageLocators.SONYXPERIAZ5)

    def name_text_phone(self):
        return self.text_by_role(*PairwisePageLocators.SONYXPERIAZ5_TEXT)
