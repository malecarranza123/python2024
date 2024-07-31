print("este programa cuenta y devuelve las vocales de una frase/palabra")
frase = input("Ingrese una frase/palabra: ")
a=0
e=0
i=0
o=0
u=0
for letra in frase:
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1
print(f"A: {a}")
print(f"E: {e}")
print(f"I: {i}")
print(f"O: {o}")
print(f"U: {u}")