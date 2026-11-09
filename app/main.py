from fastapi import FastAPI
from app.database import engine, Base
from app import models, schemas
from app.routes import api
from app.routes import web

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Tracker")

# Подключаем маршруты
app.include_router(api.router) 
app.include_router(web.router)

@app.get("/")
def root():
    return {"message": "Hello, Book Tracker!"}