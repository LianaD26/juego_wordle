import random
class Wordle:
    def __init__(self):
        self.palabra_ingresada: list[str] = []

    def seleccionar_palabra(self) -> str:
        with open("lista_palabras.txt", "r") as archivo:
            lineas = archivo.readlines()
            lista = []
            for linea in lineas:
                palabra = linea.strip()  # sin saltos de línea
                lista.append(palabra)
        num_pal = random.randint(0, len(lista) - 1)
        pal = lista[num_pal]
        return pal
class Color:
    def __init__(self):
        self.GRIS = "\033[90m"
        self.VERDE = "\033[92m"
        self.AMARILLO = "\033[93m"
class Tablero:
    def __init__(self):
        self.num_intentos: int = 0
        self.matriz = []
    def llenar_matriz(self):
        for i in range(6):
            self.matriz.append(["_" for e in range(5)])
    def ingresar_palabra(self):
        if self.num_intentos <= 6:
            for m in range(5):
                e = input("letra: ")
                self.matriz[self.num_intentos][m].append(e)
            self.num_intentos += 1
            for i in range(6):
                for j in range(5):
                    print(self.matriz[i][j])
        else:
            for i in range(6):
                for j in range(5):
                    print(self.matriz[i][j])

    def verificar_fila(self):
        pass
    def colorear_matriz(self):
        pass
