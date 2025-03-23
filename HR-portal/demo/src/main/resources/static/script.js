const API_URL = "http://localhost:8080/api/employees";


// Redirect to login if HR is not authenticated
if (!sessionStorage.getItem("hrLoggedIn")) {
    window.location.href = "login.html";
}

// Load employees when page loads
async function loadEmployees() {
    let response = await fetch(API_URL);
    let employees = await response.json();
    
    let tableBody = document.querySelector("#employeeTable tbody");
    tableBody.innerHTML = ""; // Clear existing table rows

    employees.forEach(emp => {
        let row = `<tr>
            <td>${emp.id}</td>
            <td>${emp.name}</td>
            <td>${emp.department}</td>
            <td>${emp.email}</td>
            <td>${emp.salary}</td>
            <td>
                <button class="action-btn edit-btn" onclick="editEmployee(${emp.id}, '${emp.name}', '${emp.department}', '${emp.email}', ${emp.salary})">Edit</button>
                <button class="action-btn delete-btn" onclick="deleteEmployee(${emp.id})">Delete</button>
            </td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

// Handle form submission
document.getElementById("employeeForm").onsubmit = async function(event) {
    event.preventDefault();

    let id = document.getElementById("employeeId").value;
    let employee = {
        name: document.getElementById("name").value,
        department: document.getElementById("department").value,
        email: document.getElementById("email").value,
        salary: parseFloat(document.getElementById("salary").value)
    };

    let method = id ? "PUT" : "POST";
    let url = id ? `${API_URL}/${id}` : API_URL;
    
    await fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(employee)
    });

    document.getElementById("employeeForm").reset();
    document.getElementById("employeeId").value = "";
    loadEmployees();
};

// Edit employee (prefill form)
function editEmployee(id, name, department, email, salary) {
    document.getElementById("employeeId").value = id;
    document.getElementById("name").value = name;
    document.getElementById("department").value = department;
    document.getElementById("email").value = email;
    document.getElementById("salary").value = salary;
}

// Delete employee
async function deleteEmployee(id) {
    if (confirm("Are you sure you want to delete this employee?")) {
        await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        loadEmployees();
    }
}
