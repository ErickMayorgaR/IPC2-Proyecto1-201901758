import xml.etree.ElementTree as ET
from ListaMatrices import listaCircularM

class Logica:
    lista_matrices = None
    def operaciones(self, nombrexml):
        arbol = ET.parse(nombrexml)
        raiz = arbol.getroot()


        for matriz in raiz:
            self.lista_matrices = listaCircularM()
            contador = 0
            nombre = ''
            filas = ''
            columnas = ''

            for atributo in matriz.attrib.values():
                contador += 1
                if contador == 1:
                    nombre = atributo
                elif contador == 2:
                    filas = atributo
                elif contador == 3:
                    columnas == atributo

            self.lista_matrices.insertar(nombre, filas, columnas)


            for elemento in matriz:
                conta
                print(elemento.tag)


               #print(elemento.attrib)
                #print(elemento.text)




