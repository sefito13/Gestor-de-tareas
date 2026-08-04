import Button from "../components/ui/Button"
import { useNavigate } from "react-router-dom"
import { eliminarToken } from "../services/tokenService"

function Sidebar() {
    const navigate = useNavigate()

    const cerrarSesion = () => {
        eliminarToken()
        navigate("/")
    }
    return (
        <aside className="w-64 h-screen bg-gray-800 text-white p-6 flex flex-col">

            <div>

                <h2 className="text-xl font-bold mb-6">Menu</h2>

                <nav className="flex flex-col gap-4">

                    <a href="/dashboard" className="hover:text-blue-300">Dashboard</a>
                    <a href="/mis-tareas" className="hover:text-blue-300">Mis tareas</a>
                    <a href="#" className="hover:text-blue-300">Perfil</a>

                </nav>

            </div>

            <div className="mt-auto pt-8 border-t border-gray-700">

                <Button texto="Cerrar Sesión" onClick={cerrarSesion} />
                
            </div>

        </aside>
    )
}

export default Sidebar