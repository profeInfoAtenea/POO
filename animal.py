class Animal:
    """Clase padre Animal"""
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #Método genérico pero con implementación particular
    def hablar(self):
        #Metodo vacio
        pass
    
    #Método genérico pero con implementación particular
    def moverse(self):
        #Metodo vacio
        pass
    
    def describeme(self):
        print("Soy un Animal del tipo  ", type(self.__name__))

class Perro(Animal):
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("Caminando a 4 patas")

def Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

def Abeja(Animal):
    def hablar(self):
        print("Bzzzzz")
    def moverse(self):
        print("Volando")
    #Nuevo método
    def picar(self):
        print("Picar!")
