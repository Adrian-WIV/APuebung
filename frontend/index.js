// Funktionsgerüst für index.js
// Implementiere die Funktionen zum Laden und Anzeigen der Bücher

/**
 * Lädt alle verfügbaren Genres und befüllt das Filter-Select-Element.
 */
async function loadGenres() {
	// TODO: Implementiere GET-Request zu /api/genres
	// und befülle das Select-Element (id="genreFilter") mit den Genres
}

/**
 * Lädt alle Bücher vom Backend und zeigt sie in der Tabelle an.
 */
async function loadBooks() {
	// TODO: Implementiere GET-Request zu /api/books
	// und setze die Ergebnisse in die Tabelle (id="booksList")
}

/**
 * Lädt Bücher eines bestimmten Genres und zeigt sie an.
 * @param {string} genreId - Die Genre-ID zum Filtern
 */
async function loadBooksByGenre(genreId) {
	// TODO: Implementiere GET-Request zu /api/books/genre/<genreId> (mit Variable!)
	// und zeige die gefilterten Bücher in der Tabelle an
}

/**
 * Zeigt die Bücher in der Tabelle an.
 * @param {Array} books - Array von Buch-Objekten
 */
function displayBooks(books) {
	// TODO: Implementiere die Darstellung der Bücher in der Tabelle
	// Jede Reihe sollte: Titel, Autor, Genre, Jahr, Verfügbarkeit zeigen
}

/**
 * Zeigt eine Fehlermeldung an.
 * @param {string} message - Die Fehlermeldung
 */
function showError(message) {
	// TODO: Zeige die Fehlermeldung in id="feedback"
}

// Event Listener - wird beim Laden der Seite ausgelöst
document.addEventListener('DOMContentLoaded', () => {
	loadGenres();
	loadBooks();
});

// Event Listener - wird beim Ändern des Genre-Filters ausgelöst
document.getElementById('genreFilter').addEventListener('change', (e) => {
	// TODO: Implementiere die Filterlogik
	// Wenn genreFilter leer ist, lade alle Bücher
	// Sonst lade Bücher des ausgewählten Genres
});

