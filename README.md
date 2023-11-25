# 🎭UI Automation with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).

## Описание

Этот проект представляет собой набор автоматических тестов пользовательского интерфейса, написанных на Python с использованием Playwright, Allure и Pytest.

## Установка

1. Установите Python: `https://www.python.org/downloads/`
2. Клонируйте репозиторий: `git clone https://github.com/ZhikharevAl/db_web_test_automation.git`
3. Перейдите в директорию проекта: `cd db_web_test_automation`
4. Установите зависимости: `pip install -r requirements.txt`

## Запуск тестов 

1. Запустите тесты: 
   - `pytest`
   - `pytest --numprocesses auto`
   
     > Команда `pytest --numprocesses auto` используется для запуска тестов в параллельном режиме с помощью плагина pytest-xdist.
     Для установки плагина pytest-xdist, вы можете использовать следующую команду в командной строке
     `pip install -U pytest-xdist` или `pip install pytest-xdist`. Если вы хотите использовать psutil для определения количества доступных процессоров, установите дополнительный пакет psutil:
     `pip install pytest-xdist[psutil]` Например: `pytest --numprocesses auto --count=100 .\tests\name_test.py`  Опция `--numprocesses` auto автоматически определяет количество процессов, равное количеству доступных процессоров, и распределяет тесты случайным образом между ними. Опция `--count=100` указывает, что каждый тест должен быть выполнен 100 раз. Путь `.\tests\name_test.py` указывает на файл с тестами, который нужно запустить.
     
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
