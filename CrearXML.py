import os

class unXML:
    paragraficar = None


    def elementoRaiz(self, listaReducidas):
        self.paragraficar = listaReducidas
        datosaux = ''''''
        datosaux += '''<Matrices>'''
        saltoL = '''\n'''
        datosaux += saltoL

        unaMatriz = listaReducidas.primero
        unrecorridoLM = False
        inicioM= unaMatriz
        contadorMatrices = 0

        while unrecorridoLM == False:
            contadorMatrices += 1

            taginicio = '''<matriz ''' + '''nombre= "''' + str(contadorMatrices) + '''.''' + inicioM.nombre + '''"''' + ''' n=''' + str(inicioM.filas) + ''' m=''' + str(inicioM.columnas) + '''>'''
            datosaux += taginicio
            datosaux += saltoL

            dato_recorrer = inicioM.ListaElementos.primero
            for i in range(inicioM.columnas*inicioM.filas):
                tagdato = '''<dato ''' + '''x=''' + str(dato_recorrer.enx) + ''' y=''' + str(dato_recorrer.eny) + '''>''' + dato_recorrer.dato
                tagcierredato = '''</dato>'''
                datosaux += tagdato
                datosaux +=tagcierredato
                datosaux += saltoL

                dato_recorrer = dato_recorrer.siguiente


            frecuencias = inicioM.frecuencias.primero
            contadorfreq = 0
            while frecuencias != None:
                contadorfreq += 1
                tagfreq = '''<frecuencia g= ''' + str(contadorfreq) + '''>''' + str(frecuencias.dato) + '''</frecuencia>'''
                datosaux += tagfreq
                datosaux += saltoL
                frecuencias = frecuencias.siguiente



            tagCierreMatriz = '''</matriz>'''
            datosaux += tagCierreMatriz
            inicioM = inicioM.siguiente


            if inicioM == listaReducidas.primero:
                unrecorridoLM = True

        print("algo")
        datosaux += '''</Matrices>'''

        with open("C:/Users/emayo/OneDrive/Desktop/IPC2-Proyecto1-201901758/MatrizReducida.xml",'w', encoding= 'utf-8') as file:
            file.write(datosaux)
            file.close()

    def graficarMatriz(self):
        listaReducidas = self.paragraficar

        datos = ''''''
        datos += '''Digraph D {'''

        saltoL ='''\n'''
        datos += saltoL
        unaMatriz = listaReducidas.primero
        recorrida = None
        numeroMatriz = 0
        print("Estas son las matrices disponibles")
        while recorrida != True:
            numeroMatriz += 1
            print(str(numeroMatriz) + ".)" + unaMatriz.nombre)
            unaMatriz = unaMatriz.siguiente
            if unaMatriz == listaReducidas.primero:
                recorrida = True
        print("Para seleccionar la Matriz escriba el numero")

        varEleccion = input()

        varCompara = 1
        while varCompara < int(varEleccion):
            unaMatriz = unaMatriz.siguiente
            varCompara +=1

        datos += '''M[label = "Matrices"];'''
        datos += saltoL
        datos += '''Ej[label = '''
        datos += '''"''' + unaMatriz.nombre + '''"];'''
        datos += saltoL
        datos += '''M -> Ej;'''
        datos += saltoL
        datos += '''F[label= "n=''' + str(unaMatriz.filas) + '''"];'''
        datos += saltoL
        datos += '''C[label = "m=''' + str(unaMatriz.columnas) + '''"];'''
        datos += saltoL
        datos += '''Ej-> F;'''
        datos += '''Ej ->C;'''

        n_datos = 0
        datos_recorrer = unaMatriz.ListaElementos.primero
        for i in range(unaMatriz.filas):
            for j in range(unaMatriz.columnas):
                n_datos += 1
                aux = '''N''' + str(n_datos) + '''[label = "''' + str(datos_recorrer.dato) + '''"];'''
                datos += aux
                datos += saltoL
                datos_recorrer = datos_recorrer.siguiente

        contador2 = 0
        for i in range(unaMatriz.filas):
            for j in range(unaMatriz.columnas):
                contador2 += 1
                if contador2 <= unaMatriz.columnas:
                    datos += '''Ej ->''' + '''N''' + str(contador2) + ''';'''
                    datos += saltoL


                else:
                    datos += '''N''' + str(contador2 - unaMatriz.columnas) +  '''-> N''' + str(contador2) + ''';'''
                    datos += saltoL


        datos += '''}'''
        with open("C:/Users/emayo/OneDrive/Desktop/IPC2-Proyecto1-201901758/Prueba.dot",'w', encoding= 'utf-8') as file:
            file.write(datos)
            file.close()

        os.system('dot -Tpng Prueba.dot -o P1.png')
        os.system("P1.png")










