import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_db_connection
import sqlite3

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Erstelle die Tabelle und lösche bestehende Daten
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS items")
    cursor.execute('''
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    connection.commit()
    connection.close()

def test_create_item(client):
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test"

def test_read_item(client):
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test"})
    item_id = response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test"

def test_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
