let body = document.querySelector('body');
let navbar = document.querySelector('.hero-container');
let menu = document.querySelector('.navbar-button');

// let scrollOffer = document.querySelector('.container-offers');
// scrollOffer.scrollTo(700, 0)

menu.addEventListener('click', () => {
    body.classList.add('show-menu');
});

navbar.addEventListener('mousedown', () => {
    if(body.classList.contains('show-menu')) {
        body.classList.remove('show-menu');
    }
})



