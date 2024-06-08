def sumar():
    print("S U M A")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    suma = a + b
    print(suma) 
    print() 


def restar():
    print("R E S T A")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    resta = a - b
    print(resta) 
    print() 


def multiplicar():
    print("M U L T I P L I C A C I Ó N")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    mul = a * b
    print(mul) 
    print() 


def dividir():
    print("D I V I S I Ó N")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    divi = a / b
    print(divi) 
    print() 


while True:
    print("""C A L C U L A D O R A"
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir""")

    operacion = int(input("Selecciona la operación que deseas realizar: "))

    if operacion == 1:
        sumar()
    elif operacion == 2:
        restar()
    elif operacion == 3:
        multiplicar()
    elif operacion == 4:
        dividir()
    elif operacion == 5:
        print("Haz salido del programa :D")
        break
    else:
        print("Valor ingresado no válido, ingresa un nuevo valor \n")