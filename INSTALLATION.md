# 📖 ReconZZer - Guia de Instalação

## 🌐 Compatibilidade

| SO | Versão | Status | Package Manager |
|---|---|---|---|
| **macOS** | 10.15+ | ✅ Suportado | Homebrew |
| **Ubuntu/Debian** | 18.04+ | ✅ Suportado | apt |
| **RHEL/CentOS** | 8+ | ✅ Suportado | dnf/yum |
| **Windows** | 10+ | ⚠️ WSL2 | bash via WSL |

## 🚀 Instalação Rápida

### 1. Clone o Repositório
```bash
git clone <repository>
cd ReconZZer
```

### 2. Dar Permissões de Execução
```bash
chmod +x run.sh setup.sh check_deps.py
```

### 3. Iniciar
```bash
./run.sh
```

O script irá:
- ✅ Verificar Python 3
- ✅ Criar ambiente virtual (venv)
- ✅ Instalar dependências Python
- ✅ Verificar ferramentas do sistema
- ✅ Mostrar instruções de instalação faltantes
- ✅ Iniciar servidor web

## 🔧 Instalação por Sistema Operacional

### 🍎 macOS

#### Requisitos Prévios
```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verificar Python3
python3 --version
```

#### Instalação Rápida
```bash
chmod +x run.sh setup.sh
./run.sh
```

#### Instalação Completa (com todas as ferramentas)
```bash
chmod +x run.sh setup.sh
sudo ./setup.sh
./run.sh
```

**Detalhes**: Veja [MACOS_SETUP.md](MACOS_SETUP.md)

---

### 🐧 Ubuntu/Debian

#### Requisitos Prévios
```bash
# Atualizar pacotes
sudo apt update && sudo apt upgrade -y

# Verificar Python3
python3 --version

# Se não tiver Python
sudo apt install python3 python3-venv python3-pip
```

#### Instalação Rápida
```bash
chmod +x run.sh setup.sh
./run.sh
```

#### Instalação Completa
```bash
chmod +x run.sh setup.sh
sudo ./setup.sh
./run.sh
```

---

### 🎩 RHEL/CentOS

#### Requisitos Prévios
```bash
# Atualizar pacotes
sudo dnf update -y

# Instalar Python
sudo dnf install python3 python3-pip

# Verificar
python3 --version
```

#### Instalação Rápida
```bash
chmod +x run.sh setup.sh
./run.sh
```

#### Instalação Completa
```bash
chmod +x run.sh setup.sh
sudo ./setup.sh
./run.sh
```

---

### 🪟 Windows (via WSL2)

#### Configuração WSL2
```bash
# No PowerShell (como admin):
wsl --install -d Ubuntu

# Então dentro do WSL:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv
```

#### Instalação
Mesmo processo de Ubuntu/Debian acima

---

## 📋 O que cada script faz

### `run.sh` - Inicia a Aplicação
```bash
./run.sh
```

**Ações**:
1. ✅ Verifica Python 3
2. ✅ Cria/ativa venv
3. ✅ Instala dependências Python (Flask, Werkzeug, etc)
4. ✅ Verifica ferramentas do sistema
5. ✅ Inicia servidor Flask em http://localhost:8080

**Notas**:
- Não requer `sudo`
- Automaticamente instala pacotes Python faltantes
- Avisa sobre ferramentas do sistema faltantes

---

### `setup.sh` - Instala Ferramentas do Sistema
```bash
sudo ./setup.sh
```

**Ações**:
1. ✅ Detecta o SO automaticamente
2. ✅ Instala ferramentas essenciais (nmap, dig, etc)
3. ✅ Instala Go (para ferramentas Go)
4. ✅ Instala ferramentas via Go (subfinder, nuclei, ffuf)
5. ✅ Instala ferramentas adicionais (nikto, dirb)
6. ✅ Instala python-nmap
7. ✅ Configura PATH permanentemente

**Requer `sudo`** (privilégios de administrador)

---

### `check_deps.py` - Verifica Dependências
```bash
python3 check_deps.py
```

**Mostra**:
- ✅ Pacotes Python instalados
- ⚠️ Ferramentas do sistema faltando
- 📋 Comandos para instalar faltantes

---

## 📦 Dependências

### Python (via pip)
```
flask>=2.3.0          # Web framework
werkzeug>=2.3.0       # WSGI utilities
requests>=2.31.0      # HTTP client
beautifulsoup4>=4.12  # HTML parsing
```

### Sistema (via package manager)
```
Essenciais:
  - nmap              (port scanning)
  - dig               (DNS queries)

Opcionais:
  - subfinder         (subdomain enumeration)
  - nuclei            (vulnerability scanning)
  - ffuf              (fuzzing)
  - nikto             (web scanner)
  - dirb              (directory brute-force)
  - python-nmap       (Python binding)
```

---

## 🔍 Verificar Instalação

```bash
# Verificar dependências
python3 check_deps.py

# Verificar Python packages
python3 -m pip list | grep -E "flask|werkzeug|requests|beautifulsoup4"

# Verificar ferramentas
nmap --version
dig --version
```

---

## ⚠️ Solução de Problemas

### ❌ "Permission denied" ao executar scripts
```bash
chmod +x run.sh setup.sh check_deps.py
./run.sh
```

### ❌ "ModuleNotFoundError: No module named 'flask'"
```bash
# Instalar manualmente
pip3 install flask werkzeug requests beautifulsoup4

# Ou
./run.sh  # Fará automaticamente
```

### ❌ "nmap: command not found"
```bash
# Opção 1: Via setup.sh
sudo ./setup.sh

# Opção 2: Manualmente
# macOS: brew install nmap
# Ubuntu: sudo apt install nmap
# RHEL: sudo dnf install nmap
```

### ❌ "Port 8080 already in use"
```bash
# Encontrar processo
lsof -i :8080

# Matar processo (ou editar app.py para porta diferente)
kill -9 <PID>
```

### ❌ "sudo: ./setup.sh: command not found"
```bash
chmod +x setup.sh
sudo ./setup.sh
```

### ❌ Erro de "go: command not found"
```bash
# O setup.sh tenta instalar Go automaticamente
# Se falhar, instale manualmente:
# macOS: brew install go
# Ubuntu: sudo apt install golang-go
# RHEL: sudo dnf install golang
```

---

## 📊 Fluxo de Instalação

```
./run.sh
    ↓
Verifica Python3 ✓
    ↓
Cria/Ativa venv ✓
    ↓
Instala dependências Python ✓
    ↓
Verifica ferramentas sistema
    ↓
├─ Essenciais presentes? → Continue
└─ Faltando → Avisa sobre setup.sh
    ↓
Inicia Flask em :8080 ✓
```

---

## 🎯 Próximos Passos

Após instalação bem-sucedida:

1. **Abrir navegador**: http://localhost:8080
2. **Ir para aba "Install"**: Ver status de todas as dependências
3. **Ir para aba "Scan"**: Começar a usar a aplicação
4. **Ler [WEB_README.md](WEB_README.md)**: Para guia de uso completo

---

## 💡 Dicas

- 💾 **Guardar configurações**: Use arquivo `.env` para variáveis
- 🚀 **Performance**: Ferramentas Go (subfinder, nuclei) são as mais rápidas
- 🔐 **Segurança**: Execute nmap com cuidado em redes que você não possui
- 📊 **Logs**: Verifique `logs/` para histórico de varreduras
- 🌐 **Produção**: Para deploy, use gunicorn ou similar

---

## 📞 Suporte

Se encontrar problemas:

1. Executar: `python3 check_deps.py`
2. Verificar: `python3 --version`
3. Ler: [MACOS_SETUP.md](MACOS_SETUP.md) (se no macOS)
4. Verificar logs em `logs/`

---

**Última atualização**: 2024 | **Mantido por**: ReconZZer Team
