export async function login(correo: string, password: string) {
    
    const response = await fetch("http://127.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            correo,
            password
        })
    })

    return await response.json()
}