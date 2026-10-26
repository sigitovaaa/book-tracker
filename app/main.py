from fastapi import FastAPI
from sqlalchemy import Column, Integer, String
from app.database import engine, Base

# 1. Создаем временную тестовую модель прямо здесь
class TestTable(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# 2. Даем команду создать все таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, database!"}