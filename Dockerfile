# Используйте официальный образ Playwright
FROM mcr.microsoft.com/playwright:v1.40.0-jammy as base

# Установите рабочий каталог в /app
WORKDIR /app

# Скопируйте текущий каталог в рабочий каталог внутри контейнера
COPY . /app

# Установите pip и все зависимости
RUN apt-get update && \
   apt-get install -y python3.11 python3-pip && \
   pip3 install --no-cache-dir -r test-requirements.txt && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

# Добавьте метаинформацию к образу
LABEL maintainer="ZhikharevAl <waltafunk@gmail.com>"
LABEL description="This container runs automated tests using Playwright and pytest."
# Установите переменную окружения BASE_URL
ENV BASE_URL=https://www.demoblaze.com/

# Запустите команду pytest при запуске контейнера
CMD ["sh", "-c", "pytest --base-url $BASE_URL --numprocesses auto"]