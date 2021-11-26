# Crear la tabla de multiplicar que elija el usuario

numero = int(input("Elige un numero: "))

for i in range(1, 11):
    result = i * numero
    if result % 2 ==0:
        print("{} x {} = {}".format(i, numero, result))