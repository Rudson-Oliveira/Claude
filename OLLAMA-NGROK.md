# OLLAMA-NGROK.md — Ollama via ngrok (LLM local acessível por todos os agentes)

> **Fonte única** para integrar qualquer agente do ecossistema com o Ollama rodando localmente via ngrok.  
> Consultar antes de criar qualquer chamada a LLM local.

---

## Endpoint público ativo

| Campo | Valor |
|---|---|
| **URL pública** | `https://manus-comet-hospital.ngrok-free.dev` |
| **Porta local** | `http://127.0.0.1:11434` |
| **Domínio ngrok** | `manus-comet-hospital.ngrok-free.dev` (fixo — plano pay-as-you-go) |
| **Plano ngrok** | Pay-as-you-go — sem interstitial, dominio fixo, bandwidth ilimitado |
| **Status** | ✅ Ativo (tunnel rodando no Windows) |
| **Traffic Policy Auth** | ⚠️ Pendente — configurar `x-api-key` no dashboard ngrok |

---

## Como qualquer agente deve chamar o Ollama

### Endpoint OpenAI-compatible (recomendado)

O Ollama expõe uma API compatível com OpenAI em `/v1/`. Qualquer cliente que aceita `OPENAI_BASE_URL` funciona direto.

```bash
# Variáveis de ambiente (definir no .env)
OLLAMA_NGROK_URL=https://manus-comet-hospital.ngrok-free.dev
OLLAMA_NGROK_KEY=SEU_KEY_AQUI  # a definir após configurar Traffic Policy
```

### Chamada direta (HTTP)

```bash
# Chat completions (OpenAI-compatible)
curl https://manus-comet-hospital.ngrok-free.dev/v1/chat/completions \
  -H "Content-Type: application/json" \
    -H "x-api-key: $OLLAMA_NGROK_KEY" \
      -d '{
          "model": "llama3",
              "messages": [{"role": "user", "content": "olá"}]
                }'

                # Generate (API nativa Ollama)
                curl https://manus-comet-hospital.ngrok-free.dev/api/generate \
                  -H "Content-Type: application/json" \
                    -H "x-api-key: $OLLAMA_NGROK_KEY" \
                      -d '{"model": "llama3", "prompt": "olá", "stream": false}'

                      # Listar modelos disponíveis
                      curl https://manus-comet-hospital.ngrok-free.dev/api/tags \
                        -H "x-api-key: $OLLAMA_NGROK_KEY"
                        ```

                        ### Via ODIN (MCP — agentes Claude Code)

                        ```python
                        # Dentro de qualquer sessão com ODIN disponível
                        odin_fetch(
                          url="https://manus-comet-hospital.ngrok-free.dev/v1/chat/completions",
                            method="POST",
                              headers='{"Content-Type": "application/json", "x-api-key": "$OLLAMA_NGROK_KEY"}',
                                body='{"model": "llama3", "messages": [{"role": "user", "content": "..."}]}'
                                )
                                ```

                                ### Via n8n (HTTP Request node)

                                ```json
                                {
                                  "url": "https://manus-comet-hospital.ngrok-free.dev/v1/chat/completions",
                                    "method": "POST",
                                      "headers": {
                                          "Content-Type": "application/json",
                                              "x-api-key": "{{ $env.OLLAMA_NGROK_KEY }}"
                                                },
                                                  "body": {
                                                      "model": "llama3",
                                                          "messages": [{"role": "user", "content": "{{ $json.prompt }}"}]
                                                            }
                                                            }
                                                            ```

                                                            ### Via Claude Code / Codex (OPENAI_BASE_URL)

                                                            ```bash
                                                            # Adicionar ao .env do projeto
                                                            OPENAI_BASE_URL=https://manus-comet-hospital.ngrok-free.dev/v1
                                                            OPENAI_API_KEY=$OLLAMA_NGROK_KEY
                                                            ```

                                                            ---

                                                            ## Modelos disponíveis (verificar com /api/tags)

                                                            Para listar os modelos instalados localmente:
                                                            ```bash
                                                            curl https://manus-comet-hospital.ngrok-free.dev/api/tags -H "x-api-key: $OLLAMA_NGROK_KEY"
                                                            ```

                                                            Modelos típicos no stack: `llama3`, `mistral`, `llama3.2-vision`, outros instalados via `ollama pull`.

                                                            ---

                                                            ## Quando usar Ollama (vs Groq/Claude)

                                                            | Critério | Ollama (local/ngrok) | Groq | Claude |
                                                            |---|---|---|---|
                                                            | Dados de pacientes (PHI) | ✅ Único permitido | ❌ Proibido | ❌ Proibido sem anonimização |
                                                            | Custo por token | ✅ Zero | ⚠️ Limite free tier | ⚠️ Faturado |
                                                            | Velocidade | ⚠️ Depende do hardware local | ✅ Muito rápido (LPU) | ⚠️ Normal |
                                                            | Qualidade | ⚠️ Modelos menores | ⚠️ Modelos mid | ✅ Melhor qualidade |
                                                            | Disponibilidade offline | ✅ Sim | ❌ Não | ❌ Não |
                                                            | Fallback automático | ✅ Usar como fallback de Groq/Claude | — | — |

                                                            **Regra:** dados sensíveis (pacientes, PHI) → sempre Ollama. Tarefas rápidas sem dados → Groq. Raz. complexo/artefatos → Claude.

                                                            ---

                                                            ## Traffic Policy ngrok (⚠️ Pendente — configurar)

                                                            O endpoint está público sem autenticação. Configurar no dashboard ngrok:

                                                            ```yaml
                                                            # Traffic Policy a aplicar no endpoint manus-comet-hospital.ngrok-free.dev
                                                            on_http_request:
                                                              - name: "Auth x-api-key"
                                                                  expressions:
                                                                        - "req.headers['x-api-key'] != 'SEU_KEY_AQUI'"
                                                                            actions:
                                                                                  - type: custom-response
                                                                                          config:
                                                                                                    status_code: 401
                                                                                                              body: '{"error":"Unauthorized"}'
                                                                                                                        headers:
                                                                                                                                    content-type: "application/json"
                                                                                                                                    
                                                                                                                                      - name: "Rate limit 30/min por IP"
                                                                                                                                          actions:
                                                                                                                                                - type: rate-limit
                                                                                                                                                        config:
                                                                                                                                                                  name: "ollama-rl"
                                                                                                                                                                            algorithm: sliding_window
                                                                                                                                                                                      capacity: 30
                                                                                                                                                                                                rate: "1m"
                                                                                                                                                                                                          bucket_key:
                                                                                                                                                                                                                      - req.headers['x-forwarded-for']
                                                                                                                                                                                                                      
                                                                                                                                                                                                                        - name: "Bloquear rotas não-API"
                                                                                                                                                                                                                            expressions:
                                                                                                                                                                                                                                  - "!req.url.path.startsWith('/api/') && !req.url.path.startsWith('/v1/')"
                                                                                                                                                                                                                                      actions:
                                                                                                                                                                                                                                            - type: custom-response
                                                                                                                                                                                                                                                    config:
                                                                                                                                                                                                                                                              status_code: 403
                                                                                                                                                                                                                                                                        body: '{"error":"Forbidden"}'
                                                                                                                                                                                                                                                                        ```
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        Após configurar: definir `OLLAMA_NGROK_KEY` no `.env` local e atualizar este arquivo.
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        ---
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        ## Outros domínios ngrok do ecossistema
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        | Domínio | Serviço | Porta local |
                                                                                                                                                                                                                                                                        |---|---|---|
                                                                                                                                                                                                                                                                        | `hospitalar-webhook.ngrok.app` | VisionAI Webhook (Anthropic Agents) | 3026 |
                                                                                                                                                                                                                                                                        | `hospitalar-openclaw-admin.ngrok.app` | OpenClaw Admin Panel | — |
                                                                                                                                                                                                                                                                        | `obsidian-rudson.ngrok-free.app` | Claude / Obsidian | — |
                                                                                                                                                                                                                                                                        | `manus-comet-hospital.ngrok-free.dev` | **Ollama LLM local** | 11434 |
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        ---
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        ## Checklist de integração (novo agente/cliente)
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        - [ ] Definir `OLLAMA_NGROK_URL` e `OLLAMA_NGROK_KEY` no `.env`
                                                                                                                                                                                                                                                                        - [ ] Testar com `curl /api/tags` para confirmar modelos disponíveis
                                                                                                                                                                                                                                                                        - [ ] Para OpenAI-compatible: usar `/v1/chat/completions` com `model: llama3`
                                                                                                                                                                                                                                                                        - [ ] Para API nativa: usar `/api/generate` ou `/api/chat`
                                                                                                                                                                                                                                                                        - [ ] Dados sensíveis: SEMPRE usar Ollama, nunca Groq/Claude externo
                                                                                                                                                                                                                                                                        - [ ] Traffic Policy ngrok configurada antes de usar em produção
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        ---
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        *Atualizado: 2026-07-02 | Agente: claude-browser*
