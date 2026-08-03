const TOKEN_KEY = "access_token"

export function guardarToken(token: string) {
    localStorage.setItem(TOKEN_KEY, token)
}

export function obtenerToken() {
    return localStorage.getItem(TOKEN_KEY)
}

export function eliminarToken() {
    localStorage.removeItem(TOKEN_KEY)
}

export function estaAutenticado() {
    return obtenerToken() !== null
}