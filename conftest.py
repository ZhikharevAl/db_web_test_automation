import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        yield browser
        browser.close()  # Закрытие браузера после теста


@pytest.fixture
def page(browser):
    page = browser.new_page()  # Открытие новой страницы в браузере
    yield page
    page.close()  # Закрытие страницы после теста


@pytest.fixture(params=[
    ('https://www.demoblaze.com/', 'STORE', 'positive'),
    ('https://www.demoblaze.com/', 'Wrong Title', 'negative'),
])
def url(request):
    return request.param
