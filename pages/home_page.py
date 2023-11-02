from pages.base_page import BasePage


class HomePage(BasePage):
    # URL домашней страницы
    URL = "https://www.demoblaze.com/"

    # Переход на домашнюю страницу
    def go_to(self):
        self.page.goto(self.URL)

    # Получение заголовка страницы
    def get_title(self):
        return self.page.title()
