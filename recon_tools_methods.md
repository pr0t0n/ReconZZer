# Ferramentas e Métodos de RECON Automatizado

A fase de Reconhecimento (RECON) no Cyber Kill Chain visa coletar informações sobre um alvo. A automação dessa fase é crucial para eficiência e escalabilidade. Abaixo, detalhamos ferramentas e métodos para as principais técnicas de RECON que podem ser automatizadas.

## 1. Open-Source Intelligence (OSINT)

OSINT envolve a coleta de informações publicamente disponíveis. A automação aqui se concentra em varrer e analisar grandes volumes de dados de fontes abertas.

### Ferramentas Comuns:

*   **Maltego:** Uma ferramenta gráfica para coletar e vincular informações de várias fontes, como registros DNS, WHOIS, redes sociais e muito mais [1]. Embora tenha uma interface gráfica, pode ser integrada em fluxos de trabalho automatizados através de suas APIs ou scripts.
*   **theHarvester:** Utilizado para coletar e-mails, subdomínios, hosts, nomes de funcionários, portas abertas e banners de fontes públicas como mecanismos de busca e servidores PGP [1]. É uma ferramenta de linha de comando, ideal para automação.
*   **SpiderFoot:** Uma plataforma de automação OSINT de código aberto com mais de 200 módulos para inteligência de ameaças e monitoramento de superfície de ataque [2]. Pode ser executado via linha de comando ou interface web.
*   **OSINT Framework:** Embora seja mais uma coleção organizada de recursos, muitas das ferramentas listadas dentro dele são automatizáveis ou possuem APIs [3].

### Métodos de Automação:

*   **Web Scraping:** Utilizar bibliotecas como `BeautifulSoup` (Python) ou `Puppeteer` (Node.js) para extrair informações de websites de forma programática.
*   **APIs de Busca:** Integrar com APIs de mecanismos de busca (Google, Bing) ou APIs específicas de plataformas (redes sociais, registros de domínio) para coletar dados de forma estruturada.
*   **Ferramentas de Linha de Comando:** Executar ferramentas como `theHarvester` via scripts para coletar dados e processar a saída.

## 2. Port Scan (Varredura de Portas)

A varredura de portas identifica portas abertas e serviços em execução em hosts de rede, revelando potenciais pontos de entrada.

### Ferramentas Comuns:

*   **Nmap (Network Mapper):** A ferramenta mais popular para varredura de portas e descoberta de rede. É altamente configurável e pode ser automatizada para varrer hosts, identificar serviços, detectar versões e sistemas operacionais [4].
*   **Masscan:** Um scanner de portas assíncrono que pode escanear toda a internet em minutos, ideal para varreduras em larga escala [5].

### Métodos de Automação:

*   **Scripts Shell/Python:** Utilizar `nmap` ou `masscan` em scripts para varreduras programadas e análise automatizada dos resultados.
*   **Integração com Ferramentas de Orquestração:** Combinar varreduras de portas com outras ferramentas em fluxos de trabalho de segurança.

## 3. SubDomain Listing (Listagem de Subdomínios)

A enumeração de subdomínios expande a superfície de ataque conhecida de um alvo, revelando aplicações ou serviços menos óbvios.

### Ferramentas Comuns:

*   **Subfinder:** Uma ferramenta rápida de enumeração de subdomínios que utiliza várias fontes passivas para encontrar subdomínios válidos [6].
*   **Amass:** Uma ferramenta de enumeração de rede e descoberta de superfície de ataque que usa várias técnicas para encontrar subdomínios, incluindo OSINT, raspagem de DNS e força bruta [7].
*   **Assetfinder:** Uma ferramenta simples e rápida para encontrar domínios relacionados a um alvo.

### Métodos de Automação:

*   **Scripts de Linha de Comando:** Executar `subfinder`, `amass` ou `assetfinder` para coletar listas de subdomínios e alimentar outras ferramentas de RECON.
*   **Integração com APIs:** Utilizar APIs de serviços como `WhoisXML API` para obter listas de subdomínios [8].

## 4. DNS DIG (Domain Information Groper)

O comando `dig` é uma ferramenta flexível para consultar servidores DNS e obter informações detalhadas sobre registros de domínio, como A, MX, NS, TXT, etc.

### Ferramentas Comuns:

*   **`dig` (comando Unix/Linux):** A ferramenta padrão para realizar consultas DNS. É essencial para verificar a configuração de DNS, identificar servidores de nomes e obter registros específicos [9].

### Métodos de Automação:

*   **Scripts Shell:** Utilizar o comando `dig` em scripts para realizar consultas DNS programadas e extrair informações relevantes. Por exemplo, para obter registros A, MX, NS de um domínio.
*   **Bibliotecas Python:** Usar bibliotecas como `dnspython` para realizar consultas DNS programaticamente e analisar os resultados de forma estruturada.

## Referências

[1] Medium. *Top 15 OSINT Tools For Cybersecurity In 2025*. Disponível em: [https://cyble.com/knowledge-hub/top-15-osint-tools-for-powerful-intelligence-gathering/](https://cyble.com/knowledge-hub/top-15-osint-tools-for-powerful-intelligence-gathering/)
[2] GitHub. *jivoi/awesome-osint*. Disponível em: [https://github.com/jivoi/awesome-osint](https://github.com/jivoi/awesome-osint)
[3] OSINT Framework. *OSINT Framework*. Disponível em: [https://osintframework.com/](https://osintframework.com/)
[4] Pentest-Tools.com. *Free Port Scanner with Nmap*. Disponível em: [https://pentest-tools.com/network-vulnerability-scanning/port-scanner-online-nmap](https://pentest-tools.com/network-vulnerability-scanning/port-scanner-online-nmap)
[5] GitHub. *robertdavidgraham/masscan*. Disponível em: [https://github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan)
[6] GitHub. *projectdiscovery/subfinder*. Disponível em: [https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)
[7] GitHub. *OWASP/Amass*. Disponível em: [https://github.com/OWASP/Amass](https://github.com/OWASP/Amass)
[8] WhoisXML API. *Subdomains Lookup*. Disponível em: [https://pt.subdomains.whoisxmlapi.com/](https://pt.subdomains.whoisxmlapi.com/)
[9] Azion. *Encontrar servidores DNS usando Comando DIG*. Disponível em: [https://www.azion.com/pt-br/documentacao/produtos/guias/executar-o-comando-dig/](https://www.azion.com/pt-br/documentacao/produtos/guias/executar-o-comando-dig/)

