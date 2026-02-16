#!/usr/bin/env python3
"""
Verificador de dependências para ReconZZer
Verifica: Python packages + ferramentas do sistema
"""

import sys
import subprocess
import shutil
from typing import Dict, List, Tuple

# ===== CORES =====
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    BOLD = '\033[1m'
    NC = '\033[0m'

# ===== VERIFICADORES =====
def check_python_package(package_name: str) -> bool:
    """Verifica se um pacote Python está instalado"""
    try:
        __import__(package_name.replace('-', '_'))
        return True
    except ImportError:
        return False

def check_system_tool(tool_name: str) -> bool:
    """Verifica se uma ferramenta do sistema está disponível"""
    return shutil.which(tool_name) is not None

def run_command(cmd: List[str]) -> Tuple[bool, str]:
    """Executa um comando e retorna (sucesso, output)"""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

# ===== ANÁLISE PRINCIPAL =====
def main():
    print(f"\n{Colors.BLUE}{Colors.BOLD}═══════════════════════════════════════{Colors.NC}")
    print(f"{Colors.BLUE}{Colors.BOLD}  ReconZZer - Verificador de Dependências{Colors.NC}")
    print(f"{Colors.BLUE}{Colors.BOLD}═══════════════════════════════════════{Colors.NC}\n")
    
    # Pacotes Python obrigatórios
    python_required = {
        'flask': 'Flask (Web Framework)',
        'werkzeug': 'Werkzeug (WSGI Utilities)',
        'requests': 'Requests (HTTP Client)',
        'bs4': 'BeautifulSoup4 (HTML Parser)'
    }
    
    # Pacotes Python opcionais
    python_optional = {
        'nmap': 'python-nmap (Nmap Integration)',
    }
    
    # Ferramentas do sistema essenciais
    system_essential = {
        'python3': 'Python 3',
        'nmap': 'Nmap (Port Scanning)',
        'dig': 'Dig (DNS Queries)',
    }
    
    # Ferramentas do sistema opcionais
    system_optional = {
        'subfinder': 'Subfinder (Subdomain Enumeration)',
        'nuclei': 'Nuclei (Vulnerability Scanning)',
        'theHarvester': 'TheHarvester (OSINT)',
        'nikto': 'Nikto (Web Scanner)',
        'dirb': 'Dirb (Directory Brute-force)',
        'ffuf': 'FFUF (Fuzzing)',
    }
    
    issues = []
    missing_essential = 0
    
    # ===== VERIFICAR PYTHON OBRIGATÓRIOS =====
    print(f"{Colors.BLUE}{Colors.BOLD}Python Packages (Obrigatórios):{Colors.NC}")
    for pkg, desc in python_required.items():
        if check_python_package(pkg):
            print(f"{Colors.GREEN}  ✓{Colors.NC} {desc}")
        else:
            print(f"{Colors.RED}  ✗{Colors.NC} {desc}")
            issues.append(f"pip install {pkg}")
            missing_essential += 1
    
    # ===== VERIFICAR PYTHON OPCIONAIS =====
    print(f"\n{Colors.BLUE}{Colors.BOLD}Python Packages (Opcionais):{Colors.NC}")
    for pkg, desc in python_optional.items():
        if check_python_package(pkg):
            print(f"{Colors.GREEN}  ✓{Colors.NC} {desc}")
        else:
            print(f"{Colors.YELLOW}  ⚠{Colors.NC} {desc} (faltando)")
    
    # ===== VERIFICAR SISTEMA ESSENCIAIS =====
    print(f"\n{Colors.BLUE}{Colors.BOLD}Ferramentas do Sistema (Essenciais):{Colors.NC}")
    for tool, desc in system_essential.items():
        if check_system_tool(tool):
            print(f"{Colors.GREEN}  ✓{Colors.NC} {desc}")
        else:
            print(f"{Colors.RED}  ✗{Colors.NC} {desc}")
            missing_essential += 1
    
    # ===== VERIFICAR SISTEMA OPCIONAIS =====
    print(f"\n{Colors.BLUE}{Colors.BOLD}Ferramentas do Sistema (Opcionais):{Colors.NC}")
    missing_optional = 0
    for tool, desc in system_optional.items():
        if check_system_tool(tool):
            print(f"{Colors.GREEN}  ✓{Colors.NC} {desc}")
        else:
            print(f"{Colors.YELLOW}  ⚠{Colors.NC} {desc} (faltando)")
            missing_optional += 1
    
    # ===== RESULTADO =====
    print(f"\n{Colors.BLUE}{Colors.BOLD}═══════════════════════════════════════{Colors.NC}")
    
    if missing_essential == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ Todas as dependências essenciais estão OK{Colors.NC}\n")
        return 0
    else:
        print(f"{Colors.RED}{Colors.BOLD}✗ {missing_essential} dependência(s) essencial(is) faltando{Colors.NC}\n")
        
        if issues:
            print(f"{Colors.YELLOW}Para instalá-las, execute:{Colors.NC}")
            for issue in issues:
                print(f"  {Colors.BOLD}{issue}{Colors.NC}")
        
        print(f"\n{Colors.YELLOW}Para instalar ferramentas de sistema, execute:{Colors.NC}")
        print(f"  {Colors.BOLD}sudo ./setup.sh{Colors.NC}\n")
        
        return 1

if __name__ == '__main__':
    sys.exit(main())
