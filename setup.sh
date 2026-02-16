#!/bin/bash
# Setup script para instalar dependências do ReconZZer
# Suporta: macOS (Homebrew), Debian/Ubuntu (apt), RHEL/CentOS (yum/dnf)

set -e

# ===== CORES =====
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# ===== LOGS =====
log_info() {
    echo -e "${GREEN}[✓]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[!]${NC} $1"
}

log_error() {
    echo -e "${RED}[✗]${NC} $1" >&2
}

log_debug() {
    echo -e "${BLUE}[ℹ]${NC} $1"
}

# ===== BANNER =====
echo -e "${BLUE}${BOLD}╔════════════════════════════════════╗${NC}"
echo -e "${BLUE}${BOLD}║  🔧 ReconZZer Setup             ║${NC}"
echo -e "${BLUE}${BOLD}╚════════════════════════════════════╝${NC}\n"

# ===== VERIFICAR PRIVILÉGIOS =====
if [[ $EUID -ne 0 ]]; then
    log_warn "Este script requer privilégios de administrador"
    echo -e "${YELLOW}Executando com sudo...${NC}\n"
    
    # Re-executar com sudo
    exec sudo bash "$0" "$@"
fi

# ===== DETECTAR SO =====
detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [ -f /etc/os-release ]; then
        . /etc/os-release
        if [[ "$ID" == "ubuntu" ]] || [[ "$ID" == "debian" ]]; then
            echo "debian"
        elif [[ "$ID" == "fedora" ]] || [[ "$ID" == "rhel" ]] || [[ "$ID" == "centos" ]]; then
            echo "rhel"
        else
            echo "unknown"
        fi
    else
        echo "unknown"
    fi
}

OS=$(detect_os)

case "$OS" in
    macos)
        log_info "Detectado: macOS"
        BREW_PATH=$(command -v brew || echo "/usr/local/bin/brew")
        if ! command -v brew &> /dev/null; then
            log_warn "Homebrew não encontrado"
            log_info "Instalando Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        PKG_MANAGER="brew"
        ;;
    debian)
        log_info "Detectado: Debian/Ubuntu"
        apt update -qq
        PKG_MANAGER="apt"
        ;;
    rhel)
        log_info "Detectado: RHEL/CentOS"
        PKG_MANAGER="dnf"
        ;;
    *)
        log_error "SO não suportado"
        exit 1
        ;;
esac

# ===== INSTALAR FERRAMENTAS =====
install_packages() {
    local -n arr=$1
    local installer=$2
    
    case "$installer" in
        apt)
            log_debug "apt install -y ${arr[*]}"
            apt install -y "${arr[@]}" || {
                log_error "Erro ao instalar pacotes"
                return 1
            }
            ;;
        dnf)
            log_debug "dnf install -y ${arr[*]}"
            dnf install -y "${arr[@]}" || {
                log_error "Erro ao instalar pacotes"
                return 1
            }
            ;;
        brew)
            for pkg in "${arr[@]}"; do
                log_debug "brew install $pkg"
                brew install "$pkg" 2>/dev/null || log_warn "  (Já instalado ou erro: $pkg)"
            done
            ;;
    esac
}

# ===== DEPENDÊNCIAS ESSENCIAIS =====
echo -e "\n${BLUE}${BOLD}Instalando ferramentas essenciais...${NC}"

case "$OS" in
    macos)
        essential_tools=("nmap" "bind-tools" "git")
        ;;
    debian|rhel)
        essential_tools=("nmap" "git" "dnsutils" "wget" "curl")
        ;;
esac

install_packages essential_tools "$PKG_MANAGER"

# ===== GOLANG (para ferramentas Go) =====
if ! command -v go &> /dev/null; then
    echo -e "\n${BLUE}${BOLD}Instalando Go...${NC}"
    case "$OS" in
        macos)
            brew install golang || log_warn "Erro ao instalar Go via Homebrew"
            ;;
        debian)
            apt install -y golang-go || log_warn "Erro ao instalar Go"
            ;;
        rhel)
            dnf install -y golang || log_warn "Erro ao instalar Go"
            ;;
    esac
else
    log_info "Go já está instalado"
fi

# ===== CONFIGURAR GOPATH =====
export GOPATH="${GOPATH:-$HOME/go}"
export PATH="$PATH:$GOPATH/bin"

# ===== FERRAMENTAS GO =====
echo -e "\n${BLUE}${BOLD}Instalando ferramentas Python/Go...${NC}"

install_go_tool() {
    local tool=$1
    local repo=$2
    
    if command -v "$tool" &> /dev/null; then
        log_info "$tool já está instalado"
    else
        log_debug "Instalando $tool..."
        if go install -v "${repo}@latest" 2>/dev/null; then
            log_info "$tool instalado"
        else
            log_warn "$tool falhou"
        fi
    fi
}

install_go_tool "subfinder" "github.com/projectdiscovery/subfinder/v2/cmd/subfinder"
install_go_tool "nuclei" "github.com/projectdiscovery/nuclei/v2/cmd/nuclei"
install_go_tool "ffuf" "github.com/ffuf/ffuf"

# ===== FERRAMENTAS ADICIONAIS =====
echo -e "\n${BLUE}${BOLD}Instalando ferramentas adicionais...${NC}"

case "$OS" in
    macos)
        addl_tools=("nikto" "dirb")
        brew install "${addl_tools[@]}" 2>/dev/null || log_warn "Alguns pacotes podem não estar disponíveis no Homebrew"
        ;;
    debian)
        addl_tools=("nikto" "dirb")
        apt install -y "${addl_tools[@]}" || log_warn "Alguns pacotes falharam"
        ;;
    rhel)
        log_warn "nikto e dirb podem precisar de instalação manual no RHEL"
        ;;
esac

# ===== PYTHON PACKAGES =====
echo -e "\n${BLUE}${BOLD}Instalando pacotes Python...${NC}"

# theHarvester é muito pesado, deixamos opcional
if pip3 list 2>/dev/null | grep -q theHarvester; then
    log_info "theHarvester já está instalado"
else
    log_warn "Instalando theHarvester (pode levar um tempo)..."
    if pip3 install theHarvester 2>/dev/null; then
        log_info "theHarvester instalado"
    else
        log_warn "theHarvester não pôde ser instalado (opcional)"
    fi
fi

# ===== CONFIGURAR PATH PERMANENTEMENTE =====
if [[ "$OS" != "macos" ]]; then
    echo -e "\n${BLUE}${BOLD}Configurando PATH permanentemente...${NC}"
    
    BASHRC="$HOME/.bashrc"
    
    # Adicionar GOPATH
    if ! grep -q "export GOPATH=" "$BASHRC"; then
        echo "export GOPATH=\"${GOPATH}\"" >> "$BASHRC"
        log_info "GOPATH adicionado ao $BASHRC"
    fi
    
    # Adicionar PATH do Go
    if ! grep -q "$GOPATH/bin" "$BASHRC" 2>/dev/null || ! echo "$PATH" | grep -q "$GOPATH/bin"; then
        echo "export PATH=\"\$PATH:${GOPATH}/bin\"" >> "$BASHRC"
        log_info "PATH do Go adicionado"
    fi
fi

# ===== CONCLUSÃO =====
echo -e "\n${GREEN}${BOLD}╔════════════════════════════════════╗${NC}"
echo -e "${GREEN}${BOLD}║  ✓ Setup concluído com sucesso  ║${NC}"
echo -e "${GREEN}${BOLD}╚════════════════════════════════════╝${NC}\n"

log_info "Ferramentas instaladas:"
echo -e "  ${BLUE}• nmap${NC} - Port scanning"
echo -e "  ${BLUE}• dig${NC} - DNS queries"
echo -e "  ${BLUE}• subfinder${NC} - Subdomain enumeration"
echo -e "  ${BLUE}• nuclei${NC} - Vulnerability scanning"
echo -e "  ${BLUE}• ffuf${NC} - Fuzzing"
echo -e "  ${BLUE}• nikto${NC} - Web scanner"
echo -e "  ${BLUE}• dirb${NC} - Directory brute-force"

if [[ "$OS" != "macos" ]]; then
    echo -e "\n${YELLOW}Para aplicar as mudanças de PATH:${NC}"
    echo -e "  ${BOLD}source ~/.bashrc${NC}"
fi

echo -e "\n${BLUE}Próximo passo: Execute ./run.sh${NC}\n"
