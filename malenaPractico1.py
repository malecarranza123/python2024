print("este programa devuelve los números pares: ")
numeros_pares = []
for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
print("Los números pares ingresados son:", numeros_pares)