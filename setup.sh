#!/bin/bash

# Script para instalar as dependências do sistema operacional para o AutoRecon (Debian/Ubuntu)

echo "[+] Atualizando pacotes do sistema..."
sudo apt update
sudo apt upgrade -y

echo "[+] Instalando ferramentas essenciais: git, wget, nmap, dnsutils (para dig)..."
sudo apt install -y git wget nmap dnsutils -y

echo "[+] Instalando Go (Golang) para subfinder e nuclei..."
sudo apt install -y golang

# Configurar GOPATH e adicionar binários do Go ao PATH
export GOPATH=${GOPATH:-$HOME/go}
export PATH=$PATH:$GOPATH/bin

echo "[+] Instalando subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

echo "[+] Instalando nuclei..."
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

echo "[+] Instalando TheHarvester..."
pip3 install theHarvester

echo "[+] Instalando Nikto..."
sudo apt install -y nikto

echo "[+] Instalando Dirb (para enumeração de diretórios)..."
sudo apt install -y dirb

echo "[+] Instalando FFUF (para fuzzing e enumeração avançada)..."
go install -v github.com/ffuf/ffuf@latest

# Adicionar o diretório de binários do Go ao PATH permanentemente (para o usuário atual)
if ! grep -q "export GOPATH=\"${GOPATH}\"" ~/.bashrc; then
    echo "export GOPATH=\"${GOPATH}\"" >> ~/.bashrc
fi

if ! grep -q "export PATH=\"$PATH\"" ~/.bashrc; then
    echo "export PATH=\"$PATH\"" >> ~/.bashrc
fi

echo "[+] Instalação das dependências do sistema e Python concluída."

