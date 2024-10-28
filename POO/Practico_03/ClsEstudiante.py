import sqlite3

class Estudiante:
    #Método constructor
    def __init__(self, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email):
        self.legajo_id=legajo_id
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.fecha_nacimiento=fecha_nacimiento
        self.curso=curso
        self.estado=estado
        self.email=email

    #Método para guardar la información del estudiante en la db
    def guardar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar

        #Ejecutar una consulta SQL para insertar los datos del estudiante
        c.execute('INSERT INTO Estudiantes (legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                    (self.legajo_id, self.dni, self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email))

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

    def modificar(self):
        conn=sqlite3.connect('escolar.db') #Conectar la base de datos 'escolar.db'
        c=conn.cursor() #Cursor para interactuar
        
        # Actualizar los datos del estudiante
        c.execute('''
            UPDATE Estudiantes 
            SET dni = ?, nombre = ?, apellido = ?, edad = ?, fecha_nacimiento = ?, curso = ?, estado = ?, email = ? 
            WHERE legajo_id = ?
        ''', (self.dni, self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email, self.legajo_id))

    @staticmethod
    def eliminar(id):
        conn = sqlite3.connect('escolar.db')  # Conectar la base de datos 'escolar.db'
        c = conn.cursor()  # Cursor para interactuar

        # Eliminar los datos del estudiante
        c.execute('DELETE FROM Estudiantes WHERE legajo_id = ?', (id,))
        conn.commit()  # Guardar los cambios
        conn.close()  # Cerrar la conexión a la base de datos
        
    