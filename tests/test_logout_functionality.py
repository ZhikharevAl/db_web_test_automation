import logging

import allure
import pytest
from allure_commons.types import Severity

from pages.logout_page import LogOutPage


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
def test_logout_functionality(page, caplog, user_account):
    """
    Тестирование функциональности выхода из системы.

    :param page: Экземпляр страницы для тестирования.
    :param caplog: Журнал для записи результатов теста.
    :param user_account: Fixture для регистрации и авторизации.
    :return:
    """
    caplog.set_level(logging.INFO)
    logout_page = LogOutPage(page)
    logout_page.log_out()
    with allure.step("Проверяем, что вышли из системы"):
        is_logged_out = logout_page.is_logged_out()
    assert is_logged_out

    if is_logged_out:
        logging.info("Выход из системы выполнен успешно.")
    else:
        logging.error("Выход из системы не выполнен.")
