# SQL-Statements für die Buch-Verwaltung
# Kopiere diese Statements in deine Endpunkte-Implementierung

CREATE_GENRES_TABLE = """
CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
"""

CREATE_BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre_id INTEGER NOT NULL,
    year INTEGER,
    available BOOLEAN DEFAULT 1,
    FOREIGN KEY (genre_id) REFERENCES genres(id)
)
"""

# ========== SELECT STATEMENTS ==========
GET_ALL_BOOKS = """
SELECT b.id, b.title, b.author, g.name as genre, b.year, b.available
FROM books b
JOIN genres g ON b.genre_id = g.id
ORDER BY b.title
"""

GET_BOOK_BY_ID = """
SELECT b.id, b.title, b.author, g.name as genre, b.year, b.available
FROM books b
JOIN genres g ON b.genre_id = g.id
WHERE b.id = ?
"""

GET_BOOKS_BY_GENRE = """
SELECT b.id, b.title, b.author, g.name as genre, b.year, b.available
FROM books b
JOIN genres g ON b.genre_id = g.id
WHERE b.genre_id = ?
ORDER BY b.title
"""

GET_ALL_GENRES = """
SELECT id, name FROM genres ORDER BY name
"""

# ========== INSERT STATEMENTS ==========
INSERT_BOOK = """
INSERT INTO books (title, author, genre_id, year, available)
VALUES (?, ?, ?, ?, ?)
"""

INSERT_GENRE = """
INSERT INTO genres (name) VALUES (?)
"""

# ========== UPDATE STATEMENTS ==========
UPDATE_BOOK = """
UPDATE books
SET title = ?, author = ?, genre_id = ?, year = ?, available = ?
WHERE id = ?
"""

# ========== DELETE STATEMENTS ==========
DELETE_BOOK = """
DELETE FROM books WHERE id = ?
"""

# ========== SAMPLE DATA ==========
SAMPLE_GENRES = [
    ('Science Fiction',),
    ('Fantasy',),
    ('Krimi',),
    ('Romantik',),
    ('Sachbuch',),
]

SAMPLE_BOOKS = [
    ('Der Hobbit', 'J.R.R. Tolkien', 2, 1937, 1),
    ('1984', 'George Orwell', 1, 1949, 1),
    ('Die Blechtrommel', 'Günter Grass', 3, 1959, 0),
    ('Das Herz der Finsternis', 'Joseph Conrad', 1, 1899, 1),
    ('Harry Potter und der Stein der Weisen', 'J.K. Rowling', 2, 1997, 1),
]
