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

// Adicione esta função ao seu scripts.js
function setupCarousel(carouselElement) {
    const imagesContainer = carouselElement.querySelector('.carousel-images');
    const images = carouselElement.querySelectorAll('.carousel-images img');
    const prevButton = carouselElement.querySelector('.carousel-button.prev');
    const nextButton = carouselElement.querySelector('.carousel-button.next');
    const dotsContainer = carouselElement.querySelector('.carousel-dots');

    if (!imagesContainer || images.length === 0 || !prevButton || !nextButton || !dotsContainer) {
        console.warn('Elementos do carrossel não encontrados ou insuficientes para configurar.', carouselElement);
        return;
    }

    let currentIndex = 0;
    const totalImages = images.length;

    // Criar os pontos indicadores
    for (let i = 0; i < totalImages; i++) {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        dot.addEventListener('click', () => {
            currentIndex = i;
            updateCarousel();
        });
        dotsContainer.appendChild(dot);
    }
    const dots = dotsContainer.querySelectorAll('.dot'); // Seleciona os pontos após criá-los

    function updateCarousel() {
        imagesContainer.style.transform = `translateX(${-currentIndex * 100}%)`;

        // Atualiza a classe 'active' nos pontos
        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    // Navegação pelos botões
    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalImages) % totalImages; // Loop infinito para trás
        updateCarousel();
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalImages; // Loop infinito para frente
        updateCarousel();
    });

    // Inicializa o carrossel na primeira imagem
    updateCarousel();
}

// Chame esta função para cada carrossel que você tiver na página
// Use document.querySelectorAll('.carousel-container') para selecionar todos
document.addEventListener('DOMContentLoaded', function() {
    // ... seu código existente para header/footer ...

    // Configurar carrosséis na página
    const allCarousels = document.querySelectorAll('.carousel-container');
    allCarousels.forEach(carousel => {
        setupCarousel(carousel);
    });
});