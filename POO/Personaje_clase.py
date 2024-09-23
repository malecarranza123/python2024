import random

class Personaje:
    estado=True
    vida=100

    def __init__(self,nombre, altura, velocidad, resistencia, fuerza):
        self.nombre=nombre
        self.altura=altura
        self.velocidad=velocidad
        self.resistencia=resistencia
        self.fuerza=fuerza
        self.estado=Personaje.estado
        self.vida=Personaje.vida

    def atacar(self, otro_personaje):
        if self.estado: #si estoy vivo
            danio=self.fuerza-(otro_personaje.resistencia)
            danio=max(0,danio)#no puede ser negativo
            print(f"{self.nombfre} ataca a {otro_personaje.nombre} causando {danio} daño")
            otro_personaje.recibir_dano(danio)#llamando al metodo recibir_dano y la cantidad es = danio
        else:
            print(f"{self.nombre} está muerto y no puede atacar")
#"cantidad" va a tomar el valor deL DANIO

    def recibir_dano(self, cantidad):
        if self.estado:
            self.vida-=cantidad
            print(f"{self.nombre} recibe {cantidad} de daño. Vida restante es {self.vida}")
            if self.vida<=0:
                self.vida=0
                print(f"{self.nombre} ha muerto")
            else:
                print(f"{self.nombre} ya está muerto")    
        
        self.resistencia -= cantidad
        if self.resistencia <= 0:
            self.resistencia = 0
            self.estado = False
            print(f"{self.nombre} ha muerto.")

    def mostrar_info(self):
        estado = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Vida: {self.vida}")
        print(f"Estado: {estado}")
