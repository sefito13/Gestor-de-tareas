import { useEffect, useState } from "react"
import { obtenerTareas, crearTarea } from "../services/taskService"
import TaskTable from "../components/task/TaskTable"
import Input from "../components/ui/Input"
import Button from "../components/ui/Button"
import Modal from "../components/ui/Modal"
import TaskForm from "../components/task/TaskForm"

function MisTareasPage() {

    const [tareas, setTareas] = useState([])
    const [buscar, setBuscar] = useState("")
    const [modalAbierto, setModalAbierto] = useState(false)

    const abrirModal = () => {
        setModalAbierto(true)
    }

    const cerrarModal = () => {
        setModalAbierto(false)
    }

    const guardarNuevaTarea = async (titulo: string, estado: string) => {
        try {

            await crearTarea(titulo, estado)

            cerrarModal()

            cargarTareas()

        } catch (error) {

            console.error(error)

        }   
    }
    
    const cargarTareas = async () => {

        const datos = await obtenerTareas()

        setTareas(datos.items)
    }

    useEffect(() => {
        cargarTareas()
    }, [])


    return (
        
        <div className="p-10 items-center">


                <h2 className="text-4xl font-bold text-blue-600 mb-8">
                    Mis Tareas
                </h2>

            <div className="flex justify-between items-center mb-6">
                
                <div className="w-96">

                    <Input type="text" placeholder="Buscar tarea ..." value={buscar} onChange={(e) => setBuscar(e.target.value)} />

                </div>

                    <Button texto="+ Nueva tarea" onClick={abrirModal}/>

            </div>

            <div className="mt-6">

                <TaskTable tareas={tareas} />
                <Modal abierto={modalAbierto} titulo="Nueva Tarea" onClose={cerrarModal}>

                    <TaskForm
                        onGuardar={guardarNuevaTarea}
                    />

                </Modal>

            </div>
            
        </div>
    )
}

export default MisTareasPage