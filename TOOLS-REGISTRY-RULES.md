# Regras do Registro de Ferramentas (TOOLS-REGISTRY)

> Leia antes de propor qualquer adição ao TOOLS-REGISTRY.json

---

## O que é o registro

`TOOLS-REGISTRY.json` é a fonte única de verdade sobre quais ferramentas existem no
ecossistema Rudson. Todos os agentes Claude (Code, Desktop, Cowork, Design) consultam
este arquivo no início de qualquer sessão.

URL de leitura direta (sem auth):
```
https://raw.githubusercontent.com/Rudson-Oliveira/Claude/main/TOOLS-REGISTRY.json
```

---

## 🚦 GATE OBRIGATÓRIO — antes de qualquer tarefa (BLOQUEANTE)

> **O agente NÃO PODE dar prosseguimento até concluir TODAS as etapas abaixo.**
> Pular este gate é o que faz agentes "comerem bola": reinventam ferramentas,
> geram retrabalho e custo desnecessário.

1. **Ler o registro inteiro** — `TOOLS-REGISTRY.json` via raw_url.
2. **Ler estas regras** — o arquivo que você está lendo agora.
3. **Antes de USAR algo** — procure no registro a ferramenta certa por objetivo/tags.
   Pergunte: *"que ferramenta aqui já resolve isso?"*
4. **Antes de CRIAR algo** — confirme pelo campo `id` que ainda não existe.
   Se existe equivalente → **use, não recrie**.
5. **Confirme internamente** antes da primeira ação:
   *"Registro lido, X ferramentas conhecidas, nada do que preciso está sendo recriado."*

### Ferramentas críticas — leia PRIMEIRO

Estas são a base do ecossistema (campo `_meta.critical_tools`). Nunca crie equivalentes:

| id | Por quê é crítica |
|---|---|
| `odin_search` / `odin_fetch` / `odin_shell` | Cobrem 100% de web e shell com fallback automático |
| `odin_status` | Diagnóstico em tempo real de todos os providers |
| `cli_connect_context` | Único ponto de entrada para onboarding de qualquer agente |

### ⚠️ Exemplo real de falha do gate

`Connect-Claude.ps1` (repo `n8n-workflows`) foi criado **duplicando** `connect-context.ps1`
que já existia — o agente não consultou o registro. Resultado: dois scripts de conexão
divergentes, manutenção dobrada. **Isso é exatamente o que o gate previne.**

---

## 🔀 Coordenação multi-agente (Git = fonte única)

> Vários agentes editam os MESMOS repositórios em paralelo: **Claude Code, Manus, Cowork,
> Desktop**. Sem disciplina de Git, eles duplicam trabalho e geram PRs concorrentes.

**Regras (obrigatórias antes de tocar em qualquer repo):**

1. `git pull origin <branch>` **antes** de começar — o estado pode ter mudado por outro agente.
2. `git fetch` + procurar no repo se o arquivo/script que você vai criar **já existe**.
3. Trabalhe em **branch designada**, nunca commit direto na `main`.
4. Ao terminar, **abra PR** — não mergeie sozinho sem o ok do Rudson.

**Casos reais (mesmo erro, 3 vezes):**
- `Connect-Claude.ps1` (n8n) duplicou `connect-context.ps1`.
- `scripts/connect-claude.ps1` (hospitalar PR #40, via Manus) — 3ª variante do mesmo bootstrap.

> Se você é Manus ou outro agente não-Claude lendo isto: o mesmo vale. Git é a fonte única;
> `pull` antes, cheque duplicata, branch + PR. Nunca dois agentes criando o mesmo arquivo.

### Antes de INSTALAR/INTEGRAR algo: cheque o inventário

Consulte `ECOSYSTEM-INVENTORY.md` **antes** de abrir uma sessão de instalação:
- ✅ já funciona → **use, não reinstale**
- ⚠️ pendente → **retome/conserte**, não recomece
- não existe → instale e **adicione ao inventário + ao registro**

> Dezenas de sessões repetidas de "installation/integration" foram retrabalho evitável.
> O inventário é o anti-retrabalho no nível de sessão.

### Ambiente DEV compartilhado

Mesmo ambiente, mesas separadas: **Git remoto + serviços locais (ODIN/Ollama/COMET/MySQL) são
compartilhados**; cada agente trabalha em **branch/worktree própria**. Nunca dois agentes editando
o mesmo working tree.

---

## Regras de adição (OBRIGATÓRIAS)

### 1. Verifique antes de adicionar

Antes de propor uma nova ferramenta, confirme que ela NÃO existe no registro:

```python
# Verificação: leia o registro e compare pelo campo "id"
# Se já existe um item com o mesmo "id" → NÃO adicione, apenas atualize last_seen
# Se não existe → siga o processo abaixo
```

### 2. Quando adicionar

Adicione uma ferramenta SOMENTE se:
- [ ] Você usou a ferramenta com sucesso (não apenas descobriu)
- [ ] Ela está disponível no ecossistema atual (não é hipotética)
- [ ] Ela agrega valor real (não é redundante com algo já existente)

### 3. Estrutura obrigatória para novas ferramentas

```json
{
  "id": "nome_unico_sem_espacos",
  "name": "Nome legível",
  "type": "mcp | local-service | external-api | skill | cli-tool",
  "server": "nome_do_servidor_mcp ou null",
  "available_in": ["claude-code", "claude-desktop-code", "all"],
  "status": "active | available | experimental | deprecated",
  "description": "Uma frase clara sobre o que faz",
  "usage": "Como chamar a ferramenta",
  "example": "Exemplo concreto de uso",
  "tags": ["tag1", "tag2"],
  "added": "YYYY-MM-DD",
  "added_by": "claude-code | claude-desktop | cowork | design | human"
}
```

### 4. Campos de status

| Status | Significa |
|---|---|
| `active` | Testada e funcionando agora |
| `available` | Instalada/configurada mas não testada recentemente |
| `experimental` | Funcionando parcialmente, use com cautela |
| `deprecated` | Não use mais — existe substituto |

### 5. IDs únicos — convenções

| Tipo | Prefixo | Exemplo |
|---|---|---|
| MCP tool | `mcp_` | `mcp_powershell` |
| Ferramenta ODIN | `odin_` | `odin_search` |
| Serviço local | `service_` | `service_ollama` |
| API externa | `api_` | `api_anthropic` |
| Skill Claude | `skill_` | `skill_superpowers` |
| CLI tool | `cli_` | `cli_git` |

### 6. Comente as ferramentas importantes

Ferramentas centrais devem ser sinalizadas para não passarem despercebidas:

- `"critical": true` — marca a ferramenta como base do ecossistema.
- `"note": "..."` — comentário livre: o que NÃO fazer, equivalentes a evitar, pegadinhas.
- Adicione o `id` em `_meta.critical_tools.ids` para que apareça no topo do gate.

> Regra de ouro: se um agente pode "comer bola" ignorando ou duplicando a ferramenta,
> ela merece `critical` + `note`.

---

## Processo de contribuição

### Para agentes Claude

1. Ao usar uma ferramenta nova com sucesso, anote os detalhes
2. Leia o TOOLS-REGISTRY.json atual via `odin_fetch` (URL acima)
3. Verifique se o `id` já existe
4. Se novo: adicione ao array `tools[]` seguindo a estrutura
5. Atualize `_meta.total_tools` e `_meta.last_updated`
6. Proponha o commit ao usuário com mensagem `registry: add [id]`

### Para o usuário (Rudson)

- Revise propostas de adição antes de commitar
- Você é o árbitro final — uma ferramenta só entra se você aprovar
- Pode marcar ferramentas como `deprecated` quando pararem de ser usadas

---

## O que NÃO adicionar

- Ferramentas que você apenas leu sobre (nunca usou)
- Serviços temporários ou de teste
- Duplicatas com nome diferente (consolide em um único entry)
- Ferramentas de terceiros sem relação com o ecossistema do Rudson

---

## Como os agentes devem usar o registro

```python
# Ao iniciar qualquer sessão Claude Code:
# 1. Leia o registro
registro = odin_fetch("https://raw.githubusercontent.com/Rudson-Oliveira/Claude/main/TOOLS-REGISTRY.json")

# 2. Filtre por available_in
ferramentas_disponiveis = [t for t in registro["tools"] if "claude-code" in t["available_in"] or "all" in t["available_in"]]

# 3. Ao iniciar uma tarefa, consulte: "que ferramenta aqui serve para [objetivo]?"
```

---

*Atualizado: 2026-06-14*
