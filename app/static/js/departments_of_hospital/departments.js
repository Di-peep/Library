fetch("/api/departments")
    .then((response) => response.json())
    .then((data) => {
        DisplayGotData(data);
    })
    .catch((error) => console.log(error))


function DisplayGotData(data) {
    if (data.length === 0) {
        let empty = document.getElementById("empty");
        let text = document.createTextNode("No departments of hospital were found");
        empty.appendChild(text);
    } else {
        CreateTable(GetData(data));
    }
}


function GetData(data) {
    let information = []
    for (let i = 0; i < data.length; i++) {
        let current_department = data[i];
        let employees = current_department['employees'].length;
        let salary = 0;
        if (employees > 0) {
            for (let j = 0; j < current_department['employees'].length; j++) {
                let single_employee = current_department['employees'][j];
                salary += single_employee['salary'];
            }
            salary /= employees;
        }
        let json_departments = {
            'identifier': current_department['id'],
            'Name': current_department['name'],
            'Whats to do': current_department['to_do'],
            'Employees': employees,
            'Avarage salary': salary
        }
        information.push(json_departments)
    }
    return information
}

function CreateTable(data) {
    let session = document.getElementById("session").textContent
    let table = document.querySelector("table");
    let keys = Object.keys(data[0])
    for (let i = 0; i < data.length; i++) {
        let element = data[i];
        let row = table.insertRow();
        for (let j = 1; j < keys.length; j++) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[keys[j]]);
            cell.appendChild(text);
        }
        if (session.includes('True')) {
            //create edit link
            let cell = row.insertCell();
            let a = document.createElement("a");
            a.setAttribute("href", `/departments/edit/${element['identifier']}`);
            let text = document.createTextNode("Edit");
            a.appendChild(text);
            cell.appendChild(a);
            cell = row.insertCell();
            //create delete request
            a = document.createElement("a");
            a.setAttribute("onclick", `api_delete(${element['identifier']})`)
            text = document.createTextNode("Delete");
            a.appendChild(text);
            cell.appendChild(a);
        }
    }
}

function api_delete(identifier) {
    fetch(`/api/departments/${identifier}`, {
        method: 'DELETE'
    })
        .then((response) => response.json())
        .then(() => {
            window.location.href = `/departments`;
        })
        .catch(() => {
            window.location = document.URL;
            swal("An error occured. Please try again.");
        })
}