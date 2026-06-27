"""
Social Hub v2 — painel local IG/FB (Meta Graph API). Python stdlib, sem dependencias.
Abas: Dashboard | Funil/Analytics | Publicar (imagem/carrossel/reels) | Agendados.
Rodar: python C:\\Users\\rudpa\\social-hub\\social_panel.py  -> http://localhost:8910
Publicar exige clique+confirmacao. Agendamento: fila local + thread publica no horario (painel precisa estar aberto).
"""
import json, hmac, hashlib, time, threading, datetime, urllib.request, urllib.parse, urllib.error, os
from http.server import HTTPServer, BaseHTTPRequestHandler

V="v21.0"; PORT=8910
ENVP=r"C:\Users\rudpa\.env"
QUEUE=os.path.join(os.path.dirname(__file__), "scheduled.json")
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def load_env():
    e={}
    for line in open(ENVP,encoding="utf-8",errors="replace"):
        if "=" in line and not line.strip().startswith("#"):
            k,v=line.split("=",1); e[k.strip()]=v.strip()
    return e
ENV=load_env()
SEC=ENV.get("FB_APP_SECRET",""); TOK=ENV.get("FB_PAGE_TOKEN",""); PAGE=ENV.get("FB_PAGE_ID",""); IG=ENV.get("IG_BUSINESS_ID","")

def proof(t): return hmac.new(SEC.encode(),t.encode(),hashlib.sha256).hexdigest()
def G(method,path,params):
    p=dict(params); p["access_token"]=TOK; p["appsecret_proof"]=proof(TOK)
    try:
        if method=="GET":
            req=urllib.request.Request("https://graph.facebook.com/%s/%s?%s"%(V,path,urllib.parse.urlencode(p)),headers={"User-Agent":UA})
        else:
            req=urllib.request.Request("https://graph.facebook.com/%s/%s"%(V,path),data=urllib.parse.urlencode(p).encode(),headers={"User-Agent":UA})
        with urllib.request.urlopen(req,timeout=120) as r:
            return json.loads(r.read().decode("utf-8","replace"))
    except urllib.error.HTTPError as e:
        try: return {"error":json.loads(e.read().decode())["error"]}
        except: return {"error":{"message":"HTTP %s"%e.code}}
    except Exception as e:
        return {"error":{"message":str(e)}}

def overview():
    return {"ig":G("GET",IG,{"fields":"username,followers_count,media_count"}) if IG else {"error":"sem IG"},
            "fb":G("GET",PAGE,{"fields":"name,fan_count,followers_count"}) if PAGE else {"error":"sem FB"}}

def analytics():
    out={"ig_account":{},"ig_media":[],"notes":[]}
    if not IG: out["notes"].append("sem IG_BUSINESS_ID"); return out
    # insights de conta (precisa instagram_manage_insights)
    for metric in ("reach","profile_views","accounts_engaged"):
        r=G("GET","%s/insights"%IG,{"metric":metric,"period":"day","metric_type":"total_value"})
        if "data" in r and r["data"]:
            tv=r["data"][0].get("total_value",{})
            out["ig_account"][metric]=tv.get("value") if isinstance(tv,dict) else None
        elif "error" in r:
            out["notes"].append("insights '%s': %s"%(metric, r["error"].get("message","")[:80]))
    # desempenho por post recente
    m=G("GET","%s/media"%IG,{"fields":"caption,media_type,media_product_type,like_count,comments_count,timestamp,permalink","limit":12})
    if "data" in m:
        for p in m["data"]:
            row={"type":p.get("media_product_type") or p.get("media_type"),"likes":p.get("like_count"),
                 "comments":p.get("comments_count"),"ts":(p.get("timestamp") or "")[:10],
                 "cap":(p.get("caption") or "")[:60],"link":p.get("permalink")}
            ins=G("GET","%s/insights"%p["id"],{"metric":"reach,saved,total_interactions"})
            if "data" in ins:
                for it in ins["data"]: row[it["name"]]=(it.get("values",[{}])[0].get("value"))
            out["ig_media"].append(row)
    elif "error" in m:
        out["notes"].append("media: %s — reautorize com instagram_basic/insights"%m["error"].get("message","")[:80])
    return out

def _wait_container(cid):
    for _ in range(40):
        s=G("GET",cid,{"fields":"status_code"})
        if s.get("status_code")=="FINISHED": return True
        if s.get("status_code")=="ERROR": return False
        time.sleep(3)
    return False

def ig_image(url,cap):
    c=G("POST","%s/media"%IG,{"image_url":url,"caption":cap}); cid=c.get("id")
    return G("POST","%s/media_publish"%IG,{"creation_id":cid}) if cid else c
def ig_carousel(urls,cap):
    kids=[]
    for u in urls:
        c=G("POST","%s/media"%IG,{"image_url":u,"is_carousel_item":"true"})
        if c.get("id"): kids.append(c["id"])
        else: return c
    par=G("POST","%s/media"%IG,{"media_type":"CAROUSEL","children":",".join(kids),"caption":cap}); cid=par.get("id")
    return G("POST","%s/media_publish"%IG,{"creation_id":cid}) if cid else par
def ig_reel(video_url,cap):
    c=G("POST","%s/media"%IG,{"media_type":"REELS","video_url":video_url,"caption":cap}); cid=c.get("id")
    if not cid: return c
    if not _wait_container(cid): return {"error":{"message":"video nao processou a tempo"}}
    return G("POST","%s/media_publish"%IG,{"creation_id":cid})
def fb_photo(url,msg): return G("POST","%s/photos"%PAGE,{"url":url,"message":msg})
def fb_video(url,msg): return G("POST","%s/videos"%PAGE,{"file_url":url,"description":msg})

def publish(kind,target,media,caption):
    res={}
    if target in ("ig","both") and IG:
        if kind=="reel": res["instagram"]=ig_reel(media[0],caption)
        elif kind=="carousel": res["instagram"]=ig_carousel(media,caption)
        else: res["instagram"]=ig_image(media[0],caption)
    if target in ("fb","both") and PAGE:
        if kind=="reel": res["facebook"]=fb_video(media[0],caption)
        else: res["facebook"]=fb_photo(media[0],caption)
    return res

def q_load():
    try: return json.load(open(QUEUE,encoding="utf-8"))
    except: return []
def q_save(q): json.dump(q,open(QUEUE,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

def scheduler():
    while True:
        try:
            q=q_load(); now=datetime.datetime.now().timestamp(); ch=False
            for item in q:
                if item.get("status")=="pending" and item.get("when_ts",0)<=now:
                    r=publish(item["kind"],item["target"],item["media"],item["caption"])
                    item["status"]="done"; item["result"]=r; ch=True
            if ch: q_save(q)
        except Exception: pass
        time.sleep(30)

HTML="""<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Social Hub — HospitaLar</title><style>
*{box-sizing:border-box}body{font-family:system-ui,Segoe UI,Arial;margin:0;background:#0f1115;color:#e8e8ea}
.wrap{max-width:920px;margin:0 auto;padding:22px}h1{font-size:20px;margin:0 0 2px}.sub{color:#9aa0a6;font-size:13px;margin-bottom:16px}
.tabs{display:flex;gap:6px;margin-bottom:16px;flex-wrap:wrap}.tab{background:#1a1d24;border:1px solid #272b33;color:#c7ccd1;border-radius:8px;padding:8px 14px;cursor:pointer;font-size:13px}
.tab.on{background:#2563eb;color:#fff;border-color:#2563eb}.panel{display:none}.panel.on{display:block}
.card{background:#1a1d24;border:1px solid #272b33;border-radius:12px;padding:16px;margin-bottom:14px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:14px}.big{font-size:26px;font-weight:600}.muted{color:#9aa0a6;font-size:13px}
label{display:block;font-size:13px;color:#c7ccd1;margin:12px 0 6px}input,textarea,select{width:100%;background:#0f1115;border:1px solid #2b2f37;border-radius:8px;color:#e8e8ea;padding:10px;font-size:14px;font-family:inherit}
textarea{min-height:90px}button{background:#2563eb;border:0;color:#fff;border-radius:8px;padding:11px 18px;font-weight:600;cursor:pointer}
table{width:100%;border-collapse:collapse;font-size:13px}td,th{border-bottom:1px solid #272b33;padding:7px;text-align:left}
#out,#aout,#sout{white-space:pre-wrap;font-size:13px;background:#11141a;border:1px solid #272b33;border-radius:8px;padding:12px;margin-top:12px}
.tag{background:#16351f;color:#7ee2a8;border-radius:999px;padding:2px 10px;font-size:12px}
</style></head><body><div class=wrap>
<h1>Social Hub — HospitaLar</h1><div class=sub>Via direta com o Claude · IG + FB · <span class=tag>conectado</span></div>
<div class=tabs>
<div class="tab on" onclick="T('d')">Dashboard</div><div class=tab onclick="T('a')">Funil / Analytics</div>
<div class=tab onclick="T('p')">Publicar</div><div class=tab onclick="T('s')">Agendados</div></div>

<div id=d class="panel on"><div class=cards>
<div class=card><div class=muted>Instagram</div><div class=big id=igf>—</div><div class=muted id=igu></div></div>
<div class=card><div class=muted>Facebook</div><div class=big id=fbf>—</div><div class=muted id=fbn></div></div></div></div>

<div id=a class=panel><div class=card><b>Funil de conteúdo (Meta)</b><div id=aout>carregando...</div></div></div>

<div id=p class=panel><div class=card>
<label>Tipo</label><select id=kind onchange=kc()><option value=image>Imagem</option><option value=carousel>Carrossel (várias imagens)</option><option value=reel>Reels / Vídeo</option></select>
<label id=ml>URL da mídia (imagem). Carrossel: separe por vírgula. Reels: URL do vídeo mp4.</label>
<textarea id=media placeholder="https://...jpg"></textarea>
<label>Legenda</label><textarea id=cap></textarea>
<label>Onde</label><select id=tgt><option value=both>Instagram + Facebook</option><option value=ig>Só IG</option><option value=fb>Só FB</option></select>
<label>Agendar para (opcional) — deixe vazio p/ publicar já</label><input id=when type=datetime-local>
<div style=margin-top:12px><button onclick=pub()>Publicar / Agendar</button></div><div id=out></div></div></div>

<div id=s class=panel><div class=card><b>Posts agendados</b><div id=sout>—</div></div></div>
</div><script>
function T(x){['d','a','p','s'].forEach(function(k){document.getElementById(k).classList.toggle('on',k==x)});
document.querySelectorAll('.tab').forEach(function(t){t.classList.remove('on')});event.target.classList.add('on');
if(x=='a')loadA();if(x=='s')loadS()}
function kc(){var k=document.getElementById('kind').value;document.getElementById('ml').textContent=k=='reel'?'URL do vídeo (mp4)':(k=='carousel'?'URLs das imagens separadas por vírgula':'URL da imagem')}
async function load(){var d=await(await fetch('/api/overview')).json();
if(d.ig&&!d.ig.error){igf.textContent=(d.ig.followers_count||0).toLocaleString('pt-BR');igu.textContent='@'+(d.ig.username||'')+' · '+(d.ig.media_count||0)+' posts'}
if(d.fb&&!d.fb.error){fbf.textContent=(d.fb.followers_count||d.fb.fan_count||0).toLocaleString('pt-BR');fbn.textContent=d.fb.name||''}}
async function loadA(){var o=document.getElementById('aout');o.textContent='carregando...';var d=await(await fetch('/api/analytics')).json();
var h='CONTA (período recente): '+JSON.stringify(d.ig_account)+'\\n\\nPOSTS:\\n';
(d.ig_media||[]).forEach(function(p){h+=(p.type||'')+' | likes '+(p.likes||0)+' com '+(p.comments||0)+' alcance '+(p.reach||'-')+' salvos '+(p.saved||'-')+' | '+(p.cap||'')+'\\n'});
if(d.notes&&d.notes.length)h+='\\nNOTAS:\\n- '+d.notes.join('\\n- ');o.textContent=h}
async function loadS(){var d=await(await fetch('/api/scheduled')).json();var o=document.getElementById('sout');
if(!d.length){o.textContent='nenhum agendado';return}o.textContent=d.map(function(i){return i.when+' | '+i.target+'/'+i.kind+' | '+i.status+' | '+(i.caption||'').slice(0,40)}).join('\\n')}
async function pub(){var media=document.getElementById('media').value.split(',').map(function(s){return s.trim()}).filter(Boolean);
var body={kind:document.getElementById('kind').value,target:document.getElementById('tgt').value,media:media,caption:document.getElementById('cap').value,when:document.getElementById('when').value};
if(!media.length){alert('Informe a URL da mídia');return}
var act=body.when?'AGENDAR para '+body.when:'PUBLICAR AGORA';
if(!confirm(act+' em '+body.target+'? É uma ação pública real.'))return;
var o=document.getElementById('out');o.textContent='processando...';
var d=await(await fetch('/api/publish',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})).json();o.textContent=JSON.stringify(d,null,2)}
load();</script></body></html>"""

class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def _s(self,c,b,ct="application/json"):
        bb=b.encode("utf-8") if isinstance(b,str) else b
        self.send_response(c);self.send_header("Content-Type",ct);self.send_header("Content-Length",str(len(bb)));self.end_headers();self.wfile.write(bb)
    def do_GET(self):
        if self.path=="/" : self._s(200,HTML,"text/html; charset=utf-8")
        elif self.path=="/api/overview": self._s(200,json.dumps(overview()))
        elif self.path=="/api/analytics": self._s(200,json.dumps(analytics()))
        elif self.path=="/api/scheduled": self._s(200,json.dumps(q_load()))
        else: self._s(404,json.dumps({"error":"not found"}))
    def do_POST(self):
        if self.path=="/api/publish":
            n=int(self.headers.get("Content-Length",0)); d=json.loads(self.rfile.read(n).decode()) if n else {}
            if d.get("when"):
                q=q_load(); ts=datetime.datetime.fromisoformat(d["when"]).timestamp()
                q.append({"when":d["when"],"when_ts":ts,"kind":d.get("kind","image"),"target":d.get("target","both"),"media":d.get("media",[]),"caption":d.get("caption",""),"status":"pending"})
                q_save(q); self._s(200,json.dumps({"agendado":True,"para":d["when"]}))
            else:
                self._s(200,json.dumps(publish(d.get("kind","image"),d.get("target","both"),d.get("media",[]),d.get("caption",""))))
        else: self._s(404,json.dumps({"error":"not found"}))

if __name__=="__main__":
    threading.Thread(target=scheduler,daemon=True).start()
    print("Social Hub v2 em http://localhost:%d"%PORT)
    HTTPServer(("127.0.0.1",PORT),H).serve_forever()
