from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс страницы. Этот класс содержит общие методы,
    которые могут быть использованы на любой странице.
    """

    def __init__(self, page: Page, base_url: str):
        """
        Инициализация экземпляра BasePage.

        :param page: Экземпляр страницы, который будет
        использоваться для взаимодействия со страницей.
        """
        self.page = page
        self.base_url = base_url

    def go_to(self, base_url: str):
        """
        Переходит на URL, указанный в self.URL.
        """
        self.page.goto(self.base_url)

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

    def click_button_by_role(self, name: str) -> None:
        """
        Метод для клика по кнопке с указанным именем.
        """
        self.page.get_by_role("button", name=name).click()

    def bring_to_front(self):
        """
        Метод для перевода страницы на передний план.
        """
        self.page.bring_to_front()

    def screenshot(self, path: str):
        """
        Метод для снимка экрана.
        """
        self.page.screenshot(path=path, full_page=True)

    def wait_for_event(self, event: str):
        """
        Метод для ожидания события.
        """
        self.page.wait_for_event(event)

    def handle_popup(self):
        """
        Метод для обработки всплывающего окна.
        """

        self.wait_for_load_state()
        print(self.title())

    def wait_for_load_state(self):
        self.wait_for_load_state()

    def focus(self, selector: str):
        """
        Метод для фокусировки элемента.
        """
        self.page.focus(selector)

    def element_is_visible(self, selector: str):
        return self.page.is_visible(selector)

    def click_get_by_role(self, role, name):
        self.page.get_by_role(role, name=name).click()

    def get_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def text_by_role(self, role, name):
        """
        Retrieves the inner text of an element by its role and name.

        Args:
            role (str): The role of the element.
            name (str): The name of the element.

        Returns:
            str: The inner text of the element.
        """
        return self.get_by_role(role, name).inner_text()

    def get_by_label(self, label):
        """
        Retrieves an element by its label.

        Args:
            label (str): The label of the element.

        Returns:
            WebElement: The element with the specified label.
        """
        return self.page.get_by_label(label)
