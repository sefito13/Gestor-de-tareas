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

export async function obtenerTareas() {
    const token = obtenerToken()

    const respuesta = await fetch(`${API}/tareas`, {

        headers: {
            Authorization: `Bearer ${token}`
        }
    })

    if (!respuesta.ok) {

        throw new Error("Error al obtener las tareas")
    }

    return respuesta.json()
}

export async function crearTarea(titulo: string, estado: string) {

    const token = obtenerToken()

    const respuesta = await fetch(`${API}/tareas`, {
        
        method: "POST",

        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },

        body: JSON.stringify({
            titulo,
            estado
        })
    })

    if (!respuesta.ok) {
        throw new Error("Error al crear la tarea")
    }

    return await respuesta.json()
    
}