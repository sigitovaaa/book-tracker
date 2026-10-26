# Инструкция по запуску Book Tracker

## Требования

- **Python 3.11+** — [скачать с python.org](https://www.python.org/downloads/)
- **Git** — [скачать с git-scm.com](https://git-scm.com/downloads)
- Больше **ничего устанавливать не нужно** — используется встроенная SQLite.

Проверить версии:
```bash
python --version
git --version
```

---

## Шаг 1. Клонировать репозиторий

```bash
git clone https://github.com/<owner>/book-tracker.git
cd book-tracker
```

> `<owner>` — логин владельца репозитория.

---

## Шаг 2. Создать виртуальное окружение

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

После активации в начале строки терминала появится `(.venv)`.

---

## Шаг 3. Установить зависимости

```bash
pip install -r requirements.txt
```

Если файла `requirements.txt` ещё нет (Спринт 1, задача #2 не выполнена),
установить вручную:
```bash
pip install fastapi uvicorn[standard] sqlalchemy jinja2 python-multipart pytest httpx
```

---

## Шаг 4. Запустить сервер

```bash
uvicorn app.main:app --reload
```

Ожидаемый вывод:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

Если видишь эти строки — **проект запущен**.

---

## Шаг 5. Открыть в браузере

| Что | Адрес |
|-----|-------|
| Главная страница | http://localhost:8000 |
| Swagger (документация API) | http://localhost:8000/docs |
| Список авторов | http://localhost:8000/authors |
| Список книг | http://localhost:8000/books |
| Список жанров | http://localhost:8000/genres |

> На Спринте 1 доступна только главная `/` — она должна вернуть
> `{"message": "Hello, Book Tracker!"}`. Остальные страницы появятся
> в Спринтах 2–3.

---

## Шаг 6. Остановить сервер

В терминале нажать **Ctrl + C**.

---

## Файл базы данных

Файл `booktracker.db` создаётся автоматически в корне проекта при первом
запуске (в Спринте 2, когда появится подключение к БД).

Чтобы **сбросить все данные** — удалить файл и перезапустить сервер:

**Windows:**
```cmd
del booktracker.db
```

**Linux / macOS:**
```bash
rm booktracker.db
```

---

## Запуск тестов

```bash
pytest -v
```

Ожидаемый вывод — все тесты `PASSED`.


## Проверка, что всё работает

1. Сервер запущен без ошибок
2. `http://localhost:8000` открывается в браузере
3. `http://localhost:8000/docs` показывает Swagger UI
4. `pytest -v` — все тесты зелёные (после Спринта 3)