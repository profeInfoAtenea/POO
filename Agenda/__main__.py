from Contacto import Contacto
from Agenda import Agenda

def crear_agenda_para_prueba():
    """Crea una Agenda con algunos datos para probar"""
    c1 = Contacto("Manuel", "666.111.666", "c1@email.test")
    c2 = Contacto("Lucia", "666.222.666", "c2@email.test")
    c3 = Contacto("Marta", "666.333.666", "c2@email.test")
    a = Agenda()
    a.agregar_contacto(c1)
    a.agregar_contacto(c2)
    a.agregar_contacto(c3)
    return a

if __name__ == '__main__':
    a = crear_agenda_para_prueba()
    a.abrir_agenda()
