from NodoListaMatriz import Matriz

class listaCircularM:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nombre, filas, columnas):
        unNodoCircular = Matriz(nombre, filas, columnas)
        if self.primero == None:
            self.primero = self.ultimo = unNodoCircular
        else:
            temp = unNodoCircular
            temp.siguiente = self.primero
            self.primero = temp
            self.ultimo.siguiente= self.primero







