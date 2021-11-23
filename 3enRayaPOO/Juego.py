from Tablero import Tablero
from Jugador import Jugador
import os


class Juego:
    def __init__(self):
        self.__movimientos = []
        self.__tablero = Tablero(3,3)
        self.__jugador1 = Jugador('★')
        self.__jugador2 = Jugador('✪')

    def __imprimeTablero(self):
        os.system ("clear")
        print("Selecciona una coordenada correcta: ")
        print( self.__tablero.coordenadasVacias())
        print(str( self.__tablero ))
        print("Jugador "+str(self.__jugador1)+": ", self.__coordenadaJugador(self.__jugador1))
        print("Jugador "+str(self.__jugador2)+": ", self.__coordenadaJugador(self.__jugador2))


    def empezar(self):
        while(True):
            self.__imprimeTablero()

            if(self.__turno()):
                coordenada = input(str(self.__jugador1) + " dime coordenada: ")
                while(self.__tablero.esCoordenadaVacia(coordenada)):
                    self.__tablero.colocarPieza(self.__jugador1, coordenada)
                    self.__movimientos.append(coordenada)
            else:
                coordenada = input(str(self.__jugador2) + " dime coordenada: ")
                while(self.__tablero.esCoordenadaVacia(coordenada)):
                    self.__tablero.colocarPieza(self.__jugador2, coordenada)
                    self.__movimientos.append(coordenada)
    def __turno(self):
        return len(self.__movimientos) % 2 == 0

    def __coordenadaJugador(self, jugador):
        coordenadas = []
        celdas = self.__tablero.celdas()
        for coordenada in celdas.keys():
           if(type(celdas[coordenada].getEstado())==Jugador):
               if(celdas[coordenada].getEstado()==jugador):
                   coordenadas.append(coordenada)
        return coordenadas

