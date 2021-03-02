import xml.etree.ElementTree as ET

class Logica:
    def operaciones(self, nombrexml):
        arbol = ET.parse(nombrexml)
        raiz = arbol.getroot()
        print(raiz)

