import pytest
from playwright.sync_api import sync_playwright, BrowserContext, Page

from generator.generator_person_data import generate_person_data
from pages.base_pages.base_test import BaseTest
from pages.product_page import ProductPage
from pages.register_and_login_page import RegisterAndLoginPage


@pytest.fixture(autouse=True)
def browser() -> sync_playwright:
    """
    Фикстура для запуска и закрытия браузера.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(autouse=True)
def page(browser: BrowserContext) -> Page:
    """
    Фикстура для открытия и закрытия новой страницы в браузере.
    """
    context = browser.new_context()  # Создание нового контекста браузера
    page = context.new_page()  # Открытие новой страницы в браузере
    yield page
    context.clear_cookies()
    page.context.close()


class TestFixtures(BaseTest):
    @pytest.fixture
    def user_account(self, page: Page, base_url: str) -> RegisterAndLoginPage:
        """
        Фикстура для регистрации и входа в систему.
        """

        person = generate_person_data()
        self.register_and_login_page.go_to(base_url)
        username = person.name
        password = person.password
        self.register_and_login_page.register_and_login(username, password)
        return self.register_and_login_page

    @pytest.fixture
    def add_to_cart(self, page: Page) -> ProductPage:
        """
        Фикстура для добавления карточки в корзину.
        """
        self.product_page.click_on_the_product()
        return self.product_page

    @pytest.fixture(params=[True, False])
    def user_account_authorized(self, request, page, base_url):
        if request.param:
            person = generate_person_data()
            self.register_and_login_page.go_to(base_url)
            username = person.name
            password = person.password
            self.register_and_login_page.register_and_login(username, password)
            return self.register_and_login_page
        else:
            return None
