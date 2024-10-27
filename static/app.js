
 if (document.getElementById("add-to-cart")) {
    console.log("add-to-cart button found");
 document.getElementById("add-to-cart").addEventListener("click", function(event) {
    event.preventDefault();  

    const articleData = {
        nom: this.getAttribute("data-nom"),
        categorie: this.getAttribute("data-categorie"),
        prix: this.getAttribute("data-prix"),
        description: this.getAttribute("data-description")
    };

    console.log(articleData);

    if (!localStorage.getItem("cart")) {
        localStorage.setItem("cart", "[]");
    }

    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(articleData);
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();

});
}

const updateCartCount = () => {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    console.log("updateCartCount", cart);
    document.getElementById("cart-count").innerText = cart.length;
}



function renderCartItems() {
    console.log("renderCartItems");
    const cartItemsContainer = document.getElementById("cart-items");
    const articlesInput = document.getElementById("articlesInput");
    const totalPriceElement = document.getElementById("total-price");
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    cartItemsContainer.innerHTML = "";  // Clear any previous content

    let formArticlesData = [];
    let totalCartPrice = 0;

    cart.forEach((article, index) => {
        const { nom, prix, description, quantity = 1 } = article;
        const totalPrice = prix * quantity;

        // Add a row for each article in the cart
        cartItemsContainer.innerHTML += `
            <tr>
                <td>${nom}</td>
                <td>${prix} €</td>
                <td>
                    <input type="number" value="${quantity}" min="1" data-index="${index}" class="quantity-input" />
                </td>
                <td>${totalPrice.toFixed(2)} €</td>
                <td><button class="btn btn-danger btn-sm delete-btn" data-index="${index}">Delete</button></td>
            </tr>
        `;

        formArticlesData.push({ nom, prix, description, quantity });
        totalCartPrice += totalPrice;
    });

    // Display the total cart price
    totalPriceElement.textContent = `Total: ${totalCartPrice.toFixed(2)} €`;

    // Store all articles data in the hidden input field as JSON
    articlesInput.value = JSON.stringify(formArticlesData);
}

// Event listener to handle quantity change and update total in localStorage and UI
document.addEventListener("input", function (event) {
    if (event.target.classList.contains("quantity-input")) {
        const cart = JSON.parse(localStorage.getItem("cart")) || [];
        const index = event.target.getAttribute("data-index");
        const newQuantity = parseInt(event.target.value);

        if (newQuantity < 1) {
            cart.splice(index, 1);
        } else {
            cart[index].quantity = newQuantity;
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        renderCartItems();
    }
});

// Event listener to handle item deletion
document.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-btn")) {
        const cart = JSON.parse(localStorage.getItem("cart")) || [];
        const index = event.target.getAttribute("data-index");

        cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(cart));
        renderCartItems();
    }
});

// Initial render of cart items on page load
document.addEventListener("DOMContentLoaded", () => {
    console.log("DOMContentLoaded");
    if (document.getElementById("cart-items")) {
        renderCartItems();
    }
});
