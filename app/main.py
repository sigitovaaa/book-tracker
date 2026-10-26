from fastapi import FastAPI
from app.database import engine, Base

# Обязательно импортируем модели, чтобы база данных узнала о них!
from app import models 

# Создаем таблицы authors, genres, books
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Tracker")

@app.get("/")
def root():
    return {"message": "Hello, Book Tracker with Database!"}