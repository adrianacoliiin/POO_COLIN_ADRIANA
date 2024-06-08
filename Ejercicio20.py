con_1 = {1,2,3}
con_2 = {4,5,6}
con_3 = {7,8,9}

conjunto = con_1.union(con_2)
conjunto = conjunto.union(con_3)

pares = set()
for n in conjunto:
    if n % 2 == 0:
        pares.add(n)
    else:
        pass

print("Los numeros son: ")
print(conjunto)
print("Los pares son: ")
print(pares)