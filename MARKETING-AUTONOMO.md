# Marketing Autônomo — Blueprint HospitaLar

> Objetivo do Rudson: **marketing autônomo de alta conversão** — da pauta à publicação à otimização,
> com mínima intervenção manual. Decisor = familiar do paciente; conversão = WhatsApp.

## A esteira (pipeline de ponta a ponta)
`Pauta → Copy/roteiro → Geração de assets (imagem/vídeo) → Edição/branding → Publicação/agendamento → Medição → Otimização (loop)`

## Mapa: o que JÁ temos × GAPS por etapa
| Etapa | Temos (hoje) | Gap |
|---|---|---|
| **Pauta/estratégia** | playbook, análise real das contas, `lead-research-assistant`, `competitive-ads-extractor` | calendário automatizado |
| **Copy/roteiro** | Claude (PT-BR), `content-research-writer` | — |
| **Imagem** | `gerar_carrossel.py` (Pillow), `canvas-design`, `image-enhancer`, ComfyUI/RunPod (IA) | biblioteca de templates branded |
| **Vídeo (geração)** | RunPod ComfyUI RTX 4090, `video-prompting` (Seedance/Veo/Wan + character-sheet) | — |
| **Edição de vídeo** (montagem/legenda/trilha) | — | **EDITOR = gap principal** (legenda auto via Whisper) |
| **Publicação** | Meta API direto, Metricool, painel social-hub | — |
| **Agendamento** | Metricool, painel (fila + scheduler) | — |
| **Analytics (topo de funil)** | painel analytics, Meta insights (alcance/salvos/interações) | — |
| **Funil de vendas (fundo)** | — | integrar **CRM** (domínio Manus): lead→oportunidade→venda |
| **Orquestração autônoma** | n8n (instalado) | **wiring** do pipeline + cron (instalar `n8n-skills`) |

## Gaps a resolver para virar AUTÔNOMO (prioridade)
1. **Editor de vídeo** — montagem + **legenda automática** (Whisper) + trilha. Opções: ComfyUI (já temos GPU), ferramentas locais (Clipchamp instalado), ou serviço. *Decidir a ferramenta.*
2. **Orquestração n8n** — cron que dispara: gera pauta → copy → asset → publica → loga métrica. (instalar `n8n-skills`)
3. **Funil de vendas** — conectar dados do CRM p/ medir conversão real (precisa do Manus liberar dados).
4. **Templates branded** reutilizáveis (carrossel/reels) — evoluir o `gerar_carrossel`.

## Stack recomendada (autônoma, alta conversão)
- **Ideação:** `lead-research` + `competitive-ads` + playbook → pauta semanal.
- **Copy:** `content-research-writer` + Claude (CTA WhatsApp, prova social).
- **Imagem:** template branded + `image-enhancer`; IA via ComfyUI/RunPod.
- **Vídeo:** `video-prompting` → RunPod 4090 → edição (legenda/trilha) → Reels.
- **Publicação:** Metricool (planejado) / Meta API (automático). 1 post por 1 canal.
- **Medição:** painel analytics + Meta; otimizar pelo que **salva/compartilha**.
- **Orquestração:** n8n + cron (a montar).

## Skills de marketing instaladas (nesta frente)
`content-research-writer` · `competitive-ads-extractor` · `lead-research-assistant` · `invoice-organizer` · `twitter-algorithm-optimizer` · `image-enhancer` · `video-prompting` · `youtube-downloader` (+ canvas-design/theme-factory/brand-guidelines dos plugins).

## Princípios de conversão (fixos)
Decisor = familiar · CTA único = WhatsApp (35) 98876-4610 · prova social (autorizada/LGPD) · conteúdo salvável/educativo · legenda em todo vídeo · cadência 3-4/semana · ONA+GPTW como autoridade.

## Atualização 27/06 — novas chaves (fecham gaps) — todas no `.env`
- **ElevenLabs** (`api_elevenlabs`) → **narração/voz** dos Reels = fecha boa parte do gap de vídeo (faltava voz).
- **MiniMax** (`api_minimax`) + **Comfy Cloud** (`api_comfy_cloud`) → geração de vídeo/imagem IA (além do RunPod).
- **Firecrawl** (`api_firecrawl`) → pesquisa/scraping de mercado e concorrentes.
- **Skyvern** (`service_skyvern`, MCP conectado) → automação de navegador (autopost onde não há API, formulários).
- **OpenRouter / Grok / Ollama** → LLMs para copy em massa (barato).
- **Vercel** (`api_vercel`) → deploy de landing pages de campanha/captura.

Gap de vídeo agora resume-se a: **montagem + legenda automática (Whisper)** — voz/geração já temos.

## Próximos passos
1. **Editor de vídeo**: montagem + legenda automática (Whisper). Voz = ElevenLabs; geração = RunPod/MiniMax/Comfy Cloud.
2. Instalar **n8n-skills** e desenhar o workflow autônomo (cron) amarrando tudo.
3. **Biblioteca de templates** branded.
4. Integrar **funil de vendas** (CRM).
