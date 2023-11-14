from playwright.sync_api import Page


class BasePage:
    URL = "https://www.demoblaze.com/"

    def __init__(self, page: Page):
        self.page = page

    def go_to(self):
        self.page.goto(self.URL)

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)

    def click_button(self, selector: str):
        self.page.click(selector)
