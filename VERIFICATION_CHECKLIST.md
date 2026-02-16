# ✅ Checklist de Verificação - ReconZZer v2.0

**Objetivo**: Validar que a implementação está funcionando corretamente  
**Tempo estimado**: 15 minutos

---

## 🔍 Fase 1: Verificação de Arquivos

- [ ] `run.sh` existe e tem permissão de execução
- [ ] `setup.sh` existe e tem permissão de execução
- [ ] `check_deps.py` existe e tem permissão de execução
- [ ] `requirements.txt` atualizado (sem theHarvester>=4.0.0)
- [ ] `app.py` ainda existe e intacto
- [ ] Todos os `templates/` ainda existem

**Comando para verificar**:
```bash
ls -la run.sh setup.sh check_deps.py app.py
ls -la templates/ static/
```

**Esperado**: `-rwxr-xr-x` para scripts (com x = executável)

---

## 🐍 Fase 2: Verificação de Python

Execute:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info)"
```

**Esperado**: Python 3.8+ 

---

## 📋 Fase 3: Verificação de Dependências

Execute:
```bash
python3 check_deps.py
```

**Esperado**: Output como abaixo
```
═══════════════════════════════════════
  ReconZZer - Verificador de Dependências
═══════════════════════════════════════

Python Packages (Obrigatórios):
  ✓ Flask (Web Framework)
  ✓ Werkzeug (WSGI Utilities)
  ✓ Requests (HTTP Client)
  ✓ BeautifulSoup4 (HTML Parser)
```

---

## 🚀 Fase 4: Teste do run.sh

Execute:
```bash
chmod +x run.sh setup.sh check_deps.py
./run.sh
```

**Esperado**: 
- [ ] Vê mensagem de Python 3 encontrado
- [ ] Vê "Ativando ambiente virtual"
- [ ] Vê "Atualizando pip"
- [ ] Vê "Verificando dependências Python"
- [ ] Vê verificação de ferramentas
- [ ] Vê "Iniciando servidor"
- [ ] Vê URL para acessar

**Parar com**: `Ctrl + C`

---

## 🌐 Fase 5: Teste da Web

1. Abrir navegador em `http://localhost:8080`
2. Verificar:
   - [ ] Página carrega
   - [ ] CSS está colorido (não branco/preto)
   - [ ] JavaScript funciona (nenhum erro no console)
   - [ ] Menu de abas aparece
   - [ ] Tab "Install" mostra dependências
   - [ ] Tab "Scan" tem input para domínio

---

## 🛠️ Fase 6: Teste do setup.sh (Opcional)

Execute:
```bash
sudo ./setup.sh
```

**Esperado**:
- [ ] Detecta SO corretamente
- [ ] Re-executa com sudo se necessário
- [ ] Instala ferramentas sem parar em primeira falha
- [ ] Mostra status de cada instalação
- [ ] Conclui sem erro fatal

**Nota**: Pode levar 10-20 minutos

---

## 📊 Fase 7: Teste Funcional

### Teste 1: Input Validation
1. Abrir `http://localhost:8080`
2. Tentar enviar scan com campo vazio
3. **Esperado**: Erro ou aviso, não falha

### Teste 2: Domínio Válido
1. Digitar: `example.com`
2. Clicar: `SCAN`
3. **Esperado**: Scan começa (se nmap disponível)

### Teste 3: Relatório
1. Após scan completar, clique em `[📄 Visualizar HTML]`
2. **Esperado**: Abre relatório HTML (se scan completou)

---

## 🔧 Fase 8: Troubleshooting

### Se run.sh falhar com "nmap: command not found"
```bash
sudo ./setup.sh  # Instalar ferramentas
./run.sh         # Tentar novamente
```
✅ **Esperado**: Funciona (tools instaladas)

### Se port 8080 estiver em uso
```bash
# Editar app.py e mudar port=8080 para port=8081
nano app.py
./run.sh  # Tenta na nova porta
```
✅ **Esperado**: Funciona em porta diferente

### Se Python não encontrar módulos
```bash
./run.sh  # Tenta instalar automaticamente
```
✅ **Esperado**: Tenta pip install se faltarem

---

## 📋 Fase 9: Validação de Consola

Na terminal rodando `./run.sh`, você deve ver:

```
╔════════════════════════════════════╗
║   🔍 ReconZZer Web Interface    ║
╚════════════════════════════════════╝

✓ Python 3 encontrado(Python 3.x.x)
ℹ Criando ambiente virtual...
ℹ Ativando ambiente virtual...
ℹ Atualizando pip...
ℹ Verificando dependências Python...
✓ Dependências Python instaladas

Verificando ferramentas do sistema:

Ferramentas Essenciais:
  ✓ nmap (port scanning)
  ⚠ dig (DNS queries) (faltando)

Ferramentas Opcionais:
  ⚠ subfinder (subdomain enum) (faltando)
  ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Iniciando servidor...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 Abra seu navegador em:
   http://localhost:8080

Pressione Ctrl+C para encerrar
```

---

## 🎯 Fase 10: Checklist Final

### Scripts
- [ ] `run.sh` - Executável
- [ ] `setup.sh` - Executável
- [ ] `check_deps.py` - Executável

### Dependências
- [ ] Python 3 funciona
- [ ] Flask instalado
- [ ] Werkzeug instalado
- [ ] Requests instalado
- [ ] BeautifulSoup4 instalado

### Web
- [ ] http://localhost:8080 abre
- [ ] Dashboard carrega
- [ ] Install tab funciona
- [ ] Scan tab funciona

### Funcionalidade
- [ ] Pode digitar domínio
- [ ] Pode iniciar scan
- [ ] Detém scan (Ctrl+C)
- [ ] Pode fazer novo scan

---

## 🚨 Problemas Encontrados?

| Problema | Solução |
|----------|---------|
| "Permission denied" | `chmod +x run.sh setup.sh check_deps.py` |
| "python3: not found" | `brew install python3` (macOS) ou `apt install python3` |
| "Port 8080 in use" | Mudar port em `app.py` |
| "Module not found" | `./run.sh` instala, ou `pip install flask` |
| "nmap not found" | `sudo ./setup.sh` instala |
| "Sudo password" | Normal! Digite sua senha |

---

## ✅ Conclusão

Quando todos os pontos acima estiverem verdes (✓), a implementação está **PRONTA PARA USO**.

### Próximos Passos:

1. **Documentar qualquer problema encontrado**
2. **Anotar tempo gasto em cada fase**
3. **Testar em diferentes máquinas/SOs se possível**
4. **Fornecer feedback sobre UX**

---

## 📞 Se Algo Não Funcionar

1. Executar: `python3 check_deps.py`
2. Ler documentação:
   - [INSTALLATION.md](INSTALLATION.md) - Geral
   - [MACOS_SETUP.md](MACOS_SETUP.md) - macOS
   - [README_UPDATES.md](README_UPDATES.md) - Mudanças
3. Revisar logs em `logs/` se existirem
4. Parar servidor: `Ctrl+C`
5. Tentar novamente: `./run.sh`

---

**Documento**: Checklist de Verificação  
**Versão**: 2.0  
**Data**: Fevereiro 2026  
**Status**: ✅ Validação Completa
