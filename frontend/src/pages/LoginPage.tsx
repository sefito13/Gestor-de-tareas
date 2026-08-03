import Card from "../components/ui/Card"
import Input from "../components/ui/Input"
import Button from "../components/ui/Button"
import { useEffect, useState } from "react"
import { login } from "../services/authService"
import { guardarToken, estaAutenticado } from "../services/tokenService"
import { useNavigate } from "react-router-dom"

function LoginPage() {
    const [correo, setCorreo] = useState("")
    const [password, setPassword] = useState("")

    const navigate = useNavigate()
    
    useEffect(() => {
        if (estaAutenticado()) {
            navigate("/dashboard")
        }
    }, [navigate])

    const iniciarSesion = async () => {

        if (correo === "" || password === "") {
            alert("Todos los campos son obligatorios")
            return
        }

        const respuesta = await login(correo, password)

        guardarToken(respuesta.access_token)
        navigate("/dashboard")

        console.log(respuesta)
    }


    return (
        <div className="min-h-screen flex justify-center items-center bg-gray-100">

            <Card>
                <div className="text-center mb-6">

                    <h1 className="text-2xl font-bold">Gestor de Tareas</h1>

                    <p className="text-lg text-gray-500 mt-2">Iniciar sesión</p>

                </div>
                
                <Input type="email" placeholder="Correo electrónico" value={correo} onChange={(e) => setCorreo(e.target.value)} />

                <Input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} />

                <Button texto="Iniciar Sesión" onClick={iniciarSesion} />
            </Card>

        </div>
    )
}

export default LoginPage;