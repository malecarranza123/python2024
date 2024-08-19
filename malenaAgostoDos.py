# Diseñar un programa que permita al usuario gestionar una lista de tareas pendientes.

tareas = {}

while True:
         print( '''
          #############################################
          #     1 - Añadir una tarea                  #
          #     2 - Ver todas las tareas              #
          #     3 - Marcar una tarea como completada  #
          #     4 - Salir                             #
          ############################################# ''')

         opcion = int(input("Ingrese el número de la opción que desea realizar: "))

         if opcion == 1:
            titulo = input("Ingrese el titulo de la tarea: ")
            tarea = input("Ingrese la tarea: ")
            tareas[titulo] = tarea
            print("Tarea agregada.")
         
         elif opcion == 2:
           if tareas:
             print("Lista de tareas:")
             for titulo, tarea in tareas.items(): 
               print(f"Título: {titulo}, Tarea: {tarea}")
           else:
            print("La lista de tareas está vacía.")

         elif opcion == 3:
           if tareas == {}:
              print("no tienes tareas guardadas")
           else:
            titulo = input("Ingrese el titulo de la tarea que ya completó: ")
            if titulo in tareas:
             del tareas[titulo]
             print("Tarea completada.")
         
         elif opcion == 4:
            break
         
         else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

print("chau, gracias por usar este programa :D")