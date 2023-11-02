from pages.home_page import HomePage


# Проверка заголовка страницы
def test_home_page_title(page):
    home_page = HomePage(page)
    home_page.go_to()
    assert home_page.get_title() == "STORE"
