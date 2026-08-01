import Card from "../components/ui/Card";
import Input from "../components/ui/Input";
import Button from "../components/ui/Button";

function LoginPage() {
    const iniciarSesion = () => {
        console.log("Iniciando sesión...")
    }

    return (
        <div className="min-h-screen flex justify-center items-center bg-gray-100">

            <Card>
                <div className="text-center mb-6">

                    <h1 className="text-2xl font-bold">Gestor de Tareas</h1>

                    <p className="text-lg text-gray-500 mt-2">Iniciar sesión</p>

                </div>
                
                <Input type="email" placeholder="Correo electrónico" />

                <Input type="password" placeholder="Contraseña" />

                <Button texto="Iniciar Sesión" onClick={iniciarSesion} />
            </Card>

        </div>
    )
}

export default LoginPage;