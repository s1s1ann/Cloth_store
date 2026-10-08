window.addEventListener("scroll", function () {
  const header = document.querySelector("header");
  const topBar = document.querySelector(".top-bar");

  if (window.scrollY > 150) {
    header.classList.add("scrolled");
    topBar.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
    topBar.classList.remove("scrolled");
  }
});

const slides = [
  {
    title: "Тупо<br>Дешево<br>Обрыгано",
    description: "Тупой шмот<br>для дешевой жизни,<br>который не жалко обрыгать",
    image: "images/hero/hero-1.jpg",
  },
  {
    title: "Старо<br>Вонюче<br>Обблевано",
    description: "Старое дерьмо,<br>и ты все прямо обблеван.<br>Выгляди как бомж, плати как человек",
    image: "images/hero/hero-2.jpg",
  },
  {
    title: "Криво<br>Стремно<br>Обдристано",
    description: "Шмот для тех,<br>кому уже прямо похуй,<br>но голым ходить очень стыдно",
    image: "images/hero/hero-3.jpg",
  },
];

const heroSection = document.querySelector(".hero");
const heroTitle = document.querySelector(".hero-title h2");
const heroDescription = document.querySelector(".hero-description");
const paginationItems = document.querySelectorAll(".hero-pagination-item");

// function showSlide(index) {
//   const slide = slides[index];

//   heroTitle.innerHTML = slide.title;
//   heroDescription.innerHTML = slide.description;
//   heroImage.src = slide.image;

//   paginationItems.forEach(function (button) {
//     button.classList.remove("active");
//   });

//   paginationItems[index].classList.add("active");
// }

function showSlide(index) {
  const slide = slides[index];

  heroTitle.innerHTML = slide.title;
  heroDescription.innerHTML = slide.description;

  heroSection.style.backgroundImage = `url("${slide.image}")`;

  paginationItems.forEach(function (button) {
    button.classList.remove("active");
  });

  paginationItems[index].classList.add("active");
}

paginationItems.forEach(function (button) {
  button.addEventListener("click", function () {
    const index = Number(button.dataset.slide);
    showSlide(index);
  });
});

showSlide(0);
