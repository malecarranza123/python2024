from Personaje_clase import Personaje

cantidadPersonaje=0
personajes=[]
while True:
    print( '''
        #############################################
        #     1 - Añadir un personaje               #
        #     2 - Jugar                             #
        #     3 - Salir                             #
        ############################################# ''')

    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    if opcion == 1:    
        #nombre,altura,velocidad,resistencia,fuerza    
        print("Ingrese los datos del personaje:")
        nombre = input("Nombre: ")
        altura = int(input("Altura(en cm): "))
        velocidad = int(input("Velocidad(0/100): "))
        resistencia = int(input("Resistencia(0/100): "))
        fuerza = int(input("Fuerza(0/100): "))

        nuevo_personaje=Personaje(nombre,altura,velocidad,resistencia,fuerza) 
        personajes.append(nuevo_personaje) #Guarda el personaje

        cantidadPersonaje+=1
        print(f"El personaje {nuevo_personaje} ha sido creado con éxito")
        print(f"Cantidad de personajes creados: {cantidadPersonaje}")

    elif opcion == 2:
        if cantidadPersonaje<=1:
            print("Se necesitan 2 personajes para jugar")
        else:
            print("Iniciando pelea con los siguientes personajes: ")
            for personaje in personajes:
                print(f"- {personaje.nombre}")
                
            atacante = personajes[0]  # Personaje 1
            defensor = personajes[1]  # Personaje 2
            atacante.atacar(defensor)

    elif opcion == 3: #Sale del programa
        print("chau")
        break

print("hasta la próxima")


         