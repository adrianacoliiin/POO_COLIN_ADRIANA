edades = [10, 12, 21, 56, 32, 14, 18, 16, 23, 19, 56]
mayores_edad = []
menores_edad = []

for edad in edades:
    if edad >= 18:
        mayores_edad.append(edad)
    else:
        menores_edad.append(edad)

print("Mayores de edad: ", mayores_edad)
print("Menores de edad: ", menores_edad)