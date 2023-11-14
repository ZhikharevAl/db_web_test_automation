from pages.base_page import BasePage
from pages.locators import SignUpPageLocators


class SignUpPage(BasePage):
    def sign_up(self, username: str, password: str):
        self.page.click(SignUpPageLocators.SIGNUP_BUTTON)
        self.page.fill(SignUpPageLocators.USERNAME_INPUT, username)
        self.page.fill(SignUpPageLocators.PASSWORD_INPUT, password)
        self.page.click(SignUpPageLocators.SIGNUP_SUBMIT_BUTTON)
        self.page.click(SignUpPageLocators.CLOSE_BUTTON)

    def is_logged_in(self, username: str, test_type: str) -> bool:
        if test_type == 'positive':
            return True
        elif test_type == 'negative':
            return False
