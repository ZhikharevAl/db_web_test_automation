import allure
import pytest
from allure_commons.types import Severity

from pages.slider_page import SliderPage

import logging


@pytest.mark.ui
@allure.severity(Severity.TRIVIAL)
@allure.description("Тестирование слайдера на веб-странице.")
@pytest.mark.parametrize('slide_index', [0, 1, 2])
def test_slider(page, slide_index, caplog):
    """
    Тестирование слайдера на веб-странице.

    :param page: Экземпляр страницы для тестирования.
    :param slide_index: Индекс слайда, который следует проверить.

    """
    caplog.set_level(logging.INFO)
    slider_page = SliderPage(page)
    with allure.step("Перейти на страницу со слайдером"):
        slider_page.go_to()
        logging.info("Страница со слайдером открыта.")
    with allure.step("Кликнуть на слайд"):
        slider_page.click_slide(slide_index)
        logging.info(f"Кликнули на слайд с индексом {slide_index}.")
    with allure.step("Проверить, что слайд активен"):
        is_slide_active = slider_page.is_slide_active(slide_index)
        assert is_slide_active, f"Слайд с индексом {slide_index} не активен."
        if is_slide_active:
            logging.info(f"Слайд с индексом {slide_index} активен.")
        else:
            logging.error(f"Слайд с индексом {slide_index} не активен.")
