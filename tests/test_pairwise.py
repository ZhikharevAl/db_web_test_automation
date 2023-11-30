import allure
import pytest
from allure_commons.types import Severity
from logging_config import configure_logger
from pages.pairwise_page import PairwisePage

logger = configure_logger(__name__, 'test.log')


@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.title("Тестирование функциональности просмотра продукта.")
def test_click_smartphone_button(page, base_url, user_account):
    """
    Тестирование функциональности просмотра продукта.

    :param page: Экземпляр страницы для тестирования.
    :param base_url: URL-адрес домашней страницы.
    :param user_account: Фикстура для регистрации и входа в систему.
    """
    pairwise_page = PairwisePage(page, base_url)

    try:
        with allure.step("Нажимаем кнопку смартфона"):
            pairwise_page.click_button_smartphone()
            logger.info("Кнопка смартфона нажата.")

        with allure.step("Нажимаем кнопку телефона"):
            pairwise_page.click_button_phone()
            logger.info("Кнопка телефона нажата.")

        with allure.step("Проверяем текст названия телефона"):
            assert pairwise_page.name_text_phone() == 'Sony xperia z5'
            logger.info("Текст названия телефона проверен и "
                        "соответствует ожидаемому.")

    except Exception as e:
        logger.error(f"Ошибка при выполнении теста: {e}")
        allure.attach(
            name="screenshot",
            body=page.screenshot(),
            attachment_type=allure.attachment_type.PNG,
        )
        raise
