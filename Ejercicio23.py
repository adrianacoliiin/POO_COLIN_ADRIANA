class Estudiante():  #Aqui se crea la clase
    def __init__(self, nombre, edad, semestre):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
    
    #Definicion de métodos de la clase
    def estudiar(self):
        print("Estudiando...")

    def participar(self):
        print("Participando...")

    def hablar(self):
        print("bla, bla, bla...")
 
#Creación de objetos de clase estudiante
estudiante_1 = Estudiante("Miguel", 19, "2do")
estudiante_2 = Estudiante("Adriana", 18, "3ro")

#Prueba de atributos del objeto 1
print(estudiante_1.nombre)
print(estudiante_1.edad)
print(estudiante_1.semestre)

#Prueba de atributos del objeto 2
print(estudiante_2.nombre)
print(estudiante_2.edad)
print(estudiante_2.semestre)

#Pruebas de los métodos
estudiante_1.estudiar()
estudiante_1.participar()

estudiante_2.estudiar()
estudiante_2.participar()

estudiante_1.hablar()
estudiante_2.hablar()