from pages.base_page import BasePage
from pages.locators import LogOutPageLocators


class LogOutPage(BasePage):
    """
    Класс LogOutPage наследует от базового класса BasePage и представляет собой
    страницу выхода из системы. Он содержит методы для выхода из системы.
    """

    def log_out(self):
        """
        Выполняет выход из системы, нажимая на кнопку выхода.
        """
        self.click_button(LogOutPageLocators.LOGOUT_BUTTON)

    def is_logged_out(self):
        """
        Проверяет, выполнен ли выход из системы.
        """
        return self.check_element(LogOutPageLocators.LOGOUT_BUTTON) is False
