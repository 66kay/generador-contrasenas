# Generador de contraseñas
import random
import string

caracteres = string.ascii_letters + string.digits + "!@#$%&*"

try:
    largo = int(input("¿Cuántos caracteres quieres? "))
except ValueError:
    print("Debes escribir un número")
    exit()

if largo < 4:
    print("El largo mínimo es 4")
else:
    contrasena = ""
    for i in range(largo):
        contrasena += random.choice(caracteres)
    print("Tu contraseña es:", contrasena)
