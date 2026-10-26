from fastapi import FastAPI
from app.database import engine, Base

from app import models 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Tracker")

@app.get("/")
def root():
    return {"message": "Hello, Book Tracker with Database!"}