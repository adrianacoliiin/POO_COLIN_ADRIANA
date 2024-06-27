class Estudiante():  #Aqui se crea la clase
    def __init__(self, nombre, edad, semestre):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
        self.matricula = None
    
    #Definicion de métodos de la clase
    def estudiar(self):
        print("Estudiando...")

    def participar(self):
        print("Participando...")

    def asignar_matricula(self, matricula):
        self.matricula = matricula

    def hablar(self):
        print("bla, bla, bla...")
        if self.matricula:
            print(f'La matricula del estudiante es {self.matricula.matricula}')


class Maestro():
    def __init__(self, nombre, escuela):
        self.nombre = nombre
        self.escuela = escuela
        self.materias = []
        self.alumnos = []

    def registrar_materias(self):
        materia = input("Ingresa la materia a agregar: ")
        self.materias.append(materia)

    def agregar_alumnos(self, estudiante):
        self.alumnos.append(estudiante)
        print(f"{estudiante.nombre} es alumno de {self.nombre}")
    
    def enseñar(self):
        print(f"{self.nombre} enseña {self.materias} a sus alumnos")

    def nombrar_lista(self):
        for alumno in self.alumnos:
            print(alumno.nombre)

class Salon():
    def __init__(self, numero):
        self.numero = numero
        self.maestros_ocupantes = []

    def registrar_maestros(self, maestro):
        self.maestros_ocupantes.append(maestro)
        print(f'{maestro.nombre}, esta enseñando en el salon {self.numero}')
 
    def listar_maestros(self):
        print(f'Los maestros que enseñaron en el salon {self.numero}: ')
        for maestro in self.maestros_ocupantes:
            print(maestro.nombre)

class Matricula():
    def __init__(self, matricula):
        self.matricula = matricula

    def hablar(self):
        print(f'La matrícula del alumno es {self.matricula}')

class EstudianteAtleta(Estudiante):
    def __init__(self, nombre, edad, semestre, deporte):
        super().__init__(nombre, edad, semestre)
        self.deporte = deporte

    def describir(self):
        super().hablar()
        print(f'Además de estudiar practico {self.deporte}')



#Creación de objetos de clase estudiante
estudiante_1 = Estudiante("Miguel", 19, "2do")
estudiante_2 = Estudiante("Adriana", 18, "3ro")
maestra = Maestro("Ana", "UTD")
maestro = Maestro("Orrico", "UTD")
salon_1 = Salon("C11")
salon_2 = Salon("E09")
estudiante_atleta = EstudianteAtleta("Mich", 18, "3ro", "softball")
estudiante_atleta.describir()

#matricula_1 = Matricula("12345678")
#matricula_2 = Matricula("87654321")

#estudiante_1.asignar_matricula(matricula_1)
#estudiante_1.hablar()

#Prueba de atributos del objeto 1
"""print(estudiante_1.nombre)
print(estudiante_1.edad)
print(estudiante_1.semestre)

#Prueba de atributos del objeto 2
print(estudiante_2.nombre)
print(estudiante_2.edad)
print(estudiante_2.semestre)

#Pruebas de los métodos de clase Estudiante
estudiante_1.estudiar()
estudiante_1.participar()

estudiante_2.estudiar()
estudiante_2.participar()

estudiante_1.hablar()
estudiante_2.hablar()

print(f"El nombre de la maestra es: {maestra.nombre}")
print(f"La maestra trabaja en {maestra.escuela}")

#Prueba de los métodos de clase Maestro
#maestra.registrar_materias()
maestra.agregar_alumnos(estudiante_1)
maestra.agregar_alumnos(estudiante_2)
maestra.enseñar()
maestra.nombrar_lista()
salon_1.registrar_maestros(maestra)
salon_1.registrar_maestros(maestro)
salon_1.listar_maestros()"""