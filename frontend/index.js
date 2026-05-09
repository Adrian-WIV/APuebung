// Funktionsgerüst für index.js
// Implementiere die Funktionen zum Laden und Anzeigen der Bücher

/**
 * Lädt alle Bücher vom Backend und zeigt sie in der Tabelle an.
 */
async function loadBooks() {
	// TODO: Implementiere GET-Request zu /api/books
	// und setze die Ergebnisse in die Tabelle (id="booksList")
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
	loadBooks();
});
