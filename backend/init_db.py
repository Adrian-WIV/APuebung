"""
Initialisierungsskript für die Buch-Datenbank.
Führe dieses Skript aus: python init_db.py
"""
import sqlite3
from sql_statements import (
    CREATE_GENRES_TABLE, CREATE_BOOKS_TABLE,
    INSERT_GENRE, INSERT_BOOK,
    SAMPLE_GENRES, SAMPLE_BOOKS
)

def init_database():
    """Initialisiert die SQLite-Datenbank mit Tabellen und Beispieldaten."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    # Tabellen erstellen
    print("Erstelle Tabellen...")
    cursor.execute(CREATE_GENRES_TABLE)
    cursor.execute(CREATE_BOOKS_TABLE)
    
    # Genres hinzufügen
    print("Füge Genres hinzu...")
    cursor.executemany(INSERT_GENRE, SAMPLE_GENRES)
    
    # Beispielbücher hinzufügen
    print("Füge Beispielbücher hinzu...")
    cursor.executemany(INSERT_BOOK, SAMPLE_BOOKS)
    
    conn.commit()
    conn.close()
    print("✓ Datenbank erfolgreich initialisiert!")

if __name__ == '__main__':
    init_database()
