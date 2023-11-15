from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Класс LoginPage наследует от базового класса BasePage и представляет собой
    страницу входа в систему. Он содержит методы для входа в систему и проверки
    статуса входа.
    """

    def login(self, username, password):
        """
        Вход в систему с указанными именем пользователя и паролем.

        :param username: Имя пользователя для входа в систему.
        :param password: Пароль для входа в систему.
        """
        self.go_to()
        self.click_button(LoginPageLocators.LOGIN_BUTTON_SELECTOR)
        self.fill(LoginPageLocators.USERNAME_FIELD_SELECTOR, username)
        self.fill(LoginPageLocators.PASSWORD_FIELD_SELECTOR, password)
        self.click_button(LoginPageLocators.SUBMIT_BUTTON_SELECTOR)

    def is_logged_in(self, username) -> bool:
        """
        Проверяет, выполнен ли вход в систему для указанного пользователя.

        :param username: Имя пользователя, для которого проверяется вход
                         в систему.
        :return: True, если пользователь вошел в систему, иначе False.
        """
        return (self.inner_text
                (LoginPageLocators.USERNAME_DISPLAY_SELECTOR) ==
                f'Welcome {username}')
