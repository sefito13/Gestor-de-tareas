type ButtonProps = {
    texto: string
    onClick: () => void
}

function Button(props: ButtonProps) {
    return (
        <button className="w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition cursor-pointer shadow-md font-semibold" onClick={props.onClick}>
            {props.texto}
        </button>
    )
}

export default Button