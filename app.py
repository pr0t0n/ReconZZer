#!/usr/bin/env python3
"""
ReconZZer Web Application
Flask-based web interface for ReconZZer
"""

import subprocess
import json
import os
import shutil
import threading
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Configurações
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)
SCAN_STATUS = {"running": False, "progress": 0, "current_task": "", "error": None}


def check_command_exists(command: str) -> bool:
    """Verifica se um comando está disponível no sistema."""
    return shutil.which(command) is not None


def check_python_package(package: str) -> bool:
    """Verifica se um pacote Python está instalado."""
    try:
        __import__(package.replace("-", "_"))
        return True
    except ImportError:
        return False


def get_system_requirements() -> dict:
    """Retorna status de todos os requirements."""
    requirements = {
        "system": {
            "nmap": check_command_exists("nmap"),
            "dig": check_command_exists("dig"),
            "git": check_command_exists("git"),
            "wget": check_command_exists("wget"),
        },
        "go_tools": {
            "subfinder": check_command_exists("subfinder"),
            "nuclei": check_command_exists("nuclei"),
            "ffuf": check_command_exists("ffuf"),
        },
        "other_tools": {
            "theHarvester": check_command_exists("theHarvester"),
            "nikto": check_command_exists("nikto"),
            "dirb": check_command_exists("dirb"),
        },
        "python_packages": {
            "requests": check_python_package("requests"),
            "beautifulsoup4": check_python_package("bs4"),
            "flask": check_python_package("flask"),
        },
    }
    return requirements


def all_requirements_met() -> bool:
    """Verifica se todos os requirements estão instalados."""
    reqs = get_system_requirements()
    for category in reqs.values():
        if not all(category.values()):
            return False
    return True


def run_recon(domain: str) -> dict:
    """Executa o reconhecimento de um domínio."""
    try:
        SCAN_STATUS["running"] = True
        SCAN_STATUS["error"] = None
        
        # Executar recon_script.py
        cmd = ["/usr/bin/env", "python3", "recon_script.py", "-d", domain]
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(timeout=3600)
        
        if process.returncode != 0:
            SCAN_STATUS["error"] = stderr or "Erro ao executar reconhecimento"
            return {"success": False, "error": SCAN_STATUS["error"]}
        
        # Verificar arquivos gerados
        json_file = REPORTS_DIR / f"recon_report_{domain}.json"
        html_file = REPORTS_DIR / f"recon_report_{domain}.html"
        
        return {
            "success": True,
            "domain": domain,
            "json_file": str(json_file),
            "html_file": str(html_file),
            "timestamp": datetime.now().isoformat()
        }
    
    except subprocess.TimeoutExpired:
        SCAN_STATUS["error"] = "Reconhecimento excedeu o tempo limite (1 hora)"
        return {"success": False, "error": SCAN_STATUS["error"]}
    except Exception as e:
        SCAN_STATUS["error"] = str(e)
        return {"success": False, "error": str(e)}
    finally:
        SCAN_STATUS["running"] = False


@app.route("/")
def index():
    """Página inicial."""
    if all_requirements_met():
        return render_template("dashboard.html")
    else:
        return render_template("install.html", requirements=get_system_requirements())


@app.route("/api/requirements", methods=["GET"])
def api_requirements():
    """API para obter status dos requirements."""
    reqs = get_system_requirements()
    all_met = all(
        all(category.values())
        for category in reqs.values()
    )
    return jsonify({
        "requirements": reqs,
        "all_met": all_met
    })


@app.route("/api/scan", methods=["POST"])
def api_scan():
    """API para iniciar reconhecimento."""
    if SCAN_STATUS["running"]:
        return jsonify({"error": "Varredura já em progresso"}), 409
    
    data = request.get_json()
    domain = data.get("domain", "").strip()
    
    if not domain:
        return jsonify({"error": "Domínio não fornecido"}), 400
    
    # Validar domínio simples
    if not (3 < len(domain) < 255 and "." in domain):
        return jsonify({"error": "Domínio inválido"}), 400
    
    # Executar em thread para não bloquear
    thread = threading.Thread(target=run_recon, args=(domain,))
    thread.daemon = True
    thread.start()
    
    return jsonify({"message": "Varredura iniciada", "domain": domain}), 202


@app.route("/api/status", methods=["GET"])
def api_status():
    """API para obter status da varredura."""
    return jsonify(SCAN_STATUS)


@app.route("/api/reports", methods=["GET"])
def api_reports():
    """API para listar relatórios disponíveis."""
    reports = []
    
    for json_file in REPORTS_DIR.glob("*.json"):
        domain = json_file.stem.replace("recon_report_", "")
        html_file = REPORTS_DIR / f"recon_report_{domain}.html"
        
        if html_file.exists():
            reports.append({
                "domain": domain,
                "json_file": json_file.name,
                "html_file": html_file.name,
                "timestamp": datetime.fromtimestamp(json_file.stat().st_mtime).isoformat()
            })
    
    return jsonify({"reports": reports})


@app.route("/reports/<filename>", methods=["GET"])
def download_report(filename):
    """Download de relatório."""
    try:
        return send_from_directory(REPORTS_DIR, filename)
    except NotFound:
        return jsonify({"error": "Arquivo não encontrado"}), 404


@app.route("/api/report/<domain>", methods=["GET"])
def api_report(domain):
    """API para obter dados do relatório em JSON."""
    json_file = REPORTS_DIR / f"recon_report_{domain}.json"
    
    if not json_file.exists():
        return jsonify({"error": "Relatório não encontrado"}), 404
    
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Erro ao ler relatório"}), 500


@app.route("/view/<domain>")
def view_report(domain):
    """Visualizar relatório HTML."""
    html_file = REPORTS_DIR / f"recon_report_{domain}.html"
    
    if not html_file.exists():
        return render_template("error.html", error="Relatório não encontrado"), 404
    
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    return html_content


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.errorhandler(404)
def not_found(error):
    """Handler para 404."""
    return render_template("error.html", error="Página não encontrada"), 404


@app.errorhandler(500)
def internal_error(error):
    """Handler para 500."""
    return render_template("error.html", error="Erro interno do servidor"), 500


if __name__ == "__main__":
    print("=" * 50)
    print("🔍 ReconZZer Web Interface")
    print("=" * 50)
    print("\n📱 Abra seu navegador em: http://localhost:8080")
    print("\nPressione Ctrl+C para encerrar\n")
    
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False,
        threaded=True
    )
