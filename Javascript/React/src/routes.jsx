// src/routes.js
import { createBrowserRouter } from 'react-router-dom';
import HomePage from './HomePage';
import LoginPage from './LoginPage';
import Dashboard from './Dashboard';
import PrivateRoute from './PrivateRoute';

const router = createBrowserRouter([
{
    path: '/',
    element: <HomePage />,
},
{
    path: '/login',
    element: <LoginPage />,
},
{
    path: '/dashboard',
    element: (
    <PrivateRoute>
        <Dashboard />
    </PrivateRoute>
    ),
},
]);

export default router;
