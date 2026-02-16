# 🍎 ReconZZer no macOS - Guia de Setup

## Pré-requisitos

### 1️⃣ Python 3
Verifique se você tem Python 3 instalado:
```bash
python3 --version
```

Se não tiver: `brew install python3`

### 2️⃣ Homebrew (Package Manager)
Instale o Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## ⚡ Início Rápido

### Opção A: Instalação Completa (Recomendado)
```bash
# 1. Instalar ferramentas do sistema
sudo ./setup.sh

# 2. Iniciar a aplicação
./run.sh
```

### Opção B: Instalação Mínima (Web apenas)
```bash
# Instalar apenas dependências web
python3 -m venv venv
source venv/bin/activate
pip install flask werkzeug requests beautifulsoup4

# Iniciar a aplicação
./run.sh
```

## 📋 Ferramentas Disponíveis

### Essenciais (para scanning básico)
- **nmap** - Network mapping
- **dig** - DNS queries

Instalar: `brew install nmap bind-tools`

### Opcionais (recursos avançados)
- **subfinder** - Subdomain enumeration → `brew install subfinder`
- **nuclei** - Vulnerability scanning → `brew install nuclei`
- **ffuf** - Web fuzzing → `brew install ffuf`
- **nikto** - Web scanner → `brew install nikto`
- **dirb** - Directory brute-force → `brew install dirb`

## 🔧 Solução de Problemas

### ❌ "python3: command not found"
```bash
brew install python3
```

### ❌ "Permission denied" ao executar run.sh
```bash
chmod +x run.sh setup.sh check_deps.py
```

### ❌ Erro de "pip not found"
```bash
python3 -m pip --version
python3 -m pip install --upgrade pip
```

### ❌ Erro ao instalar via Homebrew
```bash
# Atualizar Homebrew
brew update
brew upgrade

# Tentar novamente
sudo ./setup.sh
```

### ❌ Port 8080 já em uso
Editar `app.py` e modificar:
```python
# Mudar de:
app.run(host='0.0.0.0', port=8080, debug=False)

# Para:
app.run(host='0.0.0.0', port=8081, debug=False)
```

## 📱 Testando a Aplicação

1. Executar: `./run.sh`
2. Abrir no navegador: `http://localhost:8080`
3. Ir para aba "Install" para verificar dependências
4. Usar aba "Scan" para iniciar reconhecimento

## 🔐 Segurança

Algumas ferramentas requerem `sudo` no macOS:
- Nmap (scanning de baixo nível)
- Setup.sh (instalação de pacotes)

Isso é normal e esperado.

## 📞 Suporte

Se encontrar problemas:

1. Verificar dependências: `python3 check_deps.py`
2. Verificar Python: `python3 --version`
3. Verificar venv: `source venv/bin/activate && python3 -c "import flask"`

## 📚 Documentação Relacionada

- [README.md](README.md) - Overview geral
- [WEB_README.md](WEB_README.md) - Documentação web
- [START.md](START.md) - Guia de início

---

**Última atualização**: 2024 | **Testado em**: macOS 12+
