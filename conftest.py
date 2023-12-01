import pytest
from playwright.sync_api import sync_playwright

from generator.generator_person_data import generate_person_data
from pages.product_page import ProductPage
from pages.register_and_login_page import RegisterAndLoginPage


@pytest.fixture(scope="session")
def browser():
    """
    Фикстура для запуска и закрытия браузера.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        yield browser
        browser.close()  # Закрытие браузера после теста


@pytest.fixture
def page(browser):
    """
    Фикстура для открытия и закрытия новой страницы в браузере.
    """
    context = browser.new_context()  # Создание нового контекста браузера
    page = context.new_page()  # Открытие новой страницы в браузере
    yield page
    context.clear_cookies()
    page.context.close()


@pytest.fixture
def user_account(page, base_url):
    """
    Фикстура для регистрации и входа в систему.
    """
    register_and_login = RegisterAndLoginPage(page, base_url)
    person = generate_person_data()
    register_and_login.go_to(base_url)
    username = person.name
    password = person.password
    register_and_login.register_and_login(username, password)
    return register_and_login


@pytest.fixture
def add_to_cart(page, base_url):
    """
    Фикстура для добавления карточки в корзину.
    """
    product_page = ProductPage(page, base_url)
    product_page.click_on_the_product()
    return product_page


@pytest.fixture(params=[True, False])
def user_account_authorized(request, page, base_url):
    if request.param:
        register_and_login = RegisterAndLoginPage(page, base_url)
        person = generate_person_data()
        register_and_login.go_to(base_url)
        username = person.name
        password = person.password
        register_and_login.register_and_login(username, password)
        return register_and_login
    else:
        return None
