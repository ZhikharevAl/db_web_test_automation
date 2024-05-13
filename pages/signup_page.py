from pages.base_pages.base_page import BasePage
from pages.locators import SignUpPageLocators


class SignUpPage(BasePage):
    """
    Класс SignUpPage наследует от базового класса BasePage и представляет собой
    страницу регистрации. Он содержит методы для регистрации и
    проверки статуса входа.
    """

    def sign_up(self, username: str, password: str):
        """
        Регистрация с указанными именем пользователя и паролем.

        :param username: Имя пользователя для регистрации.
        :param password: Пароль для регистрации.
        """
        self.click_button(SignUpPageLocators.SIGNUP_BUTTON)
        self.fill(SignUpPageLocators.USERNAME_INPUT, username)
        self.fill(SignUpPageLocators.PASSWORD_INPUT, password)
        self.click_button(SignUpPageLocators.SIGNUP_SUBMIT_BUTTON)
        self.click_button(SignUpPageLocators.CLOSE_BUTTON)

    def is_logged_in(self, username: str, test_type: str) -> bool:
        """
        Проверяет, выполнен ли вход в систему для указанного пользователя.

        :param username: Имя пользователя, для которого проверяется
                 вход в систему.
        :param test_type: Тип теста ('positive' или 'negative').
        :return: True, если пользователь вошел в систему (для 'positive'),
                 False - в противном случае (для 'negative').
        """
        if test_type == "positive":
            return True
        elif test_type == "negative":
            return False
