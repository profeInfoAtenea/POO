from Celda import Celda
from Vacio import Vacio

class Tablero:

    def __init__(self, total_filas, total_columnas):
        self.__total_filas = total_filas
        self.__total_columnas = total_columnas
        self.__celdas = {}
        
        for i in range(0,total_filas):
            fila = i 
            for j in range(total_columnas):
                columna = self.__numeroALetra(j)
                clave = columna+str(fila)
                v_celda = Celda(i,j, Vacio())
                self.__celdas[clave] = v_celda
    
    def __str__(self):
        ret = ""
        for i in range(0,self.__total_filas):
            fila = i 
            ret += "\n"
            for j in range(0,self.__total_columnas):
                columna = self.__numeroALetra(j)
                clave = columna+str(fila)
                v_celda = self.__celdas[clave]

                ret += " "+ str(v_celda.getEstado()) + ""
        return ret

    def __numeroALetra(self,numero):
        letra = ['a','b','c','d','e','f','g', 'h']
        try:
            return letra[numero]
        except:
            print("Error")
    
    def colocarPieza(self, pieza, coordenada):
        if(coordenada in self.coordenadasVacias()):
            celda = self.__celdas[coordenada]
            celda.setEstado(pieza)
            self.__celdas[coordenada] = celda

    def celdas(self):
        return self.__celdas
    
    def coordenadasVacias(self):
        coordenadasVacias = []
        for coordenada in self.__celdas:
            celda = self.__celdas[coordenada]
            if(type(celda.getEstado()) == Vacio):
                coordenadasVacias.append(coordenada)
        return coordenadasVacias

    def esCoordenadaVacia(self, coordenada):
        return coordenada in self.coordenadasVacias()

