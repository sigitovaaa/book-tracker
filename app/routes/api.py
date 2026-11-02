from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

# Создаем роутер с префиксом /api
router = APIRouter(prefix="/api", tags=["Authors"])

# 1. CREATE (Создать автора)
@router.post("/authors/", response_model=schemas.AuthorOut)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    new_author = models.Author(name=author.name, country=author.country)
    db.add(new_author)
    db.commit()
    db.refresh(new_author) # Обновляем, чтобы получить ID из базы
    return new_author

# 2. READ (Получить всех авторов)
@router.get("/authors/", response_model=list[schemas.AuthorOut])
def get_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()

# 3. READ (Получить одного автора по ID)
@router.get("/authors/{author_id}", response_model=schemas.AuthorOut)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return author

# 4. UPDATE (Обновить данные автора)
@router.put("/authors/{author_id}", response_model=schemas.AuthorOut)
def update_author(author_id: int, updated_author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    
    # Обновляем поля
    author.name = updated_author.name
    author.country = updated_author.country
    db.commit()
    db.refresh(author)
    return author

# 5. DELETE (Удалить автора)
@router.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    
    db.delete(author)
    db.commit()
    return {"message": f"Автор с ID {author_id} успешно удален"}
