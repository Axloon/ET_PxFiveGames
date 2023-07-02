const carouselSlide = document.querySelector(".carousel-slide");

const firstSlide = carouselSlide.firstElementChild;
const lastSlide = carouselSlide.lastElementChild;
carouselSlide.insertBefore(lastSlide.cloneNode(true), firstSlide);
carouselSlide.appendChild(firstSlide.cloneNode(true));

let slidePosition = -600;

carouselSlide.style.transform = `translateX(${slidePosition}px)`;

function moveToNextSlide() {
  slidePosition -= 600;
  carouselSlide.style.transition = "transform 0.5s ease-in-out";
  carouselSlide.style.transform = `translateX(${slidePosition}px)`;
}

setInterval(moveToNextSlide, 3000);
