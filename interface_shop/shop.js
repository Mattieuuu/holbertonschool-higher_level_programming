let selectedColors = [];
let allProducts = [];

function initShop() {
    allProducts = JSON.parse(localStorage.getItem('products') || '[]');
    displayProducts(allProducts);
    setupFilters();
}

function setupFilters() {
    const colorPicker = document.getElementById('colorPicker');
    const addColorBtn = document.getElementById('addColor');
    const selectedColorsContainer = document.querySelector('.selected-colors');
    const colorCounter = document.querySelector('.color-counter');
    
    addColorBtn.addEventListener('click', () => {
        if (selectedColors.length >= 5) {
            alert('Vous ne pouvez pas sélectionner plus de 5 couleurs');
            return;
        }

        const color = colorPicker.value;
        if (!selectedColors.includes(color)) {
            selectedColors.push(color);
            updateColorDisplay();
        }
    });

    function updateColorDisplay() {
        selectedColorsContainer.innerHTML = selectedColors.map(color => `
            <div class="color-tag" style="background-color: ${color}" data-color="${color}"></div>
        `).join('');

        colorCounter.textContent = `${selectedColors.length}/5 couleurs sélectionnées`;

        // Ajouter les événements de suppression
        document.querySelectorAll('.color-tag').forEach(tag => {
            tag.addEventListener('click', () => {
                const color = tag.dataset.color;
                selectedColors = selectedColors.filter(c => c !== color);
                updateColorDisplay();
            });
        });
    }

    document.getElementById('applyFilters').addEventListener('click', applyFilters);

    // Réinitialisation des couleurs
    document.getElementById('resetColors').addEventListener('click', () => {
        selectedColors = [];
        updateSelectedColorsDisplay();
    });

    // Réinitialisation de tous les filtres
    document.getElementById('resetAllFilters').addEventListener('click', () => {
        // Réinitialiser la recherche
        document.getElementById('searchInput').value = '';
        
        // Réinitialiser les catégories
        document.querySelectorAll('.category-filter').forEach(checkbox => {
            checkbox.checked = false;
        });
        
        // Réinitialiser les prix
        document.getElementById('minPrice').value = '';
        document.getElementById('maxPrice').value = '';
        
        // Réinitialiser les couleurs
        selectedColors = [];
        updateSelectedColorsDisplay();
        
        // Réafficher tous les produits
        displayProducts(allProducts);
    });
}

function updateColorFilter() {
    const filteredProducts = allProducts.filter(product => {
        if (selectedColors.length === 0) return true;
        return product.colors.some(color => selectedColors.includes(color));
    });

    console.log(`Filtrage par couleurs: ${selectedColors.length} couleurs sélectionnées`);
    console.log('Produits filtrés:', filteredProducts);
}

function applyFilters() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const selectedCategories = Array.from(document.querySelectorAll('.category-filter:checked')).map(cb => cb.value);
    const minPrice = parseFloat(document.getElementById('minPrice').value) || 0;
    const maxPrice = parseFloat(document.getElementById('maxPrice').value) || Infinity;

    const filteredProducts = allProducts.filter(product => {
        const matchesSearch = product.name.toLowerCase().includes(searchText);
        const matchesCategory = selectedCategories.length === 0 || selectedCategories.includes(product.category);
        const matchesPrice = product.price >= minPrice && product.price <= maxPrice;
        const matchesColor = selectedColors.length === 0 || 
            product.colors.some(color => selectedColors.includes(color));

        return matchesSearch && matchesCategory && matchesPrice && matchesColor;
    });

    displayProducts(filteredProducts);
}

function displayProducts(products) {
    ['fleurs', 'seches', 'composition'].forEach(id => {
        document.getElementById(id).innerHTML = '';
    });

    products.forEach(product => {
        const productCard = `
            <div class="product-card">
                <h3>${product.name}</h3>
                <div class="product-colors">
                    ${product.colors.map(color => 
                        `<span class="color-dot" style="background: ${color}"></span>`
                    ).join('')}
                </div>
                <p class="product-price">${product.price} €</p>
                <button class="add-to-cart">Ajouter au panier</button>
            </div>
        `;

        const container = document.getElementById(product.category);
        if (container) {
            container.innerHTML += productCard;
        }
    });
}

window.onload = initShop;
