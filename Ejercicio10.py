print("CALCULADORA DE SUMAS")

while True:
    print("1. Hacer una suma")
    print("2. Salir del programa")

    opcion = int(input("Ingresa el número que corresponda a la opcion que deseas realizar: "))

    if opcion == 2:
        break
    else:
        None

    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))

    suma = n1 + n2

    print("La suma de los numeros ingresados es de: ", suma)
    
    