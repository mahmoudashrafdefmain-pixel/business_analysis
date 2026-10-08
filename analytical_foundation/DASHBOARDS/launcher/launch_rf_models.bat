@echo off
title Production Random Forest Models Benchmark
setlocal
if exist "D:\Python\Python312\python.exe" (
    set "PYTHON_EXE=D:\Python\Python312\python.exe"
) else (
    set "PYTHON_EXE=python"
)
"%PYTHON_EXE%" "%~dp0launch_rf_models.py"
if not "%1"=="--no-pause" pause