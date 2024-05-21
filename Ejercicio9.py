correct_pass = "POO123"

while True:
    passw = str(input("Ingresa la contraseña correcta para entrar: "))

    if passw == correct_pass:
        print("¡La contraseña es correcta!")
        break
    else:
        print("La contraseña es incorrecta, intenta de nuevo")