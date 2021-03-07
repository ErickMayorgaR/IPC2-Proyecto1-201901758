import xml.etree.ElementTree as ET
from ListaMatrices import listaCircularM
from ListaElementos import ListaElementos
from NodoListaMatriz import  Matriz
from ListaFilas import ListaFilas
from NodoPaReducir import nodoUtil
from Nodofilas import datosFila
from ListaSimple import ListaS
from NodoElemento import Elemento

class Logica:
    lista_matrices_reducidas = ListaS()
    lista_matrices = None
    columnas = None
    filas = None

    def operaciones(self, nombrexml):
        arbol = ET.parse(nombrexml)
        raiz = arbol.getroot()
        self.lista_matrices = listaCircularM()


        for matriz in raiz:

            elemen = ListaElementos()
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
                    columnas = atributo


            for elemento in matriz:
                contaratdato = 0
                x = ''
                y = ''


                for atributodato in elemento.attrib.values():
                    contaratdato += 1
                    if elemento.tag.lower() == "frecuencia":
                        elemen.frecuencia = True
                    else:
                        if contaratdato == 1:
                            x = atributodato
                        elif contaratdato == 2:
                            y = atributodato

                unElemento = Elemento(elemento.text, x, y)

                if elemento.text == '0':
                    unElemento.estado = False
                else:
                    unElemento.estado = True

                elemen.insertar(unElemento)
            matriz_aux = Matriz(nombre,filas, columnas, elemen)
            self.lista_matrices.insertaralfinal(matriz_aux)
        var = 'solo pal debuger'

    def escribisalida(self):
        unrecorridoLM = False
        lista_aux  = self.lista_matrices
        inicioM = lista_aux.primero

        while unrecorridoLM == False:
            matriz_aux = inicioM
            self.reducirMatriz(matriz_aux, matriz_aux.filas, matriz_aux.columnas)

            print(inicioM.nombre)
            inicioM = inicioM.siguiente

            if inicioM == lista_aux.primero:
                unrecorridoLM = True

    def reducirMatriz(self, Matriz, filas, columnas):

        filasn = int(filas)
        columnasn = int(columnas)
        self.filas = filasn
        self.columnas = columnasn
        auxElemento = Matriz.ListaElementos.primero
        listacomparar = ListaFilas()
        recorridodato = False
        #Compone aca
        while auxElemento != None:
            listaFil = ListaS()
            listaEstado = ListaS()

            for i in range(columnasn):
                if auxElemento.estado == False:
                    listaEstado.insertar(0)
                else:
                    listaEstado.insertar(1)
                listaFil.insertar(auxElemento.dato)

                auxElemento = auxElemento.siguiente
            listacomparar.insertar(listaFil,listaEstado)

        #Comparar Lista
        #SeparaFilas ok

        #Hasta aqui lo hace correctamente
        #sumar = ListaFilas()

        listaRed = ListaS()
        listaFreq = ListaS()
        a_comparar = listacomparar.primero
        fila_aux2 = a_comparar
        contadorPrimera = 0
        #var1 = fila_aux2.comparaFila
        #var2 = a_comparar.siguiente.siguiente.comparaFila
        #if var1.primero.dato == var2.primero.dato:
          #print("Son iguales")
        #else:
            #print("me lleva la verga")
        fila_aux = a_comparar
        fila_auxn = None
        filas_usadas = ListaS()
        for f in range(1,(filasn+1)):
            if fila_aux != None:
                fila_aux = self.posicionarFila(fila_aux, f)
                fila_aux.fueComparado = True
            filas_sumar = ListaS()

            contadorSaltados = 0
            contadorFrecuencia = 0
            mandoSumar = False


            while fila_aux != None:
                soniguales = True
                if fila_aux.fueComparado == True:
                    fila_aux = fila_aux.siguiente
                    contadorSaltados += 1
                    continue
                else:
                    varcomp = a_comparar.comparaFila.primero
                    varfilaux = fila_aux.comparaFila.primero
                    for i in range (1, columnasn):
                        if soniguales != False:
                            if varcomp.dato == varfilaux.dato:
                                soniguales = True
                            else:
                                soniguales = False
                            varcomp = varcomp.siguiente
                            varfilaux = varfilaux.siguiente

                    if soniguales == True:
                        if contadorPrimera < 1:
                            filas_sumar.insertar(a_comparar.datosFila)
                            filas_sumar.insertar(fila_aux.datosFila)
                            filas_usadas.insertar(a_comparar.datosFila)
                            filas_usadas.insertar(fila_aux.datosFila)
                            fila_aux.fueComparado = True
                            mandoSumar = True
                            contadorPrimera += 1
                            contadorFrecuencia += 1
                        else:
                            filas_sumar.insertar(fila_aux.datosFila)
                            filas_usadas.insertar(fila_aux.datosFila)
                            fila_aux.fueComparado = True
                            mandoSumar = True
                    else:
                        if fila_aux.siguiente == None:
                            fila_auxn = fila_aux
                        fila_aux = fila_aux.siguiente
                        continue
                if fila_aux.siguiente == None:
                    fila_auxn = fila_aux
                fila_aux = fila_aux.siguiente
                print("llega?")
                print("algebugg")

            if mandoSumar == False:
                yaseuso = None
                if filas_usadas != None:
                    yaseuso = self.revisarEnFilasUsadas(a_comparar, filas_usadas)
                if yaseuso != True:
                    listaRed.insertar(a_comparar.datosFila)
            elif mandoSumar == True:
                listaRed.insertar(self.filas_sumar(filas_sumar))

            a_comparar = a_comparar.siguiente
            fila_aux = fila_auxn
            while fila_aux.anterior != None:
                fila_aux = fila_aux.anterior
            contadorPrimera = 0
            listaFreq.insertar(contadorFrecuencia)
        self.lista_matrices_reducidas.insertar(listaRed  )
        print("debbug")

    def filas_sumar(self, hayquesumar):
        datosFila = ListaS()
        columnas = self.columnas
        for i in range(columnas):
            primerFila = hayquesumar.primero
            numerodato = 0
            while primerFila != None:
                numerodato += int(self.regresaDato(primerFila, i))
                primerFila = primerFila.siguiente
            otravaraux = str(numerodato)
            datosFila.insertar(otravaraux)
        return datosFila



    def regresaDato(self, iterarFila, nite):
        i = 0
        aux = iterarFila.dato.primero
        while i < nite:
            aux = aux.siguiente
            i +=1

        return aux.dato

    def posicionarFila(self, fila, iteracion):
        n = 1
        while n < iteracion:
            fila.fueComparado = True
            fila = fila.siguiente
            n += 1
        return fila


    def revisarEnFilasUsadas(self, fila,usadas) -> object:
        fila_comparar = fila
        fila_aux = usadas.primero
        #fila_aux = filas_aux.dato
        fueUsada = None
        unaFilaUsada = None

        while fila_aux != None:
                fueUsada = True
                varcomp = fila_comparar.datosFila.primero
                varfilaux = fila_aux.dato.primero
                for i in range(1, self.columnas):
                    if fueUsada != False:
                        if varcomp.dato == varfilaux.dato:
                            fueUsada = True
                        else:
                            fueUsada = False
                        varcomp = varcomp.siguiente
                        varfilaux = varfilaux.siguiente
                fila_aux = fila_aux.siguiente
                if fueUsada == True:
                    unaFilaUsada = True

        return unaFilaUsada





















