from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

router = APIRouter(tags=["Web"])
templates = Jinja2Templates(directory="app/templates")

# ==========================================
# АВТОРЫ (Author)
# ==========================================
@router.get("/authors")
def authors_page(request: Request, db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return templates.TemplateResponse(request=request, name="authors.html", context={"authors": authors})

@router.post("/authors/new")
def create_author_form(name: str = Form(...), country: str = Form(None), db: Session = Depends(get_db)):
    new_author = models.Author(name=name, country=country)
    db.add(new_author)
    db.commit()
    return RedirectResponse(url="/authors", status_code=303)

# --- РЕДАКТИРОВАНИЕ АВТОРА ---
@router.get("/authors/{author_id}/edit")
def edit_author_page(request: Request, author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        return RedirectResponse(url="/authors", status_code=303)
    return templates.TemplateResponse(request=request, name="edit_author.html", context={"author": author})

@router.post("/authors/{author_id}/edit")
def update_author_form(author_id: int, name: str = Form(...), country: str = Form(None), db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author:
        author.name = name
        author.country = country
        db.commit()
    return RedirectResponse(url="/authors", status_code=303)

@router.post("/authors/{author_id}/delete")
def delete_author_form(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
    return RedirectResponse(url="/authors", status_code=303)


# ==========================================
# КНИГИ (Book)
# ==========================================
@router.get("/books")
def books_page(request: Request, db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    authors = db.query(models.Author).all() 
    genres = db.query(models.Genre).all()   
    authors_dict = {a.id: a.name for a in authors}
    genres_dict = {g.id: g.title for g in genres}

    return templates.TemplateResponse(
        request=request, name="books.html", 
        context={"books": books, "authors": authors, "genres": genres, "authors_dict": authors_dict, "genres_dict": genres_dict}
    )

@router.post("/books/new")
def create_book_form(title: str = Form(...), year: int = Form(None), author_id: int = Form(...), genre_id: int = Form(...), db: Session = Depends(get_db)):
    new_book = models.Book(title=title, year=year, author_id=author_id, genre_id=genre_id)
    db.add(new_book)
    db.commit()
    return RedirectResponse(url="/books", status_code=303)

# --- РЕДАКТИРОВАНИЕ КНИГИ ---
@router.get("/books/{book_id}/edit")
def edit_book_page(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    authors = db.query(models.Author).all()
    genres = db.query(models.Genre).all()
    if not book:
        return RedirectResponse(url="/books", status_code=303)
    return templates.TemplateResponse(request=request, name="edit_book.html", context={"book": book, "authors": authors, "genres": genres})

@router.post("/books/{book_id}/edit")
def update_book_form(book_id: int, title: str = Form(...), year: int = Form(None), author_id: int = Form(...), genre_id: int = Form(...), db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.title = title
        book.year = year
        book.author_id = author_id
        book.genre_id = genre_id
        db.commit()
    return RedirectResponse(url="/books", status_code=303)

@router.post("/books/{book_id}/delete")
def delete_book_form(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return RedirectResponse(url="/books", status_code=303)


# ==========================================
# ЖАНРЫ (Genre)
# ==========================================
@router.get("/genres")
def genres_page(request: Request, db: Session = Depends(get_db)):
    genres = db.query(models.Genre).all()
    return templates.TemplateResponse(request=request, name="genres.html", context={"genres": genres})

@router.post("/genres/new")
def create_genre_form(title: str = Form(...), db: Session = Depends(get_db)):
    new_genre = models.Genre(title=title)
    db.add(new_genre)
    db.commit()
    return RedirectResponse(url="/genres", status_code=303)

# --- РЕДАКТИРОВАНИЕ ЖАНРА ---
@router.get("/genres/{genre_id}/edit")
def edit_genre_page(request: Request, genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if not genre:
        return RedirectResponse(url="/genres", status_code=303)
    return templates.TemplateResponse(request=request, name="edit_genre.html", context={"genre": genre})

@router.post("/genres/{genre_id}/edit")
def update_genre_form(genre_id: int, title: str = Form(...), db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if genre:
        genre.title = title
        db.commit()
    return RedirectResponse(url="/genres", status_code=303)

@router.post("/genres/{genre_id}/delete")
def delete_genre_form(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if genre:
        db.delete(genre)
        db.commit()
    return RedirectResponse(url="/genres", status_code=303)