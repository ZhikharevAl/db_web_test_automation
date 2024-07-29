# 🎭UI Automation with Python and Playwright

[![CI/CD](https://github.com/ZhikharevAl/db_web_test_automation/actions/workflows/run_tests.yml/badge.svg)](https://github.com/ZhikharevAl/db_web_test_automation/actions/workflows/run_tests.yml)

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
>
> Or:
>
> ```sh
> pip install pytest-xdist
> ```
>
> If you want to use psutil to determine the number of available processors, install the additional psutil package:
>
> ```sh
> pip install pytest-xdist[psutil]
> ```
>
> Example:
>
> ```sh
> pytest --numprocesses auto --count=100 .\tests\name_test.py
> ```
>
> The `--numprocesses auto` option automatically determines the number of processes equal to the number of available processors and randomly distributes tests among them. The `--count=100` option specifies that each test should be run 100 times. The path `.\tests\name_test.py` points to the test file to be run.

<https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/a16482bf-ff1d-49ae-9837-335163a4fb1d>

2. Run with a specified base URL:
   - `pytest --base-url https://demoblaze.com/`

> The `pytest-base-url` plugin is a simple plugin for pytest that provides an optional base URL via the command line or configuration file. You can install pytest-base-url with pip:
>
> ```sh
> pip install pytest-base-url
> ```
>
> After installation, you can specify the base URL on the command line:
>
> ```sh
> pytest --base-url https://demoblaze.com/
> ```
>
> Or you can specify the base URL in the configuration file:
>
> ```ini
> [pytest]
> base_url = https://demoblaze.com/
> ```

3. Automatic test restart on failure:

> If you want the test to automatically restart on failure, you can use the `pytest-rerunfailures` plugin. This plugin allows you to automatically rerun failed tests. To install the plugin, execute the following command:
>
> ```sh
> pip install pytest-rerunfailures
> ```
>
> Then, in the `pytest.ini` file, specify the following:
>
> ```ini
> [pytest]
> addopts = --reruns=5
> ```
>
![286441348-049dfb7e-668a-4c6b-ba03-6794fddc7c82](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/5fdb13f9-c727-400e-870b-3a62a5a15bba)

4. Generate Allure report: `allure serve allure-results`

## Project Structure

- `.github/workflows/` - directory with workflow files
- `data/` - directory with data
- `docs/` - directory with documentation
- `tests/` - directory with tests
- `pages/` - directory with page descriptions
- `.gitignore` - file with ignored files
- `.dockerignore` - file with ignored files
- `conftest.py` - configuration file
- `docker-compose.yml` - docker-compose configuration file
- `Dockerfile` - Dockerfile
- `pytest.ini` - Pytest configuration file
- `requirements.txt` - project dependencies file

## Documentation

Descriptions of tests and documentation can be found [here](https://zhikhareval.github.io/db_web_test_automation/).

### Pairwise Testing

![293063023-eef58ea5-62fb-47e5-8222-93c750683260](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/611cf28a-af6a-4b65-8f58-fde14cfededa)

### State Transition Diagram

![293064089-015b7990-d614-4986-8e5c-062fc6b6c47d](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/48a8297f-27f2-4ca5-a2c1-62115a4b99ec)

## Coverage

![Screenshot 2024-05-09 193751](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/a527289e-4150-4be6-bf66-8b2d43f810f5)

## Allure Report

![Screenshot 2024-06-17 195516](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/9784c787-aadf-45e6-b525-7fd10dcaf861)
![Screenshot 2024-05-15 203604](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/56e7e260-06d2-492d-9469-5eb16a0076f9)
![Screenshot 2024-05-15 203957](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/e98d5d07-091c-43c8-b7df-21354be67b55)

## Telegram Notification

For Telegram notifications, you can use a [Telegram bot](https://t.me/information_message_bot).
![302050143-f9c81f88-df69-4824-b9f6-9ff7e5c63b66](https://github.com/ZhikharevAl/db_web_test_automation/assets/81284552/53f22342-e7e4-4ec8-9cac-b901c09c383a)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
