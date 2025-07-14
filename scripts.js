document.addEventListener('DOMContentLoaded', function() {
    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    fetch('../header.html')
        .then(response => response.text())
        .then(html => { if (headerPlaceholder) headerPlaceholder.innerHTML = html; })
        .catch(error => console.error('Erro ao carregar ou injetar o header:', error));

    fetch('../footer.html')
        .then(response => response.text())
        .then(html => { if (footerPlaceholder) footerPlaceholder.innerHTML = html; })
        .catch(error => console.error('Erro ao carregar ou injetar o footer:', error));

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

    if (!imagesContainer || images.length === 0 || !prevButton || !nextButton || !dotsContainer) {
        console.error('ERRO: Elementos essenciais do carrossel não encontrados.', carouselElement);
        return;
    }

    let currentIndex = 0;
    const totalImages = images.length;
    const counter = document.createElement('div');
    counter.classList.add('carousel-counter');
    carouselElement.appendChild(counter); // Add the counter to the carousel container

    // Remove the dots container
    dotsContainer.remove();

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

    updateCarousel(); // Initial counter update
}