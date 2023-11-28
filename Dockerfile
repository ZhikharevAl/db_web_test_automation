# TO DO: does not work
# Используйте официальный образ Playwright
FROM mcr.microsoft.com/playwright:v1.40.0-jammy

# Установите рабочий каталог в /app
WORKDIR /app

# Скопируйте текущий каталог в рабочий каталог внутри контейнера
COPY . /app

# Установите pip и все зависимости
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip && \
    pip3 install --no-cache-dir -r test-requirements.txt && \
    pip3 install pytest-base-url

# Установите переменную окружения BASE_URL
ENV BASE_URL=https://demoblaze.com/

# Запустите команду pytest при запуске контейнера
CMD ["pytest", "--base-url", "$BASE_URL", "--numprocesses", "auto"]
