from NodoListaMatriz import Matriz

class listaCircularM:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertaralfinal(self, Matriz):
        if self.primero == None:
            self.primero = self.ultimo = Matriz
            self.ultimo.siguiente = self.primero
        else:
            temp = self.ultimo
            self.ultimo = temp.siguiente = Matriz
            self.ultimo.siguiente = self.primero
            

    #def reducir(self):

        







