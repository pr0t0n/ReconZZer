
# -*- coding: utf-8 -*-

import subprocess
import json
import argparse
import os
import requests
from bs4 import BeautifulSoup

def run_command(command, env=None, timeout=300):
    """Executa um comando no shell e retorna a saída."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True, env=env, timeout=timeout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Comando falhou: {e.cmd}")
        print(f"[ERROR] Saída padrão: {e.stdout}")
        print(f"[ERROR] Saída de erro: {e.stderr}")
        return f"Erro: {e.stderr}"
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Comando excedeu o tempo limite ({timeout}s): {command}")
        return f"Erro: Tempo limite excedido ({timeout}s)"

def get_subdomains(domain):
    """Obtém subdomínios usando subfinder."""
    print(f"[*] Enumerando subdomínios para {domain} com subfinder...")
    command = f"subfinder -d {domain} -silent"
    env = os.environ.copy()
    env["PATH"] = f"{env.get("PATH", "")}:/snap/bin:/home/ubuntu/go/bin"
    subdomains_str = run_command(command, env=env)
    subdomains = subdomains_str.strip().split("\n")
    return [s for s in subdomains if s] # Remove linhas em branco

def get_dns_info(domain):
    """Obtém informações DNS usando dig."""
    print(f"[*] Obtendo informações DNS para {domain} com dig...")
    records = ["A", "MX", "NS", "TXT"]
    dns_info = {}
    for record in records:
        command = f"dig +short {domain} {record}"
        dns_info[record] = run_command(command).strip().split("\n")
    return dns_info

def port_scan(domain):
    """Realiza uma varredura de portas usando nmap."""
    print(f"[*] Realizando varredura de portas em {domain} com nmap...")
    command = f"nmap -F {domain}" # -F para varredura rápida
    return run_command(command)

def run_theharvester(domain):
    """Executa TheHarvester para OSINT."""
    print(f"[*] Executando TheHarvester para {domain}...")
    # TheHarvester pode gerar muitos resultados, limitando a fontes comuns
    command = f"theHarvester -d {domain} -b google,linkedin,twitter -l 50"
    return run_command(command, timeout=600) # Aumentar timeout para TheHarvester

def run_nikto(target_url):
    """Executa Nikto para varredura de vulnerabilidades web."""
    print(f"[*] Executando Nikto em {target_url}...")
    # Nikto pode ser barulhento, usar -host para especificar o alvo
    command = f"nikto -h {target_url}"
    return run_command(command, timeout=600)

def run_nuclei(target_url):
    """Executa Nuclei para varredura de vulnerabilidades e informações."""
    print(f"[*] Executando Nuclei em {target_url}...")
    # Executa com templates padrão para informações e vulnerabilidades de baixo risco
    command = f"nuclei -u {target_url} -silent -severity info,low"
    env = os.environ.copy()
    env["PATH"] = f"{env.get("PATH", "")}:/snap/bin:/home/ubuntu/go/bin"
    return run_command(command, env=env, timeout=600)

def run_dirb(target_url):
    """Executa Dirb para enumeração de diretórios."""
    print(f"[*] Executando Dirb em {target_url}...")
    # Usar wordlist padrão e saída para stdout
    command = f"dirb {target_url} /usr/share/dirb/wordlists/common.txt -o /dev/stdout"
    return run_command(command, timeout=600)

def run_ffuf(target_url):
    """Executa FFUF para fuzzing e enumeração avançada."""
    print(f"[*] Executando FFUF em {target_url}...")
    # Exemplo básico de fuzzing de diretórios/arquivos
    command = f"ffuf -w /usr/share/wordlists/dirb/common.txt:FUZZ -u {target_url}/FUZZ -mc 200,204,301,302,307,401,403 -recursion -recursion-depth 1"
    env = os.environ.copy()
    env["PATH"] = f"{env.get("PATH", "")}:/snap/bin:/home/ubuntu/go/bin"
    return run_command(command, env=env, timeout=600)

def get_osint_brazuca_urls():
    """Lê as URLs do arquivo OSINT.txt."""
    try:
        script_dir = os.path.dirname(__file__)
        osint_file_path = os.path.join(script_dir, "osint_data", "OSINT.txt")
        with open(osint_file_path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("[ERROR] Arquivo OSINT.txt não encontrado em osint_data/")
        return []

def generate_json_report(data, filename):
    """Gera um relatório em formato JSON."""
    print(f"[*] Gerando relatório JSON: {filename}...")
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def generate_html_report(data, filename):
    """Gera um relatório em formato HTML."""
    print(f"[*] Gerando relatório HTML: {filename}...")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Relatório de Reconhecimento para {data["domain"]}</title>
        <style>
            body {{ font-family: sans-serif; margin: 2em; background-color: #f8f8f8; color: #333; }}
            h1 {{ color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 0.5em; }}
            h2 {{ color: #007bff; margin-top: 1.5em; }}
            pre {{ background-color: #e9ecef; padding: 1em; border-radius: 5px; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word; }}
            .section {{ margin-bottom: 2em; border: 1px solid #dee2e6; border-radius: 5px; padding: 1.5em; background-color: #fff; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 0.5em; }}
        </style>
    </head>
    <body>
        <h1>Relatório de Reconhecimento para {data["domain"]}</h1>

        <div class="section">
            <h2>Informações DNS</h2>
            <pre>{json.dumps(data["dns_info"], indent=4)}</pre>
        </div>

        <div class="section">
            <h2>Subdomínios</h2>
            <ul>
                {"\n".join([f"<li>{sub}</li>" for sub in data["subdomains"]])}
            </ul>
        </div>

        <div class="section">
            <h2>Varredura de Portas (Nmap)</h2>
            <pre>{data["port_scan"]["main_domain"]}</pre>
        </div>

        {"".join([f"""
        <div class="section">
            <h2>Varredura de Portas (Nmap) - {sub}</h2>
            <pre>{scan}</pre>
        </div>
        """ for sub, scan in data["port_scan"]["subdomains"].items()])}

        <div class="section">
            <h2>OSINT - TheHarvester</h2>
            <pre>{data["osint_results"]["theharvester"]}</pre>
        </div>

        <div class="section">
            <h2>Varredura Web - Nikto</h2>
            <pre>{data["web_scan_results"]["nikto"]}</pre>
        </div>

        <div class="section">
            <h2>Varredura Web - Nuclei</h2>
            <pre>{data["web_scan_results"]["nuclei"]}</pre>
        </div>

        <div class="section">
            <h2>Enumeração de Diretórios - Dirb</h2>
            <pre>{data["web_scan_results"]["dirb"]}</pre>
        </div>

        <div class="section">
            <h2>Fuzzing - FFUF</h2>
            <pre>{data["web_scan_results"]["ffuf"]}</pre>
        </div>

        <div class="section">
            <h2>OSINT - Fontes do OSINT Brazuca</h2>
            <ul>
                {"".join([f"<li><a href=\"{url}\">{url}</a></li>" for url in data["osint_results"]["osint_brazuca_urls"]])}
            </ul>
        </div>

    </body>
    </html>
    """
    with open(filename, "w") as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description="Script de automação de RECON.")
    parser.add_argument("-d", "--domain", required=True, help="Domínio alvo para o reconhecimento.")
    args = parser.parse_args()

    domain = args.domain
    target_url = f"http://{domain}" # Assumindo HTTP para varreduras web, pode ser ajustado

    print(f"[+] Iniciando RECON para o domínio: {domain}")
    recon_data = {
        "domain": domain,
        "dns_info": {},
        "subdomains": [],
        "port_scan": {
            "main_domain": "",
            "subdomains": {}
        },
        "osint_results": {
            "theharvester": "",
            "osint_brazuca_urls": []
        },
        "web_scan_results": {
            "nikto": "",
            "nuclei": "",
            "dirb": "",
            "ffuf": ""
        }
    }

    print("[+] Coletando informações DNS...")
    recon_data["dns_info"] = get_dns_info(domain)
    print("[+] Informações DNS coletadas.")

    print("[+] Enumerando subdomínios...")
    recon_data["subdomains"] = get_subdomains(domain)
    print(f"[+] {len(recon_data["subdomains"])} subdomínios encontrados.")

    print("[+] Realizando varredura de portas no domínio principal com Nmap...")
    recon_data["port_scan"]["main_domain"] = port_scan(domain)
    print("[+] Varredura de portas no domínio principal concluída.")

    # Limitar a varredura de portas a 3 subdomínios para o exemplo
    print("[+] Realizando varredura de portas em subdomínios (limitado a 3 para exemplo) com Nmap...")
    for sub in recon_data["subdomains"][:3]:
        recon_data["port_scan"]["subdomains"][sub] = port_scan(sub)
    print("[+] Varredura de portas em subdomínios concluída.")

    print("[+] Realizando buscas OSINT com TheHarvester...")
    recon_data["osint_results"]["theharvester"] = run_theharvester(domain)
    print("[+] Buscas OSINT com TheHarvester concluídas.")

    print("[+] Realizando varredura web com Nikto...")
    recon_data["web_scan_results"]["nikto"] = run_nikto(target_url)
    print("[+] Varredura web com Nikto concluída.")

    print("[+] Realizando varredura web com Nuclei...")
    recon_data["web_scan_results"]["nuclei"] = run_nuclei(target_url)
    print("[+] Varredura web com Nuclei concluída.")

    print("[+] Realizando enumeração de diretórios com Dirb...")
    recon_data["web_scan_results"]["dirb"] = run_dirb(target_url)
    print("[+] Enumeração de diretórios com Dirb concluída.")

    print("[+] Realizando fuzzing com FFUF...")
    recon_data["web_scan_results"]["ffuf"] = run_ffuf(target_url)
    print("[+] Fuzzing com FFUF concluído.")

    print("[+] Coletando URLs do OSINT Brazuca...")
    recon_data["osint_results"]["osint_brazuca_urls"] = get_osint_brazuca_urls()
    print("[+] URLs do OSINT Brazuca coletadas.")

    # Gerar relatórios
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    json_report_file = os.path.join(reports_dir, f"recon_report_{domain}.json")
    html_report_file = os.path.join(reports_dir, f"recon_report_{domain}.html")

    generate_json_report(recon_data, json_report_file)
    generate_html_report(recon_data, html_report_file)

    print(f"\n[+] Relatórios gerados: {json_report_file}, {html_report_file}")

if __name__ == "__main__":
    main()

