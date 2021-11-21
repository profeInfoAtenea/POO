
class Coche:
    """Esta clase define el estado y el comportamiento de un coche"""
    rueda = 4
    
    def __init__(self, color, aceleracion):
        self.__color = color
        self.__aceleracion = aceleracion
        self.__velocidad = 0
    
    def acelera(self):
        self.__velocidad = self.__velocidad + self.__aceleracion
    
    def pitido(self):
        print("ppiiii")
    
    def frena(self):
        self.__velocidad = self.__velocidad - self.__aceleracion
    
    def verVelocidad(self):
        print(self.__velocidad)
    
    def __str__(self):
        return "color: " + self.__color + ", aceleracion: " + str(self.__velocidad) + ", ruedas: " + str(self.ruedas)



