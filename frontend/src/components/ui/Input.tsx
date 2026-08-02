type InputProps = {
    type: string
    placeholder: string
    value: string
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
}

function Input({ type, placeholder, value, onChange }: InputProps) {
    return (
        <input
            className="w-full border rounded-lg p-3 mb-4"
            type={type}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
        />
    );
}

export default Input