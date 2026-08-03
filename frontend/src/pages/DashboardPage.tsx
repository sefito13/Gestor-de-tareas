import { useEffect, useState } from "react"
import StatCard from "../components/dashboard/StatCard"
import { obtenerResumen } from "../services/taskService"


function DashboardPage() {

    const [resumen, setResumen] = useState({
        pendientes: 0,
        en_curso: 0,
        completadas: 0
    })

    useEffect(() => {

        const cargarResumen = async () => {
            try {

                const datos = await obtenerResumen()

                console.log(datos)

                setResumen(datos)

            } catch (error) {

                console.error(error)
            }
        }

        cargarResumen()

    }, [])

    return (
        <div className="p-10">
            <div className="flex justify-between items-center">

                <h1 className="text-4xl font-bold text-blue-600">
                    Dashboard
                </h1>

                <p className="mt-4 text-gray-600">
                    Bienvenido al Gestor de Tareas
                </p>

            </div>

            <div className="grid grid-cols-3 gap-6 mt-10">
                
                <StatCard titulo="Pendientes" valor={resumen.pendientes} />
                <StatCard titulo="En curso" valor={resumen.en_curso} />
                <StatCard titulo="Completadas" valor={resumen.completadas} />

            </div>
            

        </div>
    );
}

export default DashboardPage