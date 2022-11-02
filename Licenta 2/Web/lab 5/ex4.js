function multiplicator(element) {
    return 2 * element;
}

Array.prototype.myMap = function(callbackFunction) {
    let newArray = [];
    for (var i = 0; i < this.length; i ++) {
        newArray.push(callbackFunction(this[i]));
    }
    return newArray;
}

console.log([1, 2, 3].map(multiplicator));
console.log([1, 2, 3].myMap(multiplicator));