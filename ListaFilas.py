from Nodofilas import datosFila
from NodoPaReducir import nodoUtil

class ListaFilas:
    def __init__(self):
        self.primero = None



    def insertar(self, dato, comparador):
        unNodo = nodoUtil(dato, comparador)
        if self.primero == None:
            self.primero= unNodo
        else:
            temp = self.primero
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = unNodo
            unNodo.anterior = temp