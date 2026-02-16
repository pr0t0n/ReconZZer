# ReconZZer Web Interface

Interface web moderna e intuitiva para o ReconZZer, permitindo realizar reconhecimento automático de domínios através de um navegador.

## 🚀 Início Rápido

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Verificar Requisitos do Sistema

Verifique se todas as ferramentas estão instaladas:

```bash
chmod +x setup.sh
sudo ./setup.sh
```

### 3. Iniciar a Aplicação

```bash
python3 app.py
```

Você verá:
```
==================================================
🔍 ReconZZer Web Interface
==================================================

📱 Abra seu navegador em: http://localhost:8080

Pressione Ctrl+C para encerrar
```

### 4. Acessar no Navegador

Abra seu navegador e acesse: **http://localhost:8080**

## 📋 Funcionalidades

### Verificação de Requisitos
Na primeira vez que você acessa, a aplicação verifica se todos os requisitos estão instalados:
- ✅ Ferramentas do Sistema (nmap, dig, git, wget)
- ✅ Ferramentas Go (subfinder, nuclei, ffuf)
- ✅ Outras Ferramentas (theHarvester, nikto, dirb)
- ✅ Pacotes Python (requests, beautifulsoup4, flask)

Se algum requisito estiver faltando, a aplicação exibe um guia de instalação.

### Dashboard Principal
Após os requisitos serem atendidos, você acessa o dashboard com:
- Campo para inserir o domínio alvo
- Monitoramento de progresso em tempo real
- Geração automática de relatórios
- Histórico de relatórios anteriores

### Relatórios
- **Relatório JSON** - Para extração de dados programática
- **Relatório HTML** - Para visualização iterativa e bonita

## 🌐 Endpoints da API

### Verificação de Requisitos
```
GET /api/requirements
```
Retorna status de todos os requisitos do sistema.

**Resposta:**
```json
{
    "requirements": {
        "system": {"nmap": true, "dig": true, ...},
        "go_tools": {...},
        "other_tools": {...},
        "python_packages": {...}
    },
    "all_met": true
}
```

### Iniciar Varredura
```
POST /api/scan
```
Inicia uma varredura de reconhecimento.

**Body:**
```json
{
    "domain": "exemplo.com"
}
```

**Resposta (202):**
```json
{
    "message": "Varredura iniciada",
    "domain": "exemplo.com"
}
```

### Status da Varredura
```
GET /api/status
```
Retorna status atual da varredura em execução.

**Resposta:**
```json
{
    "running": true,
    "progress": 45,
    "current_task": "Enumerando subdomínios...",
    "error": null
}
```

### Listar Relatórios
```
GET /api/reports
```
Lista todos os relatórios gerados.

**Resposta:**
```json
{
    "reports": [
        {
            "domain": "exemplo.com",
            "json_file": "recon_report_exemplo.com.json",
            "html_file": "recon_report_exemplo.com.html",
            "timestamp": "2026-02-16T10:30:00"
        }
    ]
}
```

### Obter Relatório JSON
```
GET /api/report/{domain}
```
Retorna os dados completos da varredura em JSON.

### Download de Relatório
```
GET /reports/{filename}
```
Faz download do arquivo JSON ou HTML.

### Visualizar Relatório HTML
```
GET /view/{domain}
```
Exibe o relatório HTML no navegador.

## 📁 Estrutura de Arquivos

```
ReconZZer/
├── app.py                    # Aplicação Flask principal
├── recon_script.py          # Script de reconhecimento
├── requirements.txt         # Dependências Python
├── templates/
│   ├── base.html           # Template base
│   ├── dashboard.html      # Dashboard principal
│   ├── install.html        # Verificação de requisitos
│   └── error.html          # Página de erro
├── static/
│   ├── css/
│   │   └── style.css       # Estilos globais
│   └── js/
│       └── script.js       # Utilitários JavaScript
└── reports/                # Relatórios gerados
    ├── *.json             # Relatórios JSON
    └── *.html             # Relatórios HTML
```

## 🔐 Segurança

A aplicação web implementa:
- ✅ Validação de entrada (domínios)
- ✅ CSRF protection (integrado ao Flask)
- ✅ Limite de tamanho de requisição
- ✅ Tratamento de erros seguro
- ✅ Logging de eventos

## ⚙️ Configuração Avançada

### Mudar Porta
Editar em `app.py`:
```python
app.run(port=8000, ...)  # Porta desejada
```

### Modo de Desenvolvimento
```python
app.run(debug=True, ...)
```

### Vincular a um Host Específico
```python
app.run(host="127.0.0.1", port=8080, ...)  # Apenas localhost
```

## 🐛 Troubleshooting

### "Endereço já em uso"
```bash
# Mudar para outra porta em app.py ou matar o processo
lsof -i :8080
kill -9 <PID>
```

### "Módulo Flask não encontrado"
```bash
pip install flask werkzeug
```

### "Requirements faltando"
Acesse a página web e clique em "Verificar Novamente" após instalar.

## 📞 Support

Para issues ou dúvidas:
1. Verifique a documentação em [recon_tools_methods.md](../recon_tools_methods.md)
2. Consulte [SECURITY.md](../SECURITY.md) para questões de segurança
3. Abra uma issue no GitHub

## 📄 Licença

Este projeto é fornecido como está para fins educacionais e de pesquisa.

---

**Desenvolvido por:** pr0t0n  
**Última atualização:** Fevereiro de 2026
