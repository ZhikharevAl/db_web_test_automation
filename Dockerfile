
# Используйте официальный образ Playwright
FROM mcr.microsoft.com/playwright:v1.40.0-jammy

# Установите рабочий каталог в /app
WORKDIR /app

# Скопируйте текущий каталог в рабочий каталог внутри контейнера
COPY . /app

# Установите pip и все зависимости
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip && \
    pip3 install --no-cache-dir -r test-requirements.txt


# Запустите команду pytest при запуске контейнера
CMD ["pytest", "--numprocesses", "auto"]


