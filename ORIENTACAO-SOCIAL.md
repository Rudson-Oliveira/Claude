# Orientação — Postagens e Análises Sociais (via Claude, direto na Meta)

> Conectado direto ao Facebook (página HospitaLar) e Instagram (@hospitalarsaude) via Graph API.
> Tokens no `.env` (FB_PAGE_TOKEN, IG_BUSINESS_ID). Esta é a "via direta" com o Claude — paralela ao Metricool/CRM.

## 1. O que eu consigo fazer direto

**Publicar:**
- Instagram: **foto**, **carrossel** (várias imagens), **reels** (vídeo), **stories**.
- Facebook (página): **foto**, **post de texto/link**, **vídeo/reel**.

**Ler / analisar (read-only):**
- Seguidores, crescimento, alcance, impressões, engajamento, visitas ao perfil, cliques no link.
- Desempenho por post (likes, comentários, salvamentos, compartilhamentos, alcance).
- Melhores horários, comparativo de períodos.

## 2. Análise de funil — o que dá e o que não dá

- **Topo de funil (marketing) — EU FAÇO pela Meta:** alcance → engajamento → visitas ao perfil → cliques no link → novos seguidores. É o funil de *conteúdo/atração*.
- **Fundo de funil (vendas: lead → oportunidade → fechamento)** vive no **CRM (HospitaLar Intel, domínio do Manus)**. Para o funil de **vendas completo**, eu preciso dos números/acesso do CRM. Sem isso, entrego só a parte social.
- **Funil completo** = cruzar Meta (atração) + CRM (conversão). Posso montar se você me der os dados do CRM.

## 3. Como você procede (3 formas)

1. **Conversa (mais rápido):** "posta essa imagem [URL ou arquivo] no IG e FB com a legenda: …" → eu publico (confirmo antes de postar).
2. **Painel web (novo):** abrir `http://localhost:8910` → compor, ver preview, publicar/agendar, ver análises. (ver SOCIAL-PANEL abaixo)
3. **Análise sob demanda:** "me dá o desempenho dos últimos 30 dias" / "como está o funil de conteúdo" → eu puxo e resumo.

## 4. Requisitos de mídia (Graph API)
- Imagem/vídeo precisa de **URL pública** OU arquivo local (eu subo via upload).
- Instagram **reels** = vídeo (mp4, vertical 9:16 recomendado). Story = imagem ou vídeo.
- IG: post precisa de pelo menos 1 imagem/vídeo (não posta só texto).

## 5. Regra de segurança
- **Publicar é sempre com seu OK** (ação pública). Leitura/análise não precisa.
- Tokens só no `.env`, nunca no Git.

## 5b. Canais de publicação (Meta direto + Metricool) — redundância com papéis

Dois canais conectados para IG/FB. Redundância é boa (resiliência), mas cada post sai por **UM** canal só, para não duplicar:
- **Metricool** (MCP): calendário/agendamento manual, multi-rede (TikTok, LinkedIn, X, GBP), melhores horários, fluxo de equipe.
- **Meta API direto** (token .env / painel social-hub): pipeline autônomo (RunPod→post), análise de funil sob medida, ações por conversa, insights profundos.
- **Regra anti-duplicação:** conteúdo planejado da semana → Metricool. Conteúdo automático do pipeline → Meta API. Nunca os dois publicando o mesmo post.

## 6. Painel web (social-hub)
Arquivo: `C:\Users\rudpa\social-hub\social_panel.py` (Python stdlib, sem dependências).
Rodar: `python C:\Users\rudpa\social-hub\social_panel.py` → abrir `http://localhost:8910`.
Funções: dashboard IG/FB, compor+publicar imagem (com confirmação), base para vídeo/agendamento.
