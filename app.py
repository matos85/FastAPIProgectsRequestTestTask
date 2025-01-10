from fastapi import FastAPI
from config import Config
from routes import router

app = FastAPI()

# Регистрация маршрутов
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
