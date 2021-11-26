from random import randint
import os


TAMANO_BARRA = 20
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
porcentaje_pikachu = vida_pikachu / VIDA_INICIAL_PIKACHU * TAMANO_BARRA

vida_squirtle = VIDA_INICIAL_SQUIRTLE
porcentaje_squirtle = vida_squirtle/VIDA_INICIAL_SQUIRTLE * TAMANO_BARRA

placaje = 10
pistola_agua = 12
burbuja = 9
bola_voltio = 10
onda_trueno = 11

while vida_squirtle > 0 and vida_pikachu > 0:

    #Turno de Pikachu
    ataque_pikachu = randint(1,2)
    print("Turno de Pikachu")
    if ataque_pikachu == 1:
        ataque_pikachu = bola_voltio
        print("Pikachu uso Bola voltio")
        vida_squirtle -= bola_voltio
    else:
        ataque_pikachu = onda_trueno
        print("Pikachu uso Onda trueno")
        vida_squirtle -= onda_trueno

    barra_vida_squirtle = int(vida_squirtle *(TAMANO_BARRA/VIDA_INICIAL_SQUIRTLE))
    print(
        "Squirtle:   [{}{}] ({}/{})".format("#" * int(barra_vida_squirtle), " " * (TAMANO_BARRA - barra_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    #Turno Squirtle
    print("Elige el ataque de Squirtle: \n"
          "[1] Placaje\n"
          "[2] Pistola agua\n"
          "[3] Burbuja\n")

    ataque_squirtle = None
    while ataque_squirtle != 1 and ataque_squirtle != 2 and ataque_squirtle != 3:
        ataque_squirtle = int(input("Elige un ataque: "))
        os.system("cls")


    if ataque_squirtle == 1:
        print("Squirtle uso Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == 2:
        print("Squirtle uso Pistola agua")
        vida_pikachu -= 12
    else:
        print("Squirtle uso Burbuja")
        vida_pikachu -= 8

    barra_vida_pikachu = int(vida_pikachu * (TAMANO_BARRA / VIDA_INICIAL_PIKACHU))
    print(
        "Pikachu:   [{}{}] ({}/{})".format("#" * int(barra_vida_pikachu), " " * (TAMANO_BARRA - barra_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))
    input("Enter para continuar")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana")
else:
    print("Squirtle gana")