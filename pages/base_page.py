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

    def click_button(self, selector: str):
        """
        Кликает по кнопке, соответствующей указанному селектору.

        :param selector: Селектор кнопки, по которой нужно кликнуть.
        """
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        """
        Заполняет поле ввода, выбранное селектором, указанным значением.

        :param selector: Селектор поля ввода, которое нужно заполнить.
        :param value: Значение, которым нужно заполнить поле ввода.
        """
        self.page.fill(selector, value)

    def title(self):
        """
        Возвращает заголовок текущей страницы.

        :return: Заголовок текущей страницы.
        """
        return self.page.title()

    def inner_text(self, selector: str):
        """
        Возвращает текст элемента, выбранного селектором.

        :param selector: Селектор элемента, текст которого нужно получить.
        :return: Текст выбранного элемента.
        """
        return self.page.inner_text(selector)

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

    def check_element(self, selector):
        """
        Проверяет, есть ли элемент на странице, соответствующий
        указанному селектору.
        :param selector: Селектор элемента, которого нужно проверить.
        """

        return self.page.is_visible(selector)

    def scroll_down(self):
        """
        Прокручивает страницу вниз.
        """
        self.page.keyboard.press('End')

    def click_button_by_role(self, name):
        """
        Метод для клика по кнопке с указанным именем.
        """
        self.page.get_by_role("button", name=name).click()

    def bring_to_front(self):
        """
        Метод для перевода страницы на передний план.
        """
        self.page.bring_to_front()