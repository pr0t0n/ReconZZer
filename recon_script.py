#!/usr/bin/env python3
"""
ReconZZer - Automação da Fase de Reconhecimento do Cyber Kill Chain
Script principal para coleta de informações sobre domínios alvo.
"""

import subprocess
import json
import argparse
import logging
import os
from typing import Dict, List, Optional
from pathlib import Path

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
)
logger = logging.getLogger(__name__)

# Constantes
DEFAULT_TIMEOUT = 300
ENHANCED_TIMEOUT = 600
GO_BIN_PATHS = ["/snap/bin", "/home/ubuntu/go/bin"]
WORDLIST_PATH = "/usr/share/wordlists/dirb/common.txt"
REPORTS_DIR = "reports"


def _setup_go_env() -> Dict[str, str]:
    """Prepara variáveis de ambiente para ferramentas Go."""
    env = os.environ.copy()
    current_path = env.get("PATH", "")
    env["PATH"] = f"{current_path}:{':'.join(GO_BIN_PATHS)}"
    return env


def run_command(command: str, env: Optional[Dict] = None, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Executa um comando no shell e retorna a saída."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            env=env,
            timeout=timeout
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr or e.stdout or str(e)
        logger.error(f"Falha no comando: {e.cmd}\nErro: {error_msg}")
        return ""
    except subprocess.TimeoutExpired:
        logger.error(f"Timeout excedido ({timeout}s): {command}")
        return ""


def get_subdomains(domain: str) -> List[str]:
    """Obtém subdomínios usando subfinder."""
    logger.info(f"Enumerando subdomínios para {domain}...")
    command = f"subfinder -d {domain} -silent"
    output = run_command(command, env=_setup_go_env())
    
    if not output:
        return []
    
    subdomains = [s.strip() for s in output.split("\n") if s.strip()]
    logger.info(f"Encontrados {len(subdomains)} subdomínios")
    return subdomains


def get_dns_info(domain: str) -> Dict[str, List[str]]:
    """Obtém informações DNS usando dig."""
    logger.info(f"Obtendo informações DNS para {domain}...")
    records = ["A", "MX", "NS", "TXT"]
    dns_info = {}
    
    for record in records:
        command = f"dig +short {domain} {record}"
        output = run_command(command)
        dns_info[record] = [line.strip() for line in output.split("\n") if line.strip()]
    
    return dns_info


def port_scan(target: str) -> str:
    """Realiza varredura de portas com nmap."""
    logger.info(f"Varredura de portas em {target}...")
    command = f"nmap -F {target}"
    return run_command(command)


def run_theharvester(domain: str) -> str:
    """Executa TheHarvester para OSINT."""
    logger.info(f"Executando TheHarvester...")
    command = f"theHarvester -d {domain} -b google,linkedin,twitter -l 50"
    return run_command(command, timeout=ENHANCED_TIMEOUT)


def run_nikto(target_url: str) -> str:
    """Executa Nikto para varredura de vulnerabilidades web."""
    logger.info(f"Executando Nikto...")
    command = f"nikto -h {target_url}"
    return run_command(command, timeout=ENHANCED_TIMEOUT)


def run_nuclei(target_url: str) -> str:
    """Executa Nuclei para varredura de vulnerabilidades."""
    logger.info(f"Executando Nuclei...")
    command = f"nuclei -u {target_url} -silent -severity info,low"
    return run_command(command, env=_setup_go_env(), timeout=ENHANCED_TIMEOUT)


def run_dirb(target_url: str) -> str:
    """Executa Dirb para enumeração de diretórios."""
    logger.info(f"Executando Dirb...")
    command = f"dirb {target_url} {WORDLIST_PATH} -o /dev/stdout"
    return run_command(command, timeout=ENHANCED_TIMEOUT)


def run_ffuf(target_url: str) -> str:
    """Executa FFUF para fuzzing."""
    logger.info(f"Executando FFUF...")
    command = (
        f"ffuf -w {WORDLIST_PATH}:FUZZ -u {target_url}/FUZZ "
        "-mc 200,204,301,302,307,401,403 -recursion -recursion-depth 1"
    )
    return run_command(command, env=_setup_go_env(), timeout=ENHANCED_TIMEOUT)


def get_osint_brazuca_urls() -> List[str]:
    """Lê URLs do arquivo OSINT.txt."""
    osint_file = Path(__file__).parent / "osint_data" / "OSINT.txt"
    
    try:
        with open(osint_file, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        logger.warning(f"Arquivo OSINT.txt não encontrado em {osint_file}")
        return []


def generate_json_report(data: Dict, filename: str) -> None:
    """Gera relatório em formato JSON."""
    logger.info(f"Gerando relatório JSON...")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_html_report(data: Dict, filename: str) -> None:
    """Gera relatório em formato HTML."""
    logger.info(f"Gerando relatório HTML...")
    
    def format_list(items: List[str]) -> str:
        """Formata lista em HTML."""
        return "\n".join(f"<li>{item}</li>" for item in items if item)
    
    def format_subdomain_scans(scans: Dict[str, str]) -> str:
        """Formata varreduras de subdomínios."""
        html = ""
        for subdomain, scan in scans.items():
            if scan:
                html += f"""
        <div class="section">
            <h2>Varredura de Portas - {subdomain}</h2>
            <pre>{scan}</pre>
        </div>"""
        return html
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Reconhecimento - {data["domain"]}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 30px;
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }}
        h2 {{
            color: #764ba2;
            margin-top: 25px;
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
            padding-left: 10px;
        }}
        .section {{
            margin-bottom: 25px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            background: #fafafa;
            transition: box-shadow 0.3s ease;
        }}
        .section:hover {{
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.4;
            font-size: 13px;
        }}
        ul {{ list-style: none; padding: 0; }}
        li {{
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }}
        li:last-child {{ border-bottom: none; }}
        a {{ color: #667eea; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Relatório de Reconhecimento</h1>
        <p><strong>Domínio:</strong> {data["domain"]}</p>

        <div class="section">
            <h2>📋 Informações DNS</h2>
            <pre>{json.dumps(data["dns_info"], indent=2, ensure_ascii=False)}</pre>
        </div>

        <div class="section">
            <h2>🌐 Subdomínios ({len(data["subdomains"])})</h2>
            <ul>{format_list(data["subdomains"])}</ul>
        </div>

        <div class="section">
            <h2>🔌 Varredura de Portas - Domínio Principal</h2>
            <pre>{data["port_scan"]["main_domain"]}</pre>
        </div>

        {format_subdomain_scans(data["port_scan"]["subdomains"])}

        <div class="section">
            <h2>🕵️ OSINT - TheHarvester</h2>
            <pre>{data["osint_results"]["theharvester"]}</pre>
        </div>

        <div class="section">
            <h2>🔐 Vulnerabilidades Web - Nikto</h2>
            <pre>{data["web_scan_results"]["nikto"]}</pre>
        </div>

        <div class="section">
            <h2>🎯 Vulnerabilidades - Nuclei</h2>
            <pre>{data["web_scan_results"]["nuclei"]}</pre>
        </div>

        <div class="section">
            <h2>📁 Enumeração de Diretórios - Dirb</h2>
            <pre>{data["web_scan_results"]["dirb"]}</pre>
        </div>

        <div class="section">
            <h2>⚡ Fuzzing - FFUF</h2>
            <pre>{data["web_scan_results"]["ffuf"]}</pre>
        </div>

        <div class="section">
            <h2>🇧🇷 Fontes OSINT Brazuca</h2>
            <ul>{format_list([f'<a href="{url}" target="_blank">{url}</a>' for url in data["osint_results"]["osint_brazuca_urls"]])}</ul>
        </div>
    </div>
</body>
</html>"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)


def main():
    parser = argparse.ArgumentParser(
        description="ReconZZer - Automação de Reconhecimento",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplo: python3 recon_script.py -d example.com"
    )
    parser.add_argument("-d", "--domain", required=True, help="Domínio alvo")
    args = parser.parse_args()

    domain = args.domain
    target_url = f"http://{domain}"

    logger.info(f"Iniciando reconhecimento para: {domain}")

    recon_data = {
        "domain": domain,
        "dns_info": {},
        "subdomains": [],
        "port_scan": {"main_domain": "", "subdomains": {}},
        "osint_results": {"theharvester": "", "osint_brazuca_urls": []},
        "web_scan_results": {"nikto": "", "nuclei": "", "dirb": "", "ffuf": ""}
    }

    # Coleta de informações
    recon_data["dns_info"] = get_dns_info(domain)
    recon_data["subdomains"] = get_subdomains(domain)
    recon_data["port_scan"]["main_domain"] = port_scan(domain)

    # Varredura de subdomínios (limitado a 3)
    logger.info(f"Iniciando varredura de portas em subdomínios...")
    for subdomain in recon_data["subdomains"][:3]:
        recon_data["port_scan"]["subdomains"][subdomain] = port_scan(subdomain)

    # OSINT
    recon_data["osint_results"]["theharvester"] = run_theharvester(domain)
    recon_data["osint_results"]["osint_brazuca_urls"] = get_osint_brazuca_urls()

    # Varreduras web
    recon_data["web_scan_results"]["nikto"] = run_nikto(target_url)
    recon_data["web_scan_results"]["nuclei"] = run_nuclei(target_url)
    recon_data["web_scan_results"]["dirb"] = run_dirb(target_url)
    recon_data["web_scan_results"]["ffuf"] = run_ffuf(target_url)

    # Gerar relatórios
    Path(REPORTS_DIR).mkdir(exist_ok=True)
    
    json_file = Path(REPORTS_DIR) / f"recon_report_{domain}.json"
    html_file = Path(REPORTS_DIR) / f"recon_report_{domain}.html"

    generate_json_report(recon_data, str(json_file))
    generate_html_report(recon_data, str(html_file))

    logger.info(f"✓ Reconhecimento concluído!")
    logger.info(f"  JSON: {json_file}")
    logger.info(f"  HTML: {html_file}")


if __name__ == "__main__":
    main()

