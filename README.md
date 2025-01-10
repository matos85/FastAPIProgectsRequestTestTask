# FastAPIProgectsRequestTestTask

## Запуск приложения
### 1. Установите зависимости:
pip install -r requirements.txt
### 2. Запустите приложение в папке где находясь в папке с файлом app.py:
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
## Проверка работы
Откройте браузер и перейдите по адресу:
http://localhost:8000/tariffs?currency=RUB
