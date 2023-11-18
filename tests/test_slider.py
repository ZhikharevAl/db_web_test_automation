import allure
import pytest
from allure_commons.types import Severity

from pages.slider_page import SliderPage


@pytest.mark.ui
@allure.severity(Severity.TRIVIAL)
@pytest.mark.parametrize('slide_index', [0, 1, 2])
def test_slider(page, slide_index):
    """
    Тестирование слайдера на веб-странице.

    :param page: Экземпляр страницы для тестирования.
    :param slide_index: Индекс слайда, который следует проверить.

    """
    slider_page = SliderPage(page)
    with allure.step("Перейти на страницу со слайдером"):
        slider_page.go_to()
    with allure.step("Кликнуть на слайд"):
        slider_page.click_slide(slide_index)
    with allure.step("Проверить, что слайд активен"):
        assert slider_page.is_slide_active(slide_index)
