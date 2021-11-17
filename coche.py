class Coche:
    """Esta clase define el estado y el comportamiento de un coche"""
    rueda = 4
    
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
    
    def pitido(self):
        print("ppiiii")
    
    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
    
    def verVelocidad(self):
        print(self.velocidad)
    
    def __str__(self):
        return "color: " + self.color + ", aceleracion: " + str(self.velocidad) + ", ruedas: " + str(self.ruedas)
