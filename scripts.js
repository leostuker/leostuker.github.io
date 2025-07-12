document.addEventListener('DOMContentLoaded', function() {

    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    // Carregar Header
    fetch('../header.html')
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
    fetch('../footer.html')
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

// A função setupCarousel deve ser definida AQUI, fora do DOMContentLoaded
function setupCarousel(carouselElement) {
    const imagesContainer = carouselElement.querySelector('.carousel-slides');
    const images = imagesContainer ? imagesContainer.querySelectorAll('img') : []; // Adicionado check para imagesContainer
    
    const prevButton = carouselElement.querySelector('.carousel-button.prev');
    const nextButton = carouselElement.querySelector('.carousel-button.next');
    const dotsContainer = carouselElement.querySelector('.carousel-dots');

    // --- Adicione estes console.log para depuração ---
    console.log('Configurando carrossel:', carouselElement);
    console.log('imagesContainer:', imagesContainer);
    console.log('images.length:', images.length);
    console.log('prevButton:', prevButton);
    console.log('nextButton:', nextButton);
    console.log('dotsContainer:', dotsContainer);
    // --- Fim dos console.log de depuração ---

    if (!imagesContainer || images.length === 0 || !prevButton || !nextButton || !dotsContainer) {
        console.error('ERRO: Elementos essenciais do carrossel não encontrados ou insuficientes para configurar.', {
            imagesContainer, imagesLength: images.length, prevButton, nextButton, dotsContainer
        });
        return; // Sai da função se algo essencial não for encontrado
    }

    let currentIndex = 0;
    const totalImages = images.length;

    // Criar os pontos indicadores
    dotsContainer.innerHTML = '';
    for (let i = 0; i < totalImages; i++) {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        dot.addEventListener('click', () => {
            currentIndex = i;
            updateCarousel();
            console.log('Ponto clicado, novo currentIndex:', currentIndex); // Depuração
        });
        dotsContainer.appendChild(dot);
    }
    const dots = dotsContainer.querySelectorAll('.dot');

    function updateCarousel() {
        imagesContainer.style.transform = `translateX(${-currentIndex * 100}%)`;

        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
        console.log('Carrossel atualizado para currentIndex:', currentIndex); // Depuração
    }

    // Navegação pelos botões
    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalImages) % totalImages;
        updateCarousel();
        console.log('Botão Anterior clicado, novo currentIndex:', currentIndex); // Depuração
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalImages;
        updateCarousel();
        console.log('Botão Próximo clicado, novo currentIndex:', currentIndex); // Depuração
    });

    // Inicializa o carrossel na primeira imagem
    updateCarousel();
}