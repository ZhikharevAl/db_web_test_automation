class LoginPageLocators:
    """
    Этот класс содержит локаторы для страницы входа в систему.
    """

    LOGIN_BUTTON_SELECTOR = "#login2"  # Селектор кнопки входа
    # Селектор поля ввода имени пользователя
    USERNAME_FIELD_SELECTOR = "#loginusername"
    # Селектор поля ввода пароля
    PASSWORD_FIELD_SELECTOR = "#loginpassword"
    # Селектор кнопки отправки формы входа
    SUBMIT_BUTTON_SELECTOR = "//button[@onclick='logIn()']"
    # Селектор для отображения имени пользователя после входа
    USERNAME_DISPLAY_SELECTOR = "#nameofuser"


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
    CLOSE_BUTTON = "(//button[@class='btn btn-secondary'])[2]"


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

    PRODUCTNAMESAMSUNG = "text=Samsung galaxy s6"


class CartPageLocators:
    """
    Этот класс содержит локаторы для страницы корзины.
    """

    # Локатор для кнопки "Корзина"
    CART = "//a[@id='cartur']"
    CART_BUTTON = "//a[contains(@onclick, 'add')]"
    PRICE = "#tbodyid > tr > td:nth-child(3)"


class PlaceOrderPageLocators:
    """
    Этот класс содержит локаторы для страницы оформления заказа.
    """

    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = "button.btn-success:has-text('Place Order')"
    NAME = "#name"  # Поле ввода имени
    COUNTRY = "#country"  # Поле ввода страны
    CITY = "#city"  # Поле ввода города
    CREDIT_CARD = "#card"  # Поле ввода номера кредитной карты
    MONTH = "#month"  # Поле ввода месяца
    YEAR = "#year"  # Поле ввода года
    PURCHASE = "button:has-text('Purchase')"  # Кнопка "Покупка"
    # Сообщение "Thank you for your purchase!"
    THANK_YOU = ".sweet-alert h2"


class PairwisePageLocators:
    """
    Этот класс содержит локаторы для pairwise теста.
    """

    PHONES = ("link", "Phones")
    LAPTOPS = ("link", "Laptops")
    MONITORS = ("link", "Monitors")
    SONYXPERIAZ5 = ("link", "Sony xperia z5")
    SONYXPERIAZ5_TEXT = ("heading", "Sony xperia z5")
    SONYXPERIAZ5_TEXT_CART = ("cell", "Sony xperia z5")
    DELL = ("link", "Dell 15.6 Inch")
    ADD_TO_CART = ("link", "Add to cart")
    CART = "a[id='cartur']"
    DELL_NAME = "//*[text() = '2017 Dell 15.6 Inch']"
    DELL_NAME_TEXT = ("heading", "Dell 15.6 Inch")
    PLACE_ORDER = ("button", "Place Order")
    NAME = "Total:"
    COUNTRY = "Country:"
    CITY = "City:"
    CREDIT_CARD = "Credit Card:"
    MONTH = "Month:"
    YEAR = "Year:"
    PURCHASE = ("button", "Purchase")
    THANK_YOU = ("heading", "Thank you for your purchase!")
    ASUS_MONITOR = "link", "ASUS Full HD"
    ASUS_MONITOR_TEXT = "//*[text() = 'ASUS Full HD']"
