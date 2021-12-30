let identifier = document.URL.substring(document.URL.lastIndexOf('/') + 1);
if (document.title === "Edit department") {
    fetch(`/api/departments/${identifier}`)
        .then((response) => response.json())
        .catch(() => {
            swal("There is no this department. Please select currect department")
                .then(() => {
                    window.location = '/departments';
                });
        })
}

function checker_where_are_you() {
    if (document.title === "Edit department") {
        is_on_edit_department(get_data(), identifier)
    } else {
        is_on_add_department(get_data())
    }
}

function get_data() {
    let name = document.getElementById("Name of department").value;
    let to_do = document.getElementById('to_do').value
    return {
        'name': name,
        'to_do': to_do
    }
}

function is_on_edit_department(department, identifier) {
    fetch(`/api/departments/${identifier}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(department)
    })
        .then((response) => response.json())
        .then(() => {
            swal("You have changed new department of hospital succesfully")
                .then(() => {
                    window.location = '/departments';
                });
        })
        .catch(() => {
            swal("An error occured. Please check insert data.")
                .then(() => {
                    window.location = document.URL;
                });
        })
}

function is_on_add_department(department) {
    fetch(`/api/departments`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(department)
    })
        .then((response) => response.json())
        .then(() => {
            swal("You have added new department of hospital succesfully")
                .then(() => {
                    window.location = '/departments';
                });
        })
        .catch(() => {
            swal("An error occured. Please check insert data.")
                .then(() => {
                    window.location = '/departments/add';
                });
        })
}
