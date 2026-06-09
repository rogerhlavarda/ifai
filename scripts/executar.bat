@echo off
setlocal
cd /d "%~dp0.."

set "PYTHON_EXE=.venv\Scripts\python.exe"

if not exist "%PYTHON_EXE%" (
    echo Ambiente virtual .venv nao encontrado.
    echo Execute scripts\configurar_ambiente.bat antes de executar o projeto.
    pause
    exit /b 1
)

.venv\Scripts\python.exe app\main.py
pause
