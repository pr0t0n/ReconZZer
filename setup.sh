#!/bin/bash
# Setup script para instalar dependências do ReconZZer
# Compatível com Debian/Ubuntu

set -e  # Sair em caso de erro

log_info() {
    echo -e "\033[1;32m[✓]\033[0m $1"
}

log_warn() {
    echo -e "\033[1;33m[!]\033[0m $1"
}

log_error() {
    echo -e "\033[1;31m[✗]\033[0m $1" >&2
}

# Verificar se é root
if [[ $EUID -ne 0 ]]; then
    log_error "Este script deve ser executado como root (use sudo)"
    exit 1
fi

log_info "Atualizando pacotes do sistema..."
apt update && apt upgrade -y

log_info "Instalando ferramentas essenciais: git, wget, nmap, dnsutils..."
apt install -y git wget nmap dnsutils

log_info "Instalando Go (Golang)..."
apt install -y golang-go

# Configurar GOPATH
export GOPATH=${GOPATH:-$HOME/go}
export PATH=$PATH:$GOPATH/bin

log_info "Instalando subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

log_info "Instalando nuclei..."
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

log_info "Instalando FFUF..."
go install -v github.com/ffuf/ffuf@latest

log_info "Instalando TheHarvester..."
pip3 install theHarvester

log_info "Instalando Nikto..."
apt install -y nikto

log_info "Instalando Dirb..."
apt install -y dirb

# Adicionar GOPATH ao PATH permanentemente
if ! grep -q "export GOPATH=" ~/.bashrc; then
    echo "export GOPATH=\"${GOPATH}\"" >> ~/.bashrc
    log_info "GOPATH adicionado ao ~/.bashrc"
fi

if ! grep -q "$GOPATH/bin" ~/.bashrc; then
    echo "export PATH=\"\$PATH:${GOPATH}/bin\"" >> ~/.bashrc
    log_info "PATH do Go adicionado ao ~/.bashrc"
fi

log_info "Instalação concluída com sucesso!"
log_warn "Execute o seguinte comando para aplicar as alterações de PATH:"
echo "    source ~/.bashrc"
