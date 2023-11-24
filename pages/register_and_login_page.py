
from pages.base_page import BasePage
from pages.locators import SignUpPageLocators, LoginPageLocators


class RegisterAndLoginPage(BasePage):
    """
    Класс RegisterAndLoginPage наследует от базового
    класса BasePage и представляет собой
    страницу регистрации и входа в систему.
    Он содержит методы для регистрации и входа в систему.
    """

    def register_and_login(self, username: str, password: str):
        """
        Регистрация и вход в систему с указанными
        именем пользователя и паролем.

        :param username: Имя пользователя для регистрации
                         и входа в систему.
        :param password: Пароль для регистрации и входа в систему.
        """
        self.click_button(SignUpPageLocators.SIGNUP_BUTTON)
        self.fill(SignUpPageLocators.USERNAME_INPUT, username)
        self.fill(SignUpPageLocators.PASSWORD_INPUT, password)
        self.click_button(SignUpPageLocators.SIGNUP_SUBMIT_BUTTON)
        self.wait_for_selector(SignUpPageLocators.CLOSE_BUTTON)
        self.click_button(SignUpPageLocators.CLOSE_BUTTON)

        self.click_button(LoginPageLocators.LOGIN_BUTTON_SELECTOR)
        self.fill(LoginPageLocators.USERNAME_FIELD_SELECTOR, username)
        self.fill(LoginPageLocators.PASSWORD_FIELD_SELECTOR, password)
        self.click_button(LoginPageLocators.SUBMIT_BUTTON_SELECTOR)
        self.wait_for_selector(LoginPageLocators.USERNAME_DISPLAY_SELECTOR)

    def is_logged_in(self, username: str) -> bool:
        """
        Проверяет, выполнен ли вход в систему для указанного пользователя.

        :param username: Имя пользователя, для которого
                         проверяется вход в систему.
        :return: True, если пользователь вошел в систему, иначе False.
        """
        return (self.inner_text
                (LoginPageLocators.USERNAME_DISPLAY_SELECTOR)
                == f'Welcome {username}')
