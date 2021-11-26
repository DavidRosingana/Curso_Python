lista_compra = []

item = None

while item != "Q":
    item = input("Que desea comprar? ([Q] para salir) > ")
    if item =="Q":
        pass
    elif item in lista_compra:
        print("{} ya esta en la lista".format(item))
    else:
        lista_compra.append(item)

print("La lista de la compra es {}".format(lista_compra))