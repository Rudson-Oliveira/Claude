# Claude — Hub Central de Conhecimento

> Este repositorio e a fonte unica de verdade sobre o ecossistema Claude do Rudson.
> Todos os agentes Claude (Code, Desktop, Cowork, Design) consultam os arquivos aqui
> antes de iniciar qualquer tarefa.

## Estrutura

```
Claude/
├── TOOLS-REGISTRY.json      # Catalogo de todas as ferramentas disponíveis
├── TOOLS-REGISTRY-RULES.md  # Protocolo de contribuicao ao catalogo
├── CONTEXT-UNIVERSAL.md     # Contexto para colar em sessoes web
└── README.md                # Este arquivo
```

## Para agentes Claude — leia primeiro

### 1. Consulte o catalogo de ferramentas

```
URL: https://raw.githubusercontent.com/Rudson-Oliveira/Claude/main/TOOLS-REGISTRY.json
```

Antes de qualquer tarefa, leia este arquivo para saber quais ferramentas existem.

### 2. Regra de ouro para contribuicao

- Ferramenta com mesmo `id` ja existe? Nao adicione. Use e pronto.
- Ferramenta nova e funcionando? Proponha adicao seguindo `TOOLS-REGISTRY-RULES.md`.
- So adicione o que voce testou e funcionou. Nunca adicione hipotetico.

### 3. Script de bootstrap (PowerShell)

```powershell
# Em qualquer maquina Windows com o ecossistema Rudson:
.\connect-context.ps1
.\connect-context.ps1 -Task "sua tarefa aqui"
.\connect-context.ps1 -CopyToClipboard
```

Gera um briefing completo do estado atual + contexto para colar em qualquer Claude web.

---

## Ecossistema atual

| Servico | Porta | Descricao |
|---|---|---|
| ODIN Hub | 8765 | Hub de web + shell com fallback automatico |
| COMET Hub | 5000 | Hub central de automacao e agentes |
| Ollama | 11434 | LLMs locais (llama3, mistral) |
| hub_central | 5002 | Gerenciador de MCPs extras |
| n8n | — | Automacao de workflows |
| ComfyUI | 8188 | Geracao de imagens |

## Links rapidos

- [Catalogo de ferramentas](TOOLS-REGISTRY.json)
- [Regras de contribuicao](TOOLS-REGISTRY-RULES.md)
- [Inventario do ecossistema (o que ja foi instalado)](ECOSYSTEM-INVENTORY.md)
- [Contexto universal](CONTEXT-UNIVERSAL.md)
- [Repositorio principal](https://github.com/Rudson-Oliveira/CLAWDBOT-27-01-26)
