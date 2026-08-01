type StatCardProps = {
    titulo: string
    valor: number
}

function StatCard(props: StatCardProps) {
    return (
        <div>
            <h3>{props.titulo}</h3>
            <h1>{props.valor}</h1>
        </div>
    )
}

export default StatCard;