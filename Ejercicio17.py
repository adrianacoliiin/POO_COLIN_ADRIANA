while True:
    print("1. Converión de Celsius a Farenheit")
    print("2. Converión de Farenheit a Celsius")
    print("3. Salir \n")

    opcion = int(input("Ingresa el número que corresponde a la operación a realizar: \n"))


    if opcion == 1:
        print("C E L S I U S  --  F A R E N H E I T")
        cel = float(input("Ingresa el valor en Celsius: \n"))

        far = (cel * (9/5)) + 32
        print(f"Es {far}°F \n")
        
    elif opcion == 2:
        print("FA R E N H E I T  --  C E L S I U S")
        far = float(input("Ingresa el valor en Farenheit: \n"))

        cel = (far - 32) * (5/9)
        print(f" Es {cel}°C \n")

    elif opcion == 3:
        print("")
        break

    else:
        print("El valor ingresado no es válido, ingresalo de nuevo: \n")

