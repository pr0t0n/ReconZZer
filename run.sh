#!/bin/bash
# Script para iniciar a aplicação web ReconZZer

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   🔍 ReconZZer Web Interface    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════╝${NC}\n"

# Verificar se Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 não está instalado${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Python 3 encontrado$(python3 --version)${NC}"

# Verificar se venv existe, senão criar
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}ℹ Criando ambiente virtual...${NC}"
    python3 -m venv venv
fi

# Ativar venv
echo -e "${YELLOW}ℹ Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Instalar dependências
echo -e "${YELLOW}ℹ Verificando dependências Python...${NC}"
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

echo -e "${GREEN}✓ Todas as dependências instaladas${NC}\n"

# Verificar se os requisitos do sistema estão instalados
echo -e "${BLUE}Verificando requisitos do sistema:${NC}"

check_tool() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}  ✓ $1${NC}"
        return 0
    else
        echo -e "${RED}  ✗ $1${NC}"
        return 1
    fi
}

MISSING=0
check_tool "nmap" || MISSING=$((MISSING+1))
check_tool "dig" || MISSING=$((MISSING+1))
check_tool "nmap" || MISSING=$((MISSING+1))

if [ $MISSING -gt 0 ]; then
    echo -e "\n${YELLOW}⚠  Alguns requisitos do sistema estão faltando.${NC}"
    echo -e "${YELLOW}   Execute: sudo ./setup.sh${NC}"
    echo -e "${YELLOW}   A aplicação web irá mostrar detalhes após iniciar.${NC}\n"
fi

# Iniciar a aplicação
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ Iniciando servidor...${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
echo -e "${BLUE}📱 Abra seu navegador em:${NC}"
echo -e "${YELLOW}   http://localhost:8080${NC}\n"
echo -e "${YELLOW}Pressione Ctrl+C para encerrar${NC}\n"

# Iniciar Flask
python3 app.py
