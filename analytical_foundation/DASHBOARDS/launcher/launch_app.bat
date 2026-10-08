@echo off
title Product Market Entry Decision Platform Launcher
setlocal
if exist "D:\Python\Python312\python.exe" (
    set "PYTHON_EXE=D:\Python\Python312\python.exe"
) else (
    set "PYTHON_EXE=python"
)
echo Starting Product Market Entry Decision Platform on http://localhost:8501 ...
"%PYTHON_EXE%" "%~dp0launch_app.py"
if not "%1"=="--no-pause" pause
