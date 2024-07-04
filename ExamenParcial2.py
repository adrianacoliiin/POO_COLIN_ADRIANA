# C R E A C I Ó N   D E   L A S   C L A S E S:
class Estudiante():  
    def __init__(self, nombre, edad, semestre):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
        self.matricula = None
    
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

    def aprobar(self, calificacion):
        print(f'El estudiante {self.nombre}, tuvo una nota de {calificacion.nota}')
        if calificacion.nota >= 80:
            print ("El estudiante aprobó")
        else:
            print("El estudiante reprobó")

    def justificar_falta(self, justificante):
        if justificante:
            print(f'{self.nombre} justificó una falta')



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

class Calificacion():
    def __init__(self, nota):
        self.nota = nota

    def anunciar(self):
        print(f'La nota final del alunmo es: {self.nota}')

class MaestoTitular(Maestro):
    def __init__(self, nombre, escuela, grupo, cubiculo):
        super().__init__(nombre, escuela)
        self.grupo = grupo
        self.cubiculo = cubiculo
        self.alumnos = []

    def agregar_alumnos(self, estudiante):
        return super().agregar_alumnos(estudiante)

    def dar_tutorias(self):
        print(f'{self.nombre} le esta dando tutorias a los alumnos:')
        for alumno in self.alumnos:
            print(alumno.nombre)

class Justificante():
    def __init__(self, fecha, motivo, maestro_titular):
        self.fecha = fecha
        self.motivo = motivo
        self.maestro_titular = maestro_titular
    
    def describir(self):
        print(f'Con fecha de: {self.fecha}')
        print(f'Con fecha de: {self.motivo}')
        print(f'Con fecha de: {self.maestro_titular}')
        


# E J E C U C I Ó N   D E L    C Ó D I G O : 
while True:
    print('\nM E N Ú    P R I N C I P A L: ')
    print('1. Clase Estudiante') # EstudianteAtleta, Matricula, Calificación y Justificante dentro de esta clase 
    print('2. Clase Maestro') # MaestroTitular también participa dentro de esta clase
    print('3. Clase Salon')
    print('4. Salir')
  

    res = int(input('Selecciona la opción a la que deseas ingresar: \n'))

    if res == 1:
        while True: 
            print('\nC L A S E    E S T U D I A N T E: ')
            print('1. Objetos de "Estudiante": ') 
            print('2. Objetos de "EstudianteAtleta": ') 
            print('3. Objetos de "Matricula": ')
            print('4. Objetos de "Calificación": ')
            print('5. Objetos de "Justificante": ')
            print('6. Menú Principal')
            
            ans = int(input('Selecciona el numero correspondiente a la seccion que deseas ingresar:'))
            
            # Creación de todos los objetos relacionados a clase Estudiante
            estudiante_1 = Estudiante("Miguel", 19, "2do")
            estudiante_2 = Estudiante("Adriana", 18, "3ro")
            estudiante_atleta_1 = EstudianteAtleta("Mich", 18, "3ro", "softball")
            estudiante_atleta_2 = EstudianteAtleta("Johana", 18, "2do", "basketball")
            matricula_1 = Matricula("12345678")
            matricula_2 = Matricula("87654321")
            calif_1 = Calificacion(94)
            calif_2 = Calificacion(50)
            just_1 = Justificante("23/jun/2024", "Motivos Familiares", "Bravo")
            just_2 = Justificante("07/abr/2024", "Cita Médica", "Isaac")

            if ans == 1:
                print('\nMETODOS DE LA CLASE ESTUDIANTE: ')
                
                print('Objeto 1: ')
                estudiante_1.estudiar()      
                estudiante_1.participar()
                estudiante_1.asignar_matricula(matricula_1)
                estudiante_1.hablar()
                estudiante_1.aprobar(calif_1)
                estudiante_1.justificar_falta(just_1)
                
                print('Objeto 2: ')
                estudiante_2.estudiar()
                estudiante_2.participar()
                estudiante_2.asignar_matricula(matricula_2)
                estudiante_2.hablar()
                estudiante_2.aprobar(calif_2)
                estudiante_2.justificar_falta(just_2)

            elif ans == 2:
                print('\nMETODOS DE LA CLASE ESTUDIANTE ATLETA: ')
                
                print('Objeto 1: ')
                estudiante_atleta_1.describir()
                
                print('Objeto 2: ')
                estudiante_atleta_2.describir()

            elif ans == 3:
                print('\nMÉTODOS DE LA CLASE MATRICULA: ')
                print('Objeto 1: ')
                matricula_1.hablar()

                print('Objeto 2: ')
                matricula_2.hablar()

            elif ans == 4:
                print('\nMETODOS DE LA CLASE CALIFICACION: ')
                print('Objeto 1: ')
                calif_1.anunciar()

                print('Objeto 2: ')
                calif_2.anunciar()

            elif ans == 5:
                print('\nMETODOS DE LA CLASE JUSTIFICANTE: ')
                print('Objeto 1: ')
                just_1.describir()
                
                print('Objeto 2: ')
                just_2.describir()

            elif ans == 6:
                print('\nVolviendo al menú principal\n')
                break

            else:
                print('\nValor ingresado no válido, intenta de nuevo')


    elif res == 2:
        while True:
            print('\nC L A S E    M A E S T R O: ')
            print('1. Objetos de "Maestro": ') 
            print('2. Objetos de "MaestroTitular": ') 
            print('3. Salir')

            ans = int(input('Selecciona el numero correspondiente a la seccion que deseas ingresar:'))

            # Objetos relacionados a la clase Maestro
            maestra = Maestro("Ana", "UTD")
            maestro = Maestro("Orrico", "UTD")
            maestro_titu_1 = MaestoTitular("Bravo", "UTD", "2-A", "Cub-03")
            maestro_titu_2 = MaestoTitular("Isaac", "UTD", "4-B", "Cub-11")
            estudiante_1 = Estudiante("Miguel", 19, "2do")
            estudiante_2 = Estudiante("Adriana", 18, "3ro")

            if ans == 1:
                print('\nMÉTODOS DE LA CLASE MAESTRO: ')
                print('Objeto 1: ')
                maestra.registrar_materias()
                maestra.agregar_alumnos(estudiante_1)
                maestra.agregar_alumnos(estudiante_2)
                maestra.enseñar()
                maestra.nombrar_lista()

                print('Objeto 2: ')
                maestro.registrar_materias()
                maestro.agregar_alumnos(estudiante_1)
                maestro.agregar_alumnos(estudiante_2)
                maestro.enseñar()
                maestro.nombrar_lista()

            elif ans == 2:
                print('\nMÉTODOS DE LA CLASE MAESTRO TITULAR: ')
                print('Objeto 1: ')
                maestro_titu_1.agregar_alumnos(estudiante_1)
                maestro_titu_1.agregar_alumnos(estudiante_2)
                maestro_titu_1.dar_tutorias()

                print('Objeto 2: ')
                maestro_titu_2.agregar_alumnos(estudiante_1)
                maestro_titu_2.agregar_alumnos(estudiante_2)
                maestro_titu_2.dar_tutorias()

            elif ans == 3:
                print('\nVolviendo al menú principal\n')
                break

            else:
                print('\nValor no válido, intentalo de nuevo')

    elif res == 3:
        while True:
            print('\nC L A S E    S A L O N: ')
            print('1. Objetos de "Salon": ') 
            print('2. Salir')

            ans = int(input('Selecciona el numero correspondiente a la seccion que deseas ingresar:'))

            # Objetos relacionados a la clase Salon
            salon_1 = Salon("C11")
            salon_2 = Salon("E09")

            if ans == 1:
                print('\nMÉTODOS DE LA CLASE SALON: ')
                print('Objeto 1: ')
                salon_1.registrar_maestros(maestra)
                salon_1.registrar_maestros(maestro_titu_1)
                salon_1.listar_maestros()

                print('Objeto 2: ')
                salon_2.registrar_maestros(maestro)
                salon_2.registrar_maestros(maestro_titu_2)
                salon_2.listar_maestros()

            elif ans == 2:
                print('\nVolviendo a menú principal')
                break

            else:
                print('\nValor ingresado no válido, intenta de nuevo')

    elif res == 4:
        print('\nHaz salido del programa :D\n')
        break

    else:
        print('\nEl valor ingresado no es válido, intenta de nuevo')