from pages.base_page import BasePage
from pages.locators import SignUpPageLocators, LoginPageLocators


class RegisterAndLoginPage(BasePage):

    def register_and_login(self, username: str, password: str):
        self.page.click(SignUpPageLocators.SIGNUP_BUTTON)
        self.page.fill(SignUpPageLocators.USERNAME_INPUT, username)
        self.page.fill(SignUpPageLocators.PASSWORD_INPUT, password)
        self.page.click(SignUpPageLocators.SIGNUP_SUBMIT_BUTTON)
        self.page.click(SignUpPageLocators.CLOSE_BUTTON)

        self.click_button(LoginPageLocators.LOGIN_BUTTON_SELECTOR)
        self.page.fill(LoginPageLocators.USERNAME_FIELD_SELECTOR, username)
        self.page.fill(LoginPageLocators.PASSWORD_FIELD_SELECTOR, password)
        self.click_button(LoginPageLocators.SUBMIT_BUTTON_SELECTOR)

    def is_logged_in(self, username: str) -> bool:
        return (self.page.inner_text
                (LoginPageLocators.USERNAME_DISPLAY_SELECTOR)
                == f'Welcome {username}')
