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
