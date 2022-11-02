
function clearPage() {
    document.getElementById("page-body").innerHTML = "";
}

var currentUserId = 0;

function getUser() {
    fetch('http://localhost:3000/users')
        .then(function (response) {
            response.json().then(function (users) {
                showAppointments(users[currentUserId]);
            });
        });
};

function showAppointments(user) {
    clearPage();

    for (index in user.appointments) {
        var appointment = user.appointments[index];
        var appointmentBox = document.createElement("div");

        // Service
        var title = document.createElement("h3");
        title.textContent = appointment.name;
        appointmentBox.appendChild(title);

        // Delete Button
        var deleteButton = document.createElement('button')
        deleteButton.addEventListener('click', function () {
            deleteAppointment(user, index)
        });
        deleteButton.innerText = 'Delete';
        appointmentBox.appendChild(deleteButton);

        // Specifics
        var detailBox = document.createElement("div");
        for (detailIndex in appointment.details) {
            var detail = document.createElement("p");
            detail.textContent = appointment.details[detailIndex];
            detailBox.appendChild(detail);
        }
        appointmentBox.appendChild(detailBox);
    
        document.getElementById("page-body").appendChild(appointmentBox);
    }
}

function deleteAppointment(user, index) {
    if (!confirm("Sunteti sigur ca vreti sa stergeti?")) {
        return ;
    }

    user.appointments.splice(index, 1);

    fetch(`http://localhost:3000/users/${currentUserId}`, {
        method: 'PUT',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(user)
    }).then(function () {
        getUser();
    });
}

getUser();

// const formName = document.getElementById('formName');
// const formUrl = document.getElementById('formUrl');
// const addButton = document.getElementById('addButton');
// let updateButton = document.getElementById('updateButton');

// function getUsers() {
//     fetch('http://localhost:3000/users')
//         .then(function (response) {
//             response.json().then(function (users) {
//                 appendUsersToDOM(users);
//             });
//         });
// };

// function deleteUser(id) {
//     fetch(`http://localhost:3000/users/${id}`, {
//         method: 'DELETE',
//     }).then(function() {
//         getUsers();
//     });
// }

// function postUser() {
//     const user = {
//         name: formName.value,
//         email: formUrl.value
//     }

//     fetch('http://localhost:3000/users', {
//         method: 'post',
//         headers: {
//             "Content-type": "application/json"
//         },
//         body: JSON.stringify(user)
//     }).then(function() {
//         getUsers();
//         resetForm();
//     });
// }

// function updateUser(id) {
//     const user = {
//         name: formName.value,
//         email: formUrl.value
//     }
//     fetch(`http://localhost:3000/users/${id}`, {
//         method: 'PUT',
//         headers: {
//             "Content-type": "application/json"
//         },
//         body: JSON.stringify(user)
//     }).then(function () {
//         getUsers();
//         addButton.disabled = false;
//         clearUpdateButtonEvents();
//         resetForm();
//     });
// }

// function editUser(user) {
//     formName.value = user.name;
//     formUrl.value = user.email;

//     addButton.disabled = true;
//     clearUpdateButtonEvents();
//     updateButton.disabled = false;
//     updateButton.addEventListener('click', function () {
//         updateUser(user.id)
//     });
// }

// function appendUsersToDOM(users) {
//     while (list.firstChild) {
//         list.removeChild(list.firstChild);
//     }
//     for (let i = 0; i < users.length; i++) {
//         let email = document.createElement('p');
//         email.textContent = users[i].email;
//         let name = document.createElement('span');
//         name.innerText = users[i].name;
//         let editButton = document.createElement('button')
//         editButton.addEventListener('click', function () {
//             editUser(users[i])
//         });
//         editButton.innerText = 'Edit';
//         let deleteButton = document.createElement('button')
//         deleteButton.addEventListener('click', function () {
//             deleteUser(users[i].id)
//         });
//         deleteButton.innerText = 'Delete';
//         let container = document.createElement('div');
//         container.appendChild(name);
//         container.appendChild(email);
//         container.appendChild(editButton);
//         container.appendChild(deleteButton);

//         list.appendChild(container);
//     }
// }

// function resetForm() {
//     formName.value = '';
//     formUrl.value = '';
// }

// function clearUpdateButtonEvents() {
//     let newUpdateButton = updateButton.cloneNode(true);
//     updateButton.parentNode.replaceChild(newUpdateButton, updateButton);
//     updateButton = document.getElementById('updateButton');
// }

// addButton.addEventListener('click', postUser);
