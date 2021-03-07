from tkinter import filedialog
from tkinter import *
from Logica import Logica


file = ''
global puedo_cargar
puedo_cargar =False

analizar_archivo = Logica()



def cargar_archivo():
    global puedo_cargar
    puedo_cargar= True

    # ruta = Tk()
    # ruta.filename = filedialog.askopenfilename(filetypes=(("XML files", "*.xml"), ("all files", "*.*")))
    # file = open(ruta.filename, "r", encoding='utf-8')
    global file
    file = 'C:/Users/emayo/OneDrive/Desktop/IPC2-Proyecto1-201901758/Matriz.xml'

    print(file)
    # ruta.destroy()


def procesar_archivo():
    if puedo_cargar == True:
        analizar_archivo.operaciones(file)
    else:
        print("Por favor ingrese una ruta de carga")



def escribir_salida():
    analizar_archivo.escribisalida()


def mostrar_datos_estudiantes():
    print("Erick Ivan Mayorga Rodriguez")
    print("201901758")
    print("Introducción a la programacion y Computacion 2 Sección D")
    print("Ingenieria en Ciencias y Sistemas")




def salir():
    sys.exit(0)

def opciones():
    print("\n")
    print("Seleccione una Opcion")
    print("1.Cargar Archivo ")
    print("2.ProcesarArchivo")
    print("3.Escribir Archivos de Salida")
    print("4.Mostrar Datos del estudiante")
    print("5.Generar Grafica")
    print("6.Salir")


def main_menu():
    opcion = -1
    while opcion != 4:
        opciones()
        opcion = int(input())
        if opcion == 1:
            cargar_archivo()
        elif opcion == 2:
            procesar_archivo()
        elif opcion == 3:
            escribir_salida()
        elif opcion == 4:
            generar_graficas()
        elif opcion == 5:
            salir()
        elif opcion == 5:
            salir()
        else:
            print("Algo")


main_menu()
"""def separador():
    print("algo") """
