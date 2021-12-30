fetch("/api/departments")
    .then((response) => response.json())
    .then((data) => {
        let departments = SelectDepartmentOfHospital(data);
        let select = document.getElementById('department');
        for (const department of departments) {
            let option = document.createElement("option");
            option.value = department['id'];
            option.text = department['name']
            select.appendChild(option);
        }
    })
    .catch((error) => console.log(error))

function SelectDepartmentOfHospital(data) {
    let select = []
    for (let i = 0; i < data.length; i++) {
        let object_department = data[i]
        let department = {
            'id': object_department['id'],
            'name': object_department['name']
        }
        select.push(department)
    }
    return select
}


function checker_where_are_you() {
    let identifier = document.URL.substring(document.URL.lastIndexOf('/') + 1);
    if (document.title === 'Edit employee') {
        is_on_edit_employee(get_data(), identifier)
    } else {
        is_on_add_employee(get_data())

    }

}


function get_data() {
    let name = document.getElementById("Name").value;
    let curdate = document.getElementById('curdate').value
    let salary = document.getElementById('salary').value
    let department = document.getElementById('department')
    if (department.value === '') {
        department.setAttribute('value', null)
    }
    return {
        'name': name,
        'date_of_birth': curdate,
        'salary': salary,
        'hospital_id': department.value
    }
}


function is_on_edit_employee(employee, identifier) {
    fetch(`/api/employees/${identifier}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employee)
    })
        .then((response) => response.json())
        .then(() => {
            swal("You have edited new employee succesfully")
                .then(() => {
                    window.location = '/employees';
                });
        })
        .catch(() => {
            swal("An error occured. Please check insert data.")
                .then(() => {
                    window.location = document.URL;
                });
        })
}

function is_on_add_employee(employee) {
    fetch(`/api/employees`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employee)
    })
        .then((response) => response.json())
        .then(() => {
            swal("You have added new employee succesfully")
                .then(() => {
                    window.location = '/employees';
                });
        })
        .catch(() => {
            swal("An error occured. Please check insert data.")
                .then(() => {
                    window.location = '/employees/add';
                });
        })

}