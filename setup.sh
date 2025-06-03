#!/bin/bash

# Cores para o output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Iniciando configuração do projeto Calazans Python...${NC}"

# Verificar se o Python 3 está instalado
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}Python 3 encontrado!${NC}"
else
    echo "Python 3 não encontrado. Por favor, instale o Python 3 e tente novamente."
    exit 1
fi

# Criar ambiente virtual
echo -e "${YELLOW}Criando ambiente virtual...${NC}"
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Erro ao criar ambiente virtual. Verifique se o módulo venv está instalado."
    exit 1
fi
echo -e "${GREEN}Ambiente virtual criado com sucesso!${NC}"

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Erro ao ativar ambiente virtual."
    exit 1
fi
echo -e "${GREEN}Ambiente virtual ativado!${NC}"

# Instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Erro ao instalar dependências."
    exit 1
fi
echo -e "${GREEN}Dependências instaladas com sucesso!${NC}"

# Inicializar o banco de dados
echo -e "${YELLOW}Inicializando banco de dados...${NC}"
flask init-db
if [ $? -ne 0 ]; then
    echo "Erro ao inicializar banco de dados."
    exit 1
fi
echo -e "${GREEN}Banco de dados inicializado com sucesso!${NC}"

echo -e "${GREEN}Configuração concluída!${NC}"
echo -e "Para executar o projeto, use os seguintes comandos:"
echo -e "  source venv/bin/activate"
echo -e "  flask run"
echo -e "O site estará disponível em http://127.0.0.1:5000/" 