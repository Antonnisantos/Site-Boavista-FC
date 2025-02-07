let currentIndex = 0; 
const batchSize = 20; 
const totalQRCodes = 500; 

function loadQRCodeGrid() {
    const container = document.getElementById('qr-codes-container'); 
    const loadMoreButton = document.getElementById('load-more-btn'); 

    function loadMore() {
        for (let i = currentIndex + 1; i <= currentIndex + batchSize && i <= totalQRCodes; i++) {
            const qrCodeImage = document.createElement('img'); 
            const imageName = `artigo${String(i).padStart(3, '0')}.png`;
            qrCodeImage.src = `QR_codes/${imageName}`;
            qrCodeImage.alt = `QR Code ${i}`;
            qrCodeImage.classList.add('qr-code');
            container.appendChild(qrCodeImage);
        }
        currentIndex += batchSize;

        if (currentIndex >= totalQRCodes) {
            loadMoreButton.style.display = 'none';
        }
    }

    loadMore();

    loadMoreButton.addEventListener('click', loadMore);
}

window.onload = loadQRCodeGrid;
