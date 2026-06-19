# Status do Ecossistema — o que temos conectado (2026-06-16)

> Inventário simples do que foi feito. Detalhe completo: `TOOLS-REGISTRY.json`.

## Hub central (fonte única)
Repo **Rudson-Oliveira/Claude** — 26 ferramentas catalogadas + gate + coordenação.
Arquivos: TOOLS-REGISTRY.json · TOOLS-REGISTRY-RULES.md · ECOSYSTEM-INVENTORY.md ·
INSTRUCOES-GLOBAIS.md · INSTRUCOES-AGENTES.md · CONTEXT-UNIVERSAL.md.

## Agentes
| Agente | Papel | Modo |
|---|---|---|
| Claude (Code/Chat/Cowork/Design) | conhecimento, arquitetura, governança | em sync |
| Codex | execução de código, testes, refactor | em sync |
| Grok | contexto 512K, codebase grande | em sync |
| COMET | hub de automação/orquestração | em sync |
| **Manus** | CRM hospitalarsaude-intel | **paralelo/isolado (caro)** |

## Serviços locais
| Serviço | Porta | Status |
|---|---|---|
| ODIN (web+shell hub) | 8765 | ✅ conectado |
| COMET Bridge | 5000 | ✅ no ar |
| Ollama (LLMs locais) | 11434 | ❌ não instalado |
| Claude MCP Bridge | 18791 | ⚙️ criado (claude-stack) |
| Grok MCP Bridge | 18790 | ⚙️ criado (claude-stack) |
| ngrok (túneis) | — | configurado |

## MCPs/integrações principais conectados
ODIN (search/fetch/shell/comet/status) · PowerShell · filesystem · context7 ·
sequential-thinking · memory · Metricool (social) · Chrome · Computer-use · n8n-mcp.

## Instruções (onde cada uma vai)
| Superfície | Local | Status |
|---|---|---|
| Claude Code | CLAUDE.md global | ✅ feito |
| Claude Chat + Cowork | campo Configurações→Geral | ⏳ colar (texto pronto) |
| Claude Design | herda da conta | ✅ nada a fazer |
| Codex | ~/.codex/AGENTS.md | ⏳ colar |
| Grok | instruções/.grok | ⏳ colar |
| COMET | system prompt do router | ⏳ colar |

## Regras-chave
- Gate obrigatório: consultar o registro antes de agir; usar a melhor ferramenta; registrar descobertas.
- Git = fonte única (pull antes, branch+PR, não duplicar).
- Manus isolado: outros só leem/revisam/orientam, sem PR no repo dele.
- 1 script de conexão canônico (`connect-context.ps1`) — parar de recriar (já há 6 variantes).

## Pendências do Rudson
1. Colar instruções (Chat/Cowork, Codex, Grok, COMET).
2. Ollama: instalar ou informar caminho.
3. (Opcional) COMET autostart no logon.
