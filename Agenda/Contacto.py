class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
    
    def __str__(self):
        return "Nombre:  {0} Telefono: {1} Email : {2}".format(self.__nombre, self.__telefono, self.__email)
    
    def getTelefono(self):
        """Get Telefono"""
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
        
'''
c1 = Contacto("manuel", "666.666.666", "c1@email.test")

c1.nombre = "Lucia"
c1.setTelefono("777")
print(str(c1))
'''