import random

class Guerrero:
    def __init__(self,nombre, vida, fuerza, precision, velocidad, defensa):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
        self.__precision = precision
        self.__velocidad = velocidad
        self.__defensa = defensa
        self.__image = '⚔'
    
    def getVelocidad(self):
        return self.__velocidad
    
    def getPrecision(self):
        return self.__precision
    
    def getVida(self):
        return self.__vida
    def setVida(self, vida):
        self.__vida = vida
    def getFuerza(self):
        return self.__fuerza
    def getDefensa(self):
        return self.__defensa
    def getNombre(self):
        return self.__nombre
    
    def golpear(self, g):
        #veo si acierto el golpe
        if( random.random() <= self.getPrecision() - g.getVelocidad() / 100):
            #en caso de acertar, agrego daño al oponente
            g.setVida(g.getVida() - max([(self.getFuerza() - g.getDefensa())+random.randrange(-10,11),1]))
            print("Golpe certero de ", self.getNombre())
        else:
            print(g.nombre , " esquiva el golpe")   

def simular_batalla(j1, j2):
    #comienza jugador más veloz
    golpeador, receptor = j1, j2
    if(j1.getVelocidad() < j2.getVelocidad()):
        golpeador, receptor = j2, j1
    
    while(j1.getVida() > 0 and j2.getVida() > 0):
        golpeador.golpear(receptor)
        #cambio de turnos
        golpeador , receptor = receptor , golpeador
        #fin
    print("\n" + j1.getNombre() , j1.getVida() , "vs", j2.getVida(), j2.getNombre())
    print("Ganador: ", receptor.getNombre())

#batalla de ejemplo
    #     Guerrero(nombre:'Superman', vida:100, fuerza:50, precision:80, velocidad:30, defensa:20)
superman = Guerrero('Superman', 100, 50, 60, 30, 20)
goku = Guerrero('Goku', 100, 75, 50, 95, 85)
chuck = Guerrero('Chuck-Norris', 100, 10, 40, 15, 5)
brucelee = Guerrero('BruceLee', 100, 15, 50, 16, 6)

#simulamos batalla
simular_batalla(chuck, brucelee)
