import sqlite3

class Materia:
    #Método constructor
    def __init__(self, id_materia, nombre, curso, descripcion, horario):
        self.id_materia=id_materia
        self.nombre=nombre
        self.curso=curso
        self.descripcion=descripcion
        self.horario=horario

    def guardar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar
         
         #Ejecutar una consulta SQL para insertar los datos de la materia
        c.execute('INSERT INTO Materias (id_materia, nombre, curso, descripcion, horario) VALUES (?, ?, ?)', 
                    (self.id_materia, self.nombre, self.curso, self.descripcion, self.horario))
        
        conn.commit() #Guardar los cambios
        conn.close() #Cerrar la conexión a la base de datos

    @staticmethod #Metodo estático, no necesita que le pases ningún argumento
    def consulta_materias():
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor()

        c.execute('SELECT * from Materias') #Ejecutar una consulta SQL para selecsionar todos los registros de la tabla materias

        materias=c.fetchall() #Obtener todos los registros encontrados
        conn.close()

        return materias #Devolver la lista de materias    