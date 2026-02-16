#!/bin/bash
# Script para iniciar a aplicação web ReconZZer

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

echo -e "${BLUE}${BOLD}╔════════════════════════════════════╗${NC}"
echo -e "${BLUE}${BOLD}║   🔍 ReconZZer Web Interface    ║${NC}"
echo -e "${BLUE}${BOLD}╚════════════════════════════════════╝${NC}\n"

# ===== VERIFICAR PYTHON =====
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 não está instalado${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1)
echo -e "${GREEN}✓ ${PYTHON_VERSION}${NC}"

# ===== PREPARAR AMBIENTE =====
VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}ℹ Criando ambiente virtual...${NC}"
    python3 -m venv "$VENV_DIR"
fi

echo -e "${YELLOW}ℹ Ativando ambiente virtual...${NC}"
source "$VENV_DIR/bin/activate"

# ===== INSTALAR DEPENDÊNCIAS PYTHON =====
echo -e "${YELLOW}ℹ Atualizando pip...${NC}"
pip install --quiet --upgrade pip setuptools wheel

echo -e "${YELLOW}ℹ Verificando dependências Python...${NC}"

# Lista de dependências obrigatórias
REQUIRED_PACKAGES=("flask" "werkzeug" "requests" "beautifulsoup4")
MISSING_PACKAGES=()

for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! python3 -c "import ${package//-/_}" 2>/dev/null; then
        MISSING_PACKAGES+=("$package")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    echo -e "${YELLOW}⚠  Instalando pacotes: ${MISSING_PACKAGES[*]}${NC}"
    
    # Tentar instalar
    if ! pip install --quiet "${MISSING_PACKAGES[@]}" 2>/dev/null; then
        echo -e "${RED}✗ Erro ao instalar dependências${NC}"
        echo -e "${YELLOW}Tentando com privilégios de root...${NC}"
        
        if sudo -n true 2>/dev/null; then
            # Já tem privilégios sudo sem senha
            sudo pip install "${MISSING_PACKAGES[@]}"
        else
            # Pedir privilégios
            echo -e "${YELLOW}⚠  Privilégios de sudo necessários${NC}"
            sudo pip install "${MISSING_PACKAGES[@]}"
        fi
    fi
fi

echo -e "${GREEN}✓ Dependências Python instaladas${NC}"

# ===== VERIFICAR REQUISITOS DO SISTEMA =====
echo -e "\n${BLUE}${BOLD}Verificando ferramentas do sistema:${NC}"

TOOLS_MISSING=0

check_tool() {
    local tool=$1
    local description=$2
    
    if command -v "$tool" &> /dev/null; then
        echo -e "${GREEN}  ✓ $description${NC}"
        return 0
    else
        echo -e "${YELLOW}  ⚠ $description (faltando)${NC}"
        TOOLS_MISSING=$((TOOLS_MISSING+1))
        return 1
    fi
}

echo -e "${BLUE}Ferramentas Essenciais:${NC}"
check_tool "nmap" "nmap (port scanning)"
check_tool "dig" "dig (DNS queries)"

echo -e "${BLUE}Ferramentas Opcionais:${NC}"
check_tool "subfinder" "subfinder (subdomain enum)"
check_tool "nuclei" "nuclei (vulnerability scan)"
check_tool "theHarvester" "theHarvester (OSINT)"
check_tool "nikto" "nikto (web vulnerabilities)"
check_tool "dirb" "dirb (directory brute-force)"
check_tool "ffuf" "ffuf (fuzzing)"

# ===== AVISOS =====
if [ $TOOLS_MISSING -gt 0 ]; then
    echo -e "\n${YELLOW}⚠  $TOOLS_MISSING ferramentas faltando${NC}"
    echo -e "${YELLOW}A aplicação web funcionará, mas com funcionalidades limitadas${NC}"
    echo -e "${YELLOW}Para instalar todas, execute: sudo ./setup.sh${NC}\n"
fi

# ===== INICIAR SERVIDOR =====
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ Iniciando servidor...${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "${BLUE}${BOLD}📱 Abra seu navegador em:${NC}"
echo -e "${YELLOW}   http://localhost:8080${NC}\n"

echo -e "${YELLOW}Pressione Ctrl+C para encerrar\n${NC}"

# Iniciar Flask (desativar output de warnings)
PYTHONWARNINGS=ignore python3 app.py

