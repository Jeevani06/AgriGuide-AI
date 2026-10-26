"""Generates illustrated crop artwork into static/images/crops/*.svg (run: python tools/make_art.py)."""
import math, random, os
random.seed(7)
OUT = os.path.join(os.path.dirname(__file__), "..", "static", "images", "crops")
def svg(body, defs="", w=400, h=300):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><defs>{defs}</defs>{body}</svg>'
def grad(i, a, b, v=True):
    return f'<linearGradient id="{i}" x1="0" y1="0" x2="{0 if v else 1}" y2="{1 if v else 0}"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
def leaf(x, y, l, ang, c="#3f8f3a", wd=.22):
    return f'<g transform="translate({x} {y}) rotate({ang})"><path d="M0 0 Q{l*.5} {-l*wd} {l} 0 Q{l*.5} {l*wd} 0 0Z" fill="{c}"/><path d="M0 0 L{l*.9} 0" stroke="#ffffff55" stroke-width="1.5"/></g>'

def rice():
    b = '<rect width="400" height="300" fill="url(#bg)"/><circle cx="320" cy="70" r="38" fill="#fff6c9" opacity=".9"/>'
    b += '<rect y="228" width="400" height="72" fill="url(#w)"/>'
    for i in range(6): b += f'<path d="M{20+i*70} {245+i%2*14} q20 -6 40 0" stroke="#ffffff88" fill="none" stroke-width="2"/>'
    for sx, top, lean in [(70,95,-40),(140,70,30),(210,60,-20),(280,85,40),(340,110,-30),(30,130,25)]:
        b += f'<path d="M{sx} 262 C{sx} 190 {sx+lean*.3} 130 {sx+lean} {top}" stroke="#6aa84f" stroke-width="5" fill="none" stroke-linecap="round"/>'
        for k in range(14):
            t = k/13; px = sx+lean+ (t*40 if lean>0 else -t*40)*.8; py = top + t*t*60 - 6 + k*1.2
            b += f'<ellipse cx="{px:.0f}" cy="{py:.0f}" rx="4.5" ry="8" fill="{"#e3b630" if k%2 else "#f0c94a"}" transform="rotate({-30 if lean>0 else 30} {px:.0f} {py:.0f})"/>'
        b += leaf(sx, 250, 90, -100 + lean*.5, "#4f9d3b", .12)
    return svg(b, grad("bg","#fdf1b8","#d6ecae")+grad("w","#9ad1a0","#4f9d7a"))

def maize():
    b = '<rect width="400" height="300" fill="url(#bg)"/><circle cx="70" cy="60" r="30" fill="#fff" opacity=".8"/><ellipse cx="110" cy="70" rx="40" ry="14" fill="#fff" opacity=".8"/>'
    b += '<rect y="235" width="400" height="65" fill="#7cae4a"/>'
    b += '<path d="M200 300 L200 60" stroke="#5c9a3a" stroke-width="12" stroke-linecap="round"/>'
    for y, a, s in [(250,-35,1),(215,-145,1),(175,-30,1.1),(140,-150,1.05),(105,-40,.9)]:
        b += leaf(200, y, 150*s, a, "#4f9d3b", .13)
    b += '<g transform="translate(205 150) rotate(18)"><ellipse rx="26" ry="62" fill="#f5c93a"/>'
    for r in range(9):
        for c in range(4): b += f'<circle cx="{-15+c*10}" cy="{-52+r*12}" r="3.6" fill="#e2a91c"/>'
    b += '<path d="M-26 20 Q0 90 26 20 Q0 40 -26 20Z" fill="#6aae44"/><path d="M-24 40 Q0 100 24 40Z" fill="#5a9c3a"/></g>'
    return svg(b, grad("bg","#a9dcf3","#e9f6dc"))

def cotton():
    b = '<rect width="400" height="300" fill="url(#bg)"/><rect y="250" width="400" height="50" fill="#a47c4e"/>'
    for sx, top in [(90,90),(200,60),(310,100)]:
        b += f'<path d="M{sx} 270 L{sx} {top}" stroke="#6b4e2e" stroke-width="7" stroke-linecap="round"/>'
        for k in range(4): b += leaf(sx, 245-k*40, 70, -30 if k%2 else -150, "#3f8f3a", .3)
        for dx, dy in [(-34,10),(34,25),(-30,70),(32,88)]:
            cx, cy = sx+dx, top+dy
            b += f'<path d="M{sx} {top+dy+8} L{cx} {cy}" stroke="#6b4e2e" stroke-width="3"/>'
            b += f'<path d="M{cx-14} {cy+10} L{cx} {cy+22} L{cx+14} {cy+10} L{cx+10} {cy+30} L{cx-10} {cy+30}Z" fill="#7a5a33"/>'
            for ox, oy, r in [(-11,-4,14),(11,-4,14),(0,-12,15),(0,3,14)]: b += f'<circle cx="{cx+ox}" cy="{cy+oy}" r="{r}" fill="#fff"/>'
            b += f'<circle cx="{cx-4}" cy="{cy-8}" r="5" fill="#eef2f6"/>'
    return svg(b, grad("bg","#dcefd3","#bfe0b0"))

def chickpea():
    b = '<rect width="400" height="300" fill="url(#bg)"/><rect y="240" width="400" height="60" fill="#b98f5b"/>'
    for sx, top in [(110,80),(210,50),(300,95)]:
        b += f'<path d="M{sx} 262 Q{sx+10} 160 {sx-10} {top}" stroke="#5c8f3a" stroke-width="5" fill="none"/>'
        for k in range(9):
            y = 245-k*20; x = sx+ (5-k*1.2); 
            for s in (-1,1): b += f'<ellipse cx="{x+s*17:.0f}" cy="{y-3}" rx="12" ry="6.5" fill="#6fae48" transform="rotate({s*-25} {x+s*17:.0f} {y-3})"/>'
        for dx, dy in [(-28,40),(26,70),(-24,110)]:
            px, py = sx+dx, top+dy
            b += f'<path d="M{sx} {py-6} L{px} {py-12}" stroke="#5c8f3a" stroke-width="2"/><ellipse cx="{px}" cy="{py}" rx="11" ry="16" fill="#cfd98a"/><ellipse cx="{px-3}" cy="{py-4}" rx="3" ry="6" fill="#ffffff66"/>'
    for i in range(7): b += f'<circle cx="{40+i*55}" cy="{268+i%2*12}" r="9" fill="#e0b873"/><circle cx="{37+i*55}" cy="{265+i%2*12}" r="3" fill="#f3d9a0"/>'
    return svg(b, grad("bg","#f6efd4","#e2eec0"))

def banana():
    b = '<rect width="400" height="300" fill="url(#bg)"/><rect y="250" width="400" height="50" fill="#6aa84f"/>'
    b += '<path d="M185 300 Q175 190 200 100" stroke="#8a6a3c" stroke-width="22" stroke-linecap="round" fill="none"/>'
    for a, l in [(-165,170),(-125,150),(-60,150),(-15,170),(-95,120)]:
        b += leaf(200, 100, l, a, "#2f8a3a", .17)
    for i in range(5):
        for j in range(4):
            x = 205+i*14+ j*2; y = 120+j*16 + i*3
            b += f'<path d="M{x} {y} q28 -4 36 38 q-14 8 -22 -6 q-6 -18 -14 -32Z" fill="{"#f6d33a" if (i+j)%2 else "#f0c421"}" stroke="#c9a017" stroke-width="1.2"/>'
    b += '<ellipse cx="240" cy="188" rx="9" ry="12" fill="#7a2f5a"/>'
    return svg(b, grad("bg","#b7e3f7","#f4f9dc"))

def mango():
    b = '<rect width="400" height="300" fill="url(#bg)"/><circle cx="330" cy="60" r="34" fill="#ffe08a" opacity=".85"/>'
    b += '<path d="M-10 90 Q150 70 410 120" stroke="#6b4a2b" stroke-width="12" fill="none" stroke-linecap="round"/>'
    for x, y, a in [(40,95,-60),(90,88,60),(150,86,-70),(215,92,55),(270,100,-60),(330,112,60),(120,92,-120),(250,98,-125)]:
        b += leaf(x, y, 85, a+ (0 if a<0 else 0), "#2f7d3a", .2)
    for cx, cy, r, s in [(95,185,-15,1.1),(190,200,10,1.25),(285,180,-5,1.0)]:
        b += f'<path d="M{cx} {cy-62*s} L{cx+3} {cy-90*s+26}" stroke="#5a4326" stroke-width="3"/><path d="M{cx} {cy-88} L{cx+2} {cy-62*s}" stroke="#5a4326" stroke-width="3"/>'
        b += f'<g transform="translate({cx} {cy}) rotate({r}) scale({s})"><path d="M0 -58 C42 -58 52 -2 28 38 C12 62 -26 58 -40 28 C-56 -8 -36 -58 0 -58Z" fill="url(#m)"/><ellipse cx="-14" cy="-24" rx="8" ry="18" fill="#ffffff55" transform="rotate(20)"/></g>'
    return svg(b, grad("bg","#ffe9c2","#d9efc2")+'<radialGradient id="m" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#ffd23f"/><stop offset=".6" stop-color="#f58a1f"/><stop offset="1" stop-color="#d8412b"/></radialGradient>')

def hero():
    b = '<rect width="1200" height="380" fill="url(#bg)"/><circle cx="930" cy="110" r="64" fill="#ffe27a"/><circle cx="930" cy="110" r="90" fill="#ffe27a" opacity=".25"/>'
    b += '<path d="M0 230 Q200 170 420 215 T860 200 T1200 215 V380 H0Z" fill="#8cc06a"/><path d="M0 270 Q300 220 620 260 T1200 255 V380 H0Z" fill="#5fa24d"/>'
    for i in range(14):
        x1 = 600 + i*30; b += f'<path d="M{x1} 380 L{500+i*14} 262" stroke="#3f8a3c" stroke-width="3" opacity=".6"/>'
    for i in range(16): b += f'<path d="M{i*80} 380 L{300+i*40} 270" stroke="#4a9142" stroke-width="3" opacity=".35"/>'
    return svg(b, grad("bg","#fff4c6","#bfe5c7"), 1200, 380)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in dict(rice=rice, maize=maize, cotton=cotton, chickpea=chickpea, banana=banana, mango=mango).items():
        open(os.path.join(OUT, n + ".svg"), "w").write(f())
    open(os.path.join(OUT, "..", "hero.svg"), "w").write(hero())
    print("ok")
