document.addEventListener('DOMContentLoaded', function() {
    // Configurar carrosséis na página
    const allCarousels = document.querySelectorAll('.carousel-container');
    allCarousels.forEach(carousel => {
        setupCarousel(carousel);
    });
});

function setupCarousel(carouselElement) {
    const imagesContainer = carouselElement.querySelector('.carousel-slides');
    const images = imagesContainer ? imagesContainer.querySelectorAll('img') : [];
    
    const prevButton = carouselElement.querySelector('.carousel-button.prev');
    const nextButton = carouselElement.querySelector('.carousel-button.next');
    const dotsContainer = carouselElement.querySelector('.carousel-dots');

    if (!imagesContainer || images.length === 0 || !prevButton || !nextButton) {
        return; // Retorna silenciosamente se não for uma página com carrossel
    }

    let currentIndex = 0;
    const totalImages = images.length;
    
    // Cria e adiciona o contador
    const counter = document.createElement('div');
    counter.classList.add('carousel-counter');
    carouselElement.appendChild(counter);

    // Remove o contêiner de pontos se ele existir no HTML
    if (dotsContainer) {
        dotsContainer.remove();
    }

    function updateCounter() {
        counter.textContent = `${currentIndex + 1}/${totalImages}`;
    }

    function updateCarousel() {
        imagesContainer.style.transform = `translateX(${-currentIndex * 100}%)`;
        updateCounter();
    }

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalImages) % totalImages;
        updateCarousel();
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalImages;
        updateCarousel();
    });

    updateCarousel();
}
