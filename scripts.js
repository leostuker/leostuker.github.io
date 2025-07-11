document.addEventListener('DOMContentLoaded', function() {

    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    // Carregar Header
    fetch('header.html')
        .then(response => {
            if (!response.ok) {
                // Se a resposta não for OK (ex: 404 Not Found), lança um erro
                throw new Error(`HTTP error! Status: ${response.status} ao carregar header.html`);
            }
            return response.text(); // Pega o conteúdo da resposta como texto
        })
        .then(html => {
            if (headerPlaceholder) {
                headerPlaceholder.innerHTML = html; // Insere o HTML no placeholder
            }
        })

    // Carregar Footer
    fetch('footer.html')
        .then(response => {
            if (!response.ok) {
                // Se a resposta não for OK (ex: 404 Not Found), lança um erro
                throw new Error(`HTTP error! Status: ${response.status} ao carregar footer.html`);
            }
            return response.text(); // Pega o conteúdo da resposta como texto
        })
        .then(html => {
            if (footerPlaceholder) {
                footerPlaceholder.innerHTML = html; // Insere o HTML no placeholder
            }
        })
});
