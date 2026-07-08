import sqlite3

conexion = sqlite3.connect('tareas.db')
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")

conexion.commit()

def db_obtener_tareas():
    cursor.execute("SELECT * FROM tareas")
    return cursor.fetchall()

def db_agregar_tarea(titulo, estado):
    cursor.execute(
        "INSERT INTO tareas (titulo, estado) " \
        "VALUES (?, ?)", 
        (titulo, estado)
    )
    conexion.commit()

def db_eliminar_tarea(id):
    cursor.execute(
        "DELETE FROM tareas " \
        "WHERE id = ?", 
        (id,)
    )
    conexion.commit()

def db_actualizar_tarea(id, estado):
    cursor.execute(
        "UPDATE tareas " \
        "SET estado = ?" \
        "WHERE id = ?", 
        (estado, id))
    conexion.commit()

def db_obtener_tarea_por_id(id):
    cursor.execute(
        "SELECT * FROM tareas " \
        "WHERE id = ?",
        (id,)
    )
    return cursor.fetchone()