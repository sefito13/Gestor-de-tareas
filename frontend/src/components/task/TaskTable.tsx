type Tarea = {
    id: number
    titulo: string
    estado: string
}

type TaskTableProps = {
    tareas: Tarea[]
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

                    </tr>
                ))}

            </tbody>
            
        </table>
    )
}

export default TaskTable