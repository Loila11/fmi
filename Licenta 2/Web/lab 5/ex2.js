var film = {
    titlu: "La Moara cu noroc",
    durata: 130,
    actori: [
        "Constantin Codrescu", 
        "Olga Tudorache", 
        "Geo Barton"
    ]
}

var info = '"' + film.titlu + '" a durat ' + film.durata + 
            ' minute. Actori: '

for (var i = 0; i < film.actori.length - 1; i ++) {
    info += film.actori[i] + ', '
}

info += film.actori[film.actori.length - 1]

console.log(info)