@echo off
title Dynamic Decision Intelligence Dashboard
setlocal
if exist "D:\Python\Python312\python.exe" (
    set "PYTHON_EXE=D:\Python\Python312\python.exe"
) else (
    set "PYTHON_EXE=python"
)
echo Starting Dynamic Decision Dashboard on http://localhost:8501 ...
set "APP_INITIAL_MODE=DYNAMIC"
"%PYTHON_EXE%" "%~dp0launch_dynamic.py"
if not "%1"=="--no-pause" pause