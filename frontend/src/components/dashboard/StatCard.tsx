type StatCardProps = {
    titulo: string
    valor: number
}

function StatCard(props: StatCardProps) {
    return (
        <div className="bg-white rounded-xl shdow-md p-6">

            <h3 className="text-gray-500 text-lg">
                {props.titulo}
            </h3>

            <h1 className="text-4xl font-bold text-blue-600 mt-3">
                {props.valor}
            </h1>
            
        </div>
    )
}

export default StatCard;