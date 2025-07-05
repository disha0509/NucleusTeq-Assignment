import { useAuth } from './AuthContext';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
const { logout } = useAuth();
const navigate = useNavigate();

const handleLogout = () => {
    logout();
    navigate('/login');
};

return (
    <div>
    <h2>Dashboard - Private Route</h2>
    <button onClick={handleLogout}>Logout</button>
    </div>
);
};

export default Dashboard;