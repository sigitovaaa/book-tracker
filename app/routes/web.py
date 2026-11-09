from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

router = APIRouter(tags=["Web"])

# Подключаем папку с шаблонами
templates = Jinja2Templates(directory="app/templates")

# 1. Показать страницу жанров
@router.get("/genres")
def genres_page(request: Request, db: Session = Depends(get_db)):
    genres = db.query(models.Genre).all()
    # ВАЖНО: request передается первым аргументом, а словарь — третьим!
    return templates.TemplateResponse(
        request=request, 
        name="genres.html", 
        context={"genres": genres}
    )

# 2. Обработать форму добавления жанра
@router.post("/genres/new")
def create_genre_form(title: str = Form(...), db: Session = Depends(get_db)):
    new_genre = models.Genre(title=title)
    db.add(new_genre)
    db.commit()
    # Возвращаем пользователя обратно на страницу
    return RedirectResponse(url="/genres", status_code=303)

# 3. Удалить жанр
@router.post("/genres/{genre_id}/delete")
def delete_genre_form(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if genre:
        db.delete(genre)
        db.commit()
    return RedirectResponse(url="/genres", status_code=303)