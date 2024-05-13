import pytest

from pages.cart_page import CartPage
from pages.e2e_page import E2EPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogOutPage
from pages.pairwise_page import PairwisePage
from pages.place_order_page import PlaceOrderPage
from pages.product_page import ProductPage
from pages.register_and_login_page import RegisterAndLoginPage
from pages.signup_page import SignUpPage
from pages.slider_page import SliderPage


class BaseTest:
    home_page: HomePage
    login_page: LoginPage
    signup_page: SignUpPage
    slider_page: SliderPage
    cart_page: CartPage
    logout_page: LogOutPage
    product_page: ProductPage
    register_and_login_page: RegisterAndLoginPage
    place_order_page: PlaceOrderPage
    pairwise_page: PairwisePage
    e2e_page: E2EPage

    @pytest.fixture(autouse=True)
    def setup(self, request, page, base_url):
        request.cls.page = page

        request.cls.home_page = HomePage(page, base_url)
        request.cls.login_page = LoginPage(page, base_url)
        request.cls.signup_page = SignUpPage(page, base_url)
        request.cls.slider_page = SliderPage(page, base_url)
        request.cls.cart_page = CartPage(page, base_url)
        request.cls.logout_page = LogOutPage(page, base_url)
        request.cls.product_page = ProductPage(page, base_url)
        request.cls.register_and_login_page = RegisterAndLoginPage(page, base_url)
        request.cls.place_order_page = PlaceOrderPage(page, base_url)
        request.cls.pairwise_page = PairwisePage(page, base_url)
        request.cls.e2e_page = E2EPage(page, base_url)
