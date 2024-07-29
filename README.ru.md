# 🎭UI Automation with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/)

[![CI/CD](https://github.com/ZhikharevAl/db_web_test_automation/actions/workflows/run_tests.yml/badge.svg)](https://github.com/ZhikharevAl/db_web_test_automation/actions/workflows/run_tests.yml)

## Содержание

1. [Описание](#описание)

2. [Установка](#установка)

3. [Запуск тестов](#запуск-тестов)

4. [Структура проекта](#структура-проекта)

5. [Документация](#документация)

    - [Pairwise Тест](#pairwise-тест)

    - [Диаграмма переходов состояний](#диаграмма-переходов-состояний)

6. [Coverage](#coverage)

7. [Allure report](#allure-report)

8. [Оповещение в Telegram](#оповещение-в-telegram)

9. [Лицензия](#лицензия)

## Описание

Этот проект представляет собой набор автоматических тестов пользовательского интерфейса, написанных на Python с использованием Playwright, Allure и Pytest.

## Установка

1. Установите Python: `https://www.python.org/downloads/`
2. Клонируйте репозиторий: `git clone https://github.com/ZhikharevAl/db_web_test_automation.git`
3. Активируйте виртуальную среду: `/.venv/Scripts/activate`
4. Установите зависимости: `pip install -r requirements.txt`

## Запуск тестов

1. **Запустите тесты:**
   - `pytest`
   - `pytest --numprocesses auto`

   > Команда `pytest --numprocesses auto` используется для запуска тестов в параллельном режиме с помощью плагина pytest-xdist. Для установки плагина pytest-xdist, выполните следующую команду в командной строке:
>
   > ```sh
   > pip install -U pytest-xdist
   > ```
>
   > Или
>
   > ```sh
   > pip install pytest-xdist
   > ```
>
   > Если вы хотите использовать psutil для определения количества доступных процессоров, установите дополнительный пакет psutil:
>
   > ```sh
   > pip install pytest-xdist[psutil]
   > ```
>
   > Например:
>
   > ```sh
   > pytest --numprocesses auto --count=100 .\tests\name_test.py
   > ```
>
   > Опция `--numprocesses auto` автоматически определяет количество процессов, равное количеству доступных процессоров, и распределяет тесты случайным образом между ними. Опция `--count=100` указывает, что каждый тест должен быть выполнен 100 раз. Путь `.\tests\name_test.py` указывает на файл с тестами, который нужно запустить.

<https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/fd486f61-f36f-42f8-84e1-cd91a8e0cba5>

2. **Запуск с указанием базового URL:**
   - `pytest --base-url https://demoblaze.com/`

   > Плагин [pytest-base-url](https://github.com/pytest-dev/pytest-base-url) - это простой плагин для pytest, который предоставляет опциональный базовый URL через командную строку или файл конфигурации. Вы можете установить pytest-base-url с помощью pip:
>
   > ```bash
   > pip install pytest-base-url
   > ```
>
   > После установки вы можете указать базовый URL в командной строке:
>
   > ```bash
   > pytest --base-url https://demoblaze.com/
   > ```
>
   > Или вы можете указать базовый URL в файле конфигурации:
>
   > ```ini
   > [pytest]
   > base_url = https://demoblaze.com/
   > ```

3. **Автоматический перезапуск тестов при падении:**
   > Если вы хотите, чтобы тест автоматически перезапускался при падении, вы можете использовать плагин [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures). Этот плагин позволяет автоматически перезапускать тесты, которые не прошли. Для установки плагина выполните следующую команду:
>
   > ```bash
   > pip install pytest-rerunfailures
   > ```
>
   > Затем в файле `pytest.ini` укажите следующее:
>
   > ```ini
   > [pytest]
   > addopts = --reruns=5
   > ```
   >
![Screenshot 2023-11-29 031825](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/049dfb7e-668a-4c6b-ba03-6794fddc7c82)

2. Сгенерируйте отчет Allure: `allure serve allure-results`

## Структура проекта

- `.github/workflows/` - директория с workflow-файлами
- `data/` - директория с данными
- `docs/` - директория с документацией
- `tests/` - директория с тестами
- `pages/` - директория с описанием страниц
- `.gitignore` - файл с игнорируемыми файлами
- `.dockerignore` - файл с игнорируемыми файлами
- `conftest.py` - файл с конфигурацией
- `docker-compose.yml` - файл с конфигурацией docker-compose
- `Dockerfile` - файл с Dockerfile
- `pytest.ini` - файл с конфигурацией Pytest
- `requirements.txt` - файл с зависимостями проекта

## Документация

Описание тестов и документация можно найти [здесь](https://github.com/ZhikharevAl/db_web_test_automation/blob/master/docs/TESTS.md).

### Pairwise Тест

![Screenshot 2023-12-27 185417](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/eef58ea5-62fb-47e5-8222-93c750683260)

### Диаграмма переходов состояний

![Screenshot 2023-12-27 185502](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/015b7990-d614-4986-8e5c-062fc6b6c47d)

## Coverage

![Screenshot 2024-05-09 193751](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/3998581c-d94a-4248-a1ef-ef2c7cbc739d)

## Allure report

![Screenshot 2024-05-15 204058](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/5802b2b9-0ca2-42fe-9585-18195eb9228b)
![Screenshot 2024-05-15 203604](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/98c2252b-040a-497a-8717-70a040f1c5ee)
![Screenshot 2024-05-15 203957](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/b49b3d20-67f2-4577-9d0c-72987920fe89)

## Оповещение в Telegram

Для оповещения в Telegram вы можете использовать [телеграм бота](https://t.me/information_message_bot).
![photo_2024-02-03_20-03-04](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/f9c81f88-df69-4824-b9f6-9ff7e5c63b66)

## Лицензия

Этот проект лицензирован в соответствии с условиями лицензии MIT - см. Файл LICENSE.md для получения дополнительной информации.
