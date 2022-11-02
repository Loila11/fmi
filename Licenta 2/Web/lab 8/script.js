fetch('http://localhost:3000/dogs')
  .then(function(response) {
    if (response.status !== 200) {
      console.log('Looks like there was a problem. Status Code: ' +
        response.status);
      return;
    }

    // Examine the text in the response
    response.json().then(function(dogs) {
      console.log(dogs);
      renderDogs(dogs);
    });
  }
)
.catch(function(err) {
  console.log('Fetch Error :-S', err);
});

function sendDogToServer(dog = {name: 'test', img: 'https://images.dog.ceo/breeds/affenpinscher/n02110627_8099.jpg'}) {
  fetch('http://localhost:3000/dogs', {
    method: 'post',
    headers: {
      "Content-type": "application/json"
    },
    body: JSON.stringify(dog)
  })
  .then(function (data) {
    console.log('Request succeeded with JSON response', data);
  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
}

function renderDogs(dogs) {
    for (var i = 0; i < dogs.length; i ++) {
        var name = document.createTextNode(dogs[i].name);
        var image = document.createElement("img");
        image.src = dogs[i].img;
        var newDog = document.createElement("div");
        newDog.appendChild(name);
        newDog.appendChild(image);
        document.body.appendChild(newDog);
    }
  }

function createDog() {
  var name = document.getElementById("name").value;
  var img = document.getElementById("img").value;
  sendDogToServer({name, img});
}

document.getElementById("create-button").addEventListener("click", createDog);