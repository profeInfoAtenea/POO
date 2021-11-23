from Contacto import Contacto
from Agenda import Agenda



def crearAgendaPrueba():
    c1 = Contacto("Manuel", "666.111.666", "c1@email.test")
    c2 = Contacto("Lucia", "666.222.666", "c2@email.test")
    c3 = Contacto("Marta", "666.333.666", "c2@email.test")
    a = Agenda()
    a.agregarContacto(c1)
    a.agregarContacto(c2)
    a.agregarContacto(c3)
    return a

if __name__ == '__main__':
    a = crearAgendaPrueba()
    a.abrirAgenda()
 