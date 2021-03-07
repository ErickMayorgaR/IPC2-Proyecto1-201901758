from ListaSimple import ListaS

class nodoUtil:
    def __init__(self, dato, comparar):
        self.datosFila = dato
        self.comparaFila = comparar
        self.fueComparado = None
        self.siguiente = None
        self.anterior = None