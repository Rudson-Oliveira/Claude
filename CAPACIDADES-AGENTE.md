# Capacidades do hub para projetos de agente (Vision · Headless · Computacional · LLM · RAG · RPA · Raciocínio)

> Elenco do que o hub JÁ oferece para um projeto autônomo (ex.: o que o Rudson roda em outro agente).
> Chaves nos `.env`; MCPs/serviços no registro. Use, não recrie.

## 1. 👁️ Vision (visão computacional) — ✅ forte
- `service_ollama` → **llava** (visão local, on-prem, grátis) — ideal p/ dados sensíveis (LGPD).
- `api_anthropic` (Claude) e Gemini (`.env GEMINI_API_KEY`) → visão multimodal de alta qualidade.
- `api_minimax` → multimodal.
- `mcp_computer_use` / `mcp_chrome` (screenshot) → "ver" tela/página.
- `service_comfyui` / RunPod → geração de imagem.

## 2. 🌐 Headless browser — ✅ forte
- **`service_skyvern`** (MCP conectado) → automação de navegador por IA, headless, login, formulários. **Top p/ RPA web.**
- `mcp_chrome` + chrome-devtools (plugin) → DOM, screenshot, navegação.
- `api_firecrawl` → crawl/scrape headless estruturado (e p/ RAG).
- Playwright (skill/plugin) → automação determinística.

## 3. 🖥️ Computacional (execução/compute) — ✅ forte
- `odin_shell`, `mcp_powershell`, `mcp_desktop_commander`, win-cli → shell/SO.
- **GPU:** `service_runpod` (RTX 4090 serverless) + `service_comfy_cloud` → compute pesado/IA.
- `service_comet` → hub de automação local.

## 4. 🧠 LLM — ✅ muito forte
- **`api_openrouter`** → 1 API p/ dezenas de modelos (o melhor p/ rotear/baratear).
- `api_anthropic` (Claude), `api_xai_grok` (Grok), `service_ollama` (local grátis).
- `.env` também: Gemini, Groq, Mistral, Perplexity, DeepSeek, NVIDIA, MiniMax.
- Bridges: `service_claude_bridge` / `service_grok_bridge` (inter-agente).

## 5. 📚 RAG — ⚠️ TEMOS AS PEÇAS, falta MONTAR (única lacuna)
- **Ingest:** `api_firecrawl` (web), `odin_scrape`, docs (context7).
- **Embeddings:** Ollama `nomic-embed-text` (local grátis), ou NVIDIA/OpenAI-compat (.env).
- **Vector store:** Qdrant (skills `qdrant-*` disponíveis) **ou** Supabase pgvector (já usado no VisionAI) **ou** AgentDB (skills).
- **Busca/memória:** claude-mem (busca semântica de sessões), memory MCP (knowledge graph).
- **Recomendação:** montar pipeline = Firecrawl/scrape → chunk → embed (Ollama nomic) → Qdrant/pgvector → retrieve+rerank → LLM. **É o que sugiro implementar.**

## 6. 🤖 RPA — ✅ forte
- **`mcp_n8n`** → workflows/automação (o motor).
- **`service_skyvern`** → RPA de navegador.
- `mcp_computer_use` + Windows-MCP → RPA de desktop.
- `service_comet` + autopilot → orquestração.
- Zapier/Make (skills/MCP) → 70+ apps.

## 7. 💭 Raciocínio — ✅ forte
- **`mcp_sequential_thinking`** → raciocínio passo a passo.
- `api_anthropic` (Claude Opus) → raciocínio profundo; via OpenRouter: DeepSeek-R1/o-series.
- `skill_superpowers` (systematic-debugging, brainstorming) + `skill_deep_research`.

## Veredito
**6/7 prontas para plugar.** A única a **implementar** é o **RAG** (montar o pipeline com as peças acima — sugiro Qdrant local + Ollama embeddings + Firecrawl ingest, custo ~zero on-prem).
