import { Navigate, Outlet } from "react-router-dom";

function ProtectedRoute() {
    const token = localStorage.getItem("acces_token");

    if (token) {
        return <Outlet />
    }
    
    return <Navigate to="/" />;
}

export default ProtectedRoute;

