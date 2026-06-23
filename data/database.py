import sqlite3

conexion = sqlite3.connect('tareas.db')
cursor = conexion.cursor()

def obtener_tareas():
    cursor.execute("SELECT * FROM tareas")
    return cursor.fetchall()

def agregar_tarea(titulo, estado):
    cursor.execute(
        "INSERT INTO tareas (titulo, estado)" \
        "VALUES (?, ?)", 
        (titulo, estado))
    conexion.commit()

def eliminar_tarea(id):
    cursor.execute(
        "DELETE FROM tareas" \
        "WHERE id = ?", 
        (id,))
    conexion.commit()

def actualizar_tarea(id, estado):
    cursor.execute(
        "UPDATE tareas" \
        "SET estado = ?" \
        "WHERE id = ?", 
        (estado, id))
    conexion.commit()

def obtener_tarea_por_id(id):
    cursor.execute(
        "SELECT * FROM tareas" \
        "WHERE id = ?"
    )