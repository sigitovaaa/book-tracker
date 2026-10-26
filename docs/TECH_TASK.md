# Техническое задание — Book Tracker

## 1. Общее описание проекта

Book Tracker — веб-приложение для учёта книг в личной библиотеке.
Пользователь добавляет авторов, жанры и книги, просматривает списки,
управляет записями через HTML-интерфейс и REST API.

**Тип проекта:** веб-сайт (клиент-серверное приложение).

### Цели проекта
- Освоить полный цикл разработки: Git Flow, Issues, Pull Requests, Review.
- Реализовать CRUD-операции через REST API и HTML-форму.
- Покрыть ключевой функционал тестами.
- Освоить ORM SQLAlchemy на примере SQLite.

### Функциональные требования
- 3 модели данных: `Author`, `Genre`, `Book`.
- 2 CRUD через REST API: `Author`, `Book`.
- 1 CRUD через HTML-форму: `Genre`.
- Вывод всех сущностей в HTML: `/authors`, `/books`, `/genres`.
- Покрытие API-тестами (pytest).

## 2. Стек технологий

- **Backend:** Python 3.11 + FastAPI
- **ORM:** SQLAlchemy
- **БД:** SQLite
- **Frontend:** Jinja2 + Bootstrap 5 Bootstrap CSS/JS хранятся локально в `static/bootstrap`,подключение через `StaticFiles` FastAPI.
- **Тесты:** pytest + httpx
- **VCS:** Git + GitHub

## 3. Модели данных

### Author
- `id` — Integer, PK — идентификатор
- `name` — String — имя автора
- `country` — String — страна

### Genre
- `id` — Integer, PK — идентификатор
- `title` — String — название жанра

### Book
- `id` — Integer, PK — идентификатор
- `title` — String — название книги
- `year` — Integer — год издания
- `author_id` — Integer, FK → authors.id — автор
- `genre_id` — Integer, FK → genres.id — жанр

## 4. REST API

### Author
- `GET /api/authors/` — список авторов
- `POST /api/authors/` — создать автора
- `GET /api/authors/{id}` — получить автора
- `PUT /api/authors/{id}` — обновить
- `DELETE /api/authors/{id}` — удалить

### Book
- `GET /api/books/` — список книг
- `POST /api/books/` — создать книгу
- `GET /api/books/{id}` — получить книгу
- `PUT /api/books/{id}` — обновить
- `DELETE /api/books/{id}` — удалить

## 5. HTML-страницы сайта

- `GET /` — главная: счётчики авторов, книг, жанров
- `GET /authors` — список всех авторов
- `GET /books` — список всех книг
- `GET /genres` — список жанров и форма добавления
- `POST /genres/new` — создать жанр (обработка формы)
- `POST /genres/{id}/delete` — удалить жанр

Все страницы рендерятся через Jinja2 + Bootstrap 5.
Базовый шаблон `base.html` содержит навигацию между разделами.

## 6. Планируемые задачи по спринтам

### Спринт 1 — Постановка задачи (2 задачи)
- Оформить README.md (краткое описание проекта, стек, состав команды, ссылка на ТЗ)
- Оформить Техническое задание.md (общее описание проекта и план по спринтам)
- Создать базовый проект (hello world на FastAPI) с инструкцией по запуску

**Результат:** репозиторий с README, ТЗ, инструкция по запуску и минимальное FastAPI-приложением, которое поднимается на `localhost:8000`.

**Спринт 2 — Модели и подключение БД (3 задачи)**
- Модели Author, Genre, Book
- Схемы Pydantic для валидации API
- Подключение БД (database.py) и создание таблиц

**Спринт 3 — CRUD-операции (3 задачи)**
- CRUD через API для Author
- CRUD через API для Book
- CRUD через HTML-форму для Genre

**Спринт 4 — UI, тесты, релиз (3 задачи)**
- HTML-страницы /authors, /books, /genres
- pytest-тесты для API (Author, Book)
- Проверить, что проект запускается с нуля по инструкции, и опубликовать
  релиз v1.0.0 в разделе Releases на GitHub

**Результат:** полноценный сайт с навигацией, зелёные тесты,
готовый релиз.