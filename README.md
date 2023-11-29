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
     `pip install pytest-xdist[psutil]` Например: `pytest --numprocesses auto --count=100 .\tests\name_test.py`  Опция `--numprocesses auto` автоматически определяет количество процессов, равное количеству доступных процессоров, и распределяет тесты случайным образом между ними. Опция `--count=100` указывает, что каждый тест должен быть выполнен 100 раз. Путь `.\tests\name_test.py` указывает на файл с тестами, который нужно запустить.
     

https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/1226ab63-5561-4161-bf12-b334187de9c9

- `pytest --base-url https://demoblaze.com/`
> Плагин [pytest-base-url](https://github.com/pytest-dev/pytest-base-url) - это простой плагин для pytest, который предоставляет опциональный базовый URL через командную строку или файл конфигурации1.
    Вы можете установить pytest-base-url с помощью pip:
    `pip install pytest-base-url`
     После установки вы можете указать базовый URL в командной строке:
      `pytest --base-url https://demoblaze.com/`

    Или вы можете указать базовый URL в файле конфигурации:

      [pytest]
      base_url = https://demoblaze.com/
-     Если вы хотите, чтобы тест автоматически перезапускался при падении, вы можете использовать плагин pytest-rerunfailures. Этот плагин позволяет автоматически перезапускать тесты, которые не прошли.
      Для установки плагина выполните следующую команду:

     > `pip install pytest-rerunfailures`
        Затем в файле pytest.ini укажите следующее:
        
        [pytest]
        addopts = --reruns=5


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
