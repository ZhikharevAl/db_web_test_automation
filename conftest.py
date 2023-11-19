import pytest
from playwright.sync_api import sync_playwright

from pages.register_and_login_page import RegisterAndLoginPage


@pytest.fixture
def browser():
    """
    Фикстура для запуска и закрытия браузера.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Запуск браузера
        yield browser
        browser.close()  # Закрытие браузера после теста


@pytest.fixture
def page(browser):
    """
    Фикстура для открытия и закрытия новой страницы в браузере.
    """
    page = browser.new_page()  # Открытие новой страницы в браузере
    yield page
    page.close()  # Закрытие страницы после теста


@pytest.fixture(params=[
    ('https://www.demoblaze.com/', 'STORE', 'positive'),
    ('https://www.demoblaze.com/', 'Wrong Title', 'negative'),
])
def url(request):
    """
    Фикстура для предоставления различных URL-адресов и ожидаемых результатов.
    """
    return request.param


@pytest.fixture
def user_account(page):
    """
    Фикстура для регистрации и входа в систему.
    """
    register_and_login = RegisterAndLoginPage(page)
    register_and_login.go_to()
    username = 'username'
    password = 'password'
    register_and_login.register_and_login(username, password)
