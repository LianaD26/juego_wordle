import random

class Wordle:
    def abrir_archivo(self) -> list:
        with open("lista_palabras.txt", "r") as archivo:
            lineas = archivo.readlines()
            lista = [linea.strip() for linea in lineas]
            return lista
    def seleccionar_palabra(self) -> str:
        lista = self.abrir_archivo()
        num_pal = random.randint(0, len(lista) - 1)
        pal = lista[num_pal]
        return pal
    def verificar_ganador(self, tablero):
        # si tengo el num_intentos es 6 y una fila vacía es porque ganó
        for fila in tablero.matriz:
            if all(elemento == "_" for elemento in fila):
                return True
        return False
    def ejecutar_juego(self, wordle):
        tablero = Tablero()
        palabra_correcta = wordle.seleccionar_palabra()
        while tablero.num_intentos < 6:
            tablero.imprimir_tablero()
            tablero.actualizar_tablero(palabra_correcta)
            tablero.colorear_matriz(palabra_correcta)
            if "".join(tablero.matriz[tablero.num_intentos-1]) == palabra_correcta:
                print("Has adivinado la palabra!")
                break
        if self.verificar_ganador(tablero) and tablero.num_intentos == 6:
            tablero.imprimir_tablero()
            print("Has adivinado la palabra!")
        else:
            tablero.imprimir_tablero()
            print(f"¡Agotaste tus intentos! La palabra correcta era: {palabra_correcta}")

class Color:
    def __init__(self):
        self.GRIS = "\033[90m"
        self.VERDE = "\033[92m"
        self.AMARILLO = "\033[93m"
        self.RESET = "\033[0m"

class Tablero:
    def __init__(self):
        self.num_intentos: int = 0
        self.matriz = []
        self.llenar_matriz()

    def llenar_matriz(self):
        for i in range(6):
            self.matriz.append(["_" for _ in range(5)])

    def imprimir_tablero(self):
        for fila in self.matriz:
            print(" ".join(fila))
        print(f"Intento {self.num_intentos}/6")

    def actualizar_tablero(self, palabra_correcta):
        if self.num_intentos < 6:
            print("Ingresa una palabra de 5 letras en minúsculas:")
            palabra = input()
            if len(palabra) == 5 and palabra.isalpha() and palabra.islower():
                if palabra == palabra_correcta:
                    for i, letra in enumerate(palabra):
                        self.matriz[self.num_intentos][i] = letra
                    self.num_intentos = 6
                    return
                else:
                    for i, letra in enumerate(palabra):
                        self.matriz[self.num_intentos][i] = letra
                    self.num_intentos += 1
            else:
                print("Por favor, ingresa una palabra válida de 5 letras en minúsculas.")
        else:
            print("Ya has alcanzado el límite de intentos.")
    def colorear_matriz(self, palabra_correcta):
        nueva_lista = palabra_correcta
        for j in range(5):
            letra = self.matriz[self.num_intentos - 1][j]
            if letra in nueva_lista and letra != nueva_lista[j]:
                self.matriz[self.num_intentos - 1][j] = f"{Color().AMARILLO}{letra}{Color().RESET}"
                nueva_lista = nueva_lista.replace(letra, "-")
            elif letra == nueva_lista[j]:
                self.matriz[self.num_intentos - 1][j] = f"{Color().VERDE}{letra}{Color().RESET}"
                nueva_lista = nueva_lista.replace(letra, "-")
            else:
                self.matriz[self.num_intentos - 1][j] = f"{Color().GRIS}{letra}{Color().RESET}"

wordle = Wordle()
wordle.ejecutar_juego(wordle)