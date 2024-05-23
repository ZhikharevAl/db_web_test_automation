# Используем более легковесный базовый образ
FROM python:3.12-slim-bookworm as base

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов и установка зависимостей в одном слое
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install playwright==1.43.0 pytest-cov \
    && playwright install --with-deps \
    && apt-get remove -y --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Копирование остальных файлов
COPY . /app

# Установка переменной окружения BASE_URL
ENV BASE_URL=https://www.demoblaze.com/

# Добавление метаинформации к образу
LABEL maintainer="ZhikharevAl <waltafunk@gmail.com>"
LABEL description="This container runs automated tests using Playwright and pytest."

# Запуск команды pytest при запуске контейнера
CMD ["sh", "-c", "pytest --cov=. --base-url $BASE_URL --numprocesses auto --alluredir=allure-results"]
