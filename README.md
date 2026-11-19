# Book Tracker

## Описание проекта
Book Tracker — веб-приложение для учёта книг в личной библиотеке.
Пользователь добавляет авторов, жанры и книги, просматривает списки
и управляет записями через веб-интерфейс и REST API.

**Тип проекта:** веб-сайт (клиент-серверное приложение).

## Стек технологий
- **Backend:** Python 3.11 + FastAPI
- **ORM:** SQLAlchemy
- **БД:** SQLite
- **Frontend:** Jinja2 + Bootstrap 5 Bootstrap CSS/JS хранятся локально в `static/bootstrap`,подключение через `StaticFiles` FastAPI.
- **Тесты:** pytest + httpx
- **VCS:** Git + GitHub

## Состав команды

1. Бадамшина Ангелина, ЭУ-212, https://github.com/AnjelinaBadamshina/
2. Геворгян Сейран, ЭУ-212, https://github.com/seyrangevorgyan/ 
3. Сигитова Анастасия, ЭУ-212, https://github.com/sigitovaaa/

## Документация

- [Техническое задание](docs/TECH_TASK.md)
- [Инструкция по запуску](docs/RUN.md)

# Book Tracker

## Краткое описание проекта
Book Tracker — веб-приложение для учёта книг в личной библиотеке.
Пользователь добавляет авторов, жанры и книги, просматривает списки
и управляет записями через веб-интерфейс и REST API.

**Тип проекта:** веб-сайт (клиент-серверное приложение).

## 🚀 Что реализовано (Спринт 4)
- 3 модели данных: Author, Genre, Book.
- 2 CRUD через REST API (Авторы и Книги).
- 1 CRUD через HTML-форму (Жанры).
- Вывод всех сущностей в HTML (/authors, /books, /genres).
- Покрытие API-тестами (pytest).

## Стек технологий
- **Backend:** Python 3.11 + FastAPI
- **ORM:** SQLAlchemy
- **БД:** SQLite (встроена в Python)
- **Frontend:** Jinja2 + Bootstrap 5 (локальные файлы, без CDN)
- **Тесты:** pytest + httpx
- **VCS:** Git + GitHub

## Состав команды
(Ваша таблица с ФИО и логинами)

## Инструкция по запуску
Подробная инструкция находится в файле [docs/RUN.md](docs/RUN.md).
