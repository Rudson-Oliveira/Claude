# Contexto — Ecossistema Rudson (cole no início de qualquer sessão)

Você está assistindo Rudson Oliveira. Este contexto te dá acesso ao ecossistema dele.

## Quem é Rudson
- Desenvolvedor, automatizador, criador de sistemas de IA
- Trabalha com Claude Code, Claude Desktop, Claude.ai Cowork e Design
- Tem um ecossistema local rodando no Windows com vários serviços de IA

## Ecossistema local (serviços ativos)

| Serviço | O que faz | Como acessar |
|---|---|---|
| **ODIN** (porta 8765) | Hub central de web + shell com fallback automático | MCP `odin_*` tools |
| **COMET** (porta 5000) | Hub de automação e agentes | HTTP localhost:5000 |
| **Ollama** (porta 11434) | LLMs locais (llama3, mistral, etc.) | HTTP localhost:11434 |
| **hub_central** (porta 5002) | Gerenciador de MCPs extras | HTTP localhost:5002 |
| **n8n** | Automação de workflows | MCP n8n conectado |
| **ngrok Plus** | Túneis para acesso remoto | URLs via odin_status() |

## Ferramentas disponíveis no Claude Code (não na web)

- `odin_search(query)` — busca web com fallback Exa→Brave→DDG→scraping
- `odin_fetch(url)` — requisição HTTP com fallback ngrok automático
- `odin_scrape(url, selector)` — extrai texto de página
- `odin_shell(command)` — executa PowerShell com fallback cmd.exe
- `odin_comet(endpoint, payload)` — chama o COMET Hub
- `odin_status()` — status de todos os providers em tempo real

## Para sessões web (Cowork, Design, Claude.ai)

Você NÃO tem acesso às tools MCP locais. Neste caso:
- Para pesquisas: peça ao usuário para rodar `odin_search` no Claude Code e te passar o resultado
- Para comandos: o usuário pode executar via Claude Code ou terminal
- Para arquivos: o usuário pode colar o conteúdo

## Projetos ativos

- **ODIN Hub** — `C:\Users\rudpa\COMET\odin\` — MCP server Python com 6 tools, FastMCP 3.4.2
- **COMET** — `C:\Users\rudpa\COMET\` — hub central de automação
- **HospitaLar VisionAI** — sistema de saúde com IA (ver projetos)

## Como o Rudson prefere trabalhar

- Direto ao ponto, sem cerimônia
- Implemente logo, pergunte só o essencial
- Use as ferramentas disponíveis sem avisar que está usando
- Commits frequentes, fases pequenas
- Python 3.14.6 em `C:\Users\rudpa\AppData\Local\Programs\Python\Python314\`
- Node.js via nvm4w em `C:\nvm4w\nodejs\`
- Git repo principal: `C:\Users\rudpa\` (branch master)

## Fallback quando ODIN não está disponível

Web: Exa MCP → autopilot browse_web → Chrome MCP → WebSearch built-in
Shell: PowerShell MCP → Desktop Commander → Bash tool
