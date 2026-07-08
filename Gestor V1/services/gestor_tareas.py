from data.database import(
    db_obtener_tareas,
    db_agregar_tarea,
    db_eliminar_tarea,
    db_actualizar_tarea,
    db_obtener_tarea_por_id
)

class GestorTareas:
    def agregar_tarea(self):
        titulo = input("Ingrese el titulo de la tarea: ")
        db_agregar_tarea(titulo, "Pendiente")
        print("Tarea agregada")

    def ver_tareas(self):
        tareas = db_obtener_tareas()
        if not tareas:
            print("No hay tareas pendientes")
            return
        
        for tarea in tareas:
            print(
                f"ID: {tarea[0]} | "
                f"Titulo: {tarea[1]} |"
                f"Estado: {tarea[2]}"
            )

    def obtener_tarea_por_id(self):
        id_tarea = int(input("Ingrese el ID de la tarea: "))
        tarea = db_obtener_tarea_por_id(id_tarea)
        if tarea:
            print(
                f"ID: {tarea[0]} | "
                f"Titulo: {tarea[1]} |"
                f"Estado: {tarea[2]}"
            )
        else:
            print("Tarea no encontrada")
    
    def completar_tarea(self):
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        
        db_actualizar_tarea(id_tarea, "Completada")
        
        print("Tarea completada")
        
    def eliminar_tarea(self):       
        id_tarea = int(input("Ingrese el numero de la tarea a eliminar: "))
        
        db_eliminar_tarea(id_tarea)
        
        print("Tarea eliminada")