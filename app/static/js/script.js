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
