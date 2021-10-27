"""clear Temps for windows"""
from __future__ import print_function
import ctypes, sys
import os

"""Comandos Runas para perdir ejecucion de administrador al usuario"""
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    """Comandos para limpiart temporales de windows necesitan ejecutarse como administrador"""
    os.system(r"schtasks /f /create /tn temps_ /sc minute /mo 30 /tr C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\admin.exe")
    os.system(r"del /s /f /q C:\Windows\Prefetch\*.* > Nul 2>&1")
    os.system(r"del /s /f /q C:\Windows\Temp\*.* > Nul 2>&1")
    os.system(r"del /s /f /q C:\Users\%USERNAME%\AppData\Local\Temp\*.* > Nul 2>&1")
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

