# Cyber Kill Chain: Fase de Reconhecimento (RECON)

O Cyber Kill Chain é um modelo que descreve as etapas de um ataque cibernético, desde o reconhecimento inicial até a exfiltração de dados. A fase de **Reconhecimento (RECON)** é a primeira e crucial etapa, onde o atacante coleta informações sobre o alvo antes de realizar qualquer ação direta [1].

## Objetivos da Fase de RECON

Durante a fase de RECON, os principais objetivos do atacante incluem:

*   **Identificar vulnerabilidades potenciais:** Procurar por fraquezas em sistemas, redes ou aplicações.
*   **Coletar informações sobre o pessoal-chave:** Obter dados sobre funcionários, como nomes, cargos, e-mails, que podem ser usados em ataques de engenharia social.
*   **Mapear configurações de rede:** Entender a infraestrutura de rede do alvo, incluindo endereços IP, domínios, subdomínios e serviços expostos.
*   **Analisar medidas de segurança:** Avaliar as defesas existentes para planejar como contorná-las.
*   **Determinar pontos de entrada:** Identificar possíveis vetores de ataque para acesso inicial.

## Técnicas de RECON

As técnicas de reconhecimento podem ser divididas em passivas e ativas:

### Reconhecimento Passivo

Envolve a coleta de informações sem interagir diretamente com o alvo, minimizando o risco de detecção. Exemplos incluem:

*   **Open-Source Intelligence (OSINT):** Coleta de informações publicamente disponíveis em fontes como redes sociais, sites corporativos, registros de domínio (WHOIS), mecanismos de busca e fóruns.
*   **Análise de metadados:** Extração de informações de documentos e arquivos públicos.
*   **Observação de tráfego de rede:** Monitoramento de tráfego em redes públicas ou comprometidas (sem interação direta com o alvo).

### Reconhecimento Ativo

Envolve a interação direta com o alvo, o que aumenta o risco de detecção, mas pode fornecer informações mais detalhadas. Exemplos incluem:

*   **Varredura de portas (Port Scanning):** Identificação de portas abertas e serviços em execução em hosts de rede.
*   **Varredura de vulnerabilidades:** Uso de ferramentas para identificar vulnerabilidades conhecidas em sistemas e aplicações.
*   **Engenharia social:** Interação com funcionários para obter informações confidenciais.

## Importância da Fase de RECON

A fase de RECON é fundamental porque as informações coletadas nesta etapa são usadas para planejar as fases subsequentes do ataque. Um reconhecimento bem-sucedido aumenta significativamente as chances de sucesso do atacante, permitindo que ele adapte suas táticas, técnicas e procedimentos (TTPs) para explorar as fraquezas específicas do alvo [1].

Para os defensores, entender e antecipar as atividades de reconhecimento dos atacantes é crucial para implementar medidas de segurança proativas e mitigar ameaças antes que elas escalem.

## Referências

[1] Darktrace. *Cyber Kill Chain: Definition & Examples*. Disponível em: [https://www.darktrace.com/cyber-ai-glossary/cyber-kill-chain](https://www.darktrace.com/cyber-ai-glossary/cyber-kill-chain)

