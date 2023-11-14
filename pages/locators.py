class LoginPageLocators:
    LOGIN_BUTTON_SELECTOR = '#login2'
    USERNAME_FIELD_SELECTOR = '#loginusername'
    PASSWORD_FIELD_SELECTOR = '#loginpassword'
    SUBMIT_BUTTON_SELECTOR = '#logInModal >> button.btn-primary'
    USERNAME_DISPLAY_SELECTOR = '#nameofuser'


class SignUpPageLocators:
    SIGNUP_BUTTON = "#signin2"
    USERNAME_INPUT = "#sign-username"
    PASSWORD_INPUT = "#sign-password"
    SIGNUP_SUBMIT_BUTTON = "button[onclick='register()']"
    CLOSE_BUTTON = ("#signInModal > div > div > div.modal-footer > "
                    "button.btn.btn-secondary")


class LogOutPageLocators:
    LOGOUT_BUTTON = "#logout2"
