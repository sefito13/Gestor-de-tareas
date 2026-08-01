type InputProps = {
    type: string
    placeholder: string
}

function Input(props: InputProps) {
    return (
        <input className="w-full border rounded-lg p-3 mb-4" type={props.type} placeholder={props.placeholder} />
    )
}

export default Input