import sqlite3
from ClsEstudiante import Estudiante
from ClsProfesor import Profesor
from ClsMateria import Materia
from ClsCalificacion import Calificacion

#función para conectar a la base de datos de sqlite3
def conectar_db():
    conn=sqlite3.connect('escolar.db')
    return conn

#funcion principal para ejecutar el programa
def main():
    conn=conectar_db() #conexión con la base de datos
    cursor=conn.cursor() #cursor para interactuar

    while True: 
        print("\n--- Sistema Escolar ---")
        print( '''
        #############################################
        #     1. Gestionar Estudiantes              #
        #     2. Gestionar Profesores               #
        #     3. Gestionar Materias                 #
        #     4. Gestionar Calificaciones           #
        #     5. Salir                              #
        ############################################# ''')
        
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            menu_estudiantes()
        elif opcion == 2:
            menu_profesores()
        elif opcion == 3:
            menu_materias()
        elif opcion == 4:
            menu_calificaciones()
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    conn.close() #cierra la conexión con la base de datos al salir del programa

def menu_estudiantes():
    while True:
        print("\n--- Gestión de Estudiantes ---")
        print( '''
        #############################################
        #     1. Agregar Estudiante                 #
        #     2. Consultar Estudiantes              #
        #     3. Modificar Estudiante               #
        #     4. Eliminar Estudiante                #
        #     5. Volver al Menú Principal           #
        ############################################# ''')

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("\n--- Agregar Estudiante ---")
            legajo_id = input("Legajo ID: ")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: ")) 
            fecha_nacimiento = input("Fecha de Nacimiento: ")
            curso = input("Curso: ")
            estado = input("Estado: ")
            email = input("Email: ")

            estudiante = Estudiante(legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email)
            estudiante.guardar() #guarda los datos cargados
            print("Estudiante agregado exitosamente.") 
        
        elif opcion == 2:
            Estudiante.mostrar_todos(conn)
            
        elif opcion == 3:
            print("\n--- Modificar Estudiante ---")
            legajo_id = input("Legajo ID del estudiante a modificar: ")
            dni = input("Nuevo DNI: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            edad = int(input("Nueva Edad: "))
            fecha_nacimiento = input("Nueva Fecha de Nacimiento: ")
            curso = input("Nuevo Curso: ")
            estado = input("Nuevo Estado: ")
            email = input("Nuevo Email: ")

            estudiante = Estudiante(legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email)
            estudiante.modificar() #guarda la modificación
            print("Estudiante modificado exitosamente.")
            
        elif opcion == 4:
            print("\n--- Eliminar Estudiante ---")
            legajo_id = input("Legajo ID del estudiante a eliminar: ")
            Estudiante.eliminar(legajo_id) #elimina al estudiante por si legajo_id
            print("Estudiante eliminado exitosamente.")
            
        elif opcion == 5:
            break #sale de menu_estudiantes
    
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_profesores():
    while True:
        print("--- Gestión de Profesores ---")
        print( '''
        #############################################
        #     1. Agregar Profesor                   #
        #     2. Consultar Profesores               #
        #     3. Modificar Profesor                 #
        #     4. Eliminar Profesor                  #
        #     5. Volver al Menú Principal           #
        ############################################# ''')

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("\n--- Agregar Profesor ---")
            dni_id = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            curso = input("Curso: ")
            estado = input("Estado: ")
            email = input("Email: ")

            profesor = Profesor(dni_id, nombre, apellido, curso, estado, email)
            profesor.guardar() #guarda los datos cargados
            print("Profesor agregado exitosamente.")

        elif opcion == 2:
            Profesor.mostrar_todos(conn)

        elif opcion == 3:
            print("\n--- Modificar Profesor ---")
            dni_id = input("DNI del profesor a modificar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            curso = input("Nuevo Curso: ")
            estado = input("Nuevo Estado: ")
            email = input("Nuevo Email: ")

            profesor = Profesor(dni_id, nombre, apellido, curso, estado, email)
            profesor.modificar() #guarda la modificación
            print("Profesor modificado exitosamente.")

        elif opcion == 4:
            print("\n--- Eliminar Profesor ---")
            dni_id = input("DNI del estudiante a eliminar: ")
            Profesor.eliminar(dni_id) #elimina al profesor por su dni_id
            print("Profesor eliminado exitosamente.")

        elif opcion == 5:
            break #sale de menu_profesores

def menu_materias():
    while True:
        print("\n--- Gestión de Materias ---")
        print( '''
        #############################################
        #     1. Agregar Materia                    #
        #     2. Consultar Materias                 #
        #     3. Modificar Materia                  #
        #     4. Eliminar Materia                   #
        #     5. Volver al Menú Principal           #
        ############################################# ''')

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("\n--- Agregar Materia ---")
            id_materia=input("ID de la materia: ")
            nombre=input("Nombre: ")
            curso=input("Curso: ")
            descripcion=input("Descripcion: ")
            horario=input("Horario: ")

            materia = Materia(id_materia, nombre, curso, descripcion, horario)
            materia.guardar() #guarda los datos cargados 
            print("Materia agregada exitosamente.") 
        
        elif opcion == 2:
            Materia.mostrar_todos(conn)
            
        elif opcion == 3:
            print("\n--- Modificar Materia ---")
            id_materia=input("ID de la materia a modificar: ")
            nombre=input("Nuevo Nombre: ")
            curso=input("Nuevo Curso: ")
            descripcion=input("Nueva Descripcion: ")
            horario=input("Nuevo Horario: ")

            materia = Materia(id_materia, nombre, curso, descripcion, horario)
            materia.modificar() #guarda la modificación
            print("Materia modificada exitosamente.")
            
        elif opcion == 4:
            print("\n--- Eliminar Materia ---")
            id_materia = input("ID de la materia a eliminar: ")
            Materia.eliminar(id_materia) #elimina la materia por el id_materia
            print("Materia eliminada exitosamente.")
            
        elif opcion == 5:
            break #sale de menu_materias
    
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_calificaciones():
     while True:
        print("\n--- Gestión de Calificaciones ---")
        print( '''
        #############################################
        #     1. Agregar Calificacion               #
        #     2. Consultar Calificaciones           #
        #     3. Modificar Calificacion             #
        #     4. Eliminar Calificacion              #
        #     5. Volver al Menú Principal           #
        ############################################# ''')

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("\n--- Agregar Calificacion ---")
            id_estudiante=input("ID del estudiante calificado: ")
            id_materia=input("ID de la materia: ")
            curso=input("Curso: ")
            nota=input("Nota: ")
            fecha=input("Fecha: ")

            calificacion = Calificacion(id_estudiante, id_materia, curso, nota, fecha)
            calificacion.guardar() #guarda los datos cargados
            print("Calificacion agregada exitosamente.") 
        
        elif opcion == 2:
            Calificacion.mostrar_todos(conn)
            
        elif opcion == 3:
            print("\n--- Modificar Materia ---")
            id_estudiante=input("ID del estudiante calificado: ")
            id_materia=input("ID de la materia: ")
            curso=input("Nuevo Curso: ")
            nota=input("Nueva Nota: ")
            fecha=input("Nueva Fecha: ")

            calificacion = Calificacion(id_estudiante, id_materia, curso, nota, fecha)
            calificacion.modificar() #guarda la modificación
            print("Calificacion modificada exitosamente.")
            
        elif opcion == 4:
            print("\n--- Eliminar Calificacion ---")
            id_materia = input("ID del estudiante calificado a eliminar: ")
            Calificacion.eliminar(id_estudiante) #elimina la calificación por el id del estudiante que tenia la calificación
            print("Calificacion eliminada exitosamente.")
            
        elif opcion == 5:
            break #sale de menu_calificaciones
    
        else:
            print("Opción no válida. Inténtalo de nuevo.")

#punto de entrada del programa
if __name__ == "__main__":
    main()        