import { obtenerToken } from "./tokenService"

const API = "http://127.0.0.1:8000"

export async function obtenerResumen() {
    const token = obtenerToken()

    console.log(obtenerToken())

    const respuesta = await fetch(`${API}/tareas/resumen`, {

        headers: {
            Authorization: `Bearer ${token}`
        
        }
    })

    if (!respuesta.ok) {

        console.log(await respuesta.json())

        throw new Error("Error al obtener el resumen")
    }

    return respuesta.json()
}