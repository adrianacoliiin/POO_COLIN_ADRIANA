import os

# ABSTRACCCIÓN
def abstraccion():
    print('\nA B S T R A C C I Ó N')
    print('Este principio consiste en identificar y definir solo las características esenciales de un objeto, ignorando los detalles irrelevantes para el contexto en el que se utiliza. La abstracción permite simplificar la complejidad del mundo real en modelos manejables y comprensibles en el software.')

# ENCAPSULAMIENTO
def encapsulamiento():
    print('\nE N C A P S U L A M I E N T O')
    print('Se refiere a la práctica de agrupar los datos (atributos) y los métodos (funciones) que operan sobre esos datos en una sola unidad, conocida como clase. Además, el encapsulamiento oculta la implementación interna del objeto, exponiendo solo las interfaces necesarias para interactuar con él. Esto protege los datos de accesos no autorizados y posibles modificaciones indebidas.')

# HERENCIA
def herencia():
    print('\nH E R E N C I A')
    print('La herencia permite crear nuevas clases basadas en clases existentes. Una clase "hija" hereda los atributos y métodos de una clase "padre", lo que facilita la reutilización del código y la creación de jerarquías de clases. Además, la herencia permite extender o modificar el comportamiento de la clase padre en la clase hija.')

# POLIMORFISMO
def polimorfismo():
    print('\nP O L I M O R F I S M O')
    print('Este principio permite que una misma operación o método pueda comportarse de diferentes maneras según el objeto o contexto en el que se aplique. El polimorfismo se logra, por ejemplo, mediante la sobrescritura de métodos en clases derivadas o la implementación de interfaces, permitiendo que diferentes objetos respondan de manera adecuada a la misma acción.')


# MENÚ INTERACTIVO:
def menu_principal():
    while True:
        print('\nM E N Ú  I N T E R A C T I V O :')
        print('1. Ejemplo de Abstracción')
        print('2. Ejemplo de Encapsulamiento')
        print('3. Ejemplo de Herencia')
        print('4. Ejemplo de Polimorfismo')
        print('5. Salir del programa')

        res = int(input('Ingresa el número que corresponda a la opcion que deseas: \n'))

        if res == 1:
            abstraccion()
        elif res == 2:
            encapsulamiento()
        elif res == 3:
            herencia()
        elif res == 4:
            polimorfismo()
        elif res == 5:
            print('\nHaz salido del programa :D')
            break
        else:
            print('Valor no válido ingresa un valor válido')

menu_principal()