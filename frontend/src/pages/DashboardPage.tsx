import StatCard from "../components/dashboard/StatCard"
import { useNavigate } from "react-router-dom"
import Button from "../components/ui/Button"
import { eliminarToken } from "../services/tokenService"

function DashboardPage() {
    const navigate = useNavigate()

    const cerrarSesion = () => {
        eliminarToken()
        navigate("/")
    }

    return (
        <div className="p-10">
            <h1 className="text-4xl font-bold text-blue-600">
                Dashboard
            </h1>

            <p className="mt-4 text-gray-600">
                Bienvenido al Gestor de Tareas
            </p>

            <Button texto= "Cerrar Sesión" onClick={cerrarSesion} />

        </div>
    );
}

export default DashboardPage