var blackFridayCart = {
    telefon: "350",
    consola: "250",
    televizor: "450",
    iepurasPlus: "10.60",
    cercei: "20.34",
    geanta: "22.36"
};

getCartValue = function (array) {
    var sum = 0;
    for (var object in blackFridayCart) {
        sum += parseFloat(blackFridayCart[object]);
    }
    return sum;
}

console.log(getCartValue(blackFridayCart))
