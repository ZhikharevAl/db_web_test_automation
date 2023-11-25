
from pages.base_page import BasePage
from pages.locators import (SignUpPageLocators, LoginPageLocators,
                            ProductPageLocators, CartPageLocators,
                            PlaceOrderPageLocators)
from pages.place_order_page import PlaceOrderPage


class E2EPage(PlaceOrderPage, BasePage):

    def go_to_e2e(self):
        self.go_to()

    def check_product_store_text(self):
        self.title()

    def register(self):
        self.click_button(SignUpPageLocators.SIGNUP_BUTTON)
        self.fill(SignUpPageLocators.USERNAME_INPUT, "test")
        self.fill(SignUpPageLocators.PASSWORD_INPUT, "test")
        self.click_button(SignUpPageLocators.SIGNUP_SUBMIT_BUTTON)
        self.click_button(SignUpPageLocators.CLOSE_BUTTON)

    def login_happy_path(self):
        self.click_button(LoginPageLocators.LOGIN_BUTTON_SELECTOR)
        self.fill(LoginPageLocators.USERNAME_FIELD_SELECTOR, "test")
        self.fill(LoginPageLocators.PASSWORD_FIELD_SELECTOR, "test")
        self.click_button(LoginPageLocators.SUBMIT_BUTTON_SELECTOR)

    def authorization_check(self):
        self.element_is_visible(LoginPageLocators.USERNAME_DISPLAY_SELECTOR)

    def add_product_to_cart(self):
        self.click_button(ProductPageLocators.PRODUCTNAME)
        self.click_button(CartPageLocators.CART_BUTTON)
        self.click_button(CartPageLocators.CART)

    def order(self):
        self.click_button(PlaceOrderPageLocators.PLACE_ORDER_BUTTON)

    def order_check(self):
        self.element_is_visible(PlaceOrderPageLocators.THANK_YOU)
