# Contribuindo para ReconZZer

Obrigado por seu interesse em contribuir para ReconZZer! Este documento fornece diretrizes e instruções para contribuir.

## 📋 Código de Conduta

Por favor seja respeitoso e profissional. Assédio, discriminação ou comportamento inapropriado não será tolerado.

## 🐛 Reportando Bugs

Encontrou um bug? Por favor crie uma issue com:

1. **Título descritivo** - "Erro ao escanear domínio com caracteres especiais"
2. **Descrição detalhada** - Explique o problema passo a passo
3. **Reprodução** - Como reproduzir o erro
4. **Ambiente** - Sistema operacional, versão Python, etc.
5. **Logs** - Cole qualquer mensagem de erro relevante

## 💡 Sugerindo Melhorias

Para sugerir uma melhoria:

1. Use um **título descritivo**
2. Forneça uma **descrição detalhada** da melhoria
3. Liste **exemplos** de como a melhoria seria útil
4. Mencione **alternativas** que considerou

## 🔧 Processo de Contribuição

### 1. Fork o Repositório
```bash
git clone https://github.com/SEU_USUARIO/ReconZZer.git
cd ReconZZer
```

### 2. Crie uma Branch
```bash
git checkout -b feature/sua-feature
# ou
git checkout -b fix/seu-fix
```

### 3. Faça as Mudanças

- Siga o estilo de código existente
- Adicione docstrings em funções novas
- Teste suas mudanças

### 4. Commit Messageados
```bash
git commit -m "type: descrição breve

Descrição mais detalhada se necessário

Fixes #123 (se aplicável)
```

**Tipos de commit:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `style:` Formatação, sem mudanças de lógica
- `refactor:` Refatoração de código existente
- `test:` Adição ou mudança de testes
- `chore:` Atualizações de dependências, etc.

### 5. Envie um Pull Request

1. Push para sua fork
```bash
git push origin feature/sua-feature
```

2. Abra um Pull Request no GitHub
3. Descreva claramente as mudanças
4. Aguarde review

## 📝 Padrões de Código

### Python
- Use **PEP 8** para estilo
- Adicione **type hints**
- Inclua **docstrings** em funções públicas
- Use **meaningful variable names**

Exemplo:
```python
def scan_domain(domain: str, timeout: int = 300) -> Dict[str, str]:
    """
    Escaneia um domínio para obter informações de reconhecimento.
    
    Args:
        domain: O domínio a ser escaneado
        timeout: Tempo máximo em segundos
        
    Returns:
        Dicionário com resultados do scan
        
    Raises:
        ValueError: Se o domínio for inválido
    """
    # implementação
    pass
```

### HTML/CSS/JavaScript
- Use **semantic HTML**
- Mantenha CSS **modular**
- Use **meaningful class names**
- Adicione **comments** em lógica complexa

### Documentação
- Use **Markdown** corretamente
- Mantenha links **atualizados**
- Inclua **exemplos de código**
- Tenha **tabelas de conteúdo** em docs longas

## 🧪 Testando Mudanças

Antes de enviar um PR:

1. Teste localmente
```bash
python3 app.py
# Acesse http://localhost:8080
```

2. Teste o script CLI
```bash
python3 recon_script.py -d teste.com
```

3. Verifique os relatórios gerados

## 📚 Documentação

Se sua mudança:
- **Adiciona funcionalidade** → Atualize README.md ou WEB_README.md
- **Muda um comando** → Atualize exemplos na documentação
- **Adiciona nova ferramenta** → Documente em recon_tools_methods.md

## 🎯 Áreas que Aceitamos Contribuições

- ✅ Novas funcionalidades
- ✅ Melhorias de performance
- ✅ Correções de bugs
- ✅ Melhorias na documentação
- ✅ Melhor tratamento de erros
- ✅ Testes
- ✅ Temas/Estilos para a web

## ❌ O que Não Aceitamos

- ✗ Mudanças que violem SECURITY.md
- ✗ Código sem testes
- ✗ Documentação incompleta
- ✗ Funcionalidades não relacionadas ao Cyber Kill Chain

## 📞 Dúvidas?

- Abra uma **issue** para perguntas
- Use **discussions** para conversas gerais
- Revise a documentação existente primeiro

Obrigado por contribuir! 🎉

---

**Desenvolvido com ❤️ pela comunidade de segurança**
