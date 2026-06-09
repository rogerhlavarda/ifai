@echo off
setlocal
cd /d "%~dp0.."

where code >nul 2>nul
if errorlevel 1 (
    echo O comando "code" nao foi encontrado no PATH.
    echo Abra o VS Code manualmente e escolha: Arquivo ^> Abrir Pasta.
    pause
    exit /b 1
)

code .
exit /b 0
