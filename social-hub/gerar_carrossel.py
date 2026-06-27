# -*- coding: utf-8 -*-
# Gera os 8 slides do carrossel "5 sinais de Home Care" (1080x1080) para @hospitalarsaude.
# Saida default: ../carrossel-5sinais (ajuste OUT). Requer Pillow (pip install Pillow) e fontes Arial (Windows).
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
M = 90
OUT = os.environ.get("CARROSSEL_OUT", r"C:\Users\rudpa\social-hub\carrossel-5sinais")
os.makedirs(OUT, exist_ok=True)
FB = r"C:\Windows\Fonts\arialbd.ttf"
FR = r"C:\Windows\Fonts\arial.ttf"

TEAL = (15, 110, 86); TEAL2 = (29, 158, 117); LIGHT = (244, 247, 246)
DARK = (26, 32, 30); WHITE = (255, 255, 255); SOFT = (200, 230, 220); MUT = (120, 140, 132)

def f(sz, bold=True): return ImageFont.truetype(FB if bold else FR, sz)
def wrap(d, t, font, maxw):
    words = t.split(); lines = []; cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=font) <= maxw: cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines
def draw_lines(d, x, y, lines, font, fill, lh):
    for ln in lines: d.text((x, y), ln, font=font, fill=fill); y += lh
    return y
def base(bg): img = Image.new("RGB", (W, H), bg); return img, ImageDraw.Draw(img)
def brand(d, color): d.text((M, 70), "HospitaLar", font=f(40), fill=color); d.text((M, 120), "Cuidado pela vida", font=f(26, False), fill=color)
def save(img, name): img.save(os.path.join(OUT, name), "PNG"); print("ok", name)

img, d = base(TEAL); brand(d, SOFT)
draw_lines(d, M, 360, wrap(d, "5 sinais de que seu pai ou sua mãe já precisa de Home Care", f(78), W - 2 * M), f(78), WHITE, 96)
d.text((M, H - 140), "Arraste para o lado  >", font=f(34, False), fill=SOFT); save(img, "01_capa.png")

sinais = [
    ("1", "Quedas frequentes ou medo de cair"),
    ("2", "Esquece os remédios ou troca as doses"),
    ("3", "Dificuldade no banho e ao se vestir"),
    ("4", "Alta hospitalar com cuidados contínuos"),
    ("5", "A família já está exausta de dar conta"),
]
for i, (num, txt) in enumerate(sinais, start=1):
    img, d = base(LIGHT); brand(d, TEAL)
    d.text((M, 210), num, font=f(300), fill=TEAL2)
    draw_lines(d, M, 720, wrap(d, txt, f(62), W - 2 * M), f(62), DARK, 78)
    d.text((M, H - 130), "sinal %d de 5" % i, font=f(30, False), fill=MUT)
    save(img, "%02d_sinal%d.png" % (i + 1, i))

img, d = base(TEAL); brand(d, SOFT)
draw_lines(d, M, 320, wrap(d, "A HospitaLar cuida na sua casa.", f(72), W - 2 * M), f(72), WHITE, 88)
draw_lines(d, M, 560, wrap(d, "Equipe multidisciplinar: enfermagem, fisioterapia e fonoaudiologia. 24 horas por dia.", f(40, False), W - 2 * M), f(40, False), SOFT, 52)
d.rounded_rectangle([M, 850, M + 560, 940], radius=45, fill=TEAL2)
d.text((M + 40, 872), "Certificada ONA + GPTW", font=f(38), fill=WHITE); save(img, "07_solucao.png")

img, d = base(TEAL); brand(d, SOFT)
draw_lines(d, M, 320, wrap(d, "Cuidar de quem você ama começa com uma mensagem.", f(60), W - 2 * M), f(60), WHITE, 76)
d.text((M, 600), "WhatsApp", font=f(46, False), fill=SOFT)
d.text((M, 660), "(35) 98876-4610", font=f(86), fill=WHITE)
draw_lines(d, M, 800, wrap(d, "Plantão 24h  ·  Atendimento Sul de Minas", f(38, False), W - 2 * M), f(38, False), SOFT, 50)
save(img, "08_cta.png")
print("TOTAL:", len(os.listdir(OUT)), "arquivos em", OUT)
