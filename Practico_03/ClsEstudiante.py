import sqlite3

class Estudiante:
    #Método constructor
    def __init__(self, nombre, edad, año_id):
        self.nombre=nombre
        self.edad=edad
        self.año_id=año_id

    #Método para guardar la información del estudiante en la db
    def guardar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar

        #Ejecutar una consulta SQL para insertar los datos del estudiante
        c.execute('INSERT INTO Estudiantes (nombre, edad, año_id) VALUES (?, ?, ?)', 
                    (self.nombre, self.edad, self.año_id))

        conn.commit() #Guardar los cambios
        conn.close() #Cerrar la conexión a la base de datos

    @staticmethod #Metodo estático, no necesita que le pases ningún argumento
    def consulta_estudiantes():
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor()

        c.execute('SELECT * from Estudiantes') #Ejecutar una consulta SQL para selecsionar todos los registros de la tabla estudiantes

        estudiantes=c.fetchall() #Obtener todos los registros encontrados
        conn.close()

        return estudiantes #Devolver la lista de estudiantes
