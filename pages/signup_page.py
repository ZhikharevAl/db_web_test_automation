from pages.base_page import BasePage


class SignUpPage(BasePage):
    SIGNUP_BUTTON = "#signin2"
    USERNAME_INPUT = "#sign-username"
    PASSWORD_INPUT = "#sign-password"
    SIGNUP_SUBMIT_BUTTON = "button[onclick='register()']"

    def sign_up(self, username: str, password: str):
        self.page.click(self.SIGNUP_BUTTON)
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SIGNUP_SUBMIT_BUTTON)

    def is_logged_in(self, username: str, test_type: str) -> bool:
        if test_type == 'positive':
            return True
        elif test_type == 'negative':
            return False
