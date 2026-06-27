# Skills recomendadas para o ecossistema HospitaLar

> Análise do catálogo **awesome-claude-skills** (awesomeclaude.ai) filtrada pelo nosso fit:
> home care/saúde + social media + automação (n8n) + dev + agentes.
> Regra: antes de instalar, conferir se já não vem nos plugins (anti-duplicação).

## ✅ Já disponíveis (plugins anthropic-skills / superpowers) — só usar
- **docx, pdf, pptx, xlsx** → propostas, relatórios, **orçamentos** (HospitaLar envia orçamentos).
- **canvas-design, theme-factory, web-artifacts-builder, slack-gif** → criação visual.
- **deep-research, brainstorming, mcp-builder, skill-creator** → pesquisa, ideação, criação de skills.
> Não reinstalar — já carregam.

## ✅ Já instaladas nesta sessão
- **image-enhancer** (artes/posts) · **video-prompting** (Reels/vídeo-novela) · **youtube-downloader** (referência).

## 🎯 Recomendadas a ADICIONAR (alto fit, ainda não temos)
| Skill | Por que serve à HospitaLar |
|---|---|
| **n8n-skills** | Vocês usam n8n — acelera criar/editar workflows de automação |
| **WhatsApp Automation** (Composio) | WhatsApp é o **CTA principal** do home care; automatizar resposta/triagem |
| **Invoice Organizer** | Organizar **orçamentos/financeiro** (financeiro02@, orcamentos@) |
| **Lead Research Assistant** | Prospecção B2B de **parceiros** (hospitais, clínicas, geriatras) |
| **Brand Guidelines / Brand Build** | Padronizar identidade visual nos posts |
| **Content Research Writer / article-extractor** | Produção de conteúdo educativo (o que converte) |
| **Competitive Ads Extractor** | Espionar anúncios de concorrentes de home care |
| **NotebookLM Integration** | Base de conhecimento (protocolos, FAQs) |

## ⚙️ Automação via Composio (avaliar — precisa do plugin Composio)
Instagram / LinkedIn / Gmail / Google Calendar / Notion / Slack Automation, etc.
> **Cuidado anti-duplicação:** IG/FB já temos por **Meta API direto + Metricool**. Só adotar Composio
> para o que ainda NÃO cobrimos (ex.: WhatsApp, Gmail, Calendar). Não duplicar o que já funciona.

## ❌ Fora de escopo (ignorar)
family-history-research, swiftui-design, raffle-winner, computer-forensics, threat-hunting, etc.

## Como instalar uma skill nova
1. Confirmar no `TOOLS-REGISTRY.json` que não existe equivalente.
2. Clonar a pasta da skill para `~/.claude/skills/<nome>/` (com SKILL.md).
3. Registrar no `TOOLS-REGISTRY.json` (id `skill_*`).

Catálogo completo: https://awesomeclaude.ai/awesome-claude-skills
