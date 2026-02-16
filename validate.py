#!/usr/bin/env python3
"""
Testes de Validação da Aplicação ReconZZer Web
Execute este arquivo para validar a estrutura
"""

import json
import sys
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    print(f"\n{Colors.BLUE}{Colors.BOLD}")
    print("╔═════════════════════════════════════════════╗")
    print("║     🧪 Validação ReconZZer Web v1.0       ║")
    print("╚═════════════════════════════════════════════╝")
    print(f"{Colors.END}\n")

def check_file_exists(file_path, description):
    """Verifica se um arquivo existe"""
    path = Path(file_path)
    if path.exists():
        size = path.stat().st_size
        print(f"{Colors.GREEN}✓{Colors.END} {description}")
        print(f"  └─ {file_path} ({size} bytes)")
        return True
    else:
        print(f"{Colors.RED}✗{Colors.END} {description}")
        print(f"  └─ Faltando: {file_path}")
        return False

def check_file_contains(file_path, keywords, description):
    """Verifica se um arquivo contém certas palavras-chave"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        found = all(kw in content for kw in keywords)
        
        if found:
            print(f"{Colors.GREEN}✓{Colors.END} {description}")
            return True
        else:
            missing = [kw for kw in keywords if kw not in content]
            print(f"{Colors.RED}✗{Colors.END} {description}")
            print(f"  └─ Faltam: {', '.join(missing)}")
            return False
    except FileNotFoundError:
        print(f"{Colors.RED}✗{Colors.END} {description} (arquivo não encontrado)")
        return False

def main():
    print_header()
    
    results = {
        'files': [],
        'content': [],
        'summary': {}
    }
    
    # ===== SEÇÃO 1: ARQUIVOS DO BACKEND =====
    print(f"{Colors.BOLD}1. Backend (Flask){Colors.END}")
    print("-" * 45)
    
    results['files'].append(check_file_exists('app.py', 'Aplicação Flask'))
    results['files'].append(check_file_exists('recon_script.py', 'Script de Reconhecimento'))
    
    # ===== SEÇÃO 2: TEMPLATES =====
    print(f"\n{Colors.BOLD}2. Templates HTML{Colors.END}")
    print("-" * 45)
    
    results['files'].append(check_file_exists('templates/base.html', 'Template Base'))
    results['files'].append(check_file_exists('templates/dashboard.html', 'Dashboard'))
    results['files'].append(check_file_exists('templates/install.html', 'Verificação Requisitos'))
    results['files'].append(check_file_exists('templates/error.html', 'Página de Erro'))
    
    # ===== SEÇÃO 3: ASSETS ESTÁTICOS =====
    print(f"\n{Colors.BOLD}3. Assets (CSS/JS){Colors.END}")
    print("-" * 45)
    
    results['files'].append(check_file_exists('static/css/style.css', 'Estilos CSS'))
    results['files'].append(check_file_exists('static/js/script.js', 'Scripts JavaScript'))
    
    # ===== SEÇÃO 4: SCRIPTS E CONFIG =====
    print(f"\n{Colors.BOLD}4. Scripts e Configuração{Colors.END}")
    print("-" * 45)
    
    results['files'].append(check_file_exists('run.sh', 'Script de Inicialização'))
    results['files'].append(check_file_exists('test.py', 'Arquivo de Testes'))
    results['files'].append(check_file_exists('START.md', 'Guia de Teste'))
    
    # ===== SEÇÃO 5: DOCUMENTAÇÃO =====
    print(f"\n{Colors.BOLD}5. Documentação{Colors.END}")
    print("-" * 45)
    
    results['files'].append(check_file_exists('WEB_README.md', 'Documentação Web'))
    results['files'].append(check_file_exists('QUICKSTART.md', 'Guia Rápido'))
    results['files'].append(check_file_exists('CONTRIBUTING.md', 'Guia Contribuição'))
    results['files'].append(check_file_exists('SECURITY.md', 'Avisos Segurança'))
    
    # ===== SEÇÃO 6: VALIDAÇÃO DE CONTEÚDO =====
    print(f"\n{Colors.BOLD}6. Validação de Conteúdo{Colors.END}")
    print("-" * 45)
    
    # Flask app
    results['content'].append(check_file_contains(
        'app.py',
        ['@app.route', 'Flask', 'check_command_exists'],
        'Flask: Rotas e verificações'
    ))
    
    # Templates
    results['content'].append(check_file_contains(
        'templates/dashboard.html',
        ['id="domain"', '/api/scan', 'reportsList'],
        'Dashboard: Elementos principais'
    ))
    
    results['content'].append(check_file_contains(
        'templates/install.html',
        ['requirement-item', 'setup.sh', 'installed'],
        'Install: Verificação requisitos'
    ))
    
    # CSS
    results['content'].append(check_file_contains(
        'static/css/style.css',
        ['.navbar', '.btn', '@media'],
        'CSS: Estilos e responsividade'
    ))
    
    # ===== RESUMO =====
    print(f"\n{Colors.BOLD}RESUMO{Colors.END}")
    print("=" * 45)
    
    total_files = len(results['files'])
    passed_files = sum(results['files'])
    
    total_content = len(results['content'])
    passed_content = sum(results['content'])
    
    total_all = total_files + total_content
    passed_all = passed_files + passed_content
    
    results['summary'] = {
        'files': {'passed': passed_files, 'total': total_files},
        'content': {'passed': passed_content, 'total': total_content},
        'total': {'passed': passed_all, 'total': total_all}
    }
    
    print(f"\nArquivos:        {passed_files}/{total_files} ✓")
    print(f"Conteúdo:        {passed_content}/{total_content} ✓")
    print(f"Total:           {passed_all}/{total_all} ✓")
    
    # ===== PRÓXIMOS PASSOS =====
    if passed_all == total_all:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Tudo OK! Pronto para testar{Colors.END}")
        print(f"\n{Colors.BOLD}Próximos Passos:{Colors.END}")
        print("1. chmod +x run.sh")
        print("2. pip install flask werkzeug")
        print("3. ./run.sh")
        print("4. Abra: http://localhost:8080")
        return 0
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}✗ Alguns itens falharam{Colors.END}")
        print(f"\nConsulte os erros acima")
        return 1

if __name__ == '__main__':
    sys.exit(main())
