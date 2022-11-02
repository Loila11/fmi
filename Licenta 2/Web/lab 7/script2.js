document.getElementById("square-button").addEventListener("click", square);

function square() {
    var number = document.getElementById("square-input").value;
    var sol = number * number;
    var solution = document.getElementById("solution");
    solution.textContent = sol;
}

document.getElementById("half-button").addEventListener("click", half);

function half() {
    var number = document.getElementById("half-input").value;
    var sol = number / 2;
    var solution = document.getElementById("solution");
    solution.textContent = sol;
}

document.getElementById("percent-button").addEventListener("click", percent);

function percent() {
    var number1 = document.getElementById("percent1-input").value;
    var number2 = document.getElementById("percent2-input").value;
    var sol = number1 / 100 * number2;
    var solution = document.getElementById("solution");
    solution.textContent = sol;
}

document.addEventListener("keypress", area); //nu merge pt o cifra
document.getElementById("area-button").addEventListener("click", area);

function area() {
    var number = document.getElementById("area-input").value;
    var sol = number * number * Math.PI;
    var solution = document.getElementById("solution");
    solution.textContent = sol;
}
