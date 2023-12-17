FROM python:3.9

# Активация виртуального окружения
ENV PATH="/venv/bin:$PATH"

# Рабочая директория
WORKDIR /app

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в /app в контейнере
COPY . .

CMD ["python", "TeleBot.py"]
