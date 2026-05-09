// Funktionsgerüst für add-book.js
// Implementiere die Funktionen zum Laden der Genres und zum Speichern neuer Bücher

/**
 * Lädt alle verfügbaren Genres und befüllt das Select-Element.
 */
async function loadGenres() {
	// TODO: Implementiere GET-Request zu /api/genres
	// und befülle das Select-Element (id="bookGenre") mit den Genres
}

/**
 * Speichert ein neues Buch via POST-Request.
 * @param {Object} bookData - Objekt mit: title, author, genre_id, year, available
 */
async function saveBook(bookData) {
	// TODO: Implementiere POST-Request zu /api/books
	// Sende die bookData als JSON
	// Bei Erfolg: leere das Formular und zeige Erfolgemeldung
	// Bei Fehler: zeige Fehlermeldung
}

/**
 * Zeigt eine Nachricht (Erfolg oder Fehler) an.
 * @param {string} message - Die Nachricht
 * @param {string} type - 'success' oder 'error'
 */
function showMessage(message, type) {
	// TODO: Zeige die Nachricht in id="feedback" an
	// Nutze verschiedene Klassen für success/error
}

/**
 * Leert das Formular.
 */
function clearForm() {
	// TODO: Leere alle Input-Felder
}

// Event Listener - wird beim Laden der Seite ausgelöst
document.addEventListener('DOMContentLoaded', () => {
	loadGenres();
});

// Event Listener - wird beim Absenden des Formulars ausgelöst
document.getElementById('addBookForm').addEventListener('submit', async (e) => {
	// TODO: Implementiere die Verarbeitung des Formulars
	// 1. Verhindere Standard-Formularverhalten
	// 2. Sammle die Formulardaten
	// 3. Rufe saveBook() auf
});
