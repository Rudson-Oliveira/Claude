# HUGGINGFACE-NGROK.md — Hugging Face via ngrok no Ecossistema Rudson

> Arquivo de referência para agentes. Registra como o Hugging Face (HF) está integrado ao ecossistema e como expô-lo via ngrok quando necessário.
> Atualizado: 2026-07-02

---

## 1. Conta e Recursos Ativos

| Campo | Valor |
|---|---|
| Usuário | `RudsonOliveira` |
| Plano | Free (com $40.00 em créditos de Inference) |
| Billing ciclo atual | encerra em **Aug 1, 2026** |
| Spaces ativos | cosmic-data-explor, medisync-magic-dos, medisync-pro-turbo |

---

## 2. Inference Providers Configurados

O HF roteia chamadas de API para provedores de LLM. Quando não há chave própria configurada, debita dos créditos HF da conta.

### Provedores com chave própria (usa a chave, não os créditos HF):
- **Groq** — chave `gsk_...VLLX` já configurada ✅
- **Zai** — chave `xai...hi2h` já configurada ✅

### Provedores ativos sem chave própria (debitam créditos HF):
Novita, Nscale, fal, Together AI, Fireworks, Featherless AI, Replicate, Cohere, Scaleway, Public AI, OVHcloud AI Endpoints, DeepInfra, WaveSpeed, HF Inference API

### Tokens de Acesso HF:
- `Chico` — FINEGRAINED, usado há 6 dias
- `Claude` — FINEGRAINED, criado em 24/Mai
- `11-05 Claude` — FINEGRAINED + WRITE, criado em 11/Mai
- `n8n-code-reviewer` — READ only
- `N8N` — FINEGRAINED
- Outros invalidados/legados

**CHAVE EM USO:** `C:\Users\rudpa\.env → HF_TOKEN` (NUNCA no Git)

---

## 3. MCP Server do Hugging Face

O HF tem um **MCP Server nativo** que conecta qualquer agente ao ecossistema HF.

### Endpoint MCP:
```
https://hf.co/mcp
```
(requer HF_TOKEN para autenticação)

### Built-in Tools disponíveis (todos ativados exceto Repository Search e Sandboxes):
| Tool | Status | Descrição |
|---|---|---|
| Spaces Semantic Search | ✅ ativo | Busca Apps por linguagem natural |
| Papers Semantic Search | ✅ ativo | Busca papers ML por linguagem natural |
| Repository Search | ❌ desativado | Busca modelos/datasets com filtros |
| Documentation Semantic Search | ✅ ativo | Busca na docs HF |
| Run and Manage Jobs | ✅ ativo | Rodar/monitorar jobs na infra HF |
| Hub Query (Experimental) | ✅ ativo | Navega repos/social/likes (usa Inference quota) |
| Hub Repository Details | ✅ ativo | Info detalhada de modelos/datasets/Spaces |
| File Management | ✅ ativo | Upload/escrita em Repos e Buckets |
| Include repository README | ✅ ativo | Inclui READMEs nos resultados |
| Create Repositories | ✅ ativo | Cria model/dataset/Space/Bucket repos |
| Sandboxes (Experimental) | ❌ desativado | Cria e usa Sandboxes |

### Spaces Tools (adicionadas ao MCP):
- `mcp-tools/Qwen-Image-Fast` — já adicionado ✅
- Dynamic Spaces: **ativado** (chama Spaces MCP-compatíveis em runtime)
- Remove Embedded Images: desativado

### Como usar o MCP HF nos agentes:
```json
{
  "mcpServers": {
      "huggingface": {
            "command": "npx",
                  "args": ["mcp-remote", "https://hf.co/mcp"],
                        "env": {
                                "HF_TOKEN": "${HF_TOKEN}"
                                      }
                                          }
                                            }
                                            }
                                            ```

                                            ---

                                            ## 4. Local Apps — Ollama já integrado

                                            O HF tem suporte nativo a **Local Apps** — quando você abre uma página de modelo compatível, o HF mostra botões "Use with Ollama", "Use with LM Studio", etc.

                                            Apps de Text Generation habilitados:
                                            - llama.cpp ✅
                                            - LM Studio ✅
                                            - Jan ✅
                                            - vLLM ✅
                                            - SGLang ✅
                                            - **Ollama ✅** ← já marcado como preferido

                                            Isso significa que modelos HF compatíveis mostram automaticamente instruções para download via Ollama local.

                                            ---

                                            ## 5. Integração via ngrok — Quando e Como

                                            ### Caso de uso: Expor Inference Local via ngrok para outros agentes

                                            Se você rodar um modelo localmente via Ollama e quiser que o HF (ou outros agentes) o acesse remotamente:

                                            ```
                                            Ollama local (:11434) → ngrok → URL pública → qualquer agente
                                            ```

                                            **Endpoint ngrok atual do Ollama:**
                                            ```
                                            https://manus-comet-hospital.ngrok-free.dev
                                            ```
                                            Ver detalhes completos em `OLLAMA-NGROK.md`.

                                            ### Caso de uso: Webhook HF → ngrok → sistema local

                                            O HF suporta Webhooks para eventos de repositório (push, discussões, etc.).
                                            Você pode registrar o endpoint ngrok como destino:

                                            ```
                                            HF Webhook → https://hospitalar-webhook.ngrok.app/webhook/hf → processamento local
                                            ```

                                            **Configurar em:** https://huggingface.co/settings/webhooks

                                            ---

                                            ## 6. Arquitetura de Uso Recomendada

                                            ```
                                            Agente (Claude/Codex/n8n)
                                                │
                                                    ├── HF Inference API (via créditos ou chave própria)
                                                        │       ├── Groq (chave própria → mais rápido/barato)
                                                            │       ├── Together AI / Fireworks (fallback via créditos HF)
                                                                │       └── HF Inference API direta (modelos free tier)
                                                                    │
                                                                        ├── HF MCP Server → Hub tools (busca, files, jobs)
                                                                            │
                                                                                └── Ollama local (:11434)
                                                                                            └── ngrok → acesso remoto quando necessário
                                                                                            ```

                                                                                            ### Regra de roteamento (LGPD):
                                                                                            - **Dados de pacientes → SEMPRE Ollama local** (nunca HF/Groq/provedores externos)
                                                                                            - **Texto genérico, pesquisa, código** → HF Inference (Groq prioritário) ou Ollama
                                                                                            - **Modelos especializados** (vision, medical) → HF Models + Ollama local

                                                                                            ---

                                                                                            ## 7. Referências Cruzadas

                                                                                            | Documento | O que tem |
                                                                                            |---|---|
                                                                                            | `OLLAMA-NGROK.md` | Configuração completa ngrok + Ollama, Traffic Policy, exemplos de uso |
                                                                                            | `TOOLS-REGISTRY.json` | Entradas: `service_ollama`, `service_ngrok`, `service_huggingface` |
                                                                                            | `INSTRUCOES-GLOBAIS.md` | Regras gerais do ecossistema |

                                                                                            ---

                                                                                            ## 8. Ações Pendentes (usuário)

                                                                                            - [ ] **Ativar Repository Search** no MCP HF (desativado — útil para buscar modelos programaticamente)
                                                                                            - [ ] **Configurar Webhook HF** apontando para `hospitalar-webhook.ngrok.app` se quiser eventos de repo
                                                                                            - [ ] **Adicionar mais Spaces MCP-compatíveis** via busca em https://huggingface.co/spaces?filter=mcp
                                                                                            - [ ] **Considerar PRO** se precisar de ZeroGPU (40min/dia em RTX Pro 6000 Blackwell) — útil para rodar modelos grandes via Spaces sem RunPod
                                                                                            
