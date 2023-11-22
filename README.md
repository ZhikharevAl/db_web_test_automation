# 🎭UI Automation with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).

## Описание

Этот проект представляет собой набор автоматических тестов пользовательского интерфейса, написанных на Python с использованием Playwright, Allure и Pytest.

## Установка

1. Установите Python: `https://www.python.org/downloads/`
2. Клонируйте репозиторий: `git clone https://github.com/ZhikharevAl/db_web_test_automation.git`
3. Перейдите в директорию проекта: `cd db_web_test_automation`
4. Установите зависимости: `pip install -r requirements.txt`

## Запуск тестов 

1. Запустите тесты: `pytest`
2. Сгенерируйте отчет Allure: `allure serve allure-results`

## Структура проекта

- `.github/workflows/` - директория с workflow-файлами
- `databases/` - директория с базами данных
- `docs/` - директория с документацией
- `tests/` - директория с тестами
- `generator` - директория с генератором
- `pages/` - директория с описанием страниц
- `.gitignore` - файл с игнорируемыми файлами
- `conftest.py` - файл с конфигурацией
- `docker-compose.yml` - файл с конфигурацией docker-compose
- `Dockerfile` - файл с Dockerfile
- `pytest.ini` - файл с конфигурацией Pytest
- `requirements.txt` - файл с зависимостями проекта



## Лицензия

Этот проект лицензирован в соответствии с условиями лицензии MIT - см. Файл LICENSE.md для получения дополнительной информации.
