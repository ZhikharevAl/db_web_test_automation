from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, username, password):
        self.go_to()
        self.click_button(LoginPageLocators.LOGIN_BUTTON_SELECTOR)
        self.page.fill(LoginPageLocators.USERNAME_FIELD_SELECTOR, username)
        self.page.fill(LoginPageLocators.PASSWORD_FIELD_SELECTOR, password)
        self.click_button(LoginPageLocators.SUBMIT_BUTTON_SELECTOR)

    def is_logged_in(self, username) -> bool:
        return (self.page.inner_text
                (LoginPageLocators.USERNAME_DISPLAY_SELECTOR) ==
                f'Welcome {username}')
