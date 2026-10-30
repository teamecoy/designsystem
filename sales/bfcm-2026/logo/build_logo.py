#!/usr/bin/env python3
"""Build the BFCM 2026 sale logo files from the sale font, so the lockup exists as an asset, not just as live type.

Outputs (in this folder):
  bfcm-2026-black-friday-<colour>.svg / .png   the event name alone
  bfcm-2026-cyber-monday-<colour>.svg / .png   the final-day event name
  bfcm-2026-lockup-black-friday-<colour>.svg / .png   Ecoy wordmark above the event name (IDENTITY.md §4)
  bfcm-2026-lockup-cyber-monday-<colour>.svg / .png

Colours are the phase colours from IDENTITY.md §3.1: white (hype), green (live), orange (end on black fabric), ink (end on an
orange ground). Glyphs are converted to outlines, so nothing needs the font installed. PNGs are 2400px wide on a transparent
ground, rendered with headless Chrome. Needs fontTools and Pillow.

  python3 build_logo.py
"""
import os, re, subprocess, tempfile, shutil
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, '..', 'fonts', 'LedDisplaySt.ttf')
WORDMARK = os.path.join(HERE, '..', '..', '..', 'logos', 'logo-white.svg')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
COLOURS = {  # name: (fill, glow)
    'white': ('#FFFFFF', True), 'green': ('#77D686', True), 'orange': ('#FF6301', True), 'ink': ('#0A0A0B', False),
}
WORDS = {'black-friday': 'BLACK FRIDAY', 'cyber-monday': 'CYBER MONDAY'}
PNG_WIDTH = 2400

font = TTFont(FONT); gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font['head'].unitsPerEm

def text_outline(text):
    """Return (path d, width, ymin, ymax) for the text in font units, y up."""
    parts, x, ymin, ymax = [], 0, 1e9, -1e9
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs, ntos=lambda v: str(int(round(v)))); gs[g].draw(pen)
        d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({x} 0)" d="{d}"/>')
            bp = BoundsPen(gs); gs[g].draw(bp)
            ymin = min(ymin, bp.bounds[1]); ymax = max(ymax, bp.bounds[3])
        x += gs[g].width
    return ''.join(parts), x, ymin, ymax

def wordmark_paths():
    s = open(WORDMARK).read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1).split()
    paths = re.findall(r'<path[^>]*/>', s)
    paths = [re.sub(r'\sfill="[^"]*"', '', p) for p in paths]
    return ''.join(paths), float(vb[2]), float(vb[3])

WM, WM_W, WM_H = wordmark_paths()

def svg(word, colour, lockup):
    fill, glow = COLOURS[colour]
    d, w, ymin, ymax = text_outline(WORDS[word])
    cap = ymax - ymin
    pad = cap * 0.25                     # room for the glow
    scale = 1.0
    # headline occupies [0, w] × [ymin, ymax] in font units; flip y for SVG
    elems = [f'<g transform="translate(0 {ymax}) scale(1 -1)" fill="{fill}">{d}</g>']
    top = 0
    if lockup:
        wm_w = w * 0.135                 # wordmark ≈ 13.5% of the headline width (IDENTITY §4)
        wm_s = wm_w / WM_W; wm_h = WM_H * wm_s
        gap = cap * 0.22
        top = -(wm_h + gap)
        elems.insert(0, f'<g transform="translate({(w - wm_w) / 2} {top}) scale({wm_s})" fill="{fill}">{WM}</g>')
    x0, y0, x1, y1 = -pad, top - pad, w + pad, cap + pad
    filt = ''
    if glow:
        sd1, sd2 = cap * 0.012, cap * 0.05
        filt = (f'<filter id="glow" x="-10%" y="-20%" width="120%" height="140%">'
                f'<feGaussianBlur in="SourceGraphic" stdDeviation="{sd2:.1f}" result="b2"/>'
                f'<feComponentTransfer in="b2" result="b2a"><feFuncA type="linear" slope="0.55"/></feComponentTransfer>'
                f'<feGaussianBlur in="SourceGraphic" stdDeviation="{sd1:.1f}" result="b1"/>'
                f'<feMerge><feMergeNode in="b2a"/><feMergeNode in="b1"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    body = ''.join(elems)
    if glow: body = f'<g filter="url(#glow)">{body}</g>'
    name = f"bfcm-2026-{'lockup-' if lockup else ''}{word}-{colour}"
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" '
           f'width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" role="img" aria-label="Ecoy {WORDS[word].title()}">'
           f'<title>{"Ecoy " if lockup else ""}{WORDS[word].title()} · BFCM 2026 · {colour}</title><defs>{filt}</defs>{body}</svg>')
    return name, out, (x1 - x0, y1 - y0)

def render_png(svg_path, png_path, w, h):
    html = tempfile.mktemp(suffix='.html', dir=HERE)
    pw = PNG_WIDTH; ph = int(round(PNG_WIDTH * h / w))
    open(html, 'w').write(f'<!doctype html><html><body style="margin:0;background:transparent"><img src="file://{svg_path}" style="display:block;width:{pw}px;height:{ph}px"></body></html>')
    subprocess.run([CHROME, '--headless=new', '--allow-file-access-from-files', '--hide-scrollbars', '--default-background-color=00000000',
                    f'--window-size={pw},{ph}', f'--screenshot={png_path}', f'file://{html}'], check=True, capture_output=True)
    os.remove(html)

made = []
for word in WORDS:
    for colour in COLOURS:
        for lockup in (False, True):
            if word == 'cyber-monday' and colour == 'green':
                continue                 # Cyber Monday is the End phase only
            name, s, (w, h) = svg(word, colour, lockup)
            p = os.path.join(HERE, name + '.svg'); open(p, 'w').write(s)
            render_png(p, os.path.join(HERE, name + '.png'), w, h)
            made.append(name)
print('\n'.join(made))
