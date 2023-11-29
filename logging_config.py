import logging
import sys

"""
Эта функция настраивает логгер для записи сообщений в файл и вывода в консоль.
:param name: Имя логгера.
:param filepath: Путь к файлу, в который будут записываться сообщения.
:return: Настроенный логгер.
"""


def configure_logger(name, filepath):
    # Создаем логгер с указанным именем
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик файла
    file_handler = logging.FileHandler(filepath)
    file_handler.setLevel(logging.DEBUG)

    # Создаем обработчик консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Создаем форматтер и добавляем его в обработчики
    formatter = logging.Formatter('%(asctime)s - %(name)s - '
                                  '%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавляем обработчики в логгер
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
