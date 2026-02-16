#!/usr/bin/env python3
"""
Testes simples para ReconZZer
"""

import sys
import subprocess
from pathlib import Path

def test_imports():
    """Verifica se todos os imports necessários funcionam."""
    print("▶ Testando imports...")
    try:
        import flask
        import requests
        import bs4
        print("  ✓ Todos os imports OK")
        return True
    except ImportError as e:
        print(f"  ✗ Import falhou: {e}")
        return False

def test_files_exist():
    """Verifica se todos os arquivos necessários existem."""
    print("\n▶ Testando arquivos necessários...")
    required_files = [
        "app.py",
        "recon_script.py",
        "requirements.txt",
        "templates/base.html",
        "templates/dashboard.html",
        "templates/install.html",
        "static/css/style.css",
        "static/js/script.js",
        "run.sh",
    ]
    
    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} FALTANDO")
            all_exist = False
    
    return all_exist

def test_python_syntax():
    """Verifica sintaxe Python."""
    print("\n▶ Testando sintaxe Python...")
    python_files = ["app.py", "recon_script.py"]
    
    all_valid = True
    for file in python_files:
        try:
            with open(file, 'r') as f:
                compile(f.read(), file, 'exec')
            print(f"  ✓ {file}")
        except SyntaxError as e:
            print(f"  ✗ {file}: {e}")
            all_valid = False
    
    return all_valid

def test_flask_app():
    """Testa se a app Flask pode ser instantiada."""
    print("\n▶ Testando aplicação Flask...")
    try:
        from app import app
        print("  ✓ App Flask carregada com sucesso")
        return True
    except Exception as e:
        print(f"  ✗ Erro ao carregar app: {e}")
        return False

def main():
    print("=" * 50)
    print("🧪 ReconZZer - Testes")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_files_exist,
        test_python_syntax,
        test_flask_app,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"  ✗ Erro ao executar teste: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"✓ Todos os {total} testes passaram!")
        print("=" * 50)
        return 0
    else:
        print(f"✗ {total - passed} de {total} testes falharam")
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
