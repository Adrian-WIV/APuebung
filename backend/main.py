from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_connection():
    """Stellt eine Verbindung zur SQLite-Datenbank her."""
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn


# ========== DEINE ENDPUNKTE ==========
# Implementiere hier die fehlenden Endpunkte:
# 1. GET /api/books - alle Bücher abrufen
# 2. GET /api/books/genre/<genre_id> - Bücher eines Genres (mit Variable!)
# 3. POST /api/books - ein neues Buch hinzufügen
# 4. GET /api/genres - alle Genres laden


if __name__ == '__main__':
    app.run(debug=True, port=5000)
