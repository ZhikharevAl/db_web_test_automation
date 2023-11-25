class LoginPageLocators:
    """
    Этот класс содержит локаторы для страницы входа в систему.
    """
    LOGIN_BUTTON_SELECTOR = '#login2'  # Селектор кнопки входа
    # Селектор поля ввода имени пользователя
    USERNAME_FIELD_SELECTOR = '#loginusername'
    # Селектор поля ввода пароля
    PASSWORD_FIELD_SELECTOR = '#loginpassword'
    # Селектор кнопки отправки формы входа
    SUBMIT_BUTTON_SELECTOR = '#logInModal >> button.btn-primary'
    # Селектор для отображения имени пользователя после входа
    USERNAME_DISPLAY_SELECTOR = '#nameofuser'


class SignUpPageLocators:
    """
    Этот класс содержит локаторы для страницы регистрации.
    """
    SIGNUP_BUTTON = "#signin2"  # Селектор кнопки регистрации
    # Селектор поля ввода имени пользователя при регистрации
    USERNAME_INPUT = "#sign-username"
    # Селектор поля ввода пароля при регистрации
    PASSWORD_INPUT = "#sign-password"
    # Селектор кнопки отправки формы регистрации
    SIGNUP_SUBMIT_BUTTON = "button[onclick='register()']"
    # Селектор кнопки закрытия модального окна регистрации
    CLOSE_BUTTON = ("#signInModal > div > div > div.modal-footer > "
                    "button.btn.btn-secondary")


class LogOutPageLocators:
    """
    Этот класс содержит локаторы для страницы выхода из системы.
    """
    LOGOUT_BUTTON = "#logout2"  # Селектор кнопки выхода


class SliderLocators:
    """
    Этот класс содержит локаторы для слайдера на главной странице.
    """
    SLIDER = ".carousel-indicators"  # Селектор контейнера слайдера
    # Селекторы отдельных слайдов в слайдере
    SLIDES = ".carousel-indicators li"


class ProductPageLocators:
    """
    Этот класс содержит локаторы для страницы продукта.
    """
    # Локатор для продукта "Sony vaio i5"
    PRODUCTNAME = "//*[text() = 'Sony vaio i5']"

    # Локатор для имени продукта на странице продукта
    NAMEPRODUCT = "#tbodyid > h2"


class CartPageLocators:
    """
    Этот класс содержит локаторы для страницы корзины.
    """
    # Локатор для кнопки "Корзина"
    CART = "#navbarExample > ul > li:nth-child(4) > a"
    CART_BUTTON = "#tbodyid > div.row > div > a"
    PRICE = "#tbodyid > tr > td:nth-child(3)"


class PlaceOrderPageLocators:
    """
        Этот класс содержит локаторы для страницы оформления заказа.
    """
    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = "#page-wrapper > div > div.col-lg-1 > button"
    NAME = "#name"  # Поле ввода имени
    COUNTRY = "#country"  # Поле ввода страны
    CITY = "#city"  # Поле ввода города
    CREDIT_CARD = "#card"  # Поле ввода номера кредитной карты
    MONTH = "#month"  # Поле ввода месяца
    YEAR = "#year"  # Поле ввода года
    PURCHASE = "//*[text() = 'Purchase"  # Кнопка "Покупка"
    # Сообщение "Thank you for your purchase!"
    THANK_YOU = "div[data-timer='null'] h2"
