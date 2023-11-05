import allure
import pytest
from allure_commons.types import Severity

from tests.test_home_page import test_home_page_title
from tests.test_login import test_login_functionality


@pytest.mark.e2e
@allure.severity(Severity.BLOCKER)
def test_e2e(page, url, caplog):
    expected_title, test_type = url[1], url[2]
    url = url[0]
    username = 'username'  # Замените на вашу фикстуру или значение
    password = 'password'  # Замените на вашу фикстуру или значение
    with allure.step("Проверка заголовка домашней страницы"):
        test_home_page_title(page, url, expected_title, test_type, caplog)
    with allure.step("Проверка функциональности входа в систему"):
        # TODO: Временно проверяем только на test_type = 'negative'
        test_type = 'negative'
        test_login_functionality(page, username, password, test_type, caplog)
    # TODO: Добавить другие тесты, чтобы сделать его полноценным e2e тестом

