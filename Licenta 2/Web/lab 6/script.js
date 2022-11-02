document.body.style.fontFamily = "Arial, sans-serif";

var span = document.getElementsByTagName("span");
span[0].textContent = "ceva";
span[1].textContent = "ceva2";
span[2].textContent = "ceva3";

var list = document.getElementsByTagName("li");
for (var i = 0; i < list.length; i ++) {
    list[i].setAttribute("class", "list-item");
}

var image = document.createElement("img");
image.setAttribute("src", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdhRo0ZqEugMzgOd3JDhhpixHwMqHI2KnxdH3GcnMtSnUiUng&s");
document.body.appendChild(image);