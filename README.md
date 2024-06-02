# UI Automation with Python and Playwright

[View Russian version of this file here](README.ru.md)

## Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Running Tests](#running-tests)
4. [Project Structure](#project-structure)
5. [Documentation](#documentation)
   - [Pairwise Testing](#pairwise-testing)
   - [State Transition Diagram](#state-transition-diagram)
6. [Coverage](#coverage)
7. [Allure Report](#allure-report)
8. [Telegram Notification](#telegram-notification)
9. [License](#license)

## Description

This project is a set of automated UI tests written in Python using Playwright, Allure, and PyTest.

## Installation

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clone the repository: `git clone https://github.com/ZhikharevAl/db_web_test_automation.git`
3. Activate the virtual environment: `/.venv/Scripts/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests

1. Run tests:
   - `pytest`
   - `pytest --numprocesses auto`

> The `pytest --numprocesses auto` command is used to run tests in parallel using the pytest-xdist plugin. To install the pytest-xdist plugin, execute the following command:
> 
> ```sh
> pip install -U pytest-xdist
> ```
> Or:
> ```sh
> pip install pytest-xdist
> ```
> If you want to use psutil to determine the number of available processors, install the additional psutil package:
> ```sh
> pip install pytest-xdist[psutil]
> ```
> Example:
> ```sh
> pytest --numprocesses auto --count=100 .\tests\name_test.py
> ```
> The `--numprocesses auto` option automatically determines the number of processes equal to the number of available processors and randomly distributes tests among them. The `--count=100` option specifies that each test should be run 100 times. The path `.\tests\name_test.py` points to the test file to be run.

2. Run with a specified base URL:
   - `pytest --base-url https://demoblaze.com/`

> The `pytest-base-url` plugin is a simple plugin for pytest that provides an optional base URL via the command line or configuration file. You can install pytest-base-url with pip:
> ```sh
> pip install pytest-base-url
> ```
> After installation, you can specify the base URL on the command line:
> ```sh
> pytest --base-url https://demoblaze.com/
> ```
> Or you can specify the base URL in the configuration file:
> ```ini
> [pytest]
> base_url = https://demoblaze.com/
> ```

3. Automatic test restart on failure:

> If you want the test to automatically restart on failure, you can use the `pytest-rerunfailures` plugin. This plugin allows you to automatically rerun failed tests. To install the plugin, execute the following command:
> ```sh
> pip install pytest-rerunfailures
> ```
> Then, in the `pytest.ini` file, specify the following:
> ```ini
> [pytest]
> addopts = --reruns=5
> ```

4. Generate Allure report: `allure serve allure-results`

## Project Structure

- `.github/workflows/` - directory with workflow files
- `databases/` - directory with databases
- `docs/` - directory with documentation
- `tests/` - directory with tests
- `generator` - directory with the generator
- `pages/` - directory with page descriptions
- `.gitignore` - file with ignored files
- `conftest.py` - configuration file
- `docker-compose.yml` - docker-compose configuration file
- `Dockerfile` - Dockerfile
- `pytest.ini` - Pytest configuration file
- `requirements.txt` - project dependencies file

## Documentation

Descriptions of tests and documentation can be found [here](https://zhikhareval.github.io/db_web_test_automation/).

### Pairwise Testing:
![Pairwise Testing Screenshot](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/pairwise_testing.png)

### State Transition Diagram:
![State Transition Diagram Screenshot](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/state_transition_diagram.png)

## Coverage
![Coverage Screenshot](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/coverage.png)

## Allure Report
![Allure Report Screenshot 1](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/allure_report1.png)
![Allure Report Screenshot 2](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/allure_report2.png)

## Telegram Notification

For Telegram notifications, you can use a [Telegram bot](https://t.me).
![Telegram Notification Screenshot](https://raw.githubusercontent.com/ZhikharevAl/db_web_test_automation/main/images/telegram_notification.png)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
