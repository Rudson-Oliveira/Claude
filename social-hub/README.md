# social-hub — painel e geradores de conteúdo social

Código versionado do canal direto IG/FB (Meta Graph API). **Tokens nunca aqui — só no `C:\Users\rudpa\.env`.**

## Arquivos
- `social_panel.py` — painel web local (Python stdlib, porta 8910). Abas: Dashboard, Funil/Analytics (insights reais), Publicar (imagem/carrossel/reels), Agendados (fila + scheduler).
- `gerar_carrossel.py` — gera os 8 slides do carrossel "5 sinais de Home Care" (1080×1080, Pillow). Saída: `carrossel-5sinais/`. As artes finais também estão em `../social-assets/carrossel-5sinais/` (URLs públicas p/ o IG).

## Como rodar
```
# painel
python social_panel.py            # abre http://localhost:8910

# gerar/editar o carrossel (precisa: pip install Pillow)
python gerar_carrossel.py
```

## Pré-requisitos
- `.env` com FB_PAGE_TOKEN, FB_PAGE_ID, IG_BUSINESS_ID, FB_APP_SECRET (Meta) — ver memória/registro.
- Publicar no IG exige URL pública da imagem → usar GitHub raw (`social-assets/`) ou host equivalente. ngrok-free NÃO serve (página de aviso).

## Relacionado (hub)
ORIENTACAO-SOCIAL.md · CONTENT-PLAYBOOK-HOSPITALAR.md · TOOLS-REGISTRY.json (service_social_panel, api_meta, mcp_metricool).
