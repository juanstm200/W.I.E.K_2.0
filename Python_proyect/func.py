"""Se importa la libreria ctype para poder manipular los Dll """
import ctypes as c
"""Se importa la libreria os para manejar operaciones del sistema como el path"""
import os

"""Se le asigna la ruta optenida por el os a la variable ruta_dll"""
"""getcwd para obtener la ruta \\"""
ruta_dll = os.getcwd() + "\\test.dll" 
"""Validamo que exista la ruta optenida y en caso contrario imprimir que no existe"""
if not os.path.exists(ruta_dll):
    print("El archivo no existe : " + ruta_dll)
print("El archivo existe")
"""en dll guardamos la funcion obtenida de la libreria del archivo .C"""
dll = c.CDLL(ruta_dll)
"""Invocamos a la variable que guarda la ruta a la funcion desde la libreria invicada"""
dll.main()