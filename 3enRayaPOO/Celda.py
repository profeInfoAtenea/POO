class Celda:
    def __init__(self, fila, columna, estado):
        self.__fila = fila
        self.__columna = columna
        self.__estado = estado
    
    def __str__(self):  
        return  self.__columna,  self.__fila
    
    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado

    def getCoordenada(self):
        return self.__columna,  self.__fila