inventario = {
    "mochila" : 400,
    "bolsa pequeña" : 150,
    "maleta" : 1500,
    "maquillaje" : 380,
    "body mist" : 90,
    "shampoo" : 150,
    "acondicionador" : 136
}

descuento = .10

for producto in inventario:
    precio_inicial = inventario[producto]
    precio_desc = precio_inicial * descuento
    precio_final = precio_inicial - precio_desc
    inventario[producto] = precio_final

print("Precios con descuentos: ")
for producto, precio in inventario.items():
    print(f"{producto} : ${precio}")




