lista =[1, 2, "Ana", 1.5, True]

print(lista[2]) #Seleccionar un elemento en una posición específica
lista.append("Miguel")
print(lista)
lista.remove(2)
print(lista)
elemento = lista.pop(2)
print(elemento)
print(lista)

"""
[i] devuelve el elemento que esta en la posción i de la lista
lista[2] = "hola", cambiara el valor de la posición 2 de la lista
lista.append() - añade elementos al final de la lista
lista.insert() - añade elementos a la lista en una posición predeterminada (posición, elemento)
lista.extend([lista2]) - fusiona listas con lista2
lista.remove(elemento) - elimina el elemento como tal que queremos eliminar de la lista
"""