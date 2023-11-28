from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Класс HomePage наследует от базового класса BasePage и представляет собой
    домашнюю страницу веб-сайта. Он содержит методы, которые специфичны для
    домашней страницы.
    """

    def get_title(self):
        """
        Получение заголовка домашней страницы. Этот метод возвращает заголовок
        текущей страницы, который можно использовать для проверки того, что
        пользователь находится на правильной странице.
        """
        return self.title()
