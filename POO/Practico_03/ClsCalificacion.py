import sqlite3

class Calificacion:
    #Método constructor
    def __init__(self, id_estudiante, id_materia, nota, fecha):
        self.id_estudiante=id_estudiante
        self.id_materia=id_materia
        self.nota=nota
        self.fecha=fecha
  
    def guardar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar
         
         #Ejecutar una consulta SQL para insertar los datos de la calificacion
        c.execute('INSERT INTO Calificaciones (id_estudiante, id_materia, nota, fecha) VALUES (?, ?, ?, ?)', 
                    (self.id_estudiante, self.id_materia, self.nota, self.fecha))
        
        conn.commit() #Guardar los cambios
        conn.close() #Cerrar la conexión a la base de datos

    @staticmethod #Metodo estático, no necesita que le pases ningún argumento
    def consulta_calificaciones():
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor()

        c.execute('SELECT * from Calificaciones') #Ejecutar una consulta SQL para selecsionar todos los registros de la tabla calificaciones

        calificaciones=c.fetchall() #Obtener todos los registros encontrados
        conn.close()

        return calificaciones #Devolver la lista de calificaciones

    def modificar(self):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Ejecutar una consulta SQL para actualizar los datos de la calificación
        c.execute('''
            UPDATE Calificaciones 
            SET nota = ?, fecha = ? 
            WHERE id_estudiante = ? AND id_materia = ?
        ''', (self.nota, self.fecha, self.id_estudiante, self.id_materia))

        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

    @staticmethod
    def eliminar(id_estudiante, id_materia):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Eliminar la calificación
        c.execute('DELETE FROM Calificaciones WHERE id_estudiante = ? AND id_materia = ?', (id_estudiante, id_materia))
        
        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos   