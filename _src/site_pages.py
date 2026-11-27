# -*- coding: utf-8 -*-
"""The English home page, How it works, Pricing and the guides.

`gen.py` owns the support and legal pages in eight languages and calls `build()`
here at the end of its run. These pages are English only for now; their words
live in this file and in `guides.py`, their styles in `assets/site.css`.

Rules these pages keep, same as the app (CLAUDE.md in the app repo):
  * only features the app has, named the way its screens name them;
  * nothing scolds anyone for the time they spend on their phone;
  * no borrowed statistics, studies, press or reviews, and no claim that the
    app sends nothing anywhere (the Privacy Policy says exactly what leaves);
  * the short video figure is an estimate and always says "about";
  * drawings of the app are drawings, and example numbers say they are examples;
  * no long dashes in copy.
"""
import json
import os
import re
import shutil

import gen
from gen import APP, APP_STORE_ID, APP_STORE_URL, BASE, COMPANY, E, EMAIL, SITE, YEAR

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = BASE + "/assets"

# App Store Connect campaign links. Paste the provider token from
# App Store Connect > Analytics > Sources > Campaigns ("pt=" in a generated link)
# and every button on these pages reports which page sent the download.
PROVIDER_TOKEN = None

UPDATED = "27 November 2026"
UPDATED_ISO = "2026-11-27"

APPLE = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.2 1.8-3.26 '
         '1.88-3.31-1.02-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 '
         '2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.85-.71 1.33 0 1.71.71 '
         '2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.2 '
         '6.13c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.7-.93 2.7.98.08 1.98-.5 2.59-1.24z"/></svg>')


def store_url(ct):
    if PROVIDER_TOKEN:
        return f"{APP_STORE_URL}?pt={PROVIDER_TOKEN}&ct={ct}&mt=8"
    return APP_STORE_URL


def store(ct):
    return (f'<a class="store" href="{E(store_url(ct))}">{APPLE}'
            f'<span><small>Download on the</small><b>App Store</b></span></a>')


# Drawings of the app's screens, in the app's own words.
M_SHIELD = ('<div class="mini m-shield"><div class="num">12</div><b>Opens today</b>'
            '<div class="btns"><span>Open Pausely</span><span>Never mind</span></div></div>')
M_BREATH = ('<div class="mini m-breath"><div class="o"></div><b>Breathe in</b>'
            '<small>Ten seconds of breathing before you continue.</small></div>')
M_CHOICE = ('<div class="mini m-choice"><b>You paused.</b>'
            '<div class="btns"><span>I changed my mind</span><span>Continue for 5 minutes</span>'
            '<span>Or walk for 10 minutes</span></div></div>')
A_SHIELD = "A drawing of the block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind."
A_BREATH = "A drawing of the breathing pause: a soft circle and the words Breathe in."
A_CHOICE = ("A drawing of the choice screen: You paused. Buttons: I changed my mind, Continue for 5 minutes, "
            "Or walk for 10 minutes.")

TODAY = """<div class="today" role="img" aria-label="An example of today's numbers in Pausely: 7 pauses today, 5 walked away, 38 minutes saved, a 6 day streak.">
  <div class="hd"><b>Protection</b><span class="sw"></span></div>
  <div class="nums">
    <div><b>7</b><span>Pauses today</span></div>
    <div><b>5</b><span>Walked away</span></div>
    <div><b>38m</b><span>Time saved</span></div>
  </div>
  <div class="streak"><i></i>6 day streak</div>
  <div class="eg">Example numbers.</div>
</div>"""

PAUSES = [
    ("Deep breath", "free", "Ten seconds of breathing before you continue."),
    ("Type to proceed", "premium", "Type a short string of characters first. Hard to do on autopilot."),
    ("Set an intention", "premium", "Tap why you are opening the app. One tap, twelve reasons."),
    ("Read a reminder", "premium", "A line to read before you go in, from Pausely or written by you."),
    ("Answer a question", "premium", "One question about your country, one try. Written by AI, and off until you turn AI pauses on."),
    ("Reflect for a moment", "premium", "A short exchange about why you are here. Written by AI, and off until you turn it on."),
]
HOLDS = [
    ("Rules", "free", "Protect certain apps at certain hours, such as bedtime or the working day. One rule is free."),
    ("Daily limits", "premium", "After so many minutes or so many opens, an app rests until tomorrow."),
    ("Block everything", "premium", "Shut every protected app for as long as you choose."),
    ("Strict mode", "premium", "Holds until a time you pick. Nothing can be undone before then, not even by you."),
    ("Lock Pausely", "premium", "Every change waits first, and no app can be deleted while it is on."),
]


def rows(items):
    def tag(kind):
        return '<i class="tag free">Free</i>' if kind == "free" else '<i class="tag">Premium</i>'
    return '<ul class="rows">' + "".join(
        f"<li><div><b>{name}</b><span>{text}</span></div>{tag(kind)}</li>" for name, kind, text in items) + "</ul>"


NAV = [("how-it-works", "How it works", "/how-it-works/"), ("pricing", "Pricing", "/pricing/"),
       ("guides", "Guides", "/guides/"), ("support", "Support", "/support/")]


def layout(key, path, title, description, body, *, ct, dark=False, jsonld=(), og_type="website"):
    """One page. `path` is its address under the site root, `ct` its campaign name."""
    url = SITE + path
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{BASE}{p}"{current if k == key else ""}>{label}</a>' for k, label, p in NAV
    )
    get = f'<a class="get" href="{E(store_url(ct + "-nav"))}">Get the app</a>'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in jsonld)
    brand = f'<a class="brand" href="{BASE}/"><img src="{BASE}/icon.png" alt="" width="32" height="32">{APP}</a>'
    top = f"""<header class="top"><div class="wrap">
  {brand}
  <a class="get get-m" href="{E(store_url(ct + "-nav"))}">Get the app</a>
  <nav aria-label="Pages">{nav}{get}</nav>
</div></header>"""
    languages = " · ".join(
        f'<a href="{BASE}{p}/" lang="{c}" hreflang="{c}">{E(gen.NATIVE_NAME[c])}</a>'
        for c, p in gen.LANGUAGES if c != "en"
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
<link rel="canonical" href="{E(url)}">
<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}">
<meta name="theme-color" content="{'#183139' if dark else '#0A1216'}">
<meta property="og:site_name" content="{APP}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{E(url)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/icon.png" type="image/png">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<link rel="preload" href="{ASSETS}/fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ASSETS}/site.css">
{ld}
</head>
<body class="{'' if dark else 'on-light'}">
<a class="skip" href="#content">Skip to content</a>
{'' if dark else top}
{body.replace('<!--TOP-->', top) if dark else body}
<footer><div class="wrap">
  <div class="who">
    {brand}
    <p>A breath before the scroll. Made by {COMPANY}. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> and a person will reply.</p>
  </div>
  <div><h4>The app</h4><ul>
    <li><a href="{BASE}/how-it-works/">How it works</a></li>
    <li><a href="{BASE}/pricing/">Pricing</a></li>
    <li><a href="{E(store_url(ct + "-footer"))}">Download on the App Store</a></li>
  </ul></div>
  <div><h4>Read</h4><ul>
    <li><a href="{BASE}/guides/">All guides</a></li>
    <li><a href="{BASE}/guides/how-to-stop-doomscrolling/">Stop doomscrolling</a></li>
    <li><a href="{BASE}/guides/how-to-block-tiktok-on-iphone/">Block TikTok on iPhone</a></li>
  </ul></div>
  <div><h4>Help and legal</h4><ul>
    <li><a href="{BASE}/support/">Support</a></li>
    <li><a href="{BASE}/privacy/">Privacy Policy</a></li>
    <li><a href="{BASE}/terms/">Terms of Use</a></li>
    <li><a href="{BASE}/delete-data/">Your data</a></li>
  </ul></div>
  <p class="legal">© {YEAR} {APP} · {COMPANY}. Pictures of the app on this site are drawings, and their numbers are examples. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. Other app names belong to their owners, and Pausely is not affiliated with them. Support in other languages: {languages}</p>
</div></footer>
</body>
</html>
"""
    return html


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

FAQ = [
    ("Will Pausely lock me out of my apps?",
     "No. An ordinary pause is a moment, not a wall. After it you choose: <kbd>I changed my mind</kbd>, or "
     "continue into the app for a few minutes. The only things with no way through are ones you set up yourself, "
     "such as a daily limit you have used, a block you started, or a rule that blocks an app during certain hours. "
     "Each of those ends on its own."),
    ("How is this different from Screen Time limits?",
     "A Screen Time limit waits until your time is used up and then offers <kbd>Ignore Limit</kbd>. Pausely steps "
     "in every time you open the app, before the scrolling starts, and asks for a breath first. "
     f'<a href="{BASE}/guides/why-screen-time-limits-dont-work/">The longer comparison.</a>'),
    ("Which apps does it work with?",
     "Any app on your iPhone or iPad. You pick them in Apple's own Screen Time picker, so it works with whichever "
     "ones take your time. Pausely never learns their names. Apple hands it private codes instead."),
    ("Does Pausely see what I do in other apps?",
     "No. It never sees your browsing, your messages or anything inside another app. iOS tells it how long the apps "
     "you chose have been open, and Pausely keeps those minutes on your device."),
    ("Is Pausely free?",
     "Yes, and free is a working product, not a demo: two apps protected, one rule, the breathing pause, your whole "
     "progress screen, today's time in each app you chose, and the countdown on the Lock Screen and in the Dynamic "
     "Island."),
    ("What does Premium add?",
     "Every app, website and category you choose, unlimited rules and daily limits, every kind of pause, Block "
     "everything, strict mode and Lock Pausely, time banners, your patterns, widgets, and the optional AI pauses. "
     f'<a href="{BASE}/pricing/">See the plans.</a>'),
    ("Do I need an account?",
     "No. There is no sign up, no email field and no password anywhere in the app."),
    ("Which devices does it need?",
     "An iPhone or iPad running iOS 17 or iPadOS 17, or newer. There is no Mac version, because the Screen Time "
     "frameworks Pausely is built on are not available there."),
]


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def home():
    from guides import GUIDES
    faq = [(q, a) for q, a in FAQ if not q.startswith("What does Premium add")]
    faq_html = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in faq)
    guide_rows = "".join(
        f'<li><a href="{BASE}/guides/{g["slug"]}/"><b>{g["title"]}</b><i>{g["minutes"]} min read</i>'
        f'<span>{g["blurb"]}</span></a></li>' for g in GUIDES[:3]
    )
    body = f"""<div class="hero">
<!--TOP-->
<main id="content">
<div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="kicker">For iPhone and iPad</p>
    <h1>Stop scrolling <em>on autopilot.</em></h1>
    <p class="lede">Pausely puts a ten second pause in front of the apps you open without thinking. Breathe first. Then decide if you still want to go in.</p>
    <div class="cta-row">
      {store("home-hero")}
      <p class="cta-note">Free to start.<br>No account.</p>
    </div>
  </div>
  <div class="hero-art">
    <div class="phone" role="img" aria-label="A drawing of Pausely's breathing pause: a circle that grows and shrinks with the words Breathe in, Hold, Breathe out.">
      <div class="breath">
        <span class="cap">A breath first</span>
        <div class="orb-box">
          <svg viewBox="0 0 100 100" aria-hidden="true"><circle class="track" cx="50" cy="50" r="46"/><circle class="run" cx="50" cy="50" r="46"/></svg>
          <div class="orb"></div>
        </div>
        <div>
          <div class="say" aria-hidden="true"><span class="in">Breathe in</span><span class="hold">Hold</span><span class="out">Breathe out</span></div>
          <div class="foot">Ten seconds. Then you choose.</div>
        </div>
      </div>
    </div>
  </div>
</div>
</main>
</div>

<section class="sec" id="how"><div class="wrap">
  <h2>One pause. <em>Then you choose.</em></h2>
  <ol class="how3">
    <li>
      <div class="n"><span>1 · You tap an app</span><i></i></div>
      <div class="pic p1" role="img" aria-label="{A_SHIELD}">{M_SHIELD}</div>
      <h3>Pausely steps in first</h3>
      <p>The app doesn't open straight away. You see how many times you have opened it today.</p>
    </li>
    <li>
      <div class="n"><span>2 · Ten seconds</span><i></i></div>
      <div class="pic p2" role="img" aria-label="{A_BREATH}">{M_BREATH}</div>
      <h3>You take a breath</h3>
      <p>In for four, hold for two, out for four. Long enough for the urge to pass.</p>
    </li>
    <li>
      <div class="n"><span>3 · Your call</span><i></i></div>
      <div class="pic p3" role="img" aria-label="{A_CHOICE}">{M_CHOICE}</div>
      <h3>You decide</h3>
      <p>Walk away and it counts as a win. Or go in for a few minutes, and the pause comes back after.</p>
    </li>
  </ol>
  <div class="trio">
    <div><b>10</b><span>seconds of breathing before a protected app opens.</span></div>
    <div><b>6</b><span>kinds of pause, from a breath to a question to answer.</span></div>
    <div><b>0</b><span>accounts. No sign up, no email, no password.</span></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2>Gentle by default. <em>Firm when you ask.</em></h2>
  <p class="intro">Most days a breath is enough. For the days it isn't, you can make Pausely hold.</p>
  <div class="two">
    <div><h3>Pick your pause</h3>{rows(PAUSES[:4])}</div>
    <div><h3>Make it hold</h3>{rows([HOLDS[0], HOLDS[1], HOLDS[2], HOLDS[3]])}</div>
  </div>
  <p><a class="more" href="{BASE}/how-it-works/">Everything Pausely does</a></p>
</div></section>

<section class="sec"><div class="wrap split">
  <div>
    <h2>See the time <em>come back.</em></h2>
    <p class="intro">Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.</p>
    <ul class="facts">
      <li><b>No account</b><span>Nothing to sign up for.</span></li>
      <li><b>Your apps stay private</b><span>Pausely can't read which apps you picked. Apple keeps that.</span></li>
      <li><b>On your device</b><span>Your time, your pauses and your journal stay on your phone.</span></li>
    </ul>
    <p class="fine"><a href="{BASE}/privacy/">What leaves the phone, exactly</a></p>
  </div>
  {TODAY}
</div></section>

<div class="light">
<section class="sec" id="pricing"><div class="wrap">
  <h2>Free to start. <em>Premium if you want more.</em></h2>
  <div class="plans">
    <div><h3>Free</h3><p class="price">No charge, no trial clock</p><ul>
      <li>Two apps protected</li>
      <li>The breathing pause and one rule</li>
      <li>Your whole progress screen</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">Monthly · Yearly · Lifetime · Family</p><ul>
      <li>Every app, website and category</li>
      <li>Every kind of pause, and daily limits</li>
      <li>Block everything, strict mode and Lock Pausely</li>
    </ul></div>
  </div>
  <p class="fine">What protects you keeps protecting you if a subscription ends. <a href="{BASE}/pricing/">Plans in full</a></p>
</div></section>

<section class="sec" id="faq"><div class="wrap">
  <h2>Questions people ask first</h2>
  <div class="faq">{faq_html}</div>
  <p class="fine">Something else? <a href="{BASE}/support/#faq">The full support page</a> covers setup, troubleshooting and how to reach us.</p>
</div></section>

<section class="sec"><div class="wrap">
  <h2>Guides, <em>with or without the app.</em></h2>
  <p class="intro">Plain instructions for the settings your iPhone already has, and honest notes on where they stop working.</p>
  <ul class="toc-list">{guide_rows}</ul>
  <p><a class="more" href="{BASE}/guides/">All guides</a></p>
</div></section>
</div>

<section class="closing"><div class="wrap">
  <h2>Take a breath <em>before the scroll.</em></h2>
  <div class="cta-row">
    {store("home-closing")}
    <p class="cta-note">iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.</p>
  </div>
</div></section>"""
    ld = [
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Pausely",
         "operatingSystem": "iOS 17 or later", "applicationCategory": "LifestyleApplication",
         "description": "An app for iPhone and iPad that puts a short pause in front of the apps you choose, "
                        "so opening them becomes a decision.",
         "url": SITE + "/", "downloadUrl": APP_STORE_URL,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": COMPANY}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq]},
    ]
    return layout("home", "/", "Pausely: Stop Scrolling on Autopilot. A Pause Before Your Apps.",
                  "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone and "
                  "iPad. Breathe first, then decide. Free to start, no account.",
                  body, ct="home", dark=True, jsonld=ld)


# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------

def how_it_works():
    def step(when, h, ps, cls, alt, pic):
        return (f'<li><div class="txt"><div class="when">{when}</div><h2>{h}</h2>'
                + "".join(f"<p>{p}</p>" for p in ps)
                + f'</div><div class="pic {cls}" role="img" aria-label="{alt}">{pic}</div></li>')

    setup_pic = ('<div class="m-list"><div class="on">Protection<span>On</span></div>'
                 '<div>Your apps<span>2 chosen</span></div><div>Pause<span>Deep breath</span></div></div>')
    window_pic = ('<div class="mini m-shield"><div class="num">4:32</div>'
                  '<small>Then the pause comes back.</small></div>')
    steps = "".join([
        step("Setup, once", "Choose the apps that take your time",
             ["Pick them in Apple's own picker. Two are free, and Premium covers every app, website and whole category you choose.",
              "Pausely uses Apple's Screen Time, the same system behind iOS's built in app limits. It asks for that permission once, and you can take it back in Settings at any time."],
             "p5", "A drawing of Pausely's Home: Protection on, two apps chosen, the pause set to Deep breath.", setup_pic),
        step("When you tap one", "The block screen comes first",
             ["Instead of the app, you see a number: how many times you have opened it today. No comment, no lecture. Only the number.",
              "Tap <kbd>Open Pausely</kbd> to take the pause, or <kbd>Never mind</kbd> to leave the app closed."],
             "p1", A_SHIELD, M_SHIELD),
        step("Ten seconds", "A pause before you go in",
             ["The breathing pause is the one everybody starts with: in for four seconds, hold for two, out for four.",
              "With Premium you can swap it for typing a short string, picking why you are opening the app, or reading a reminder. Or let Pausely pick a different one each time."],
             "p2", A_BREATH, M_BREATH),
        step("Then", "You choose, on purpose",
             ["<kbd>I changed my mind</kbd> closes it there, and Pausely counts the win.",
              "<kbd>Continue for 5 minutes</kbd> opens the app for a set time. Or take the third way out: one of the things you said you would rather do, such as a walk, a book or a glass of water, with a timer when you start it."],
             "p3", A_CHOICE, M_CHOICE),
        step("If you go in", "The time is yours, and it ends",
             ["A countdown runs on the Lock Screen and in the Dynamic Island while the app is open.",
              "When the time is up, the pause is back in front of the app. Nothing is taken from you. You are asked again."],
             "p6", "A drawing of a countdown: 4 minutes 32 seconds left, then the pause comes back.", window_pic),
        step("Over time", "Watch it add up",
             ["Progress shows pauses today, the times you walked away, the time saved, your streak and a chart of the week. All of it is free.",
              "Time per app shows today's minutes in the apps you chose. With Premium, Pausely also shows your patterns over four weeks."],
             "plain", "An example of today's numbers: 7 pauses today, 5 walked away, 38 minutes saved, a 6 day streak.",
             TODAY.replace(' role="img"', "").split(">", 1)[0].split(" aria-label")[0] + ">" + TODAY.split(">", 1)[1]),
    ])
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">How it works</p>
  <h1>A breath, <em>then a decision.</em></h1>
  <p class="lede">Pausely doesn't delete your apps or lock them away. It steps in at the moment you open one, asks for ten seconds, and lets you decide with a clear head.</p>
</div>
<div class="wrap"><ol class="steps">{steps}</ol></div>

<section class="sec" style="border-top:1px solid var(--line-d)"><div class="wrap">
  <h2>Gentle by default. <em>Firm when you ask.</em></h2>
  <p class="intro">Some days a breath is enough. Some weeks you want a boundary that holds. You choose how strict Pausely is.</p>
  <div class="two">
    <div><h3>Six kinds of pause</h3>{rows(PAUSES)}</div>
    <div><h3>Ways to make it hold</h3>{rows(HOLDS)}</div>
  </div>
  <p class="fine">The two AI pauses are off until you switch them on, and the Privacy Policy lists what they send. <a href="{BASE}/privacy/#ai">Read it</a></p>
</div></section>

<section class="sec"><div class="wrap">
  <h2>And around the pause</h2>
  {rows([
      ("Things to do instead", "free", "Pick up to three things you would rather do. They sit on the choice screen as a third way out. Premium has room for six."),
      ("A journal", "free", "For the times you would rather write than scroll. It stays on your device."),
      ("Time banners", "premium", "Every few minutes in an app you picked, a banner says how long you have spent in it today."),
      ("Short videos", "premium", "About how many short videos your time came to. An estimate, never a count."),
      ("Widgets and Siri", "premium", "Home Screen and Lock Screen widgets, Control Center buttons, Siri and Shortcuts."),
  ])}
</div></section>

<section class="sec"><div class="wrap">
  <h2>Setting it up takes <em>a few minutes.</em></h2>
  <ol class="setup">
    <li><span><b>Choose your apps.</b> Apple asks for Screen Time access on the same screen. Pausely can't work without it.</span></li>
    <li><span><b>Try your pause once,</b> so you know what is coming.</span></li>
    <li><span><b>Add things you would rather do.</b> A walk, a book, a glass of water, or something of your own.</span></li>
    <li><span><b>Allow notifications if you want them.</b> Pausely says why it uses them first.</span></li>
    <li><span><b>Done.</b> Open one of your apps and meet the pause.</span></li>
  </ol>
  <div class="cta-row" style="margin-top:34px">{store("how-it-works")}<p class="cta-note">Free to start.<br>iPhone and iPad, iOS 17 or newer.</p></div>
</div></section>
</main>"""
    return layout("how-it-works", "/how-it-works/", "How Pausely Works: A Pause Before the Apps You Overuse",
                  "Step by step: choose your apps, meet the block screen, take a ten second breath, then decide "
                  "whether to go in. Plus rules, daily limits and strict mode.", body, ct="how-it-works")


# ---------------------------------------------------------------------------
# Pricing
# ---------------------------------------------------------------------------

def pricing():
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">Pricing</p>
  <h1>Free is a working app, <em>not a demo.</em></h1>
  <p class="lede">Protect two apps for as long as you like. Premium is there when you want every app covered and firmer rules.</p>
</div>
<div class="wrap">
  <div class="plans" style="margin-top:0">
    <div><h3>Free</h3><p class="price">No charge, no trial clock</p><ul>
      <li>Two apps protected</li>
      <li>One rule</li>
      <li>The breathing pause</li>
      <li>The whole progress screen: pauses, wins, time saved, streak and chart</li>
      <li>Time per app</li>
      <li>The countdown on the Lock Screen and in the Dynamic Island</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">Everything in Free, plus</p><ul>
      <li>Every app, website and category you choose</li>
      <li>As many rules as you like, and daily limits</li>
      <li>Every kind of pause, and a pause that asks a little more when you keep reaching for the same app</li>
      <li>Block everything, strict mode and Lock Pausely</li>
      <li>Time banners and the short video estimate</li>
      <li>Your patterns, the mood insight and your week in words</li>
      <li>Room for six things to do instead</li>
      <li>Widgets, Control Center, Siri and Shortcuts</li>
      <li>The optional AI pauses, off until you turn them on</li>
    </ul></div>
  </div>

  <div class="table-scroll"><table class="price-table">
    <thead><tr><th>Premium plan</th><th>How it is billed</th><th>Good to know</th></tr></thead>
    <tbody>
      <tr><td>Monthly</td><td class="num">Every month</td><td>Cancel any time in your App Store settings.</td></tr>
      <tr><td>Yearly</td><td class="num">Every year</td><td>Starts with a free trial where one is offered.</td></tr>
      <tr><td>Lifetime</td><td class="num">One payment</td><td>No renewal.</td></tr>
      <tr><td>Family Yearly</td><td class="num">Every year</td><td>Shared through Apple's Family Sharing. Starts with a free trial where one is offered.</td></tr>
      <tr><td>Family Lifetime</td><td class="num">One payment</td><td>One payment for the whole family group.</td></tr>
    </tbody>
  </table></div>
  <p class="fine">The price for your country is shown in the app and on the App Store before you pay, in your own currency. Billing, refunds and cancellations are handled by Apple. <a href="{BASE}/terms/#subscriptions">Subscription terms</a></p>
</div>

<section class="sec" style="margin-top:clamp(48px,7vw,90px);border-top:1px solid var(--line-d)"><div class="wrap">
  <h2>The small print, <em>in plain words.</em></h2>
  <div class="faq">
    <details open><summary>What happens if my subscription ends?</summary><div><p>What protects you keeps protecting you. Every app you chose and every rule keeps running and stays editable, and the pause you chose keeps standing in front of your apps. Adding more closes, and so do the extras that show you things, such as widgets and time banners.</p></div></details>
    <details><summary>How do the family plans work?</summary><div><p>Family Yearly and Family Lifetime are shared through Apple's Family Sharing. Each person gets Premium in their own copy of Pausely, on their own device. Nobody sees anyone else's apps, numbers or journal.</p></div></details>
    <details><summary>Can I restore Premium on a new phone?</summary><div><p>Yes. Open the Premium screen in Pausely and tap <kbd>Restore purchases</kbd>. Premium belongs to your Apple Account, not to the device.</p></div></details>
    <details><summary>Are there ads in Pausely?</summary><div><p>No. Pausely shows no ads, and Premium is the only thing it sells.</p></div></details>
  </div>
  <div class="cta-row" style="margin-top:34px">{store("pricing")}<p class="cta-note">Start free.<br>Upgrade inside the app if you want to.</p></div>
</div></section>
</main>"""
    return layout("pricing", "/pricing/", "Pausely Pricing: Free Plan and Premium",
                  "Pausely is free for two apps, with the breathing pause and your progress screen. Premium adds "
                  "every app and website, every pause, daily limits and strict mode.", body, ct="pricing")


# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------

def guides_index():
    from guides import GUIDES
    rows_html = "".join(
        f'<li><a href="{BASE}/guides/{g["slug"]}/"><b>{g["title"]}</b><i>{g["minutes"]} min read</i>'
        f'<span>{g["blurb"]}</span></a></li>' for g in GUIDES
    )
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">Guides</p>
  <h1>Use your phone less, <em>without white knuckles.</em></h1>
  <p class="lede">Step by step instructions for the settings your iPhone already has, written by the people who make Pausely. Each guide starts with the free way and says plainly where it stops working.</p>
</div>
<div class="wrap" style="padding-bottom:clamp(56px,8vw,110px)">
  <ul class="toc-list" style="margin-top:0">{rows_html}</ul>
</div>
</main>"""
    return layout("guides", "/guides/", "Guides: Stop Doomscrolling and Block Apps on iPhone",
                  "Practical guides to blocking TikTok and Instagram on iPhone, stopping doomscrolling, and "
                  "making Screen Time limits hold.", body, ct="guides")


def guide_page(g):
    from guides import GUIDES
    others = [o for o in GUIDES if o["slug"] != g["slug"]][:3]
    rel = "".join(
        f'<li><a href="{BASE}/guides/{o["slug"]}/"><b>{o["title"]}</b><i>{o["minutes"]} min read</i></a></li>'
        for o in others
    )
    ct = "guide-" + g["ct"]
    appbox = f"""<aside class="appbox">
  <img src="{BASE}/apple-touch-icon.png" alt="" width="64" height="64">
  <div><b>{g["box_title"]}</b><p>{g["box_text"]}</p>{store(ct)}</div>
</aside>"""
    content = g["body"].format(BASE=BASE, ASSETS=ASSETS)
    body = f"""<main id="content">
<article class="article">
  <header>
    <p class="crumbs"><a href="{BASE}/guides/">Guides</a> / {g["topic"]}</p>
    <h1>{g["title"]}</h1>
    <p class="standfirst">{g["standfirst"]}</p>
    <p class="byline">By the Pausely team · Updated {UPDATED} · {g["minutes"]} min read</p>
  </header>
  <div class="prose">
{content}
{appbox}
  </div>
</article>
<div class="related"><h2>Keep reading</h2><ul class="toc-list">{rel}</ul></div>
</main>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
           "description": g["description"], "dateModified": UPDATED_ISO, "datePublished": UPDATED_ISO,
           "author": {"@type": "Organization", "name": "Pausely"},
           "publisher": {"@type": "Organization", "name": COMPANY},
           "mainEntityOfPage": SITE + f'/guides/{g["slug"]}/'}]
    return layout("guides", f'/guides/{g["slug"]}/', g["seo_title"], g["description"], body, ct=ct,
                  jsonld=ld, og_type="article")


# ---------------------------------------------------------------------------

def check(rel, html):
    """What a reader of these pages must never meet."""
    if "—" in html or "–" in html:
        raise SystemExit(f"{rel}: long dash in copy")
    low = strip_tags(html).lower()
    for claim in ("no tracking", "no analytics", "nothing leaves", "never leaves your phone", "scientifically"):
        if claim in low:
            raise SystemExit(f"{rel}: a claim the app cannot make: {claim!r}")


def build():
    """[(file, html, sitemap path or None)]"""
    from guides import GUIDES
    out = [
        ("index.html", home(), "/"),
        ("how-it-works/index.html", how_it_works(), "/how-it-works/"),
        ("pricing/index.html", pricing(), "/pricing/"),
        ("guides/index.html", guides_index(), "/guides/"),
    ]
    for g in GUIDES:
        out.append((f'guides/{g["slug"]}/index.html', guide_page(g), f'/guides/{g["slug"]}/'))
    for rel, html, _ in out:
        check(rel, html)
    return out


def copy_assets(out):
    """When building somewhere other than the repo root, bring the static files along."""
    if os.path.abspath(out) == ROOT:
        return
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"), dirs_exist_ok=True)
    for name in ("apple-touch-icon.png", "icon.png"):
        shutil.copy(os.path.join(ROOT, name), out)
