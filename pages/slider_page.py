from pages.base_pages.base_page import BasePage
from pages.locators import SliderLocators


class SliderPage(BasePage):
    """
    Класс SliderPage наследует от базового класса BasePage и представляет собой
    страницу со слайдером. Он содержит методы для взаимодействия со слайдером.
    """

    def get_slides(self):
        """
        Получение всех слайдов на странице.

        :return: Список всех слайдов на странице.
        """
        return self.query_selector_all(SliderLocators.SLIDES)

    def click_slide(self, slide_index):
        """
        Клик по слайду с указанным индексом.

        :param slide_index: Индекс слайда, по которому нужно кликнуть.
        """
        slides = self.get_slides()
        if slide_index < len(slides):
            slides[slide_index].click()

    def is_slide_active(self, slide_index):
        """
        Проверка, является ли слайд с указанным индексом активным.

        :param slide_index: Индекс слайда, который нужно проверить.
        :return: True, если слайд активен, иначе False.
        """
        slides = self.get_slides()
        if slide_index < len(slides):
            return "active" in slides[slide_index].get_attribute("class")
        return False
