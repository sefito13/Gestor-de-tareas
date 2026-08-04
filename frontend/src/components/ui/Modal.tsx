type ModalProps = {
    abierto: boolean
    titulo: string
    onClose: () => void
    children: React.ReactNode
}

function Modal(props: ModalProps) {

    if (!props.abierto) {
        return null
    }

    return (

        <div className="fixed inset-0 bg-black/50 flex justify-center items-center">

            <div className="bg-white rounded-lg shadow-lg w-[500px]">

                <div className="flex justify-between items-center p-4 border-b">

                    <h2 className="text-xl font-bold">
                        {props.titulo}
                    </h2>

                    <button
                        onClick={props.onClose}
                        className="text-gray-500 hover:text-red-500"
                    >
                        ✕
                    </button>

                </div>

                <div className="p-6">

                    {props.children}

                </div>

            </div>

        </div>

    )
}

export default Modal