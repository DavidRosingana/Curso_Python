print("Contador de puntuación")
puntos = 0
comas = 0
espacios = 0

texto = input("Introduce un texto: ")

for i in texto:
    if i == " ":
        espacios += 1
    elif i == ".":
        puntos += 1
    elif i == ",":
        comas += 1

print(espacios, puntos, comas)