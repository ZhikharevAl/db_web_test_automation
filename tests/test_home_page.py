import pytest

from pages.home_page import HomePage


# Проверка заголовка страницы
@pytest.mark.smoke
@pytest.mark.parametrize('url, expected_title, test_type', [
    ('https://www.demoblaze.com/', 'STORE', 'positive'),
    ('https://www.demoblaze.com/', 'Wrong Title', 'negative'),
])
def test_home_page_title(page, url, expected_title, test_type):
    home_page = HomePage(page)
    home_page.go_to()
    if test_type == 'positive':
        assert home_page.get_title() == expected_title, f"Wrong title for {url}"
    elif test_type == 'negative':
        assert home_page.get_title() != expected_title, f"Title should not be {expected_title}"

