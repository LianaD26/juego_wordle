import random
with open("lista_palabras.txt", "r") as archivo:
    lineas = archivo.readlines()
    lista = []
    for linea in lineas:
        palabra = linea.strip() #sin saltos de línea
        lista.append(palabra)
    pal = random.randint(0,len(lista)-1)
    print(lista[pal])
    if "e" in lista[pal]:
        print("está e")