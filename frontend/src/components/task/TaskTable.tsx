type Tarea = {
    id: number
    titulo: string
    estado: string
}

type TaskTableProps = {
    tareas: Tarea[]
    onEliminar: (id: number) => void
}

function TaskTable(props: TaskTableProps) {
    return (
        <table className="w-full bg-white rounded-lg shadow">

            <thead>

                <tr className="border-b">

                    <th className="p-4 text-left">
                        Titulo
                    </th>

                    <th className="p-4 text-left">
                        Estado
                    </th>

                    <th className="p-4 text-left">
                        Acciones
                    </th>

                </tr>

            </thead>

            <tbody>

                {props.tareas.map((tarea) => (

                    <tr key={tarea.id} className="border-b">

                        <td className="p-4">
                            {tarea.titulo}
                        </td>

                        <td className="p-4">
                            {tarea.estado}
                        </td>

                        <td className="p4 text-center">

                            <button onClick={() => props.onEliminar(tarea.id)} className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md transition-colors">
                                Eliminar
                            </button>

                        </td>

                    </tr>
                ))}

            </tbody>
            
        </table>
    )
}

export default TaskTable