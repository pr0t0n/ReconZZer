# 🚀 Quick Start - ReconZZer Web

Comece a usar ReconZZer em **menos de 5 minutos**!

## Pré-requisitos

- **Linux** (Ubuntu/Debian recomendado)
- **Python 3.8+**
- **Conexão com Internet**
- **Privilégios sudo** (para instalar ferramentas)

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/pr0t0n/ReconZZer.git
cd ReconZZer
```

## 2️⃣ Permissões dos Scripts

```bash
chmod +x setup.sh
chmod +x run.sh
chmod +x test.py
```

## 3️⃣ Instalar Dependências

```bash
# Instalar ferramentas do sistema
sudo ./setup.sh

# Ativar nova sessão ou recarregar PATH
source ~/.bashrc

# Instalar dependências Python
pip install -r requirements.txt
```

**⏱️ Tempo estimado: 5-10 minutos** (dependendo da velocidade da rede)

## 4️⃣ Iniciar a Aplicação

```bash
./run.sh
```

Você verá algo como:

```
╔════════════════════════════════════╗
║   🔍 ReconZZer Web Interface    ║
╚════════════════════════════════════╝

✓ Python 3 encontrado
✓ Todas as dependências instaladas
✓ Iniciando servidor...

📱 Abra seu navegador em:
   http://localhost:8080

Pressione Ctrl+C para encerrar
```

## 5️⃣ Acessar no Navegador

Abra seu navegador e vá para:

```
http://localhost:8080
```

### Na primeira vez:
- A página irá verificar os requisitos
- Se tudo estiver OK ✓, você verá o dashboard
- Se faltarem ferramentas, você verá um guia de instalação

## 6️⃣ Usar a Aplicação

1. **Digite o domínio** no campo (ex: `google.com`)
2. **Clique em "Iniciar Varredura"**
3. **Aguarde a conclusão** (pode levar alguns minutos)
4. **Veja os resultados** e baixe os relatórios

### Exemplos de Domínios para Testar:
- `google.com`
- `github.com`
- `example.com`

## 📊 Resultados

Após concluir, você pode:

### 📕 Visualizar HTML
- Clique em **"Visualizar Relatório HTML"**
- Veja um relatório bonito e interativo no navegador

### 💾 Download JSON
- Clique em **"Download JSON"**
- Use os dados em ferramenta de análise ou scripts

## 🔧 Dicas Úteis

### Mudar Porta (se 8080 estiver em uso)

1. Edite `app.py`:
```python
app.run(host="0.0.0.0", port=9090, ...)  # Mude 9090 para a porta desejada
```

2. Execute novamente:
```bash
./run.sh
```

### Parar a Aplicação

```bash
Pressione Ctrl+C no terminal
```

### Ver Logs

Os logs aparecem automaticamente no terminal enquanto a aplicação está rodando.

### Limpar Relatórios Antigos

```bash
rm reports/*.json reports/*.html
```

## ⚠️ Primeiro Uso - Possíveis Problemas

### "Porta já em uso"
```bash
# Mudar para outra porta em app.py
nano app.py  # Edite a linha port=
```

### "Comando não encontrado"
```bash
# Recarregue o PATH
source ~/.bashrc
```

### "ModuleNotFoundError"
```bash
# Reinstale dependências
pip install --upgrade -r requirements.txt
```

### "Requisitos faltando"
- A própria web interface mostrará quais ferramentas instalar
- Execute: `sudo ./setup.sh` novamente
- Recarregue a página do navegador

## 📚 Próximos Passos

- Leia [WEB_README.md](WEB_README.md) para documentação completa
- Veja [recon_tools_methods.md](recon_tools_methods.md) para entender ferramentas
- Consulte [SECURITY.md](SECURITY.md) para avisos e melhores práticas

## 🎓 Exemplos de Casos de Uso

### Teste de Segurança Autorizado
```
1. Obtenha autorização por escrito
2. Certifique-se de estar na rede correta
3. Use ReconZZer via web interface
4. Revise e exporte os resultados
5. Relate vulnerabilidades responsavelmente
```

### Pesquisa Acadêmica
```
1. Use domínios públicos (google.com, exemplo.com)
2. Colete e analise dados
3. Cite ReconZZer em seu trabalho
```

### Aprendizado Pessoal
```
1. Use seu próprio domínio
2. Explore as ferramentas
3. Entenda cada etapa
```

## 💬 Suporte

Encontrou um problema?

1. Verifique o [SECURITY.md](SECURITY.md)
2. Leia [WEB_README.md](WEB_README.md)
3. Consulte problemas similares no GitHub
4. Abra uma nova issue

## 🎉 Você está pronto!

Agora pode começar a fazer reconhecimento automático. Boa sorte! 🔍

---

**Tempo total de setup:** ~15 minutos  
**Dificuldade:** ⭐ Muito Fácil  
**Requer conhecimento técnico?** Não
