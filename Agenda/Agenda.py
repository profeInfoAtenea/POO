class Agenda:
    """Clase Agenda que gestiona listado de Contacto"""
    def __init__(self):
        self.__contactos = []
        self.__abierta = False
    
    def agregar_contacto(self, contacto):
        """Agrega un Contacto a una lista"""
        self.__contactos.append(contacto)
    
    def listar_contacto(self):
        """Listarla lista de Contacto """
       for c in self.__contactos:
           print(str(c))

    def buscar_contacto(self):
        pass

    def editar_contacto(self):
        pass

    def cerrar_agenda(self):
       self.__abierta = False

    def abrir_agenda(self):
        self.__abierta = True
        while( self.__abierta):
            self.__muestra_menu()
            self.__leer_opcion()
    
    def __muestra_menu(self):
        """Muestra las opciones disponibles"""
        print("------ SELECCIONA OPCIÓN ------")
        print("| 1.- Listar Contacto: ")
        print("| 2.- Buscar Contacto: ")
        print("| 3.- Editar Contacto: ")
        print("| 4.- Cerrar Agenda: ")
        print("-----------------------")
    
    def __leer_opcion(self):
        """ Función auxiliar para leer datos del Usuario"""
        try:
            opcion = -1
            while((opcion > 4) or (opcion < 1)):
                opcion = int(input(">"))
        except:
            print("Error")
        
        if(opcion == 1):
            self.listar_contacto()
        elif(opcion == 2 ):
            pass
        elif(opcion == 4 ):
            self.cerrar_agenda()
        
