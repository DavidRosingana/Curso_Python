numeros = []

numero_intruducido = int(input("Diga una lista de numeros: "))
numeros.append(numero_intruducido)

while input("Desea añadir mas números: [S/N]: ") == "S":
    numero_intruducido = int(input("Diga una lista de numeros: "))
    numeros.append(numero_intruducido)

for i in numeros:
    