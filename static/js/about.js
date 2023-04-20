let index = 0;
const image = [];

image[0] = "/static/images/hero-image1.webp";
image[1] = "/static/images/hero-image2.webp";
image[2] = "/static/images/hero-image3.webp";

function slider() {
  document.slide.src = image[index];
  if (index < image.length - 1) {
    index++;
  } else {
    index = 0;
  }
  setTimeout("slider()", 3000);
}
slider();
