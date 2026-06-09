@echo off
setlocal
cd /d "%~dp0.."

echo Criando ambiente virtual .venv...

where py >nul 2>nul
if not errorlevel 1 (
    py -3.10 -m venv .venv
) else (
    python -m venv .venv
)

if errorlevel 1 (
    echo.
    echo Erro: nao foi possivel criar o ambiente virtual.
    echo Verifique se o Python 3.10.x esta instalado.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat

echo.
echo Atualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando dependencias do projeto...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Erro: falha ao instalar dependencias.
    pause
    exit /b 1
)

echo.
echo Ambiente configurado com sucesso.
pause
