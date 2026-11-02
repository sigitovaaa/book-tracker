from fastapi import FastAPI
from app.database import engine, Base
from app import models, schemas
from app.routes import api # <-- Импортируем наш роутер

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Tracker")

# Подключаем маршруты
app.include_router(api.router) # <-- Добавляем эту строку

@app.get("/")
def root():
    return {"message": "Hello, Book Tracker!"}