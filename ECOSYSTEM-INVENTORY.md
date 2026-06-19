# Inventário do Ecossistema — o que já foi instalado/integrado

> Snapshot das sessões Claude (Desktop/Code) em **2026-06-16**. Capturado da lista de sessões.
> **Objetivo:** parar o retrabalho. Antes de instalar/integrar algo, **cheque aqui** se já existe.
> Parcial (havia "+9" sessões não exibidas) — completar conforme surgirem.
>
> Legenda: ✅ funcionando · ⚠️ verificar/pendente · 🔄 em andamento

## MCP servers / plugins
| Item | Status |
|---|---|
| MCP internet plugin ("Canivete suíço") | 🔄 |
| Metricool MCP server | ✅ |
| n8n-mcp (GitHub integration) | ✅ |
| MCP Windows desktop | 🔄 |
| Browser Use integration (webhook n8n — repo n8n-workflows PR#2) | ⚠️ não verificado: sem processo/porta local; vive como workflow n8n |

## Skills / ferramentas de agente
| Item | Status |
|---|---|
| Superpowers (setup) | ✅ |
| Claude Mem (installation check) | ✅ |
| Awesome-claude-code | ✅ |
| Obsidian skills | ⚠️ |
| Get-shit-done (setup) | ⚠️ |
| Remotion (video — relacionado ao gap de vídeo do HospitaLar Intel) | ⚠️ |

## Ecossistemas / integrações
| Item | Status |
|---|---|
| Salesforce Agentforce | ✅ |
| LlamaIndex | 🔄 |
| Holo-cine | 🔄 |
| Open Design platform (avaliação de interesse) | 🔄 |
| RUFLO (installation status) | ⚠️ |

## Automação / publicação
| Item | Status |
|---|---|
| Social media auto-publishing (HospitaLar Intel) | ✅ |
| Metricool (installation) | ✅ |
| Local N8N (basic plan) | 🔄 |
| Dynamic workflows | 🔄 |

## Agentes
| Item | Status |
|---|---|
| Claude managed agents (form) | 🔄 |

## Bridges inter-agente (claude-stack)
> Em `C:\Users\rudpa\Documents\claude-stack\`. Expõem um agente como MCP para os outros.

| Item | Porta | Status |
|---|---|---|
| Claude MCP Bridge (`claude_mcp_bridge.py`) | 18791 | ✅ criado |
| Grok MCP Bridge (`grok_mcp_bridge.py`) | 18790 | ✅ criado |

> ⚠️ **Fragmentação a consolidar:** o `claude-stack` tem docs próprias (`ECOSYSTEM-REF.md`,
> `project_context.md`, `CLAUDE_ORIENTATION.md`) **paralelas e em parte desatualizadas** vs.
> este hub (ex.: ECOSYSTEM-REF aponta Python313; o ODIN usa Python314). Unificar para o hub
> central ser a única fonte. Configs `[mcp_servers.claude]`/`[mcp_servers.grok]` em `.codex/` e `.grok/`.

---

## Regra (anti-retrabalho)

Antes de abrir uma sessão "Installation/Integration check" ou instalar algo:
1. Procure o item nesta tabela.
2. Se está ✅ → **use, não reinstale**. Veja a ferramenta no [TOOLS-REGISTRY.json](TOOLS-REGISTRY.json).
3. Se está ⚠️ → **retome/conserte**, não recomece do zero.
4. Só se não existir → instale, e **adicione aqui** + ao registro.

> Várias sessões repetidas ("Ecosystem installations and guidance", "Installation check")
> indicam o retrabalho que este inventário existe para evitar.
