import random

class Guerrero:
    def __init__(self,nombre, vida, fuerza, precision, velocidad, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.precision = precision
        self.velocidad = velocidad
        self.defensa = defensa
        self.image = '⚔'
    def golpear(self, g):
        if( random.random() <= self.precision - g.velocidad / 100):
            g.vida -= max([(self.fuerza - g.defensa)+random.randrange(-10,11),1])
            print("Golpe certero de ", self.nombre)
        else:
            print(g.nombre , " esquiva el golpe")
            
def simularbatalla(j1, j2):
    #comienza jugador  más veloz
    golpeador, receptor = j1, j2
    if(j1.velocidad < j2.velocidad):
        golpeador, receptor = j2, j1
        
    #Se golpean hasta que alguno tenga vida cero
    while(j1.vida > 0 and j2.vida>0):
        print("\n" + j1.nombre, j1.vida, "vs", j2.nombre, j2.vida)
        golpeador.golpear(receptor)
        #cambio de turnos
        golpeador, receptor = receptor, golpeador
    #fin
    print("\n" + j1.nombre, j1.vida , "vs" , j2.vida, j2.nombre)
    print("Ganador:", receptor.nombre)

# batalla de ejemplo
superman = Guerrero("Superman", 100, 50, 80, 30, 20)
goku = Guerrero("Goku", 100, 60, 80, 40, 20)
chuck = Guerrero("Chuck norris", 200, 99, 99,99, 99)

#Simula batalla
simularbatalla(goku,superman)
