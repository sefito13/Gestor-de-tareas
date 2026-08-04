import { useState } from "react"
import Input from "../ui/Input"
import Button from "../ui/Button"

type TaskFormProps = {
    onGuardar: (titulo: string, estado: string) => void
}

function TaskForm(props: TaskFormProps) {
    
    const [titulo, setTitulo] = useState("")
    const [estado, setEstado] = useState("Pendiente")

    const guardar = () => {

        if (titulo.trim() === "") {
            alert("El titlo es obligatorio")
            return
        }

        props.onGuardar(titulo, estado)
    }

    return (

        <div className="flex flex-col gap-4">
            
            <Input type="text" placeholder="Titulo de la tarea" value={titulo} onChange={(e) => setTitulo(e.target.value)} />

            <select value={estado} onChange={(e) => setEstado(e.target.value)} className="border rounded.lg p-2">

                <option value="Pendiente"> Pendiente </option>
                <option value="En Curso"> En Curso </option>
                <option value="Completa"> Completa </option>
            </select>

            <Button texto="Guardar" onClick={guardar} />

        </div>
    )
    
}

export default TaskForm