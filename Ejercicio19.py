frutas_1 = {"manzana", "pera", "sandia", "piña", "plátano"} 
frutas_2 = {"durazno", "uva", "frambuesa", "mora", "naranja"}

frutas_3 = frutas_1.union(frutas_2)

frutas_3.add("toronja <3")

print("La frutas dentro de los conjuntos son:")
for fruta in frutas_3:
    print(fruta)
