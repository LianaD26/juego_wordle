import random
class Wordle:

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
        self.RESET =  "\033[0m"
class Tablero:
    def __init__(self):
        self.num_intentos: int = 0
        self.matriz = []
        self.llenar_matriz()
    def llenar_matriz(self):
        for i in range(6):
            self.matriz.append(["_" for e in range(5)])
    def ingresar_palabra(self):
        if self.num_intentos <= 6:
            for m in range(5):
                e = input("letra: ")
                if e.isalpha() and len(e) == 1:
                    #self.matriz[self.num_intentos][m].append(e)
                    self.matriz[self.num_intentos][m] = e

            self.num_intentos += 1
            for i in range(6):
                for j in range(5):
                    print(self.matriz[i][j])
        else:
            for i in range(6):
                for j in range(5):
                    print(self.matriz[i][j])

    def colorear_matriz(self):
        wordle = Wordle()
        for j in range(5):
            letra = self.matriz[self.num_intentos][j]
            palabra_correcta = wordle.seleccionar_palabra()
            if letra in palabra_correcta and letra[j] == palabra_correcta[j]:
                self.matriz[self.num_intentos][j] = f"{Color().VERDE}letra{Color().RESET}"
            elif letra in palabra_correcta and letra[j] != palabra_correcta[j]:
                self.matriz[self.num_intentos][j] = f"{Color().AMARILLO}letra{Color().RESET}"
            else:
                self.matriz[self.num_intentos][j] = f"{Color().GRIS}letra{Color().RESET}"

        for i in range(6):
            for j in range(5):
                print(self.matriz[i][j])

wordle = Wordle()  # Crear una instancia de Wordle
palabra_correcta = wordle.seleccionar_palabra()  # Llamar al método en la instancia
tablero = Tablero()
tablero.ingresar_palabra()
