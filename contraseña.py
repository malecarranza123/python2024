contrasena=input("ingrese su contraseña: ")
listaContrasena=[]

for i in contrasena:
    print("*", end="")
    listaContrasena.append(i)
print()
print(listaContrasena)    
listaContrasena.pop(2)
print(listaContrasena)