import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext"; // Make sure AuthContext is implemented

const HomePage = () => {
    const navigate = useNavigate();
    const { isLoggedIn } = useAuth(); // Get login status from context

const handleDashboardClick = () => {
    if (isLoggedIn) {
    navigate("/dashboard");
    } else {
    alert("Please login to access the Dashboard.");
    navigate("/login");
    }
};

return (
    <div>
    <div style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        gap: "20px",
        padding: "20px 0",
        borderBottom: "1px solid #eee"
    }}>
        <button onClick={() => navigate("/login")}>Login</button>
        <button onClick={handleDashboardClick}>Dashboard</button>
        <button onClick={() => navigate("/")}>Home</button>
    </div>
    <h2 style={{ textAlign: "center" }}>Welcome to Home Page</h2>
    </div>
);
};

export default HomePage;