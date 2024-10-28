import sqlite3

class Profesor:
    #Método constructor
    def __init__(self, dni_id, nombre, apellido, curso, estado, email):
        self.dni_id=dni_id
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso
        self.estado=estado
        self.email=email

    def guardar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar
         
         #Ejecutar una consulta SQL para insertar los datos del profesor
        c.execute('INSERT INTO Profesores (dni_id, nombre, apellido, curso, estado, email) VALUES (?, ?, ?, ?, ?, ?)', 
                    (self.dni_id, self.nombre, self.apellido, self.curso, self.estado, self.email))
        
        conn.commit() #Guardar los cambios
        conn.close() #Cerrar la conexión a la base de datos

    @staticmethod #Metodo estático, no necesita que le pases ningún argumento
    def consulta_profesores():
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor()

        c.execute('SELECT * from Profesores') #Ejecutar una consulta SQL para selecsionar todos los registros de la tabla profesores

        profesores=c.fetchall() #Obtener todos los registros encontrados
        conn.close()

        return profesores #Devolver la lista de estudiantes    

    def modificar(self):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Actualizar los datos del profesor
        c.execute('''
            UPDATE Profesores
            SET nombre = ?, apellido = ?, curso = ?, estado = ?, email = ?
            WHERE dni_id = ?
        ''', (self.nombre, self.apellido, self.curso, self.estado, self.email, self.dni_id))

        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos

    @staticmethod
    def eliminar(dni_id):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()

        # Eliminar los datos del profesor
        c.execute('DELETE FROM Profesores WHERE dni_id = ?', (dni_id,))
        
        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos
   