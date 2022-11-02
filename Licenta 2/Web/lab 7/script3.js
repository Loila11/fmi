var movePixels = 10; // number of pixels
var delayMs = 50; // number of miliseconds
var dogTimer = null;

// Move the image on screen with 10px
function dogWalk() {
    var img = document.getElementsByTagName("img")[0];
    var currentLeft = parseInt(img.style.left);
    img.style.left = currentLeft + movePixels + "px";
    // reset image position to start
    if (currentLeft > window.innerWidth - img.width) {
    img.style.left = "0px";
    }
}

// Call dogWalk function every 50 ms
function startDogWalk() {
    stopDogWalk();
    dogTimer = window.setInterval(dogWalk, delayMs);
}

function stopDogWalk() {
    window.clearInterval(dogTimer);
}

function speedDogWalk() {
    stopDogWalk();
    dogTimer = window.setInterval(dogWalk, delayMs / 2);
}

document.getElementById("start-button").addEventListener("click", startDogWalk);
document.getElementById("stop-button").addEventListener("click", stopDogWalk);
document.getElementById("speed-button").addEventListener("click", speedDogWalk);