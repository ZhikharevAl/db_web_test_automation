import allure
import pytest
from allure_commons.types import Severity

from logging_config import configure_logger
from pages.slider_page import SliderPage

import time

logger = configure_logger(__name__, 'test.log')


@pytest.mark.ui
@allure.severity(Severity.TRIVIAL)
@allure.description("Тестирование слайдера на веб-странице.")
@pytest.mark.parametrize('slide_index', [0, 1, 2])
def test_slider(page, base_url, slide_index):
    """
    Тестирование слайдера на веб-странице.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param slide_index: Индекс слайда, который следует проверить.
    """
    slider_page = SliderPage(page, base_url)

    try:
        with allure.step(f"Перейти на страницу со слайдером ({base_url})"):
            start_time = time.time()
            slider_page.go_to(base_url)
            end_time = time.time()
            logger.info(f"Страница со слайдером открыта за "
                        f"{end_time - start_time:.2f} секунд.")

        with allure.step(f"Кликнуть на слайд с индексом {slide_index}"):
            start_time = time.time()
            slider_page.click_slide(slide_index)
            end_time = time.time()
            logger.info(f"Кликнули на слайд с индексом {slide_index} "
                        f"за {end_time - start_time:.2f} секунд.")

        with allure.step(f"Проверить, что слайд с индексом "
                         f"{slide_index} активен"):
            start_time = time.time()
            is_slide_active = slider_page.is_slide_active(slide_index)
            end_time = time.time()

            assert is_slide_active, (f"Слайд с индексом "
                                     f"{slide_index} не активен.")
            if is_slide_active:
                logger.info(f"Слайд с индексом {slide_index} активен "
                            f"за {end_time - start_time:.2f} секунд.")
            else:
                logger.error(f"Слайд с индексом {slide_index} не "
                             f"активен за {end_time - start_time:.2f} секунд.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
