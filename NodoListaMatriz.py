from ListaElementos import ListaElementos

class Matriz:
    ListaElementos = ListaElementos()
    def __init__(self, nombre, filas, columnas, ListaElementos):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.ListaElementos = ListaElementos
        self.siguiente = None
