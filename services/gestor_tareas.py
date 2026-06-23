import json
import os
from models.tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.ruta_json = os.path.join("data", "tareas.json")
        self.cargar_tareas()

    def guardar_tareas(self):
        os.makedirs("data", exist_ok=True)
        lista_diccionario = [tarea.to_dict() for tarea in self.tareas]

        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionario, archivo, indent=4, ensure_ascii=False)
        print("[Sistema] Datos guardados en tareas.json")
    
    def cargar_tareas(self):
        if os.path.exists(self.ruta_json):
            with open(self.ruta_json, "r", encoding="utf-8") as archivo:
                lista_diccionarios = json.load(archivo)
            self.tareas = [
                    Tarea(d["titulo"], d["estado"]) for d in lista_diccionarios
                ]
            print("[Sistema] Datos cargados desde tareas.json")
        else:
            self.tareas = []
            print("[Sistema] No se encontraron datos previos, comenzando con una lista vacia")

    def agregar_tarea(self):
        titulo = input("Ingrese el titulo de la tarea: ")
        nueva_tarea = Tarea(titulo)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada")
        self.guardar_tareas()

    def ver_tareas(self):
        print("Tareas:")
        if not self.tareas:
            print("No hay tareas pendientes")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea.titulo} - {tarea.estado}")

    def completar_tarea(self):
        if not self.tareas:
            print("No hay tareas pendientes")
            return

        indice = int(input("Ingrese el numero de la tarea a completar: "))
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice -1].completar()
            print("Tarea marcada como completada")
            self.guardar_tareas()
        else:
            print("Tarea no encontrada")
        
    def eliminar_tarea(self):
        if not self.tareas:
            print("No hay tareas pendientes")
            return
        
        indice = int(input("Ingrese el numero de la tarea a eliminar: "))
        if 1 <= indice <= len(self.tareas):
            self.tareas.pop(indice -1)
            print("Tarea eliminada")
            self.guardar_tareas()
        else:
            print("Tarea no encontrada")