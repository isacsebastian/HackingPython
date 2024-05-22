print("Tareas CRUD 🤖")


tareas = []
while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        tarea = input("Escribe la tarea a agregar: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
    elif opcion == '2':
        if not tareas:
            print("no hay tareas para eliminar.")
        else:
            for idx, tarea in enumerate(tareas):
                print(f"{idx + 1}. {tarea}")
            tarea_num = int(input("escoger número de la tarea a eliminar: "))
            if 1 <= tarea_num <= len(tareas):
                tarea_eliminada = tareas.pop(tarea_num - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número de tarea inválido.")
    elif opcion == '3':
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for idx, tarea in enumerate(tareas):
                print(f"{idx + 1}. {tarea}")
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida, por favor intenta de nuevo.")
