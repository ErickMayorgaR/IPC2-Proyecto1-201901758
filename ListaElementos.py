from NodoElemento import Elemento

class ListaElementos:
    def __init__(self):
        self.primero = None


    def insertar(self, Elemento):

        unNodo = Elemento
        if self.primero == None:
            self.primero= unNodo
        else:
            temp = self.primero
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = unNodo
            unNodo.anterior = temp




