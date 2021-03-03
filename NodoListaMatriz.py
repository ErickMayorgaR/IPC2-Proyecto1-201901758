from ListaElementos import ListaElementos

class Matriz:
    def __init__(self, nombre, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.siguiente = None
