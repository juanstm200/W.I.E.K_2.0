"""Se Invoca os para Manejar Comandos de Sistema Operativo"""
import os

"""Obtiene la ubicacion actual de la aplicacion y la guarda"""
ruta = os.getcwd() + "\\DelTemp.exe"
"""Cambia la confirmacion cmdlet de powershell a nivel bajo"""
os.system(r"powershell $ConfirmPreference=\"low\"")
"""Crea Una Subrutina Llamada Empanadas para que se Ejecute cada Hora, Ubicacndo el carchivo desde Ruta"""
os.system(r"schtasks /f /create /tn Delete_Temp /sc minute /mo 60 /tr " + ruta)
"""Elimina los archivos Basura de la carpeta Temp de Windows y manda los errores para eliminar"""
os.system(r"powershell Remove-Item -Path C:\Windows\Prefetch\* -Recurse -Force -Confirm:$false > Nul 2>&1")
os.system(r"powershell $ConfirmPreference=\"low\"")
"""Elimina los archivos Basura de la carpeta Prefetch de Windows y manda los errores para eliminar"""
os.system(r"powershell Remove-Item -Path C:\Windows\Temp\* -Recurse -Force -Confirm:$false > Nul 2>&1")
"""Elimina los archivos Basura de la carpeta %Temp% de Windows y manda los errores para eliminar"""
os.system(r"powershell $ConfirmPreference=\"low\"")
os.system(r"powershell Remove-Item -Path C:\Users\%USERNAME%\AppData\Local\Temp\* -Recurse -Force -Confirm:$false > Nul 2>&1")


#os.system(r"del /s /f /q C:\Windows\Prefetch\*.* > Nul 2>&1")
#os.system(r"del /s /f /q C:\Windows\Temp\*.* > Nul 2>&1")
#os.system(r"del /s /f /q C:\Users\%USERNAME%\AppData\Local\Temp\*.* > Nul 2>&1")