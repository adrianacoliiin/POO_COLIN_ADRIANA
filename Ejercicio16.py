p1 = float(input("Ingresa el primer promedio: "))
p2 = float(input("Ingresa el segundo promedio: "))
p3 = float(input("Ingresa el tercer promedio: "))

if p1 > p2 and p1 > p3:
    p_mayor = p1
    print("El promedio mayor es el primero: ", p_mayor)
elif p2 > p3 and p2 > p1:
    p_mayor = p2
    print("El promedio mayor es el segundo: ", p_mayor)
else:
    p_mayor = p3
    print("El promedio mayor es el tercero: ", p_mayor)

