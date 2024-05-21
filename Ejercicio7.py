print("CALCULADORA DE COSTOS DE ENVIO")

peso = float(input("Ingresa el peso (en kg) del paquete ingresado: "))

if peso < 1:
    costo = peso * 50
elif peso >= 1 and peso < 5:
    costo = peso * 100
elif peso >= 5  and peso < 10:
    costo = peso * 200
elif peso >= 10:
    costo = peso * 500

print("El precio de tu envio sera de : ", costo)