import pytest
import allure
import logging

from allure_commons.types import Severity

from pages.home_page import HomePage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('url, expected_title, test_type', [
    ('https://www.demoblaze.com/', 'STORE', 'positive'),
    ('https://www.demoblaze.com/', 'Wrong Title', 'negative'),
])
def test_home_page_title(page, url, expected_title, test_type, caplog):
    """
    Тестирование заголовка домашней страницы.

    :param page: Экземпляр страницы для тестирования.
    :param url: URL-адрес домашней страницы.
    :param expected_title: Ожидаемый заголовок страницы.
    :param test_type: Тип теста ('positive' или 'negative').
    :param caplog: Журнал для записи результатов теста.
    """
    caplog.set_level(logging.INFO)
    home_page = HomePage(page)
    with allure.step("Открываем страницу входа"):
        home_page.go_to()
    with ((allure.step("Проверка заголовка"))):
        if test_type == 'positive':
            assert home_page.get_title() == expected_title, \
                f"Wrong title for {url}"
            logging.info(f"Title is correct for {url}")
        elif test_type == 'negative':
            assert home_page.get_title() != expected_title, \
                f"Title should not be {expected_title}"
            logging.info(f"Title is not {expected_title} as "
                         f"expected for {url}")
