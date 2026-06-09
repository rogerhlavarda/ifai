@echo off
setlocal
cd /d "%~dp0.."

set "PYTHON_EXE=.venv\Scripts\python.exe"

if not exist "%PYTHON_EXE%" (
    echo Ambiente virtual .venv nao encontrado.
    echo Execute scripts\configurar_ambiente.bat primeiro.
    pause
    exit /b 1
)

echo Verificando versao do Python...
"%PYTHON_EXE%" --version

rem O MediaPipe usado no projeto e compativel com Python 3.10.x.
rem Esta checagem evita que o aluno rode sem perceber com outra versao.
"%PYTHON_EXE%" -c "import sys; raise SystemExit(0 if sys.version_info[:2] == (3, 10) else 1)"

if errorlevel 1 (
    echo.
    echo Erro: o ambiente .venv nao esta usando Python 3.10.x.
    echo Execute scripts\configurar_ambiente.bat novamente.
    pause
    exit /b 1
)

echo Python 3.10.x confirmado.

echo.
echo Testando bibliotecas do projeto...
"%PYTHON_EXE%" -c "import cv2; print('OpenCV OK')"
if errorlevel 1 goto erro_import

"%PYTHON_EXE%" -c "import mediapipe; print('MediaPipe OK')"
if errorlevel 1 goto erro_import

"%PYTHON_EXE%" -c "import pyfirmata; print('pyFirmata OK')"
if errorlevel 1 goto erro_import

"%PYTHON_EXE%" -c "import serial; print('pyserial OK')"
if errorlevel 1 goto erro_import

echo.
echo Tudo certo: ambiente verificado com sucesso.
pause
exit /b 0

:erro_import
echo.
echo Erro: alguma biblioteca nao foi encontrada.
echo Execute scripts\configurar_ambiente.bat para instalar as dependencias.
pause
exit /b 1
