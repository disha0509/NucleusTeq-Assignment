import { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
const [isAuthenticated, setIsAuthenticated] = useState(() => {
    const storedAuth = localStorage.getItem("isAuthenticated");
    return storedAuth === "true";
});

useEffect(() => {
    localStorage.setItem("isAuthenticated", isAuthenticated);
}, [isAuthenticated]);

const login = () => setIsAuthenticated(true);
const logout = () => setIsAuthenticated(false);

return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
    {children}
    </AuthContext.Provider>
);
};

export const useAuth = () => useContext(AuthContext);