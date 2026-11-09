def test_create_author(client):
    response = client.post("/api/authors/", json={"name": "Джоан Роулинг", "country": "Великобритания"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Джоан Роулинг"
    assert "id" in data

def test_read_authors(client):
    client.post("/api/authors/", json={"name": "Стивен Кинг", "country": "США"})
    response = client.get("/api/authors/")
    assert response.status_code == 200
    authors = response.json()
    assert len(authors) == 1
    assert authors[0]["name"] == "Стивен Кинг"

def test_create_book(client):
    author_res = client.post("/api/authors/", json={"name": "Джордж Оруэлл", "country": "Великобритания"})
    author_id = author_res.json()["id"]
    
    from app import models
    db = client.app.dependency_overrides[__import__('app.database', fromlist=['get_db']).get_db]().__next__()
    genre = models.Genre(title="Антиутопия")
    db.add(genre)
    db.commit()
    db.refresh(genre)
    genre_id = genre.id
    
    book_data = {
        "title": "1984",
        "year": 1949,
        "author_id": author_id,
        "genre_id": genre_id
    }
    response = client.post("/api/books/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "1984"

def test_delete_author(client):
    res = client.post("/api/authors/", json={"name": "Временный Автор", "country": "Тест"})
    author_id = res.json()["id"]
    
    del_res = client.delete(f"/api/authors/{author_id}")
    assert del_res.status_code == 200
    
    get_res = client.get(f"/api/authors/{author_id}")
    assert get_res.status_code == 404