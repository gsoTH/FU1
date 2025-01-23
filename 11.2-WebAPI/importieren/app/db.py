import sqlite3

DATABASE_URL = "sqlite:///./test.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL[10:])  # Entfernen des "sqlite:///" Präfix
    return conn
