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

# ReconZZer

**ReconZZer** é um framework de automação para a fase de **Reconhecimento** do Cyber Kill Chain. Integra ferramentas de código aberto para **OSINT**, **Port Scanning**, **Enumeração de Subdomínios**, **Análise DNS**, **Varredura de Vulnerabilidades** e **Fuzzing**, gerando relatórios detalhados em JSON e HTML.

Agora com **Interface Web Moderna** para facilitar o uso!

## 🎯 Funcionalidades

### Core
- **Enumeração de Subdomínios** - Subfinder
- **Análise DNS** - Coleta de registros A, MX, NS, TXT com `dig`
- **Varredura de Portas** - Nmap (domínio principal e subdomínios)
- **OSINT** - TheHarvester + URLs Brazuca
- **Varredura Web** - Nikto, Nuclei, Dirb, FFUF
- **Relatórios** - JSON e HTML interativo

### Web Interface
- 🌐 Dashboard moderno e responsivo
- ✅ Verificação automática de requisitos
- 📊 Monitoramento de progresso em tempo real
- 📁 Histórico de relatórios
- 💾 Download de relatórios (JSON/HTML)
- 📱 Interface mobile-friendly

## 📋 Pré-requisitos

- **Debian/Ubuntu Linux**
- **Python 3.8+**
- **Privilégios sudo** (para instalação de ferramentas)

## 🚀 Instalação Rápida

### 1. Instalar Dependências do Sistema

```bash
chmod +x setup.sh
sudo ./setup.sh
source ~/.bashrc
```

### 2. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

### 3. Usar ReconZZer

**Web Interface (Recomendado):**
```bash
./run.sh
```

**Ou via CLI:**
```bash
python3 recon_script.py -d exemplo.com
```

## 💻 Uso

### Opção 1: Interface Web (Recomendado)

**Mais fácil e intuitivo!**

```bash
chmod +x run.sh
./run.sh
```

Abra seu navegador em: **http://localhost:8080**

A interface web irá:
1. ✅ Verificar todos os requisitos
2. 📋 Mostrar guia de instalação se necessário
3. 🖥️ Fornecer dashboard para iniciar varreduras
4. 📊 Monitorar progresso em tempo real
5. 📁 Exibir histórico de relatórios

**Documentação completa:** [WEB_README.md](WEB_README.md)

### Opção 2: Linha de Comando

```bash
python3 recon_script.py -d seu-dominio.com
```

Os relatórios serão salvos em `reports/`:
- `recon_report_seu-dominio.com.json`
- `recon_report_seu-dominio.com.html`

## 📂 Estrutura do Projeto

```
ReconZZer/
├── app.py                      # Aplicação Flask
├── recon_script.py             # Script de reconhecimento
├── requirements.txt            # Dependências Python
├── run.sh                      # Script para iniciar web
├── setup.sh                    # Instalação de ferramentas
├── pyproject.toml              # Configuração Python
├── .gitignore                  # Git ignore
├── WEB_README.md               # Documentação da web
├── README.md                   # Este arquivo
├── SECURITY.md                 # Avisos legais
├── cyber_kill_chain_recon.md   # Contexto teórico
├── recon_tools_methods.md      # Documentação técnica
├── templates/                  # Templates Flask
│   ├── base.html
│   ├── dashboard.html
│   ├── install.html
│   └── error.html
├── static/                     # Arquivos estáticos
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── osint_data/
│   └── OSINT.txt               # URLs OSINT Brazuca
└── reports/                    # Relatórios gerados
    ├── *.json
    └── *.html
```

## 🔧 Configuração Avançada

### Ajustar Timeouts

Editar em `recon_script.py`:
```python
DEFAULT_TIMEOUT = 300        # 5 minutos
ENHANCED_TIMEOUT = 600       # 10 minutos
```

### Limitar Subdomínios

No `main()`, mudar:
```python
for subdomain in recon_data["subdomains"][:N]:  # N = número de subdomínios
```

### Mudar Targets de OSINT

Editar `osint_data/OSINT.txt` com suas URLs

## ⚠️ Avisos Legais

- **Uso único para teste autorizado** em ambientes que você possui ou tem permissão
- Respeite legislações locais
- Não realize varreduras não autorizadas
- Use apenas para fins educacionais ou profissionais legítimos

## 📚 Documentação Adicional

- [🚀 QUICKSTART.md](QUICKSTART.md) - **COMECE AQUI** - Guia de início rápido (5 minutos)
- [💻 WEB_README.md](WEB_README.md) - Documentação completa da interface web
- [cyber_kill_chain_recon.md](cyber_kill_chain_recon.md) - Contexto do Cyber Kill Chain
- [recon_tools_methods.md](recon_tools_methods.md) - Detalhes das ferramentas
- [🤝 CONTRIBUTING.md](CONTRIBUTING.md) - Guia para contribuições
- [🔒 SECURITY.md](SECURITY.md) - Avisos legais e melhores práticas

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:
1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é fornecido como está para fins educacionais e de pesquisa.

## 👨‍💻 Autor

**pr0t0n**

---

**Última atualização:** Fevereiro de 2026
