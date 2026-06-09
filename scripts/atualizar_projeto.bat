@echo off
setlocal
cd /d "%~dp0.."

echo Atualizando codigo com git pull...
git pull

if errorlevel 1 (
    echo.
    echo Erro: nao foi possivel atualizar o projeto com git pull.
    pause
    exit /b 1
)

if not exist .venv\Scripts\python.exe (
    echo.
    echo Ambiente .venv nao encontrado.
    echo Execute scripts\configurar_ambiente.bat primeiro.
    pause
    exit /b 1
)

echo.
echo Atualizando dependencias...
.venv\Scripts\python.exe -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Erro: falha ao atualizar dependencias.
    pause
    exit /b 1
)

echo.
echo Projeto atualizado com sucesso.
pause
