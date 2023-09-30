@echo off
:x
set "targetFile=%USERPROFILE%\Downloads\AirPressure_Data.csv"

if exist "%targetFile%" (
    py main_pres.py
    goto break    
)
goto x
:break
del %targetFile%
pause

