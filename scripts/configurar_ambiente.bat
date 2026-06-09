@echo off
setlocal
cd /d "%~dp0.."

echo Configurando o ambiente do projeto com Python 3.10...
echo.

rem O uv baixa e gerencia uma versao isolada do Python para este projeto.
rem Assim, nao precisamos alterar nem fazer downgrade do Python global do Windows.
where uv >nul 2>nul
if errorlevel 1 (
    echo uv nao encontrado. Instalando uv automaticamente...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    if errorlevel 1 (
        echo.
        echo Erro: nao foi possivel instalar o uv.
        echo Verifique a internet ou peca ajuda ao professor.
        pause
        exit /b 1
    )

    set "PATH=%USERPROFILE%\.local\bin;%USERPROFILE%\.cargo\bin;%PATH%"
)

where uv >nul 2>nul
if errorlevel 1 (
    echo.
    echo Erro: uv instalado, mas ainda nao encontrado no PATH.
    echo Feche este terminal, abra novamente e execute este script outra vez.
    pause
    exit /b 1
)

echo.
echo Baixando/garantindo Python 3.10 para o projeto...
uv python install 3.10

if errorlevel 1 (
    echo.
    echo Erro: nao foi possivel instalar o Python 3.10 com uv.
    pause
    exit /b 1
)

echo.
echo Criando ambiente virtual .venv com Python 3.10...
uv venv .venv --python 3.10

if errorlevel 1 (
    echo.
    echo Erro: nao foi possivel criar o ambiente virtual .venv.
    pause
    exit /b 1
)

echo.
echo Instalando dependencias do requirements.txt...
uv pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Erro: falha ao instalar dependencias.
    pause
    exit /b 1
)

echo.
echo Ambiente configurado com sucesso.
echo O VS Code deve usar: .venv\Scripts\python.exe
pause
