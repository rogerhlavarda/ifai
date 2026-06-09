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
