# Tarefas Pendentes — Ecossistema Rudson (handoff)

> Última atualização: 2026-06-21. Qualquer agente: leia isto + MEMORY.md antes de continuar.
> Status: [ ] a fazer · [~] em andamento · [x] feito

## 🔴 PRIORIDADE — Conteúdo / Postagens (social)

- [ ] **1. Postar o carrossel "5 sinais de Home Care"**
  - Arte pronta: `C:\Users\rudpa\social-hub\carrossel-5sinais\` (8 PNGs 1080x1080, com acentos).
  - Legenda pronta: em `CONTENT-PLAYBOOK-HOSPITALAR.md` (seção 3).
  - **Bloqueio técnico:** IG exige URL pública das imagens. Resolver: servir a pasta via ngrok (o painel social-hub pode ganhar uma rota estática) OU subir as imagens num host.
  - Publicar por **UM** canal: Metricool (agendar) OU Meta API (painel :8910). Nunca os dois.

- [ ] **2. Reels / vídeo de humanização**
  - Roteiro pronto no playbook (seção 4).
  - Gerar vídeo via RunPod (endpoint ComfyUI `xs4fuq5jjkem1h`, RTX 4090). **Gasta crédito** → só com OK do Rudson.
  - Publicar como Reels (IG) + vídeo (FB).

- [ ] **3. Calendário de conteúdo** (cadência 3-4 posts/semana) — montar no Metricool (brand 6395876).

## 🟡 Analytics / Funil
- [ ] **4. Funil de vendas completo** = cruzar Meta (atração) + CRM HospitaLar Intel (conversão). Precisa dos dados do CRM (domínio do Manus). Funil de conteúdo (topo) já dá pra fazer pela Meta.

## 🟢 Ecossistema — decisões do Rudson (colar/decidir)
- [ ] **5. Colar instruções globais** no campo do Claude (Chat/Cowork) — texto em `INSTRUCOES-GLOBAIS.md`.
- [ ] **6. Colar instruções por agente** — Codex (`~/.codex/AGENTS.md`), Grok, COMET — texto em `INSTRUCOES-AGENTES.md`.
- [ ] **7. PR #44** (gate no repo hospitalarsaude-intel) — mergear ou fechar. **Decisão do Rudson/Manus** (repo é exclusivo do Manus).
- [ ] **8. Ollama** — instalar ou informar caminho. **COMET autostart** no logon (opcional).

## ⚠️ Segurança (importante)
- [ ] **9. Regenerar tokens expostos no chat** e atualizar `.env`: RunPod (RUNPOD_API_KEY), Facebook App Secret (FB_APP_SECRET) e Page Token. O `.env` está fora do Git (ok), mas o chat pode ter sido logado.

## ✅ Já concluído nesta sessão (não refazer)
- Meta FB/IG conectado direto (Graph API, tokens no .env). Metricool conectado.
- Painel `social-hub` v2 (:8910): dashboard, analytics real, publicar, agendar.
- Carrossel "5 sinais" gerado (8 PNGs). Playbook + orientação no hub.
- Fix node MCP (Claude+Codex → Program Files\nodejs). Claude×Codex separados (sem conflito). COMET :5000 no ar.
- RunPod conectado (endpoint ComfyUI RTX 4090). Registro central com 30 ferramentas.
- **NADA tocado no repo hospitalarsaude-intel (Manus trabalha sozinho lá).**
