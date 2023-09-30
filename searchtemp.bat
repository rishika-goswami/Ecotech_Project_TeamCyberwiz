@echo off
:x
set "targetFile=%USERPROFILE%\Downloads\Temp_Data.csv"

if exist "%targetFile%" (
    py main_temp.py
    goto break    
)
goto x
:break
del %targetFile%
pause

