import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escolares'
)

if connection.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

cursor = connection.cursor()


# S E L E C T 
cursor.execute("SELECT * FROM alumnos")
alumnos = cursor.fetchall()
print("Datos de la tabla 'alumnos':")
for alumno in alumnos:
    print(alumno)

# I N S E R T 
alumno_nuevo = ("Adriii", 18, "Cerquita", 1)
cursor.execute("INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)", alumno_nuevo)
connection.commit()
print("\nNuevo alumno insertado")

# U P D A T E 
cursor.execute("UPDATE alumnos SET edad = 19 WHERE nombre = 'Adriii'")
connection.commit()
print("\nEdad actualizada")

# D E L E T E 
cursor.execute("DELETE FROM alumnos WHERE nombre = 'Adriii'")
connection.commit()
print("\nAlumno eliminado")


cursor.close()
connection.close()