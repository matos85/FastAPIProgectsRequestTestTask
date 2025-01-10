# FastAPIProgectsRequestTestTask


▎Структура проекта

my_fastapi_app/

app.py               # Файл приложения

config.py            # Конфигурационный файл

routes.py            # Файл с роутами

services.py          # Файл для взаимодействия с внешними API

requirements.txt     # Зависимости



Запуск приложения

1. Установите зависимости:

pip install -r requirements.txt

2. Запустите приложение:

uvicorn app:app --host 0.0.0.0 --port 8000 --reload


Проверка работы

Теперь вы можете проверить, работает ли ваш роут. Откройте браузер или используйте инструмент вроде Postman и перейдите по адресу:

http://localhost:8000/tariffs?currency=RUB
