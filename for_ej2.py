import string

print("Contador de letras mayusculas")

texto = input("Introduzca un texto: ")
mayusculas = 0

for i in texto:
    if i in string.ascii_uppercase:
        mayusculas += 1

print("El numero de letras mayusculas es: {}".format(mayusculas))