const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".navbar_menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
});