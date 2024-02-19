document.addEventListener('DOMContentLoaded', function () {
    // Pobierz wartość atrybutu data-is-new-user
    var isNewUser = document.getElementById('welcomeModal').getAttribute('data-is-new-user') === 'True';

    // Jeżeli użytkownik jest nowy, otwórz modal
    if (isNewUser) {
        var welcomeModal = new bootstrap.Modal(document.getElementById('welcomeModal'));
        welcomeModal.show();
    }

    // Znajdź przycisk zamknięcia modala
    var closeButton = document.getElementById('closeButton');

    // Dodaj zdarzenie kliknięcia
    closeButton.addEventListener('click', function () {
        // Tutaj możesz zdefiniować adres URL, na który ma przenieść
        window.location.href = '/strona_glowna/';
    });
});