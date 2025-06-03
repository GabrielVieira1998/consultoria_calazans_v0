@echo off
echo Iniciando configuracao do projeto Calazans Python...

REM Verificar se o Python 3 está instalado
python --version 2>NUL
if %ERRORLEVEL% NEQ 0 (
    echo Python nao encontrado. Por favor, instale o Python e tente novamente.
    exit /b 1
)

REM Criar ambiente virtual
echo Criando ambiente virtual...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo Erro ao criar ambiente virtual. Verifique se o modulo venv esta instalado.
    exit /b 1
)
echo Ambiente virtual criado com sucesso!

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo Erro ao ativar ambiente virtual.
    exit /b 1
)
echo Ambiente virtual ativado!

REM Instalar dependências
echo Instalando dependencias...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Erro ao instalar dependencias.
    exit /b 1
)
echo Dependencias instaladas com sucesso!

REM Configurar variável de ambiente
echo Configurando variaveis de ambiente...
set FLASK_APP=app.py
set FLASK_ENV=development

REM Inicializar o banco de dados
echo Inicializando banco de dados...
flask init-db
if %ERRORLEVEL% NEQ 0 (
    echo Erro ao inicializar banco de dados.
    exit /b 1
)
echo Banco de dados inicializado com sucesso!

echo Configuracao concluida!
echo.
echo Para executar o projeto, use os seguintes comandos:
echo   venv\Scripts\activate
echo   flask run
echo O site estara disponivel em http://127.0.0.1:5000/

pause 