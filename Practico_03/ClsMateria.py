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
        c.execute('INSERT INTO Materias (id_materia, nombre, curso, descripcion, horario) VALUES (?, ?, ?, ?, ?)', 
                    (self.id_materia, self.nombre, self.curso, self.descripcion, self.horario))
        
        conn.commit() #Guardar los cambios
        conn.close() #Cerrar la conexión a la base de datos

    @staticmethod #Metodo estático, no necesita que le pases ningún argumento
    def mostrar_todas():
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor()

        c.execute('SELECT * from Materias') #Ejecutar una consulta SQL para selecsionar todos los registros de la tabla materias

        materias=c.fetchall() #Obtener todos los registros encontrados
        conn.close()

        return materias #Devolver la lista de materias    

    def modificar(self):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Actualizar los datos de la materia
        c.execute('''
            UPDATE Materias 
            SET nombre = ?, curso = ?, descripcion = ?, horario = ? 
            WHERE id_materia = ?
        ''', (self.nombre, self.curso, self.descripcion, self.horario, self.id_materia))

        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

    @staticmethod
    def eliminar(id_materia):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Eliminar la materia
        c.execute('DELETE FROM Materias WHERE id_materia = ?', (id_materia,))
        
        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos