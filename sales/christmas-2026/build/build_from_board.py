"""Rebuild sale.css, components/ and assets/ for Christmas 2026 from Sam's concept board.
The board lives outside this repo: Ecoy Web Development/releases/christmas-2026/concepts/christmas-concepts.html
Usage (from the Ecoy Web Development folder):
  python3 design-system/sales/christmas-2026/build/build_from_board.py releases/christmas-2026/concepts/christmas-concepts.html design-system/sales/christmas-2026
IDENTITY.md, BRIEF.md, assets/assets.json and reference/ are written by hand and never touched by this script.
New shoot photos must be added to PHOTOS so they load from the CDN instead of being copied.
"""
import re, sys, os, shutil, json

BOARD, OUT = sys.argv[1], sys.argv[2]
IMG = os.path.join(os.path.dirname(BOARD), 'img')
s = open(BOARD).read()
st, se = s.find('<style>'), s.find('</style>')
css = s[st + 7:se]

CDN = 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/'
PHOTOS = {  # board copy -> CDN original (matched by image 4 Nov 2026)
    'photo-burgundy-polka': 'BambooQuiltCover-Polka-BurgundyPolka-High45-Horizontal-NoTalent-Real-01',
    'photo-burgundy-qc': 'BambooQuiltCover-Solid-Burgundy-Freestyle-Horizontal-Talent-Real-01',
    'photo-jump-green': 'BambooQuiltCover-Polka-ForestGreenPolka-Freestyle-Vertical-Talent-Real-46',
    'photo-mug-burgundy': 'BambooQuiltCover-Polka-BurgundyPolka-Freestyle-Vertical-Talent-Real-58',
    'photo-mug-pine': 'BambooQuiltCover-Solid-MidnightPine-Freestyle-Talent-Real-17',
    'photo-sleep-green': 'BambooSheetSet-Solid-ForestGreen-Overhead-Talent-Real-01',
    'photo-tote': 'ToteBag-AllColours-Freestyle-Vertical-NoTalent-Real-01',
    'tote-allcolours-talent': 'ToteBag-AllColours-Freestyle-Vertical-Talent-Real-01',
    'tote-matcha-high45': 'ToteBag-MatchaForest-High45-Vertical-NoTalent-Real-01',
    'tote-matcha-overhead': 'ToteBag-MatchaForest-Overhead-Horizontal-NoTalent-Real-01',
    'tote-matcha-stool': 'ToteBag-MatchaForest-Freestyle-Vertical-NoTalent-Real-01',
    'tote-oatmeal-closeup': 'ToteBag-OatmealCharcoal-CloseUp-Vertical-Talent-Real-01',
    'tote-oatmeal-high45': 'ToteBag-OatmealCharcoal-High45-Vertical-NoTalent-Real-01',
    'tote-oatmeal-talent': 'ToteBag-OatmealCharcoal-Freestyle-Vertical-Talent-Real-03',
    'tote-pink-talent': 'ToteBag-EggplantPink-Freestyle-Vertical-Talent-Real-01',
    'tote-pink-high45': 'ToteBag-EggplantPink-High45-Vertical-NoTalent-Real-01',
    'pack-bloomingpink-stripe': 'BambooSheetSet-Stripe-BloomingPinkStripe-Packshot-NoTalent-AI-01',
    'pack-icedchoc-polka': 'BambooSheetSet-Polka-IcedChocolatePolka-Packshot-NoTalent-AI-01',
    'pack-maltcaramel-stripe': 'BambooQuiltCover-Stripe-MaltCaramelStripe-Packshot-NoTalent-Real-01',
}

# ---------- CSS: split board chrome from sale components ----------
CHROME = re.compile(r'^(\*|body|html|:root.*|\.wrap|h1|h2|h3|p|\.eyebrow|\.note|section|\.shead|\.intro|\.facts|\.fact|\.rules|\.sw|\.lockups|\.lk|\.nw|\.grid|\.g3|\.g2|\.gkit|\.gfin|\.cell|\.lab|\.cap|\.toggle|\.gcmp|\.trio|\.cmpnotes|\.adiv|\.phase-div|\.next|\.mob-row|\.gem|\.inbox)([\s.:>,\[]|$)')

def split_rules(text):
    """Yield (prelude, body) for top-level rules; nested @media bodies are returned raw."""
    i, n = 0, len(text)
    while i < n:
        j = text.find('{', i)
        if j < 0: break
        prelude = text[i:j].strip()
        depth, k = 1, j + 1
        while depth and k < n:
            if text[k] == '{': depth += 1
            elif text[k] == '}': depth -= 1
            k += 1
        yield prelude, text[j + 1:k - 1]
        i = k

def strip_comments(p):
    return re.sub(r'/\*.*?\*/', '', p, flags=re.S).strip()

def scope_sel(sel):
    sel = sel.strip()
    return '.xm26 ' + sel

def build(text, chrome_out, sale_out, media=None):
    for prelude, body in split_rules(text):
        p = strip_comments(prelude)
        if not p or p.startswith('@font-face'): continue
        if p.startswith('@media') or p.startswith('@supports'):
            c, sa = [], []
            build(body, c, sa)
            if c: chrome_out.append(p + '{' + ''.join(c) + '}')
            if sa: sale_out.append(p + '{' + ''.join(sa) + '}')
            continue
        if p.startswith('@keyframes'):
            sale_out.append(p + '{' + body + '}'); continue
        sels = [x.strip() for x in p.split(',')]
        ch = [x for x in sels if CHROME.match(x)]
        sa = [x for x in sels if not CHROME.match(x)]
        if ch: chrome_out.append(','.join(ch) + '{' + body.strip() + '}')
        if sa: sale_out.append(','.join(scope_sel(x) for x in sa) + '{' + body.strip() + '}')

chrome, sale = [], []
build(css, chrome, sale)

head = '''/* Christmas 2026 sale identity ("One for them, one for you"). Scoped to .xm26 so none of it leaks
   into evergreen. Read IDENTITY.md first. Put .xm26 on an ancestor (the page body or a wrapper);
   every frame is .f.feed (4:5) or .f.story (9:16), emails are .em, site banners .wp / .wfs / .wpm.
   Sizes are container units (cqw) of the frame, so one class works at any size.
   Built 2026-11-04 from the concept board (releases/christmas-2026/concepts, artifact v84). */

@import url('../../css/tokens.css');

@font-face { font-family: 'Malinton'; font-weight: 500; font-style: normal; font-display: swap; src: url('../../fonts/Malinton-Medium.otf') format('opentype'); }
@font-face { font-family: 'Malinton'; font-weight: 600; font-style: normal; font-display: swap; src: url('../../fonts/Malinton-SemiBold.otf') format('opentype'); }
@font-face { font-family: 'Malinton'; font-weight: 700; font-style: normal; font-display: swap; src: url('../../fonts/Malinton-Bold.otf') format('opentype'); }
@font-face { font-family: 'Satoshi'; font-weight: 400; font-style: normal; font-display: swap; src: url('../../fonts/Satoshi-Regular.otf') format('opentype'); }
@font-face { font-family: 'Satoshi'; font-weight: 500; font-style: normal; font-display: swap; src: url('../../fonts/Satoshi-Medium.otf') format('opentype'); }
@font-face { font-family: 'Satoshi'; font-weight: 700; font-style: normal; font-display: swap; src: url('../../fonts/Satoshi-Bold.otf') format('opentype'); }

.xm26 {
  /* Brand tokens only: the sale adds no new colours. */
  --deep-green: var(--color-deep-green);
  --burgundy: var(--color-burgundy);
  --off-white: var(--color-off-white);
  --light-green: var(--color-light-green);
  --light-pink: var(--color-light-pink);
  --bright-orange: var(--color-bright-orange);
  --charcoal: var(--color-charcoal);
  --font-display: var(--font-display-stack, 'Malinton', 'Fredoka', 'Nunito', system-ui, sans-serif);
  --font-text: 'Satoshi', 'Inter', system-ui, -apple-system, sans-serif;
  --rule: rgba(28,28,28,.14);
}

/* Paper tiles (assets/). Use as background-image on .paper / .paperf / .pp / .wp / .pbar / .ebar. */
.xm26 .paper--launch, .xm26 .wp--launch { background-image: url('assets/wrap-offwhite.svg'); }
.xm26 .paper--lc, .xm26 .wp--lc { background-image: url('assets/wrap-burgundy.svg'); }
.xm26 .bar--dark { background-image: url('assets/wrap-dark.svg'); }
.xm26 .bar--pink { background-image: url('assets/wrap-pink.svg'); }

'''
os.makedirs(os.path.join(OUT, 'components'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
open(os.path.join(OUT, 'sale.css'), 'w').write(head + '\n'.join(sale) + '\n')
open(os.path.join(OUT, 'components', 'board.css'), 'w').write(
    '/* Demo-page chrome for the Christmas 2026 component pages only. Never load this in production. */\n'
    ':root{--bg:#F6F2E8;--fg:#1C1C1C;--muted:#5d5a52;--rule:#ddd6c6;--chip:#ebe5d6;'
    '--font-display:"Malinton","Fredoka","Nunito",system-ui,sans-serif;--font-text:"Satoshi","Inter",system-ui,sans-serif}\n'
    + '\n'.join(chrome) + '\n')

# ---------- assets ----------
used = sorted(set(re.findall(r'img/([A-Za-z0-9_.\-]+\.(?:webp|svg|png|jpg))', s)))
copied = []
for u in used:
    stem = u.rsplit('.', 1)[0]
    if stem in PHOTOS: continue
    shutil.copy(os.path.join(IMG, u), os.path.join(OUT, 'assets', u)); copied.append(u)

def rewrite(html):
    def img(m):
        f = m.group(1); stem = f.rsplit('.', 1)[0]
        if stem in PHOTOS: return CDN + PHOTOS[stem] + '.webp?width=1200'
        return '../assets/' + f
    return re.sub(r'img/([A-Za-z0-9_.\-]+\.(?:webp|svg|png|jpg))', img, html)

symbols = re.findall(r'<symbol\b.*?</symbol>', s, flags=re.S)
sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + '\n'.join(symbols) + '</defs></svg>'
open(os.path.join(OUT, 'assets', 'symbols.svg'), 'w').write(
    sprite.replace('<svg width="0" height="0" style="position:absolute" aria-hidden="true">',
                   '<svg xmlns="http://www.w3.org/2000/svg">'))

# ---------- component pages ----------
main_start = s.find('<main class="wrap" id="board">')
main_end = s.find('</main>', main_start)
main = s[main_start + len('<main class="wrap" id="board">'):main_end]
script = s[s.find('<script>', main_end):s.find('</script>', main_end) + 9]

def section_slice(start_marker, end_marker):
    a = main.find(start_marker); b = main.find(end_marker, a + 1) if end_marker else len(main)
    assert a >= 0, start_marker
    return main[a:b]

header = main[:main.find('<div class="adiv phase-div" id="phase-1">')]
p1 = section_slice('<div class="adiv phase-div" id="phase-1">', '<div class="adiv phase-div" id="phase-2">')
p2 = section_slice('<div class="adiv phase-div" id="phase-2">', '<div class="adiv phase-div" id="phase-3">')
p3 = section_slice('<div class="adiv phase-div" id="phase-3">', '<section class="next"')
nxt = section_slice('<section class="next"', None)

def page(card, title, intro, body, with_script=False):
    return f'''<!-- @dsCard group="Sale · Christmas 2026" name="{card}" -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="../sale.css">
<link rel="stylesheet" href="board.css">
</head>
<body class="xm26">
{sprite}
<main class="wrap" id="board">
<div class="shead" style="padding-top:32px"><span class="eyebrow">Sale · Christmas 2026</span><h1>{title}</h1><p>{intro}</p></div>
{rewrite(body)}
</main>
{script if with_script else ''}
</body>
</html>
'''

open(os.path.join(OUT, 'components', 'callouts.html'), 'w').write(page(
    'Christmas 2026 rules and callouts', 'Christmas 2026 · global rules and callouts',
    'Everything that applies to both phases: the five formats, the accent rule, how the set is tied, the paper scale, callouts and the promotion lockup. Rules are in <code>IDENTITY.md</code>.',
    p1 + nxt, with_script=False).replace('<div class="grid gcmp" id="cmp-grid"></div>',
    '<p class="note">The five format heroes are shown at the top of <a href="templates.html">templates.html</a>.</p>'))
open(os.path.join(OUT, 'components', 'templates.html'), 'w').write(page(
    'Christmas 2026 templates', 'Christmas 2026 · templates',
    'Every format in both phases with live text: statics (4:5 and 9:16), emails (600 and 375 wide), site heroes, banners and announcement bars (desktop and 390 mobile). Photos load from the Shopify CDN; the ribbon renders and paper tiles are in <code>../assets/</code>. Switch on the story safe zones with the toggle.',
    p1 + p2 + p3, with_script=True))

print('sale rules', len(sale), 'chrome rules', len(chrome), 'assets', len(copied))
