
var questions = [{
    id: 0,
    q: "Se impaca Vero cu Buliga?",
    ans: [{
        a: "Da",
        next_id: 1
    }, {
        a: "Nu"
    }]
}, {
    id: 1,
    q: "Cat ii tine?",
    ans: [{
        a: "Sub 1 an"
    }, {
        a: "Peste 1 an",
        next_id: "3"
    }]
}, {
    id: 2,
    q: "De ce se despart?",
    ans: [{
        a: "ceva1"
    }, {
        a: "ceva2"
    }]
}, {
    id: 3,
    q: "Cand o cere in casatorie, Vero zice da?",
    ans: [{
        a: "Da",
        next_id: 5
    }, {
        a: "Nu",
        next_id: 4
    }]
}, {
    id: 4,
    q: "Ce motiv da?",
    ans: [{
        a: "ceva1"
    }, {
        a: "ceva2"
    }]
}, {
    id: 5,
    q: "Se si casatoresc?",
    ans: [{
        a: "Da",
        next_id: 6
    }, {
        a: "Nu",
        next_id: 8
    }]
}, {
    id: 6,
    q: "Dupa cat timp?",
    ans: [{
        a: "ceva1",
        next_id: 6
    }, {
        a: "ceva2"
    }]
}, {
    id: 7,
    q: "Cat ii tine?",
    ans: [{
        a: "ceva1",
    }, {
        a: "ceva2"
    }]
}, {
    id: 8,
    q: "Fuge de la altar?",
    ans: [{
        a: "Da",
    }, {
        a: "Nu",
        next_id: 4
    }]
}]
