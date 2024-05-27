while True:
    print("\nC A L C U L A D O R A   D E    A R E A S")
    print("1. Área de un cuadrado")
    print("2. Área de un triangulo")
    print("3. Area de un rectángulo")
    print("4. Salir \n")

    opcion = int(input("Ingresa el número que corresponde al cáclulo que deseas realizar: \n"))


    if opcion == 1:
        lado = float(input("Ingresa el valor del lado del cuadrado "))

        area = lado * lado

        print("El área del cuadrado es de: ", area)

    elif opcion == 2:
        base = float(input("Ingresa el valor de la base del triángulo: "))
        altura = float(input("Ingresa el valor de la altura del triángulo: "))

        area = (base * altura) / 2

        print("El área del triángulo es de: ", area)

    elif opcion == 3:
        base = float(input("Ingresa el valor de la base del rectángulo: "))
        altura = float(input("Ingresa el valor de la altura del rectángulo: "))

        area = base * altura

        print("El área del rectángulo es de: ", area)

    elif opcion == 4:
        print("¡Haz salido del programa! :D")
        break

    else: 
        print("El valor ingresado no es válido, ingresa un número del 1 al 4")