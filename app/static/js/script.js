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
        fetch("{{ url_for('orders.remove_from_cart', product_id='') }}" + productId, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            if (response.ok) {
                location.reload(); // Refresh the page after successful removal
            } else {
                console.error('Error removing item from cart:', response.statusText);
            }
        }).catch(error => {
            console.error('Error removing item from cart:', error);
        });
    }
});