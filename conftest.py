import pytest
from playwright.sync_api import sync_playwright

from pages.product_page import ProductPage
from pages.register_and_login_page import RegisterAndLoginPage


@pytest.fixture(autouse=True)
def browser():
    """
    Фикстура для запуска и закрытия браузера.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Запуск браузера
        yield browser
        browser.close()  # Закрытие браузера после теста


@pytest.fixture(autouse=True)
def page(browser):
    """
    Фикстура для открытия и закрытия новой страницы в браузере.
    """
    context = browser.new_context()  # Создание нового контекста браузера
    page = context.new_page()  # Открытие новой страницы в браузере
    yield page
    context.clear_cookies()
    page.context.close()


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
    return register_and_login


@pytest.fixture
def add_to_cart(page):
    """
    Фикстура для добавления карточки в корзину.
    """
    product_page = ProductPage(page)
    product_page.click_on_the_product()
    return product_page
