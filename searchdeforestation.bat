@echo off
:x
set "targetFile=%USERPROFILE%\Downloads\Deforestation.csv"

if exist "%targetFile%" (
    py main_deforestation.py
    goto break    
)
goto x
:break
del %targetFile%
pause