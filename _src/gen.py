# -*- coding: utf-8 -*-
"""Renders the Pausely App Store pages into the repo root.

    python3 _src/gen.py

One file, no dependencies. Every visual value below is taken from the app's own
design tokens (Core/DesignSystem/Theme.swift in the Pausely repo) so the pages
read as the same product: the same page/card/fill greys, the same calm teal, the
same dark hero island, the same radii.
"""
import os, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)

BASE = "/pausely-links"
SITE = "https://sohaibiii.github.io" + BASE
APP = "Pausely"
COMPANY = "TOPSOL"
EMAIL = "topsol.org@gmail.com"
UPDATED = "24 August 2026"
YEAR = "2026"

# Set this to the App Store page once App Store Connect has assigned the Apple ID,
# e.g. "https://apps.apple.com/app/id1234567890". Until then every "App Store"
# button renders as a quiet "coming soon" label rather than a dead link.
APP_STORE_URL = None

NAV = [
    ("support", "Support", f"{BASE}/"),
    ("about", "About", f"{BASE}/about/"),
    ("privacy", "Privacy", f"{BASE}/privacy/"),
    ("terms", "Terms", f"{BASE}/terms/"),
    ("data", "Your data", f"{BASE}/delete-data/"),
]

E = lambda s: html.escape(s, quote=True)
CUR = ' aria-current="page"'

# ---------------------------------------------------------------------------
# Chrome
# ---------------------------------------------------------------------------

CSS = r"""
:root{
  --bg:#F4F6F9;--surface:#FFFFFF;--fill:#EAEEF3;--ink:#0E1116;--ink-2:#5B6573;--ink-3:#5F6875;
  --line:rgba(0,0,0,.06);--accent:#0B7065;--accent-strong:#127A6F;--accent-soft:rgba(11,112,101,.12);--on-accent:#FFFFFF;
  --glow:transparent;--card-shadow:0 10px 30px rgba(24,33,52,.08);--card-edge:transparent;
  --streak:#A3640F;--streak-soft:rgba(163,100,15,.14);--success:#23744A;--success-soft:rgba(35,116,74,.14);
  --hero-top:#18313A;--hero-bottom:#0E1820;--hero-glow:rgba(94,212,198,.40);--hero-ink:#F2F4F7;--hero-ink-2:rgba(242,244,247,.72);--hero-stroke:rgba(255,255,255,.10);--hero-fill:rgba(255,255,255,.08);
  --orb-core:#D1FAF2;--orb-edge:#5ED4C6;--orb-glow:rgba(94,212,198,.75);
  --r-card:20px;--r-hero:28px;--r-control:14px;--r-chip:12px;--r-tile:10px;
  --max:760px;--wide:1080px;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#0E1116;--surface:#171B22;--fill:#1E242D;--ink:#F2F4F7;--ink-2:#9AA3AF;--ink-3:#7C8594;
  --line:rgba(255,255,255,.08);--accent:#5ED4C6;--accent-strong:#6EDED0;--accent-soft:rgba(94,212,198,.16);--on-accent:#0E1116;
  --glow:rgba(94,212,198,.35);--card-shadow:none;--card-edge:rgba(255,255,255,.06);
  --streak:#F3B562;--streak-soft:rgba(243,181,98,.18);--success:#7FC98F;--success-soft:rgba(127,201,143,.18);
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Inter","Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:3px;overflow-wrap:anywhere}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
.skip{position:absolute;top:8px;left:8px;background:var(--surface);color:var(--ink);padding:8px 12px;z-index:20;border-radius:var(--r-chip);box-shadow:var(--card-shadow)}
.skip:not(:focus){clip:rect(0 0 0 0);clip-path:inset(50%);width:1px;height:1px;overflow:hidden;white-space:nowrap;padding:0;margin:-1px}
h1,h2,h3{margin:0;letter-spacing:-.02em;text-wrap:balance;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Inter","Segoe UI",Roboto,sans-serif}
h1{font-weight:700;font-size:clamp(32px,4.6vw,48px);line-height:1.08}
h2{font-weight:700;font-size:24px;line-height:1.25}
h3{font-weight:600;font-size:18px;line-height:1.3}
p{margin:0 0 1em}
p:last-child{margin-bottom:0}
ul,ol{margin:0;padding-left:1.3em}
li{margin:.45em 0}
li::marker{color:var(--accent)}
strong{font-weight:600}
.muted{color:var(--ink-2)}
small,.small{font-size:14px;color:var(--ink-2)}
code{font:.92em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:var(--fill);padding:.1em .4em;border-radius:6px}
kbd{font:inherit;background:var(--fill);border-radius:8px;padding:.05em .5em;white-space:nowrap}

/* top bar — the one glass surface, like the app's navigation layer */
.topbar{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 82%,transparent);-webkit-backdrop-filter:saturate(1.4) blur(14px);backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--line)}
.topbar .in{max-width:var(--wide);margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.brand{display:inline-flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-weight:700;font-size:19px;letter-spacing:-.01em}
.orb{width:22px;height:22px;border-radius:50%;flex:none;background:radial-gradient(circle at 38% 32%,var(--orb-core) 0,var(--orb-edge) 62%,color-mix(in srgb,var(--orb-edge) 70%,#0E1116) 100%);box-shadow:0 0 0 1px var(--hero-stroke),0 0 14px var(--orb-glow)}
nav.pages{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
nav.pages a{text-decoration:none;color:var(--ink-2);font-size:15px;font-weight:500;padding:7px 12px;border-radius:999px}
nav.pages a[aria-current="page"]{color:var(--accent);background:var(--accent-soft)}
nav.pages a:hover{color:var(--ink)}
@media (max-width:640px){nav.pages{margin-left:0;width:100%;overflow-x:auto;flex-wrap:nowrap;scrollbar-width:none;padding-bottom:2px}nav.pages::-webkit-scrollbar{display:none}nav.pages a{flex:none}}

/* hero — the home screen's dark island, dark in both appearances */
.hero-wrap{max-width:var(--wide);margin:24px auto 0;padding:0 20px}
.hero{position:relative;overflow:hidden;border-radius:var(--r-hero);background:linear-gradient(180deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke),0 24px 60px rgba(14,17,22,.18);padding:clamp(36px,6vw,64px) clamp(24px,5vw,56px)}
.hero::before{content:"";position:absolute;inset:-40% auto auto -20%;width:70%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--hero-glow) 0,transparent 62%);pointer-events:none}
.hero>*{position:relative}
.hero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--hero-ink-2);margin-bottom:18px}
.hero .eyebrow .dot{width:8px;height:8px;border-radius:50%;background:var(--orb-edge);box-shadow:0 0 10px var(--orb-glow)}
.hero h1{max-width:18ch}
.hero .sub{margin:16px 0 0;max-width:56ch;font-size:clamp(17px,2vw,20px);color:var(--hero-ink-2)}
.hero .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px;align-items:center}
.hero .ctas a,.hero .ctas span{color:var(--hero-ink)}
.hero .ctas .btn.primary{background:#5ED4C6;color:#0E1116;box-shadow:0 8px 24px rgba(94,212,198,.30)}
.hero .ctas .btn.quiet{background:var(--hero-fill);color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke)}
.hero .meta{margin-top:22px;font-size:14px;color:var(--hero-ink-2)}
.hero .meta a{color:var(--hero-ink);text-decoration-color:rgba(255,255,255,.4)}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:16px;line-height:1;padding:14px 20px;border-radius:var(--r-control);text-decoration:none;white-space:nowrap}
.btn.primary{background:var(--accent);color:var(--on-accent);box-shadow:0 8px 24px var(--glow)}
.btn.quiet{background:var(--fill);color:var(--ink)}
.btn svg{width:18px;height:18px;flex:none}
.soon{display:inline-flex;align-items:center;gap:8px;font-size:15px;color:var(--hero-ink-2);padding:12px 4px}
.soon svg{width:18px;height:18px;flex:none}

/* content */
main{max-width:var(--wide);margin:0 auto;padding:32px 20px 64px}
.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:20px}
@media (min-width:900px){.grid.with-toc{grid-template-columns:240px minmax(0,1fr);align-items:start}}
.toc{position:sticky;top:76px;padding:20px 22px;border-radius:var(--r-card);background:var(--surface);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge)}
.toc .lbl{font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);margin-bottom:10px}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{margin:0}
.toc a{display:block;padding:6px 0;font-size:15px;color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line)}
.toc li:last-child a{border-bottom:0}
.toc a:hover{color:var(--accent)}
.stack{display:grid;gap:20px;max-width:var(--max)}
.grid.with-toc .stack{max-width:none}
.card{background:var(--surface);border-radius:var(--r-card);padding:clamp(22px,3.4vw,32px);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge)}
.card h2{margin-bottom:12px;scroll-margin-top:84px}
.card h3{margin:20px 0 6px}
.card h3:first-of-type{margin-top:0}
.card p+h3{margin-top:18px}
.lead{font-size:clamp(18px,2vw,21px);line-height:1.5;color:var(--ink)}
.stamp{font-size:14px;color:var(--ink-2);margin:0 0 4px}
.callout{display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:var(--r-control);background:var(--accent-soft)}
.callout .tile{flex:none;width:32px;height:32px;border-radius:var(--r-tile);display:grid;place-items:center;background:var(--accent);color:var(--on-accent)}
.callout .tile svg{width:18px;height:18px}
.callout.warm{background:var(--streak-soft)}.callout.warm .tile{background:var(--streak);color:#fff}
.rows{list-style:none;padding:0;margin:0;display:grid;gap:2px}
.rows li{display:grid;grid-template-columns:40px minmax(0,1fr);gap:14px;padding:12px 0;margin:0;border-bottom:1px solid var(--line);align-items:start}
.rows li:last-child{border-bottom:0}
.rows .tile{width:40px;height:40px;border-radius:var(--r-tile);display:grid;place-items:center;background:var(--accent-soft);color:var(--accent)}
.rows .tile svg{width:20px;height:20px}
.rows b{display:block;font-weight:600}
.rows span{color:var(--ink-2);font-size:15.5px}
.features{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.features .card{display:flex;flex-direction:column;gap:10px}
.features .tile{width:44px;height:44px;border-radius:var(--r-chip);display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);margin-bottom:6px}
.features .tile svg{width:22px;height:22px}
.features .card h3{margin:0}
.features .card p{color:var(--ink-2);font-size:16px}
.tiers{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.tier{background:var(--surface);border-radius:var(--r-card);padding:24px;box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge);display:flex;flex-direction:column;gap:10px}
.tier .lbl{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.tier .price{font-size:28px;font-weight:700;letter-spacing:-.02em}
.tier .price small{font-size:15px;font-weight:500;color:var(--ink-2)}
.tier ul{margin-top:4px;color:var(--ink-2);font-size:15.5px}
.tier.premium{background:linear-gradient(180deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke)}
.tier.premium .lbl,.tier.premium ul{color:var(--hero-ink-2)}
.tier.premium li::marker{color:#5ED4C6}
.chip{display:inline-flex;align-items:center;gap:6px;background:var(--fill);color:var(--ink-2);border-radius:999px;padding:4px 10px;font-size:13.5px;font-weight:500}
dl.faq{margin:0}
dl.faq dt{font-weight:600;margin-top:18px}
dl.faq dt:first-child{margin-top:0}
dl.faq dd{margin:6px 0 0;color:var(--ink-2)}
table{width:100%;border-collapse:collapse;font-size:15.5px}
th,td{text-align:left;vertical-align:top;padding:10px 12px 10px 0;border-bottom:1px solid var(--line)}
th{font-weight:600;color:var(--ink-2);font-size:13px;letter-spacing:.06em;text-transform:uppercase}
tr:last-child td{border-bottom:0}
.table-wrap{overflow-x:auto}
.steps{counter-reset:s;list-style:none;padding:0;margin:0;display:grid;gap:12px}
.steps li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:14px;margin:0;align-items:start}
.steps li::before{counter-increment:s;content:counter(s);width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:var(--on-accent);font-weight:700;font-size:14px}

/* footer */
footer{border-top:1px solid var(--line);padding:28px 20px 44px;color:var(--ink-2);font-size:14.5px}
footer .in{max-width:var(--wide);margin:0 auto;display:flex;gap:10px 22px;flex-wrap:wrap;align-items:center;justify-content:space-between}
footer nav{display:flex;gap:6px 16px;flex-wrap:wrap}
footer a{color:var(--ink-2)}
footer a:hover{color:var(--accent)}
"""

ICONS = {
    "pause": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M9 5v14M15 5v14"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/></svg>',
    "wind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h8a2.5 2.5 0 1 1-2.5 2.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 0 2 2h14"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
    "eye-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3l18 18M10.6 10.6a2 2 0 0 0 2.8 2.8M9.9 5.1A10 10 0 0 1 12 5c5 0 8.5 4 9.5 7-.4 1.1-1.1 2.3-2 3.3M6.6 6.6C4.6 8 3.3 10 2.5 12c1 3 4.5 7 9.5 7 1.6 0 3-.4 4.3-1"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
    "info": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l4 4L19 6"/></svg>',
    "apple": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.3 1.2 9.7.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.2-.8s1.9.8 3.2.8 2.1-1.2 2.9-2.4c.9-1.4 1.3-2.7 1.3-2.8-.1 0-2.5-1-2.5-3.8zM14 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.2-.6 2.8-1.4z"/></svg>',
    "widget": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></svg>',
    "bell": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15L6 16z"/><path d="M10 21h4"/></svg>',
    "card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>',
}

def store_button(hero=False):
    if APP_STORE_URL:
        cls = "btn primary"
        return f'<a class="{cls}" href="{E(APP_STORE_URL)}">{ICONS["apple"]} Download on the App Store</a>'
    return f'<span class="soon">{ICONS["apple"]} Coming soon to the App Store</span>'


def page(key, title, description, hero, body, toc=None, canonical=""):
    nav = "".join(
        f'<a href="{E(href)}"{CUR if k == key else ""}>{E(label)}</a>'
        for k, label, href in NAV
    )
    footnav = " · ".join(f'<a href="{E(href)}">{E(label)}</a>' for k, label, href in NAV)
    toc_html = ""
    grid_cls = "grid"
    if toc:
        grid_cls = "grid with-toc"
        toc_html = '<aside class="toc" aria-label="On this page"><div class="lbl">On this page</div><ol>' + "".join(
            f'<li><a href="#{E(i)}">{E(t)}</a></li>' for i, t in toc
        ) + "</ol></aside>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{E(description)}">
<meta name="robots" content="index,follow">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F4F6F9">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0E1116">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{E(SITE + canonical)}">
<link rel="canonical" href="{E(SITE + canonical)}">
<link rel="icon" href="{BASE}/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<title>{E(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="topbar"><div class="in">
  <a class="brand" href="{BASE}/"><span class="orb" aria-hidden="true"></span>{APP}</a>
  <nav class="pages" aria-label="Pages">{nav}</nav>
</div></header>
<div class="hero-wrap"><section class="hero">{hero}</section></div>
<main id="content"><div class="{grid_cls}">{toc_html}<div class="stack">{body}</div></div></main>
<footer><div class="in">
  <div>© {YEAR} {APP} · {COMPANY} · All rights reserved.</div>
  <nav aria-label="Footer">{footnav} · <a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""


def hero(eyebrow, h1, sub, ctas="", meta=""):
    return (
        f'<div class="eyebrow"><span class="dot" aria-hidden="true"></span>{eyebrow}</div>'
        f"<h1>{h1}</h1><p class=\"sub\">{sub}</p>"
        + (f'<div class="ctas">{ctas}</div>' if ctas else "")
        + (f'<p class="meta">{meta}</p>' if meta else "")
    )


def card(id_, h2, inner):
    return f'<section class="card" id="{id_}"><h2 id="{id_}-h">{h2}</h2>{inner}</section>'


def callout(icon, text, warm=False):
    return f'<div class="callout{" warm" if warm else ""}"><span class="tile">{ICONS[icon]}</span><div>{text}</div></div>'


MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
RESET = "<kbd>Settings</kbd> → <kbd>Your data</kbd> → <kbd>Reset all data</kbd>"

# ---------------------------------------------------------------------------
# Support — the App Store "Support URL"
# ---------------------------------------------------------------------------

SUPPORT_TOC = [
    ("how", "How Pausely works"),
    ("requirements", "Requirements"),
    ("start", "Getting started"),
    ("faq", "Frequently asked questions"),
    ("trouble", "Troubleshooting"),
    ("contact", "Contact"),
]

support_body = "".join([
    card("how", "How Pausely works", f"""
<p class="lead">Pausely puts a small speed bump between you and the apps that eat your day.</p>
<p>You choose the apps you would rather use less. After that, tapping one of them does not open it straight away — Pausely stands in front of it first with a short pause: a breath, a sentence to type, or a question about why you are opening it. If you still want to go in, you can, for a timed window. When the window ends, the pause comes back.</p>
<p>The point is not to lock you out. It is to turn an automatic, thumb-driven habit into a decision you actually make. Given ten seconds to think, most people close the app instead — and Pausely counts that as a win.</p>
<ul class="rows">
  <li><span class="tile">{ICONS['shield']}</span><div><b>Protection</b><span>One switch. While it is on, your chosen apps show Pausely's calm block screen instead of opening.</span></div></li>
  <li><span class="tile">{ICONS['wind']}</span><div><b>Three pauses</b><span>A breathing exercise, a typing challenge, or naming your intention. Setup picks the one that fits you; you can change it any time.</span></div></li>
  <li><span class="tile">{ICONS['clock']}</span><div><b>Rules</b><span>Protect certain apps at certain hours — a bedtime, a working day — with their own pause and their own window. A rule can also block completely until its hours are over.</span></div></li>
  <li><span class="tile">{ICONS['lock']}</span><div><b>Strict mode</b><span>Hold yourself to it for an hour, a day, or until a time you choose. While it runs, protection cannot be switched off and rules cannot be deleted — not even by you.</span></div></li>
  <li><span class="tile">{ICONS['book']}</span><div><b>Alternatives and journal</b><span>Up to three healthy alternatives appear on the pause screen as a third way out, and there is a journal for the times you would rather write than scroll.</span></div></li>
  <li><span class="tile">{ICONS['chart']}</span><div><b>Progress</b><span>Pauses kept, time reclaimed, your streak and a weekly chart — plus Home Screen widgets and a Lock Screen countdown while a window is open.</span></div></li>
</ul>
"""),
    card("requirements", "Requirements", f"""
<div class="table-wrap"><table>
<tr><th>Device</th><td>iPhone running <strong>iOS 17 or newer</strong>. Pausely is designed for iPhone.</td></tr>
<tr><th>Permission</th><td><strong>Screen Time</strong> access, granted once during setup through Apple's own prompt. Pausely uses Apple's Screen Time framework — the same system behind iOS's built-in app limits — and Apple, not Pausely, is what actually blocks an app.</td></tr>
<tr><th>Account</th><td>None. There is no sign-up, no email field and no password anywhere in the app.</td></tr>
<tr><th>Internet</th><td>Not needed. Every pause, rule, chart and journal entry works offline. The only network traffic is Apple's, when you buy or restore Premium.</td></tr>
<tr><th>Notifications</th><td>Optional, and local to the phone. Pausely uses them to hand you from the block screen into the pause, and to ask afterwards how a session left you feeling.</td></tr>
</table></div>
"""),
    card("start", "Getting started", f"""
<p>Setup is seven screens and takes under three minutes. It ends with protection already on and your first rule already written.</p>
<ol class="steps">
  <li><div><b>Say how much of the day your phone gets</b> — your own guess, nothing measured.</div></li>
  <li><div><b>Allow Screen Time access</b> when Apple asks. Pausely cannot work without it, and you can revoke it any time in <kbd>Settings</kbd> → <kbd>Screen Time</kbd>.</div></li>
  <li><div><b>Pick your apps</b> in Apple's picker. Pausely never learns their names — see <a href="{BASE}/privacy/">Privacy</a>.</div></li>
  <li><div><b>Answer three questions</b> that choose the pause that fits you.</div></li>
  <li><div><b>Add up to three alternatives</b> — a walk, a book, a glass of water, or something of your own with a link into another app.</div></li>
  <li><div><b>Done.</b> Open one of your apps and meet the pause.</div></li>
</ol>
"""),
    card("faq", "Frequently asked questions", f"""
<dl class="faq">
<dt>Is Pausely free?</dt>
<dd>Yes. Free is a working product, not a demo: <strong>one rule</strong>, the <strong>breathing pause</strong> and your <strong>whole progress screen</strong> — pauses, wins, time reclaimed, the streak and the chart.</dd>
<dt>What does Premium add?</dt>
<dd>As many rules as you like, the other two pauses (type to proceed, set an intention), strict mode, and the mood insight that compares how you feel after a session with how you feel after walking away. Premium is a monthly or yearly subscription — the yearly plan starts with a <strong>free trial</strong> — or a single lifetime purchase. Prices are shown in the app and in the App Store for your country, and billing is handled by Apple.</dd>
<dt>What happens if my subscription lapses?</dt>
<dd>Nothing you built is taken away. Every rule keeps running and stays editable, and the pause you chose keeps standing in front of your apps. Only the ability to add more closes. An app that stopped protecting your phone because a card expired would be letting you down at the exact moment you asked it not to.</dd>
<dt>Can I restore a purchase on a new phone?</dt>
<dd>Yes. Open the Premium screen and tap <kbd>Restore Purchases</kbd>. Premium belongs to your Apple ID, not to the phone.</dd>
<dt>Why can't Pausely tell me which apps I blocked?</dt>
<dd>Because it genuinely does not know. Apple's Screen Time hands Pausely opaque tokens that are meaningless outside your phone — no app names, no identifiers. Pausely can ask iOS to block them; it cannot read them.</dd>
<dt>I can't turn protection off. Is something broken?</dt>
<dd>Check whether <strong>strict mode</strong> is running — the home screen says so. While it runs, protection cannot be switched off and rules cannot be deleted, by design. It ends on its own at the time you chose.</dd>
<dt>Does Pausely see what I do in other apps?</dt>
<dd>No. It never observes your browsing, messages or activity inside any app. It records only its own events — that a pause was shown, and what you chose — and keeps those on your phone.</dd>
<dt>Does it work on iPad or Mac?</dt>
<dd>Pausely is built for iPhone. It is not offered on other devices.</dd>
<dt>How do I erase everything?</dt>
<dd>{RESET}. That empties every pause, win, rule, journal entry and check-in, takes the blocks down and starts you at the beginning. It refuses while strict mode is running. Details on the <a href="{BASE}/delete-data/">Your data</a> page.</dd>
</dl>
"""),
    card("trouble", "Troubleshooting", f"""
<h3>An app opens without a pause</h3>
<ul>
  <li>Check the <strong>Protection</strong> switch on the home screen.</li>
  <li>Check that Screen Time access is still granted: <kbd>Settings</kbd> → <kbd>Screen Time</kbd> → <kbd>Apps with Screen Time access</kbd>. If it was revoked, Pausely shows a recovery screen with a button to ask again.</li>
  <li>If the app is only in a <strong>rule</strong>, the pause appears only during that rule's hours.</li>
  <li>An <strong>access window</strong> you opened earlier may still be running — the Lock Screen countdown shows how long is left.</li>
</ul>
<h3>The block screen appears but the pause never opens</h3>
<ul>
  <li>Tapping the block screen's button hands you to the app through a notification. If notifications are off for Pausely, iOS cannot deliver the hand-off — turn them on in <kbd>Settings</kbd> → <kbd>Notifications</kbd> → <kbd>Pausely</kbd>.</li>
  <li>Opening Pausely directly also opens the waiting pause.</li>
</ul>
<h3>Widgets are behind</h3>
<p>iOS refreshes widgets on its own schedule. Opening Pausely brings them up to date immediately.</p>
<h3>Premium isn't recognised</h3>
<p>Tap <kbd>Restore Purchases</kbd> on the Premium screen, and make sure the phone is signed into the same Apple ID that made the purchase. Refunds and billing questions are handled by Apple through <a href="https://support.apple.com/billing">Apple Support</a>.</p>
"""),
    card("contact", "Contact", f"""
<p>Questions, a bug, or something that should work and doesn't — write to us and a person will reply.</p>
{callout('mail', f'<strong>{MAIL}</strong><br><span class="small">Include your iPhone model, the iOS version, and what you expected to happen. Never send us your journal or check-ins — we do not need them and would rather not hold them.</span>')}
<p style="margin-top:16px" class="small">Billing, refunds and subscription changes are handled by Apple: <a href="https://apps.apple.com/account/subscriptions">manage subscriptions</a> · <a href="https://support.apple.com/billing">request a refund</a>.</p>
"""),
])

support_hero = hero(
    "Support",
    "Help with Pausely",
    "A breath before the scroll. Pausely stands in front of the apps you chose and asks for ten seconds first. This page covers how it works, what it needs, and how to reach us.",
    store_button(True) + f'<a class="btn quiet" href="#faq">Read the FAQ</a>',
    f'No account · nothing leaves your phone · <a href="{BASE}/privacy/">Privacy Policy</a>',
)

# ---------------------------------------------------------------------------
# About — the App Store "Marketing URL"
# ---------------------------------------------------------------------------

about_body = f"""
<section class="card"><p class="lead">Pausely puts a small speed bump between you and the apps that eat your day. Not a lockout, not a guilt trip — ten seconds to decide whether you meant to open it.</p></section>
<div class="features">
  <section class="card"><span class="tile">{ICONS['wind']}</span><h3>A breath before the scroll.</h3><p>Pausely stands in front of the apps you chose and asks for ten seconds first — a breathing exercise, a sentence to type, or a moment to name your intention.</p></section>
  <section class="card"><span class="tile">{ICONS['pause']}</span><h3>Why are you opening it?</h3><p>Turn a reflex into a decision — and make it on purpose. Most of the time, given the chance to think, people close the app instead.</p></section>
  <section class="card"><span class="tile">{ICONS['check']}</span><h3>Walking away counts.</h3><p>Keep the win, or go in for five minutes — no lockouts, no guilt trips. Your own alternatives sit on the pause screen as a third way out.</p></section>
  <section class="card"><span class="tile">{ICONS['chart']}</span><h3>See the time come back.</h3><p>Every pause you kept, every hour reclaimed, a streak and a weekly chart — with widgets for the Home Screen and a countdown on the Lock Screen.</p></section>
  <section class="card"><span class="tile">{ICONS['clock']}</span><h3>Your apps. Your rules.</h3><p>A switch and a pause for every app, with schedules for evenings and workdays. Strict mode holds you to it when you ask it to.</p></section>
  <section class="card"><span class="tile">{ICONS['eye-off']}</span><h3>Nothing leaves your phone.</h3><p>No account, no analytics, no server. Pausely cannot even read which apps you picked — Apple keeps that. <a href="{BASE}/privacy/">How that works.</a></p></section>
</div>
<section class="card" id="pricing"><h2>What it costs</h2>
<p>Free is a working product, not a demo, and nothing you set up is ever taken away — even if a subscription lapses.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Free</div><div class="price">$0</div><ul><li>One rule</li><li>The breathing pause</li><li>The whole progress screen — wins, time reclaimed, streak and chart</li><li>Widgets and the Lock Screen countdown</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Monthly · Yearly · Lifetime</div><ul><li>As many rules as you like</li><li>All three pauses</li><li>Strict mode</li><li>The mood insight</li><li>Yearly starts with a free trial</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Prices are shown in the app and on the App Store for your country. Billing is handled by Apple. <a href="{BASE}/terms/#subscriptions">Subscription terms.</a></p>
</section>
<section class="card"><h2>Built on Apple's Screen Time</h2>
<p>Pausely uses the same framework that powers iOS's built-in app limits. Apple grants it only to apps it has reviewed for the purpose, and Apple — not Pausely — is what actually stands between you and the app. That is why Pausely can block an app without ever learning its name.</p>
<p>iPhone · iOS 17 or newer · English</p>
</section>
"""

about_hero = hero(
    "About Pausely",
    "A breath before the scroll.",
    "Pick the apps you'd rather use less. From then on, opening one gets you a pause first — and a choice you actually make.",
    store_button(True) + f'<a class="btn quiet" href="{BASE}/">Support</a>',
    "No account · nothing leaves your phone · iPhone, iOS 17+",
)

# ---------------------------------------------------------------------------
# Privacy Policy
# ---------------------------------------------------------------------------

PRIVACY_TOC = [
    ("summary", "The short version"),
    ("collect", "What we collect"),
    ("device", "What stays on your phone"),
    ("screentime", "Screen Time and your app selection"),
    ("purchases", "Purchases"),
    ("notifications", "Notifications, widgets and the Lock Screen"),
    ("third", "Third parties"),
    ("delete", "Deleting your data"),
    ("rights", "Your rights"),
    ("children", "Children"),
    ("future", "Changes we already know about"),
    ("changes", "Changes to this policy"),
    ("contact", "Contact"),
]

privacy_body = "".join([
    f'<p class="stamp">Last updated: {UPDATED}</p>',
    card("summary", "The short version", f"""
<p class="lead"><strong>Pausely collects nothing.</strong> It has no account, no analytics, no advertising, no third-party SDKs and no server. It makes no network calls of its own. Everything it knows is written to your iPhone and stays there.</p>
{callout("eye-off", "Pausely does not even know which apps you chose to pause. Apple's Screen Time gives it opaque tokens that only your phone can interpret. There is no app name, no identifier, and nothing to send.")}
<p style="margin-top:16px">This policy applies to the Pausely app for iPhone, published by {COMPANY}, and to this website. It is written to be read, and it says the same thing as the privacy label on Pausely's App Store page: <strong>Data Not Collected.</strong></p>
"""),
    card("collect", "What we collect", f"""
<p>Nothing. In Apple's terms, "collecting" means transmitting data off the device and storing it somewhere that is not transient. Pausely has no channel through which that could happen.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Collected?</th><th>Why not</th></tr>
<tr><td>Contact info</td><td>No</td><td>There is no account, no sign-in and no email field anywhere in the app.</td></tr>
<tr><td>Identifiers</td><td>No</td><td>No user ID, no device ID, no advertising identifier. Pausely never asks for App Tracking Transparency because it has nothing to ask about.</td></tr>
<tr><td>Usage data</td><td>No</td><td>No analytics SDK and no product-interaction events. Nothing is counted anywhere except on your phone, for your own progress screen.</td></tr>
<tr><td>User content</td><td>No</td><td>Your journal, your check-ins, the sentence you type on the pause screen and your custom alternatives are stored on the device and nowhere else.</td></tr>
<tr><td>Purchases</td><td>No</td><td>Payment is Apple's, in the App Store sheet. Pausely never sees a card and sends nothing about the purchase anywhere.</td></tr>
<tr><td>Location, health, contacts, browsing, search, diagnostics</td><td>No</td><td>Pausely does not link the frameworks that would read them and has no crash or performance reporter of its own.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> none. Pausely does not link anything about you with data from other companies' apps or websites, and shares nothing with data brokers or advertisers.</p>
"""),
    card("device", "What stays on your phone", f"""
<p>Pausely stores the following in its own private storage on your iPhone, protected by your device's passcode and encryption. None of it is uploaded, backed up by us, or visible to us.</p>
<ul>
  <li><strong>Your app selection</strong> — as opaque Screen Time tokens Pausely cannot read (see below).</li>
  <li><strong>Your rules and schedules</strong> — the names you give them, their hours and their pause.</li>
  <li><strong>Pause outcomes</strong> — that a pause was shown, when, and whether you walked away, went in, or chose an alternative. This is what the progress screen, the streak and the chart are made of.</li>
  <li><strong>What you write</strong> — journal entries, the words you type on the pause screen, mood check-ins after a session, and the names of custom alternatives.</li>
  <li><strong>Settings</strong> — your chosen pause, strict-mode state, alternatives, and preferences.</li>
  <li><strong>Your Premium entitlement</strong> — a tier and an expiry date, so the app knows what to unlock.</li>
</ul>
<p>If you use iCloud Backup or an encrypted local backup, Apple may include Pausely's data in that backup under your own Apple ID and Apple's privacy terms. We have no access to it.</p>
"""),
    card("screentime", "Screen Time and your app selection", f"""
<p>Pausely is built on Apple's Screen Time framework (Family Controls, Managed Settings and Device Activity). You grant it access once, through Apple's own prompt, and can revoke it at any time in <kbd>Settings</kbd> → <kbd>Screen Time</kbd>.</p>
<p>When you pick apps, Apple's picker returns <strong>tokens</strong>: values that identify the app to iOS but mean nothing to Pausely and nothing outside your phone. Pausely stores those tokens so it can ask iOS to shield the apps you chose. It never receives a bundle identifier or an app name, and it could not report one if it wanted to. Where it needs to compare tokens between its own components it compares one-way hashes of them, never the tokens themselves.</p>
<p>Pausely does not observe your browsing, your messages, or what you do inside any app. iOS itself draws the block screen and enforces the shield. Pausely learns only that its own pause was shown and what you chose on it.</p>
"""),
    card("purchases", "Purchases", f"""
<p>Premium is sold through Apple's App Store using StoreKit. The transaction is between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Apple tells Pausely whether a purchase is active — nothing else — and Pausely tells Apple nothing about how you use the app. No usage data, no journal, no app selection and no identifier of ours travels with a purchase.</p>
"""),
    card("notifications", "Notifications, widgets and the Lock Screen", f"""
<p><strong>Notifications</strong> are optional and are generated on your phone. Pausely uses them to hand you from the block screen into the pause, and to ask afterwards how a session left you feeling. No notification is sent from a server, because there is no server.</p>
<p><strong>Widgets and the Live Activity</strong> show counts and dates — today's wins, your streak, time reclaimed, and how long an access window has left. They deliberately do not have Screen Time access and never see which apps you blocked. A Lock Screen countdown names the <em>rule</em> you wrote ("Bedtime"), never the app, because a Lock Screen is readable by anyone holding the phone.</p>
"""),
    card("third", "Third parties", f"""
<p>None. Pausely contains no third-party code, no analytics, no advertising and no crash reporter. The only other party involved is <strong>Apple</strong>: it operates the App Store, processes purchases, enforces the Screen Time shield, and — if you have opted in to sharing with developers — may share crash logs with us under its own policy. We do not sell, rent or share personal data with anyone, because we hold none.</p>
"""),
    card("delete", "Deleting your data", f"""
<p>Everything Pausely holds is erasable from inside the app, without asking us:</p>
{callout('trash', f'{RESET}<br><span class="small">Empties every pause, win, rule, journal entry and check-in, takes the shields down, withdraws the schedules and starts you at the beginning. It refuses while strict mode is running — the one commitment you asked the app to hold you to — and it does not touch your subscription, which belongs to your Apple ID.</span>')}
<p style="margin-top:16px">Deleting the app removes all of its data from the phone as well. There is nothing on our side to delete, and so nothing to request — but you are welcome to write to us anyway. See the <a href="{BASE}/delete-data/">Your data</a> page.</p>
"""),
    card("rights", "Your rights", f"""
<p>Wherever you live — including under the GDPR, the UK GDPR and the CCPA/CPRA — you have rights to access, correct, export, restrict and erase personal data a company holds about you, and to complain to a supervisory authority. Because Pausely holds no personal data about you, there is nothing for us to produce or delete; the data on your phone is already in your hands, and the app's own controls exercise every one of those rights for you. If you believe otherwise, write to {MAIL} and we will respond.</p>
"""),
    card("children", "Children", f"""
<p>Pausely is a self-directed tool for the person using the phone. It is not a parental-control product and does not manage another person's device. It is not directed at children under 13 (or the age of digital consent where you live), and we do not knowingly collect personal information from anyone — of any age.</p>
"""),
    card("future", "Changes we already know about", f"""
<p>We are designing one optional feature that would change the sentence at the top of this page: an <strong>AI reflection</strong> that turns the "why are you opening it?" question into a short conversation. It is <strong>not in the app today</strong>. When it ships:</p>
<ul>
  <li>It will be <strong>off until you switch it on</strong>, and switching it off returns the app to making no network calls at all.</li>
  <li>It will send only the display name of the app you are opening, three numbers (how many times today, the time on the clock, your streak) and the words you type into that one screen — to Pausely's own service, never a model vendor's API from the app.</li>
  <li>It will never send your journal, your check-ins, your app selection or any identifier, and nothing sent will be linked to you.</li>
</ul>
<p>This policy will be updated on the day that feature ships, before it is switched on for anyone.</p>
"""),
    card("changes", "Changes to this policy", f"""
<p>We may update this policy as the app changes. The date at the top moves when we do, and material changes will be noted in the app's release notes. Continued use of Pausely after a change means you accept the revised policy.</p>
"""),
    card("contact", "Contact", f"""
<p>{COMPANY}, the publisher of Pausely, is the controller for anything covered here. Questions about privacy: {MAIL}.</p>
"""),
])

privacy_hero = hero(
    "Privacy Policy",
    "Nothing leaves your phone.",
    "Pausely has no account, no analytics and no server. Which apps you use, how often, what you write — all of it stays on your iPhone, and this page explains why that is not a slogan.",
    "",
    f"Effective {UPDATED} · applies to the Pausely app for iPhone and to this site",
)

# ---------------------------------------------------------------------------
# Terms of Use (EULA)
# ---------------------------------------------------------------------------

TERMS_TOC = [
    ("acceptance", "1. Acceptance"),
    ("who", "2. Who may use Pausely"),
    ("what", "3. What Pausely is — and is not"),
    ("screentime", "4. Screen Time, strict mode and your commitments"),
    ("data", "5. Your data and your device"),
    ("subscriptions", "6. Premium, subscriptions and billing"),
    ("licence", "7. Licence and intellectual property"),
    ("use", "8. Acceptable use"),
    ("termination", "9. Termination"),
    ("warranty", "10. Warranties and liability"),
    ("apple", "11. Apple"),
    ("changes", "12. Changes to these Terms"),
    ("law", "13. Governing law"),
    ("contact", "14. Contact"),
]

terms_body = "".join([
    f'<p class="stamp">Last updated: {UPDATED}</p>',
    card("acceptance", "1. Acceptance of Terms", f"""
<p>These Terms of Use ("Terms") are an agreement between you and {COMPANY} ("we", "us"), the publisher of the Pausely app for iPhone ("Pausely" or "the app"). By installing or using Pausely you accept these Terms and our <a href="{BASE}/privacy/">Privacy Policy</a>. If you do not agree, do not use the app.</p>
"""),
    card("who", "2. Who may use Pausely", f"""
<p>You must be at least 13 years old, or the age of digital consent where you live, to use Pausely. Pausely is a tool you install for yourself, on your own iPhone. It is not a parental-control product and must not be used to manage or monitor another person's device.</p>
"""),
    card("what", "3. What Pausely is — and is not", f"""
<p>Pausely is a self-directed tool that adds a pause before apps you choose, records the outcomes on your phone, and shows you your own progress. It is designed to make an automatic habit into a conscious choice.</p>
<p>Pausely is <strong>not</strong> a medical, psychological or therapeutic service, and nothing in it — including mood check-ins, journal prompts and insights — is advice, diagnosis or treatment. If you are struggling with compulsive use, anxiety, depression or anything else that affects your wellbeing, please speak to a qualified professional. In an emergency, call your local emergency number.</p>
<p>Pausely is also <strong>not a security or parental-control product</strong>. It is designed to be exactly as strong as you ask it to be: the app can be deleted, Screen Time access can be revoked in iOS Settings, and the shield exists only while the app is installed and authorised.</p>
"""),
    card("screentime", "4. Screen Time, strict mode and your commitments", f"""
<p>Pausely relies on Apple's Screen Time framework. Apple enforces the shield; Pausely asks for it. Whether a shield appears, how quickly, and whether it persists across restarts and iOS updates is ultimately determined by iOS, and we cannot guarantee it in every circumstance.</p>
<p><strong>Strict mode</strong> is a commitment you make to yourself. While it runs, for the duration you chose, protection cannot be switched off, rules cannot be deleted and data cannot be reset — <em>including by you, and including by us</em>. We cannot end a strict-mode session early on request. Do not start one you are not prepared to keep, and do not start one on a phone you may need unrestricted access to. Deleting the app ends every shield, as described in section 3.</p>
<p>A <strong>hard-block rule</strong> offers no way through during its hours. The same warning applies.</p>
"""),
    card("data", "5. Your data and your device", f"""
<p>Everything Pausely records is stored on your iPhone and nowhere else — see the <a href="{BASE}/privacy/">Privacy Policy</a>. You are responsible for your device, its passcode and its backups. If you delete the app, reset all data, or lose the device without a backup, your rules, journal and history are gone, and we have no copy to restore. Your Premium purchase is separate: it belongs to your Apple ID and can be restored on any iPhone signed into it.</p>
<p>What you write into Pausely is yours. We claim no rights over it and never receive it.</p>
"""),
    card("subscriptions", "6. Premium, subscriptions and billing", f"""
<p>Pausely is free to download and use. <strong>Pausely Premium</strong> unlocks additional features and is sold in three forms, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Premium Monthly</strong> — an auto-renewing subscription, billed monthly.</li>
  <li><strong>Premium Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered.</li>
  <li><strong>Premium Lifetime</strong> — a one-time purchase that does not renew.</li>
</ul>
<p>Payment is charged to your Apple ID at confirmation of purchase. A free trial converts to a paid subscription unless you cancel at least 24 hours before the trial ends. Subscriptions renew automatically at the same price and period unless auto-renew is turned off at least 24 hours before the end of the current period; renewal is charged within the 24 hours before that period ends. You can manage or cancel a subscription in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; cancellation takes effect at the end of the current period, and no partial refund is given for the unused part of a period. Refunds are handled by Apple under Apple's policies. Use <kbd>Restore Purchases</kbd> in the app to recover Premium on a new device.</p>
<p><strong>If a subscription lapses</strong>, nothing you have already set up is removed: every rule keeps running and stays editable, and your chosen pause keeps working. Only the ability to add more Premium content closes. The set of Premium features may change over time; we will not remove a feature from an active subscription without notice.</p>
"""),
    card("licence", "7. Licence and intellectual property", f"""
<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to install and use Pausely on an iPhone you own or control, in accordance with these Terms and the App Store's usage rules. Pausely, its name, design, artwork, text and code are owned by {COMPANY} and protected by copyright and other laws. You may not copy, modify, distribute, sell, lease, reverse-engineer or create derivative works from the app except where the law expressly allows it.</p>
"""),
    card("use", "8. Acceptable use", f"""
<p>You agree not to use Pausely in any way that is unlawful, that interferes with the app or Apple's services, that attempts to bypass the App Store's purchase mechanisms, or that installs it on a device you are not entitled to manage. You agree not to use it to restrict or monitor another person without their informed consent.</p>
"""),
    card("termination", "9. Termination", f"""
<p>You may stop using Pausely at any time by deleting it. We may suspend or end your licence if you breach these Terms. Sections 5, 7, 10, 11 and 13 survive termination. Deleting the app does not cancel an active subscription — cancel it in your App Store settings.</p>
"""),
    card("warranty", "10. Warranties and liability", f"""
<p>Pausely is provided "as is" and "as available", without warranties of any kind, express or implied, including that it will block any app in every circumstance, that it will be uninterrupted or error-free, or that it will change your habits. To the fullest extent permitted by law, {COMPANY} shall not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of data, arising from your use of or inability to use the app — including any consequence of a shield that did or did not appear, or of a strict-mode session you chose to start. Where liability cannot be excluded, it is limited to the amount you paid us for Premium in the twelve months before the claim. Nothing in these Terms limits rights you have as a consumer that cannot be waived.</p>
"""),
    card("apple", "11. Apple", f"""
<p>Pausely is distributed through the Apple App Store. These Terms are between you and {COMPANY}, not Apple. Apple has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to it, including product-liability, legal-compliance or intellectual-property claims. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them against you. Where these Terms are silent, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a> applies. You represent that you are not in a country subject to a U.S. government embargo or listed as a prohibited party, and you must comply with any applicable third-party terms when using the app.</p>
"""),
    card("changes", "12. Changes to these Terms", f"""
<p>We may update these Terms from time to time. The date at the top will change when we do, and material changes will be noted in the app's release notes. Continued use after an update means you accept the revised Terms.</p>
"""),
    card("law", "13. Governing law", f"""
<p>These Terms are governed by the laws of Pakistan, where {COMPANY} operates, without regard to conflict-of-law provisions. Where the law of your country of residence gives you protections that cannot be contracted out of, those protections apply.</p>
"""),
    card("contact", "14. Contact", f"""
<p>Questions about these Terms: {MAIL}.</p>
"""),
])

terms_hero = hero(
    "Terms of Use",
    "The agreement, in plain words.",
    "What Pausely does, what it does not promise, how Premium is billed, and what strict mode asks of you.",
    "",
    f"Effective {UPDATED} · Pausely by {COMPANY}",
)

# ---------------------------------------------------------------------------
# Your data / delete
# ---------------------------------------------------------------------------

DATA_TOC = [
    ("where", "What is stored where"),
    ("inapp", "Erase it in the app"),
    ("uninstall", "Delete the app"),
    ("subscription", "Your subscription"),
    ("email", "Ask us"),
]

data_body = "".join([
    card("where", "What is stored where", f"""
<p class="lead">Pausely has no account and no server, so there is nothing to delete on our side. Everything it holds is on your iPhone, and you can erase it without asking anyone.</p>
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Rules, pause history, streak, journal, check-ins, alternatives, settings</td><td>The app's private storage on your phone</td><td>{RESET}, or delete the app</td></tr>
<tr><td>Your app selection</td><td>Opaque Screen Time tokens in the app's private storage</td><td>Same as above; revoking Screen Time access in iOS Settings also ends every shield</td></tr>
<tr><td>Widget snapshot</td><td>A small file of counts and dates on your phone</td><td>Removed with the reset and with the app</td></tr>
<tr><td>Premium entitlement</td><td>Your Apple ID (Apple) and a copy of its status on your phone</td><td>Managed in your App Store settings — see below</td></tr>
<tr><td>Anything on our servers</td><td>—</td><td>There are none.</td></tr>
</table></div>
"""),
    card("inapp", "Erase it in the app", f"""
<ol class="steps">
  <li><div>Open Pausely and go to <kbd>Settings</kbd>.</div></li>
  <li><div>Tap <kbd>Your data</kbd>, then <kbd>Reset all data</kbd>.</div></li>
  <li><div>Confirm. Every pause, win, rule, journal entry and check-in is erased, the shields come down, the schedules are withdrawn, and the app starts again from setup.</div></li>
</ol>
{callout('lock', '<strong>It refuses while strict mode is running.</strong> That is the one commitment you asked the app to hold you to. Wait for the session to end at the time you chose, then reset.', warm=True)}
"""),
    card("uninstall", "Delete the app", f"""
<p>Deleting Pausely from your iPhone removes all of its data with it, including the Screen Time tokens, and ends every shield immediately. If the app is included in an iCloud or encrypted local backup, that copy belongs to your Apple ID and is governed by Apple's terms; we have no access to it.</p>
"""),
    card("subscription", "Your subscription", f"""
<p>Neither resetting data nor deleting the app cancels a subscription — it belongs to your Apple ID, not to the app. Cancel it in <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; it stays active until the end of the current period. Refunds are handled by <a href="https://support.apple.com/billing">Apple Support</a>. A lifetime purchase does not renew and needs nothing cancelled.</p>
"""),
    card("email", "Ask us", f"""
<p>If you would like written confirmation that we hold nothing about you, or you believe we do, write to {MAIL} from any address. We will reply within 30 days. Please do not send us your journal, check-ins or screenshots of them — we do not need them to answer.</p>
"""),
])

data_hero = hero(
    "Your data",
    "Delete your data",
    "Everything Pausely knows is on your phone. Here is how to erase it, what happens to your subscription, and what — nothing — is left on our side.",
    "",
    f'See also the <a href="{BASE}/privacy/">Privacy Policy</a>',
)

# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

nf_body = f"""<section class="card"><p class="lead">That page isn't here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.</p></section>"""
nf_hero = hero("404", "Nothing to see here.", "Which, for once, is not the point.", f'<a class="btn primary" href="{BASE}/">Back to Support</a>')

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><radialGradient id="g" cx="38%" cy="32%" r="70%"><stop offset="0" stop-color="#D1FAF2"/><stop offset=".62" stop-color="#5ED4C6"/><stop offset="1" stop-color="#3FA599"/></radialGradient></defs><rect width="64" height="64" rx="16" fill="#0E1116"/><circle cx="32" cy="32" r="20" fill="url(#g)"/><path d="M27 24v16M37 24v16" stroke="#0E1116" stroke-width="4" stroke-linecap="round"/></svg>"""

PAGES = [
    ("index.html", page("support", f"{APP} — Support", "Official support for Pausely, the iPhone app that puts a pause in front of the apps you chose. How it works, requirements, FAQ and contact.", support_hero, support_body, SUPPORT_TOC, "/")),
    ("about/index.html", page("about", f"{APP} — A breath before the scroll", "Pausely puts a small speed bump between you and the apps that eat your day. No account, nothing leaves your phone.", about_hero, about_body, None, "/about/")),
    ("privacy/index.html", page("privacy", f"Privacy Policy — {APP}", "Pausely collects nothing. No account, no analytics, no server. This policy explains what stays on your phone and why.", privacy_hero, privacy_body, PRIVACY_TOC, "/privacy/")),
    ("terms/index.html", page("terms", f"Terms of Use — {APP}", "Terms of Use (EULA) for Pausely: what the app is and is not, how Premium is billed, and what strict mode asks of you.", terms_hero, terms_body, TERMS_TOC, "/terms/")),
    ("delete-data/index.html", page("data", f"Delete your data — {APP}", "How to erase everything Pausely holds — all of it on your phone — and what happens to your subscription.", data_hero, data_body, DATA_TOC, "/delete-data/")),
    ("404.html", page("404", f"Not found — {APP}", "Page not found.", nf_hero, nf_body, None, "/404.html")),
]

for rel, content in PAGES:
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)

with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON)
print("wrote favicon.svg")
