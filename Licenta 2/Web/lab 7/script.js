document.getElementById("story-button").addEventListener("click", makestory);

function makestory() {
    var places = document.getElementById("places").value;
    var adjective = document.getElementById("adjective").value;
    var person = document.getElementById("person").value;
    var story = person + " a vizitat " + adjective + " " + places;
    var story_place = document.getElementById("story");
    story_place.textContent = story;
}