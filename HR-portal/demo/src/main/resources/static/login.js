document.getElementById("loginForm").onsubmit = async function(event) {
    event.preventDefault();

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    let response = await fetch("http://localhost:8080/api/hr/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    let result = await response.json();

    if (result.status === "success") {
        sessionStorage.setItem("hrLoggedIn", "true");
        window.location.href = "index.html";  // Redirect to employee dashboard
    } else {
        document.getElementById("errorMessage").style.display = "block";
    }
};
