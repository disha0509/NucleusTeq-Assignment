import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

const LoginPage = () => {
const {isAuthenticated, login } = useAuth();
const navigate = useNavigate();

useEffect(() => {
    if (isAuthenticated) {
    navigate("/dashboard");
    }
}, [isAuthenticated, navigate]);



const handleLogin = (e) => {
    e.preventDefault();
    login();
    navigate("/dashboard");
  };

return (
    <div>
    <h2>Login Page</h2>
    <button onClick={handleLogin}>Login</button>
    </div>
);
};

export default LoginPage;
