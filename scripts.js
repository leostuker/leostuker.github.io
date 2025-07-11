document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM completamente carregado. Tentando carregar fragmentos...');

    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    if (!headerPlaceholder) {
        console.error('ERRO: Elemento com ID "header-placeholder" não encontrado no HTML.');
    }
    if (!footerPlaceholder) {
        console.error('ERRO: Elemento com ID "footer-placeholder" não encontrado no HTML.');
    }

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
                console.log('Header carregado e injetado com sucesso.');
            }
        })
        .catch(error => console.error('Erro ao carregar ou injetar o header:', error));

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
                console.log('Footer carregado e injetado com sucesso.');
            }
        })
        .catch(error => console.error('Erro ao carregar ou injetar o footer:', error));
});
