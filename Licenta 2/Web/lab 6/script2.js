let filme = [
    {
        titlu: "film 1",
        durata: 120,
        actori: ["ana", "matei"],
        vazut: 0,
        poza: "https://img.freepik.com/free-vector/stylish-hexagonal-line-pattern-background_1017-19742.jpg?size=626&ext=jpg",
    },
    {
        titlu: "film 2",
        durata: 160,
        actori: ["maria", "ana", "ion"],
        vazut: 1,
        poza: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdhRo0ZqEugMzgOd3JDhhpixHwMqHI2KnxdH3GcnMtSnUiUng&s",
    }
]

for (var i = 0; i < filme.length; i ++) {
    var newP = document.createElement("p");
    newP.textContent = filme[i].titlu;
    document.body.appendChild(newP);

    var list = document.createElement("ul")
    document.body.appendChild(list);
    
    var durata = document.createElement("li");
    durata.textContent = "Durata: " + filme[i].durata + " min";
    list.appendChild(durata);

    var actori = document.createElement("li");
    actori.textContent = "Actori: ";
    for (var j = 0; j < filme[i].actori.length; j ++) {
        actori.textContent += filme[i].actori[j] + ', ';
    }
    list.appendChild(actori);

    var vazut = document.createElement("li");
    vazut.textContent = "Vazut: " + (filme[i].vazut == 1);
    list.appendChild(vazut);

    var poza = document.createElement("img");
    poza.setAttribute("src", filme[i].poza);
    list.appendChild(poza);

    if (filme[i].vazut == 0) list.style.color = "red";
}