@echo off
title Run Full Validation Test Suite
setlocal
if exist "D:\Python\Python312\python.exe" (
    set "PYTHON_EXE=D:\Python\Python312\python.exe"
) else (
    set "PYTHON_EXE=python"
)
cd /d "%~dp0..\.."
echo Running 29 Automated Validation Tests...
"%PYTHON_EXE%" -m pytest "%~dp0..\..\MODEL\validation\tests" -v -p no:cacheprovider
if exist ".pytest_cache" rmdir /s /q ".pytest_cache"
if not "%1"=="--no-pause" pause