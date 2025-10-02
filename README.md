# AutoRecon

**AutoRecon** é um projeto de automação da fase de Reconhecimento (RECON) do Cyber Kill Chain, utilizando ferramentas de código aberto e técnicas de OSINT (Open-Source Intelligence), Port Scan, SubDomain Listing, DNS DIG, varredura de vulnerabilidades web e fuzzing. O objetivo é fornecer um script Python que automatize a coleta de informações sobre um domínio alvo e gere relatórios em formatos JSON e HTML.

## Funcionalidades

*   **Enumeração de Subdomínios:** Utiliza `subfinder` para descobrir subdomínios associados a um domínio alvo.
*   **Informações DNS:** Coleta registros DNS (A, MX, NS, TXT) usando `dig`.
*   **Varredura de Portas:** Realiza varreduras rápidas de portas usando `nmap` no domínio principal e em subdomínios selecionados.
*   **OSINT com TheHarvester:** Coleta informações de fontes abertas como e-mails, subdomínios, hosts, nomes de funcionários, etc.
*   **Varredura de Vulnerabilidades Web com Nikto:** Identifica vulnerabilidades e configurações incorretas em servidores web.
*   **Varredura de Vulnerabilidades e Informações com Nuclei:** Utiliza templates para detectar vulnerabilidades, configurações erradas e expor informações.
*   **Enumeração de Diretórios com Dirb:** Busca por diretórios e arquivos ocultos em servidores web.
*   **Fuzzing com FFUF:** Realiza fuzzing para descobrir recursos ocultos, parâmetros e vulnerabilidades.
*   **OSINT Brazuca:** Utiliza uma lista de URLs do projeto OSINT Brazuca para análise de fontes abertas brasileiras.
*   **Geração de Relatórios:** Produz relatórios detalhados em JSON e HTML para fácil análise e visualização.

## Estrutura do Projeto

```
AutoRecon/
├── recon_script.py
├── requirements.txt
├── setup.sh
├── reports/
│   ├── recon_report_example.com.json
│   └── recon_report_example.com.html
└── osint_data/
    └── OSINT.txt # Arquivo com URLs do OSINT Brazuca
```

*   `recon_script.py`: O script principal de automação do RECON.
*   `requirements.txt`: Lista as dependências Python necessárias.
*   `setup.sh`: Script para instalar as dependências do sistema operacional.
*   `reports/`: Diretório para armazenar os relatórios gerados (JSON e HTML).
*   `osint_data/OSINT.txt`: Arquivo contendo URLs relevantes para OSINT no contexto brasileiro, extraídas do projeto OSINT Brazuca.

## Instalação

Para configurar o ambiente e instalar todas as dependências necessárias, siga os passos abaixo:

### 1. Instalar Dependências do Sistema Operacional

Execute o script `setup.sh` para instalar as ferramentas de linha de comando como `git`, `wget`, `nmap`, `dnsutils`, `go`, `subfinder`, `nuclei`, `theHarvester`, `nikto`, `dirb` e `ffuf`. Este script é projetado para sistemas baseados em Debian/Ubuntu.

```bash
chmod +x setup.sh
./setup.sh
```

### 2. Instalar Dependências Python

Instale as dependências Python usando `pip`:

```bash
pip install -r requirements.txt
```

## Como Usar

Para executar o script, navegue até o diretório `AutoRecon` e utilize o seguinte comando, substituindo `seualvo.com` pelo domínio desejado:

```bash
python3 recon_script.py -d seualvo.com
```

Os relatórios `recon_report_seualvo.com.json` e `recon_report_seualvo.com.html` serão gerados no diretório `reports/`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, novas funcionalidades ou correções de bugs.
