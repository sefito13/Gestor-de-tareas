type CardProps = {
    children: React.ReactNode
}

function Card(props: CardProps) {
    return (
        <div className="bg-white p-8 rouded-xl shadow-lg w-full max-w-md">
            {props.children}
        </div>
    )
}

export default Card