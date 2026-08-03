import { Navigate, Outlet } from "react-router-dom"
import { estaAutenticado } from "../services/tokenService"

function ProtectedRoute() {

    if (estaAutenticado()) {
        return <Outlet />
    }
    
    return <Navigate to="/" />
}

export default ProtectedRoute

