@echo off
title Static Executive Market Intelligence Dashboard
setlocal
if exist "D:\Python\Python312\python.exe" (
    set "PYTHON_EXE=D:\Python\Python312\python.exe"
) else (
    set "PYTHON_EXE=python"
)
echo Starting Static Executive Dashboard on http://localhost:8501 ...
set "APP_INITIAL_MODE=STATIC"
"%PYTHON_EXE%" "%~dp0launch_static.py"
if not "%1"=="--no-pause" pause