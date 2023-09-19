class Color:
    def __init__(self):
        self.GRIS = "\033[90m"
        self.VERDE = "\033[92m"
        self.AMARILLO = "\033[93m"
        self.RESET =  "\033[0m"
l = "a"
print(l)
a = f"{Color().VERDE}l{Color().RESET}"
print(a)
print(l,a)