edades = [6, 56, 34, 18, 23, 10, 13, 25, 32, 8]

infancia = []
adolescentes = []
jovenes = []
adultos = []

for edad in edades:
    if edad >= 6 and edad <= 11:
        infancia.append(edad)

    elif edad >= 12 and edad <= 17:
        adolescentes.append(edad)

    elif edad >= 18 and edad <=26:
        jovenes.append(edad)
    
    else:
        adultos.append(edad)


print("Edades que corresponden a Infancia: ", infancia)
print("Edades que corresponden a Adolescentes: ", adolescentes)
print("Edades que corresponden a Jovenes: ", jovenes)
print("Edades que corresponden a Adultos: ", adultos)