// preloader start
window.addEventListener("load", function () {
    const preloader = document.getElementById("preloader");
    const content = document.getElementById("content");
    
    // Hide the preloader
    preloader.style.display = "none";
    
    // Show the content
    content.style.display = "block";
  });
    // preloader end  

let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    navBar.classList.remove('active');
    userProfile.classList.remove('active')
}

let shoppingCart = document.querySelector('.shopping-cart');

document.querySelector('#cart-btn').onclick = () =>{
    shoppingCart.classList.toggle('active');
    navBar.classList.remove('active');
    searchForm.classList.remove('active');
    userProfile.classList.remove('active')
}

let userProfile = document.querySelector('.login-form');

document.querySelector('#login-btn').onclick = () =>{
    userProfile.classList.toggle('active')
    navBar.classList.remove('active');
    shoppingCart.classList.remove('active');
    searchForm.classList.remove('active');
}

let navBar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navBar.classList.toggle('active');
    shoppingCart.classList.remove('active');
    searchForm.classList.remove('active');
    userProfile.classList.remove('active')
}

window.onscroll = () =>{
    navBar.classList.remove('active');
    shoppingCart.classList.remove('active');
    searchForm.classList.remove('active');
}

// remove item from cart
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to trash icons
    document.querySelectorAll('.remove-item').forEach(function (trashIcon) {
        trashIcon.addEventListener('click', function (event) {
            event.preventDefault();
            var productId = this.getAttribute('data-product-id');
            removeFromCart(productId);
        });
    });

    // Function to remove item from cart via AJAX
    function removeFromCart(productId) {
        fetch(`/orders/remove_from_cart/${productId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => response.json()).then(data => {
            // Display return message in message area
            document.getElementById('message-area').innerHTML = data.message;
            // Remove the item from the DOM if it was successfully removed from the cart
            if (data.success) {
                document.querySelector(`a[data-product-id="${productId}"]`).closest('.box').remove();
                // Optionally, update the total price displayed
                updateTotalPrice();
            }
        }).catch(error => {
            console.error('Error removing item from cart:', error);
        });
    }

    // Function to update the total price displayed in the shopping cart
    function updateTotalPrice() {
        fetch('/calculate_total_price', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => response.json()).then(data => {
            document.querySelector('.total').textContent = `total : KSH. ${data.total_price}/-`;
        }).catch(error => {
            console.error('Error updating total price:', error);
        });
    }
});
