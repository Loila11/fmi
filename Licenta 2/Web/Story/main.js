
function addToHistory(id, checkedAns) {
    var question = questions[id];
    var div = document.createElement("div");
    div.className = "div";
    var q = document.createElement("h3");
    q.textContent = question.q;
    div.appendChild(q);
    var ans = document.createElement("p");
    ans.textContent = checkedAns;
    div.appendChild(ans);
    document.getElementById("history").appendChild(div)
}

function addQuestion(id) {
    var question = questions[id];
    var div = document.createElement("div");
    div.className = "div";
    var q = document.createElement("h2");
    q.textContent = question.q;
    div.appendChild(q);

    for (index in questions[id].ans) {
        var answer = question.ans[index];
        var ansLabel = document.createElement("label");
        ansLabel.textContent = answer.a;
        ansLabel.classList.add("service");
        var ansInput = document.createElement("input");
        ansInput.required = true;
        ansInput.type = "radio";
        ansInput.name = "answer" + id;
        ansInput.value = answer.next_id;
        if (answer.next_id) {
            ansInput.addEventListener("click", function() {
                addToHistory(id, answer.a);
                addQuestion(this.value);
            });
        }

        div.appendChild(ansInput);
        div.appendChild(ansLabel);
    }
    document.getElementById("question").innerHTML = "";
    document.getElementById("question").appendChild(div);
}

window.addEventListener("load", function () {
    addQuestion(0);
});
