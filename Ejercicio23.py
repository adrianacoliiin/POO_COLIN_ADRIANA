class Estudiante():
    def __init__(self, nombre, edad, semestre):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
    
    def estudiar(self):
        print("Estudiando...")

    def participar(self):
        print("Participando...")

    def hablar(self):
        print("bla, bla, bla...")

estudiante_1 = Estudiante("Miguel", 19, "2do")
estudiante_2 = Estudiante("Adriana", 18, "3ro")

print(estudiante_1.nombre)
print(estudiante_1.edad)
print(estudiante_1.semestre)

print(estudiante_2.nombre)
print(estudiante_2.edad)
print(estudiante_2.semestre)

estudiante_1.estudiar()
estudiante_1.participar()

estudiante_2.estudiar()
estudiante_2.participar()

estudiante_1.hablar()
estudiante_2.hablar()