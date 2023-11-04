
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_SELECTOR = '#login2'
    USERNAME_FIELD_SELECTOR = '#loginusername'
    PASSWORD_FIELD_SELECTOR = '#loginpassword'
    SUBMIT_BUTTON_SELECTOR = '#logInModal >> button.btn-primary'
    USERNAME_DISPLAY_SELECTOR = '#nameofuser'

    def login(self, username, password):
        self.go_to()  # Использовать метод go_to из BasePage
        self.click_button(self.LOGIN_BUTTON_SELECTOR)  # Использовать метод click_button из BasePage
        self.page.fill(self.USERNAME_FIELD_SELECTOR, username)
        self.page.fill(self.PASSWORD_FIELD_SELECTOR, password)
        self.click_button(self.SUBMIT_BUTTON_SELECTOR)

    def is_logged_in(self, username) -> bool:
        return self.page.inner_text(self.USERNAME_DISPLAY_SELECTOR) == f'Welcome {username}'
