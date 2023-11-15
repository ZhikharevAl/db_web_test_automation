from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс страницы. Этот класс содержит общие методы,
    которые могут быть использованы на любой странице.
    """
    URL = "https://www.demoblaze.com/"

    def __init__(self, page: Page):
        """
        Инициализация экземпляра BasePage.

        :param page: Экземпляр страницы, который будет
        использоваться для взаимодействия со страницей.
        """
        self.page = page

    def go_to(self):
        """
        Переходит на URL, указанный в self.URL.
        """
        self.page.goto(self.URL)

    def query_selector_all(self, selector):
        """
        Возвращает все элементы на странице, которые соответствуют
        указанному селектору.

        :param selector: Селектор для поиска элементов на странице.
        :return: Список элементов, соответствующих селектору.
        """
        return self.page.query_selector_all(selector)

    def wait_for_selector(self, selector: str):
        """
        Ожидает, пока на странице не появится элемент, соответствующий
        указанному селектору.

        :param selector: Селектор элемента, который нужно дождаться.
        """
        self.page.wait_for_selector(selector)

    def click_button(self, selector: str):
        """
        Кликает по кнопке, соответствующей указанному селектору.

        :param selector: Селектор кнопки, по которой нужно кликнуть.
        """
        self.page.click(selector)
