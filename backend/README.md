# Übung: Buch-Verwaltung

## Aufgabenstellung

Diese Übung behandelt die Erstellung einer einfachen Buch-Verwaltungsanwendung mit Flask und SQLite.

### Deine Aufgaben:

1. **Endpunkte in `main.py` implementieren:**
   - GET `/api/books` - alle Bücher abrufen
   - GET `/api/books/genre/<genre_id>` - Bücher eines Genres abrufen (mit Variable!)
   - POST `/api/books` - ein neues Buch hinzufügen
   - GET `/api/genres` - alle verfügbaren Genres laden (für Dropdown)

2. **JavaScript-Dateien implementieren:**
   - `index.js` - Logik zum Laden und Anzeigen der Büchertabelle
   - `add-book.js` - Logik für das Formular zum Hinzufügen von Büchern

3. **SQL-Statements in `sql_statements.py` verwenden**, um Datenbankoperationen durchzuführen

4. **Testen:**
   - Stelle sicher, dass die Buch-Tabelle korrekt befüllt wird
   - Überprüfe, dass das Formular neue Bücher hinzufügen kann
   - Teste alle Endpunkte

## Datenbankstruktur

Die SQLite-Datenbank enthält folgende Tabellen:
- **books**: Titel, Autor, Genre, Erscheinungsjahr, Verfügbarkeit
- **genres**: Liste aller Genres

## Dependencies

```sh
uv sync
```

## Running the server

```sh
uv run main.py
```
