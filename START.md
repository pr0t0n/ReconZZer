# 🧪 Guia de Teste - ReconZZer Web

Este guia vai ajudar você a testar a aplicação web localmente.

## ✅ O que foi Criado

### Backend (app.py)
```python
✓ Verificação automática de requisitos
✓ API REST com 7 endpoints
✓ Execução assíncrona de varreduras
✓ Gestão de relatórios
✓ Tratamento de erros robusto
```

### Frontend
```
✓ Dashboard.html - Interface principal
✓ Install.html - Verificação de requisitos
✓ Base.html - Template base
✓ style.css - Estilos modernos (Gradiente roxo/azul)
✓ script.js - Lógica JavaScript
```

### Estrutura Completa
```
templates/
├── base.html ✓
├── dashboard.html ✓
├── install.html ✓
└── error.html ✓

static/
├── css/
│   └── style.css ✓
└── js/
    └── script.js ✓

app.py ✓
recon_script.py (existente)
requirements.txt (atualizado) ✓
run.sh ✓
test.py ✓
```

## 🚀 Como Testar Localmente

### Passo 1: Clonar o Repositório (com mudanças)

```bash
# Se ainda não clonou
git clone https://github.com/pr0t0n/ReconZZer.git
cd ReconZZer

# Se já clonou, puxe as atualizações
git pull origin main
```

### Passo 2: Preparar o Ambiente

```bash
# Dar permissão ao script
chmod +x run.sh

# Instalar dependências (contém Flask)
pip install flask werkzeug requests beautifulsoup4

# Opcional: criar venv
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Passo 3: Iniciar a Aplicação

#### Opção A: Usar o Script (Recomendado)
```bash
./run.sh
```

#### Opção B: Iniciar Diretamente
```bash
python3 app.py
```

Você deve ver:
```
==================================================
🔍 ReconZZer Web Interface
==================================================

📱 Abra seu navegador em: http://localhost:8080

Pressione Ctrl+C para encerrar
```

### Passo 4: Testar no Navegador

Abra o navegador e vá para:
```
http://localhost:8080
```

## 📋 Testes a Fazer

### Teste 1: Verificação de Requisitos
- [ ] Página abre sem erros
- [ ] Sistema verifica requisitos automaticamente
- [ ] Mostra status visual (checkmark/X)
- [ ] Agrupa requisitos por categoria

### Teste 2: Dashboard
Se todos requisitos estão OK:
- [ ] Vê o dashboard principal
- [ ] Campo de input para domínio
- [ ] Botão "Iniciar Varredura"
- [ ] Seção de histórico de relatórios vazia

### Teste 3: Interface Responsiva
- [ ] Desktop (1920px) - Layout normal
- [ ] Tablet (768px) - Botões em coluna
- [ ] Mobile (320px) - Menu adaptado

```bash
# Teste no navegador:
# F12 > Responsivo > Selecione dispositivo
```

### Teste 4: Integração de API

Abra o console do navegador (F12) e teste:

```javascript
// Teste 1: Obter requisitos
fetch('/api/requirements')
  .then(r => r.json())
  .then(d => console.log(d))

// Teste 2: Listar relatórios (inicialmente vazio)
fetch('/api/reports')
  .then(r => r.json())
  .then(d => console.log(d))

// Teste 3: Health check
fetch('/health')
  .then(r => console.log(r.status))
```

### Teste 5: Simulação de Varredura

⚠️ **Importante**: Para testar varredura real, você precisa:
- Ter `nmap`, `dig`, `subfinder`, etc instalados
- Ou ter autorização explícita para scanear um domínio

```javascript
// Se tiver as ferramentas:
fetch('/api/scan', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({domain: 'example.com'})
})
.then(r => r.json())
.then(d => console.log(d))
```

## 🔍 Estrutura de Arquivos Criados

### app.py (295 linhas)
```
✓ Configurações Flask
✓ Funções de verificação de requisitos
✓ Função check_command_exists()
✓ Função check_python_package()
✓ Função get_system_requirements()
✓ Função run_recon()
✓ 7 Rotas (@app.route)
✓ Handlers de erro
```

### templates/dashboard.html (550+ linhas)
```
✓ Header e input de domínio
✓ Seção de status com progress bar
✓ Seção de resultados com botões
✓ Grid de relatórios anteriores
✓ CSS inline para estilo completo
✓ JavaScript para lógica
```

### templates/install.html (400+ linhas)
```
✓ Grid de 4 seções de requisitos
✓ Status visual (checkmark/X)
✓ Instruções de instalação
✓ Botão "Verificar Novamente"
✓ Estilos responsivos
```

### static/css/style.css (150+ linhas)
```
✓ Estilos da navegação
✓ Gradiente roxo/azul
✓ Responsividade completa
✓ Animações suaves
✓ Scrollbar customizado
```

## 🛠️ Troubleshooting

### Erro: "Port 8080 already in use"
```bash
# Mudar a porta em app.py (linha ~232)
# Mude: app.run(host="0.0.0.0", port=9090, ...)

# Ou matar o processo
lsof -i :8080
kill -9 <PID>
```

### Erro: "Module not found: flask"
```bash
pip install flask werkzeug
```

### Página em branco
- Abra o console do navegador (F12)
- Procure por mensagens de erro
- Verifique se app.py está rodando

### API não responde
```bash
# Verifique se app.py rodou sem erros
# Tente: curl http://localhost:8080/health
```

## 📊 Endpoints para Testar

| Método | URL | O que testa |
|--------|-----|-----------|
| GET | `http://localhost:8080/` | Página principal |
| GET | `http://localhost:8080/api/requirements` | Requirements |
| GET | `http://localhost:8080/api/reports` | Lista relatórios |
| GET | `http://localhost:8080/health` | Health check |
| POST | `http://localhost:8080/api/scan` | Iniciar varredura |

## 📸 Screenshots Esperados

### Antes de requisitos: Página Install
```
┌─────────────────────────────────────┐
│ 🔍 Verificação de Requisitos        │
│                                      │
│ Ferramentas do Sistema   │ Fail.    │
│   ✓ nmap                │ Go Tools │
│   ✓ dig                 │   ✗ sub  │
│   ✗ git                 │          │
│                                      │
│ [Execute: chmod +x setup.sh]         │
│ [Comando: sudo ./setup.sh]           │
│ [Botão: Verificar Novamente]         │
└─────────────────────────────────────┘
```

### Depois de requisitos: Dashboard
```
┌─────────────────────────────────────┐
│ 🔍 Iniciar Reconhecimento           │
│                                      │
│ Domínio Alvo                         │
│ [example.com        ] [▶ Iniciar]   │
│                                      │
│ 📋 Relatórios Anteriores             │
│ ┌────────────┐ ┌────────────┐       │
│ │ site1.com  │ │ site2.com  │       │
│ │ [📄][📥]   │ │ [📄][📥]   │       │
│ └────────────┘ └────────────┘       │
└─────────────────────────────────────┘
```

## ✨ Recursos Implementados

- [x] Verificação automática de requisitos
- [x] Dashboard moderno com gradiente
- [x] API REST completa
- [x] Monitoramento de progresso
- [x] Download de relatórios
- [x] Histórico de varreduras
- [x] Responsividade mobile
- [x] Tratamento de erros
- [x] Documentação completa

## 📞 Se Encontrar Problemas

1. Verifique o console do navegador (F12)
2. Veja os logs do terminal onde app.py está rodando
3. Consulte [WEB_README.md](WEB_README.md)
4. Abra uma issue no GitHub

## 🎯 Próximos Passos

Após confirmar que funciona:
1. Teste com domínios reais (if authorized)
2. Revise os relatórios gerados
3. Customize estilos em `static/css/style.css`
4. Integrate com seu pipeline de CI/CD

---

**Data de Criação:** Fevereiro 16, 2026
**Arquivos Criados:** 11
**Linhas de Código:** 1500+
**Status:** ✅ Pronto para Teste
