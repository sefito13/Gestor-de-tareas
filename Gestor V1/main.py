from services.gestor_tareas import GestorTareas

gestor = GestorTareas()

while True:
    print("\n")
    print("Seleccione una opcion:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tareas")
    print("5. Salir")
    print("\n")


    opcion = input("Opcion: ")
    if opcion == "1":
        gestor.agregar_tarea()
    elif opcion == "2":
        gestor.ver_tareas()
    elif opcion == "3":
        gestor.completar_tarea()
    elif opcion == "4":
        gestor.eliminar_tarea()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida")
    