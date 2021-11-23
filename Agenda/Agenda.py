class Agenda:
    def __init__(self):
        self.__contactos = []
        self.__abierta = False
    
    def agregarContacto(self, contacto):
        self.__contactos.append(contacto)
    
    def listarContacto(self):
       for c in self.__contactos:
           print(str(c))

    def buscarContacto(self):
        pass

    def editarContacto(self):
        pass

    def cerrarAgenda(self):
       self.__abierta = False

    def abrirAgenda(self):
        self.__abierta = True
        while( self.__abierta):
            self.__muestraMenu()
            self.__leerOpcion()
    
    def __muestraMenu(self):
        print("------ SELECCIONA OPCIÓN ------")
        print("| 1.- Listar Contacto: ")
        print("| 2.- Buscar Contacto: ")
        print("| 3.- Editar Contacto: ")
        print("| 4.- Cerrar Agenda: ")
        print("-----------------------")
    
    def __leerOpcion(self):
        try:
            opcion = -1
            while((opcion > 4) or (opcion < 1)):
                opcion = int(input(">"))
        except:
            print("Error")
        
        if(opcion == 1):
            self.listarContacto()
        elif(opcion == 2 ):
            pass
        elif(opcion == 4 ):
            self.cerrarAgenda()
        