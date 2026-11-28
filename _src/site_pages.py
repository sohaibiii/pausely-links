# -*- coding: utf-8 -*-
"""The English home page, How it works, Pricing and the guides.

`gen.py` owns the support and legal pages in eight languages and calls `build()`
here at the end of its run. These pages are English only for now; their words
live in this file and in `guides.py`, their styles in `assets/site.css`.

Rules these pages keep, same as the app (CLAUDE.md in the app repo):
  * only features the app has, named the way its screens name them;
  * nothing scolds anyone for the time they spend on their phone;
  * no borrowed press or reviews, and no claim that the app sends nothing
    anywhere (the Privacy Policy says exactly what leaves);
  * one study is cited, on the home page, and only this way: its own figures,
    its source, that it tested another app and not Pausely, and that one of
    its authors makes that app. Nothing here is called proven;
  * the short video figure is an estimate and always says "about";
  * drawings of the app are drawings, and example numbers say they are examples;
  * the app is on iPhone, iPad and Android, and the three are not the same: anything
    only one of them does says which (the floating reels card is Android's, the
    Dynamic Island is the iPhone's), and nothing is promised for a Mac;
  * no long dashes in copy.
"""
import hashlib
import json
import os
import re
import shutil
import urllib.parse

import analytics
import gen
import i18n
from i18n import t
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

# The stylesheet is cached for a year (see `_headers`), so its address carries a
# hash of its contents: change the file and every page asks for a new one.
with open(os.path.join(ROOT, "assets", "site.css"), "rb") as _f:
    CSS_VERSION = hashlib.sha256(_f.read()).hexdigest()[:10]

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": COMPANY, "url": SITE + "/",
       "logo": SITE + "/apple-touch-icon.png", "email": EMAIL}


def crumbs(*trail):
    """A breadcrumb trail from the home page: crumbs(("Guides", "/guides/"), ...)."""
    items = [("Home", "/")] + list(trail)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": name, "item": SITE + path}
        for i, (name, path) in enumerate(items, 1)]}


APPLE = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.2 1.8-3.26 '
         '1.88-3.31-1.02-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 '
         '2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.85-.71 1.33 0 1.71.71 '
         '2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.2 '
         '6.13c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.7-.93 2.7.98.08 1.98-.5 2.59-1.24z"/></svg>')


# The Android app (Google Play, live since November 2026).
PLAY_ID = "com.social.pausely"
PLAY_URL = "https://play.google.com/store/apps/details?id=" + PLAY_ID

PLAY = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path fill="#00D7FE" d="M3.5 1.9c-.3.3-.4.8-.4 1.3v17.6c0 .5.1 1 .4 1.3L13.4 12z"/>'
        '<path fill="#00F076" d="M16.7 8.6 5.2 2c-.7-.4-1.3-.4-1.7-.1L13.4 12z"/>'
        '<path fill="#FF3A44" d="M16.7 15.4 13.4 12l-9.9 10.1c.4.3 1 .3 1.7-.1z"/>'
        '<path fill="#FFCE00" d="m16.7 15.4 4-2.3c1.1-.6 1.1-1.6 0-2.2l-4-2.3-3.3 3.4z"/></svg>')


def store_url(ct):
    if PROVIDER_TOKEN:
        return f"{APP_STORE_URL}?pt={PROVIDER_TOKEN}&ct={ct}&mt=8"
    return APP_STORE_URL


def play_url(ct):
    """Google Play, with the page that sent the visitor in the install referrer."""
    ref = urllib.parse.quote(f"utm_source={gen.DOMAIN or 'website'}&utm_medium=website&utm_campaign={ct}", safe="")
    return f"{PLAY_URL}&referrer={ref}"


def store(ct):
    """Both shops, side by side. On an Android phone the page puts Google Play first."""
    return (f'<span class="stores"><a class="store" href="{E(store_url(ct))}">{APPLE}'
            f'<span><small>{t("Download on the")}</small><b>App Store</b></span></a>'
            f'<a class="store play" href="{E(play_url(ct))}">{PLAY}'
            f'<span><small>{t("Get it on")}</small><b>Google Play</b></span></a></span>')


# On an Android phone, "Get the app" goes to Google Play and its button comes first.
ANDROID_JS = ('<script>(function(){if(!/Android/i.test(navigator.userAgent))return;'
              'document.documentElement.className+=" android";'
              'var a=document.querySelectorAll("a[data-play]");'
              'for(var i=0;i<a.length;i++)a[i].href=a[i].getAttribute("data-play")})();</script>')


# Drawings of the app's screens, in the app's own words (its Localizable strings
# when the page is translated).
def drawings():
    m_shield = (f'<div class="mini m-shield"><div class="num">12</div><b>{t("Opens today")}</b>'
                f'<div class="btns"><span>{t("Open Pausely")}</span><span>{t("Never mind")}</span></div></div>')
    m_breath = (f'<div class="mini m-breath"><div class="o"></div><b>{t("Breathe in")}</b>'
                f'<small>{t("Ten seconds of breathing before you continue.")}</small></div>')
    m_choice = (f'<div class="mini m-choice"><b>{t("You paused.")}</b>'
                f'<div class="btns"><span>{t("I changed my mind")}</span><span>{t("Or walk for 10 minutes")}</span>'
                f'<span>{t("Continue for 5m")}</span></div></div>')
    a_shield = t("A drawing of the block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind.")
    a_breath = t("A drawing of the breathing pause: a soft circle and the words Breathe in.")
    a_choice = t("A drawing of the choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, "
                 "Continue for 5 minutes.")
    return m_shield, m_breath, m_choice, a_shield, a_breath, a_choice


# The Android app's floating card ("Reels & time"), in its own words and in the
# corner it starts in. The player behind it is a made-up app (called Clips, the
# name the app's own examples use): its layout is the one every short-video app
# shares, with no real app's name or logo. The clips are stock footage whose
# licence allows this use (see REEL_CLIPS), never somebody's
# real post, and the names and numbers on them are invented.
_ICON = {
    "up": '<path d="M2 10h4v11H2zM8 21h9.3a2 2 0 0 0 1.9-1.4l2.6-7.8A2 2 0 0 0 19.9 9H14l.8-4.2a1.9 1.9 0 0 0-3.4-1.4L8 9.5z"/>',
    "down": '<path transform="rotate(180 12 12)" d="M2 10h4v11H2zM8 21h9.3a2 2 0 0 0 1.9-1.4l2.6-7.8A2 2 0 0 0 19.9 9H14l.8-4.2a1.9 1.9 0 0 0-3.4-1.4L8 9.5z"/>',
    "say": '<path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/>',
    "send": '<path d="M14 4l8 7.5-8 7.5v-4.6C8.5 14.4 4.9 16 2 20c.8-6 4.3-10.6 12-11.5z"/>',
    "home": '<path d="M12 3l9 8h-2.5v9h-5v-6h-3v6h-5v-9H3z"/>',
    "clips": '<path d="M7 2h10a3 3 0 0 1 3 3v14a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3zm3 6.5v7l6-3.5z"/>',
    "plus": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1 5h2v4h4v2h-4v4h-2v-4H7v-2h4z"/>',
    "subs": '<path d="M6 3h12v2H6zM4 7h16v2H4zm-1 4h18a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1zm7 2.5v5l4.5-2.5z"/>',
    "you": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 4a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zm0 14a8 8 0 0 1-6-2.7c1.2-2 3.4-3.3 6-3.3s4.8 1.3 6 3.3A8 8 0 0 1 12 20z"/>',
}


def _ic(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{_ICON[name]}</svg>'


# Where the clip plays from, who posted it, the line under the name, likes,
# comments. The clips are Mixkit's (Stock Video Free License: commercial use,
# no credit needed) and play straight from Mixkit's own address. The names,
# lines and numbers are invented.
_MIXKIT = "https://assets.mixkit.co"
REEL_CLIPS = [
    (_MIXKIT + "/videos/12171/12171-720.mp4", "Kitchen diaries", "The easiest weeknight dinner", "24K", "312"),
    (_MIXKIT + "/videos/1548/1548-720.mp4", "Dog days", "He heard the word walk", "108K", "1.2K"),
    (_MIXKIT + "/videos/51500/51500-720.mp4", "Somewhere south", "Found this beach by accident", "9.4K", "87"),
    (_MIXKIT + "/active_storage/video_items/100357/1723573133/100357-video-720.mp4", "Sweet shift", "Sprinkles, in slow motion", "61K", "540"),
    (_MIXKIT + "/active_storage/video_items/100490/1724285970/100490-video-720.mp4", "Studio hours", "Day 12 of painting every day", "15K", "203"),
]


def _reel(clip, n):
    f, who, line, likes, says = clip
    return (f'<div class="rv rv{n}">'
            f'<video muted loop playsinline preload="none" src="{E(f)}"></video>'
            f'<span class="rail"><span>{_ic("up")}<b>{likes}</b></span><span>{_ic("down")}<b>{t("Dislike")}</b></span>'
            f'<span>{_ic("say")}<b>{says}</b></span><span>{_ic("send")}<b>{t("Share")}</b></span></span>'
            f'<span class="cap"><span class="who"><i>{E(who[0])}</i><b>{E(who)}</b><em>{t("Follow")}</em></span>'
            f'<span class="line">{E(t(line))}</span><span class="snd">♪ {t("Original sound")}</span></span>'
            f'<i class="prog"></i></div>')


_REEL_TRACK = REEL_CLIPS + REEL_CLIPS[:1]   # the first again, so the feed can loop
def reels():
    """The phone in the reels section, in the page's language."""
    return f"""<div class="phone droid" id="reels" role="img" data-nosnippet aria-label="{E(t("An Android phone playing short videos in a made-up app. In the top right corner Pausely's floating card reads 00:42, 12 reels, this visit, estimated. Example numbers."))}">
  <div class="reel-screen">
    <div class="rview"><div class="rf" style="height:{len(_REEL_TRACK) * 100}%">{"".join(_reel(c, n) for n, c in enumerate(_REEL_TRACK))}</div></div>
    <div class="rnav"><span>{_ic("home")}<b>{t("Home")}</b></span><span class="on">{_ic("clips")}<b>{t("Clips")}</b></span><span class="add">{_ic("plus")}</span><span>{_ic("subs")}<b>{t("Following")}</b></span><span>{_ic("you")}<b>{t("You")}</b></span></div>
    <div class="rbadge"><span><b><span class="rb-time">00:42</span> · <span class="rb-count">12</span> {t("reels")}</b><small>{t("This visit · estimated")}</small></span><i class="x"></i></div>
  </div>
</div>"""
REELS_JS = ('<script>(function(){var r=document.getElementById("reels");'
            'if(!r||!window.IntersectionObserver)return;'
            'var t=r.querySelector(".rb-time"),c=r.querySelector(".rb-count"),f=r.querySelector(".rf"),b=r.querySelector(".rbadge"),'
            'v=r.querySelectorAll(".rv"),N=v.length,s=42,n=12,i=0,on=false;'
            'function vid(k){return v[k].querySelector("video")}'
            # nothing is fetched until the phone is nearly in view; then the first picture
            'new IntersectionObserver(function(e,o){if(e[0].isIntersecting){o.disconnect();var m=vid(0);m.preload="metadata";m.load()}},{rootMargin:"500px"}).observe(r);'
            'if(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches)return;'
            'function two(x){return(x<10?"0":"")+x}'
            # play the clip in view from its start, stop the rest, and fetch the next one early
            'function show(k,keep){for(var j=0;j<N;j++){var m=vid(j);if(j===k){v[j].classList.add("on");'
            'if(!keep){try{m.currentTime=0}catch(e){}}var p=m.play();if(p&&p.catch)p.catch(function(){})}'
            'else{v[j].classList.remove("on");m.pause()}}'
            'if(k>=0&&k<N-1){var x=vid(k+1);if(x.preload!=="auto"){x.preload="auto";if(!x.readyState)x.load()}}}'
            'function go(k,jump){f.style.transition=jump?"none":"";f.style.transform="translateY(-"+k*100/N+"%)"}'
            'function tick(){if(!on)return;s++;'
            'if(s>=150){s=42;n=12}'
            't.textContent=two(Math.floor(s/60))+":"+two(s%60);'
            'if(s%3===0){i++;n++;c.textContent=n;go(i);show(i);'
            'b.classList.remove("bump");void b.offsetWidth;b.classList.add("bump");'
            # the last clip is the first again: once it has slid in, swap to the real first
            'if(i===N-1)setTimeout(function(){try{vid(0).currentTime=vid(N-1).currentTime}catch(e){}i=0;go(0,true);show(0,true)},600)}}'
            'new IntersectionObserver(function(e){on=e[0].isIntersecting;show(on?i:-1,true)},{threshold:.3}).observe(r);'
            'setInterval(tick,1000)})();</script>')


def shot(img, alt, lazy=True):
    load = ' loading="lazy" decoding="async"' if lazy else ""
    return (f'<figure class="phone"><img src="{ASSETS}/img/{img}.webp" alt="{E(alt)}" width="660" height="1435"'
            f'{load}></figure>')


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


def layout(key, path, title, description, body, *, ct, dark=False, jsonld=(), og_type="website", alternates=(),
           head=""):
    """One page. `path` is its address under the site root, `ct` its campaign name.

    `alternates` are (language, path) pairs for a page that exists in more than one
    language (only the home page so far). While `i18n.use()` has picked a language
    other than English, the page is built in that language with a slimmer header and
    footer, because the other English-only pages have no translation to link to.
    """
    lang = i18n.current()
    prefix, home_path = i18n.HOMES[lang][0], i18n.HOMES[lang][1]
    W = gen.copy_for(lang) if lang != "en" else None
    url = SITE + path
    current = ' aria-current="page"'
    if lang == "en":
        nav = "".join(
            f'<a href="{BASE}{p}"{current if k == key else ""}>{label}</a>' for k, label, p in NAV
        )
    else:
        nav = f'<a href="{BASE}{prefix}/">{W["nav.support"]}</a>'
    play = E(play_url(ct + "-nav"))
    get = f'<a class="get" href="{E(store_url(ct + "-nav"))}" data-play="{play}">{t("Get the app")}</a>'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in jsonld)
    brand = f'<a class="brand" href="{BASE}{home_path}"><img src="{BASE}/icon.png" alt="" width="32" height="32">{APP}</a>'
    top = f"""<header class="top"><div class="wrap">
  {brand}
  <a class="get get-m" href="{E(store_url(ct + "-nav"))}" data-play="{play}">{t("Get the app")}</a>
  <nav aria-label="{t("Pages")}">{nav}{get}</nav>
</div></header>"""
    languages = " · ".join(
        f'<a href="{BASE}{p}{gen.path_of(c, "support")}" lang="{c}" hreflang="{c}">{E(gen.NATIVE_NAME[c])}</a>'
        for c, p in gen.LANGUAGES if c != lang
    )
    this_page = ""
    if alternates:
        this_page = t("This page in:") + " " + " · ".join(
            f'<a href="{BASE}{p}" lang="{c}" hreflang="{c}">{E(gen.NATIVE_NAME[c])}</a>'
            for c, p in alternates if c != lang
        ) + ". "
    hreflang = "".join(
        f'<link rel="alternate" hreflang="{c}" href="{E(SITE + p)}">\n' for c, p in alternates
    ) + (f'<link rel="alternate" hreflang="x-default" href="{E(SITE + dict(alternates)["en"])}">\n' if alternates else "")
    if lang == "en":
        footer = f"""<footer><div class="wrap">
  <div class="who">
    {brand}
    <p>A breath before the scroll. Made by {COMPANY}. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> and a person will reply.</p>
  </div>
  <div><p class="fh">The app</p><ul>
    <li><a href="{BASE}/how-it-works/">How it works</a></li>
    <li><a href="{BASE}/pricing/">Pricing</a></li>
    <li><a href="{E(store_url(ct + "-footer"))}">Download on the App Store</a></li>
    <li><a href="{E(play_url(ct + "-footer"))}">Get it on Google Play</a></li>
  </ul></div>
  <div><p class="fh">Read</p><ul>
    <li><a href="{BASE}/guides/">All guides</a></li>
    <li><a href="{BASE}/guides/how-to-stop-doomscrolling/">Stop doomscrolling</a></li>
    <li><a href="{BASE}/guides/how-to-block-tiktok-on-iphone/">Block TikTok on iPhone</a></li>
  </ul></div>
  <div><p class="fh">Help and legal</p><ul>
    <li><a href="{BASE}/support/">Support</a></li>
    <li><a href="{BASE}/privacy/">Privacy Policy</a></li>
    <li><a href="{BASE}/terms/">Terms of Use</a></li>
    <li><a href="{BASE}/delete-data/">Your data</a></li>{analytics.footer_link(BASE)}
  </ul></div>
  <p class="legal">© {YEAR} {APP} · {COMPANY}. Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. Android and Google Play are trademarks of Google LLC. TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed by them or by any other app named or shown here. {this_page}Support in other languages: {languages}</p>
</div></footer>"""
    else:
        footer = f"""<footer><div class="wrap">
  <div class="who">
    {brand}
    <p>{t("A breath before the scroll. Made by {company}. Write to {email} and a person will reply.").format(company=COMPANY, email=f'<a href="mailto:{EMAIL}">{EMAIL}</a>')}</p>
  </div>
  <div><p class="fh">{t("The app")}</p><ul>
    <li><a href="{E(store_url(ct + "-footer"))}">{t("Download on the App Store")}</a></li>
    <li><a href="{E(play_url(ct + "-footer"))}">{t("Get it on Google Play")}</a></li>
  </ul></div>
  <div><p class="fh">{t("Help and legal")}</p><ul>
    <li><a href="{BASE}{prefix}/">{W["nav.support"]}</a></li>
    <li><a href="{BASE}{prefix}/privacy/">{W["nav.privacy"]}</a></li>
    <li><a href="{BASE}{prefix}/terms/">{W["nav.terms"]}</a></li>
    <li><a href="{BASE}{prefix}/delete-data/">{W["nav.data"]}</a></li>{analytics.footer_link(BASE)}
  </ul></div>
  <p class="legal">© {YEAR} {APP} · {COMPANY}. {t("Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. Android and Google Play are trademarks of Google LLC. TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed by them or by any other app named or shown here.")} {this_page}{t("Support in other languages:")} {languages}</p>
</div></footer>"""
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
<link rel="canonical" href="{E(url)}">
{hreflang}<meta name="robots" content="{gen.ROBOTS}">
<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}">
<meta name="theme-color" content="{'#183139' if dark else '#0A1216'}">
<meta property="og:site_name" content="{APP}">
<meta property="og:locale" content="{i18n.HOMES[lang][2]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{E(url)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{E(t("Pausely: a pause before the apps you open without thinking."))}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/icon.png" type="image/png">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<link rel="preload" href="{ASSETS}/fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ASSETS}/site.css?v={CSS_VERSION}">
{head}{ld}
{analytics.head()}</head>
<body class="{'' if dark else 'on-light'}">
<a class="skip" href="#content">{t("Skip to content")}</a>
{'' if dark else top}
{body.replace('<!--TOP-->', top) if dark else body}
{footer}
{analytics.banner(BASE, prefix)}{ANDROID_JS}</body>
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
     "Any app on your phone, so it works with whichever ones take your time. On iPhone and iPad you pick them in "
     "Apple's own Screen Time picker, and Pausely never learns their names: Apple hands it private codes instead. "
     "On Android you pick them from the list of apps on your phone."),
    ("Does Pausely see what I do in other apps?",
     "On iPhone and iPad, no. It never sees your browsing, your messages or anything inside another app. iOS tells "
     "it how long the apps you chose have been open, and Pausely keeps those minutes on your device. On Android, "
     "Pausely uses the Accessibility service to see which app is in front. It never reads your messages or what "
     "you type, and never taps or types for you. In Chrome and a few other browsers it also sees the address of "
     "the site you open, so it can pause the sites you chose. It asks first, and explains all of this before you "
     "say yes."),
    ("Is Pausely free?",
     "Yes, and free is a working product, not a demo: two apps protected, one rule, the breathing pause and your "
     "whole progress screen. On iPhone and iPad it also covers today's time in each app you chose, and the "
     "countdown on the Lock Screen and in the Dynamic Island."),
    ("What does Premium add?",
     "Every app, website and category you choose, unlimited rules and daily limits, every kind of pause, Block "
     "everything, strict mode and Lock Pausely, time banners on iPhone, the floating reels card on Android, your "
     "patterns, widgets, and the optional AI pauses. "
     f'<a href="{BASE}/pricing/">See the plans.</a>'),
    ("Do I need an account?",
     "No. There is no sign up, no email field and no password anywhere in the app."),
    ("Which devices does it need?",
     "An iPhone or iPad running iOS 17 or iPadOS 17 or newer, or an Android phone running Android 8 or newer. "
     "There is no Mac version."),
]


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def home():
    from guides import GUIDES
    lang = i18n.current()
    prefix, home_path = i18n.HOMES[lang][0], i18n.HOMES[lang][1]
    support = BASE + prefix + gen.path_of(lang, "support")
    M_SHIELD, M_BREATH, M_CHOICE, A_SHIELD, A_BREATH, A_CHOICE = drawings()
    if lang == "en":
        faq = [(q, a) for q, a in FAQ if not q.startswith("What does Premium add")]
    else:
        faq = i18n.faq()
    faq_html = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in faq)
    guide_rows = "".join(
        f'<li><a href="{BASE}/guides/{g["slug"]}/"><b>{g["title"]}</b><i>{g["minutes"]} min read</i>'
        f'<span>{g["blurb"]}</span></a></li>' for g in GUIDES[:3]
    )
    guides = f"""
<section class="sec"><div class="wrap">
  <h2>Guides, <em>with or without the app.</em></h2>
  <p class="intro">Plain instructions for the settings your iPhone already has, and honest notes on where they stop working.</p>
  <ul class="toc-list">{guide_rows}</ul>
  <p><a class="more" href="{BASE}/guides/">All guides</a></p>
</div></section>""" if lang == "en" else ""
    # Links to pages that exist only in English stay on the English home page.
    def en_link(href, text):
        return f' <a href="{BASE}{href}">{text}</a>' if lang == "en" else ""
    # The recording and the screenshots are of the English app. A translated page says so.
    shots_note = (t("Screens from the iPhone app, showing its demo data.") if lang == "en" else
                  t("Screens from the English iPhone app, showing its demo data. The app itself is in your language."))
    body = f"""<div class="hero">
<!--TOP-->
<main id="content">
<div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="kicker">{t("For iPhone, iPad and Android")}</p>
    <h1>{t("Stop scrolling <em>on autopilot.</em>")}</h1>
    <p class="lede">{t("Pausely puts a short pause in front of TikTok, Instagram or any app you open without thinking. Breathe first. Then decide if you still want to go in.")}</p>
    <div class="cta-row">
      {store("home-hero")}
      <p class="cta-note">{t("Free to start.<br>No account.")}</p>
    </div>
  </div>
  <div class="hero-art">
    <div class="phone">
      <video id="demo" autoplay muted loop playsinline preload="metadata" width="600" height="1300" poster="{ASSETS}/video/demo-poster.jpg" aria-label="{E(t("A screen recording style demo: someone taps TikTok on the Home Screen. Pausely steps in and shows 12 opens today. A breathing pause follows, then a pause where you type a short code, then the choice screen: You paused."))}">
        <source src="{ASSETS}/video/demo.mp4" type="video/mp4">
      </video>
    </div>
    <script>(function(){{var v=document.getElementById("demo");if(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches){{v.removeAttribute("autoplay");v.pause();v.controls=true}}}})();</script>
  </div>
</div>
</main>
</div>

<section class="sec" id="how"><div class="wrap">
  <h2>{t("One pause. <em>Then you choose.</em>")}</h2>
  <ol class="how3">
    <li>
      <div class="n"><span>{t("1 · You tap an app")}</span><i></i></div>
      <div class="pic p1" role="img" aria-label="{E(A_SHIELD)}">{M_SHIELD}</div>
      <h3>{t("Pausely steps in first")}</h3>
      <p>{t("The app doesn't open straight away. You see how many times you have opened it today.")}</p>
    </li>
    <li>
      <div class="n"><span>{t("2 · Ten seconds")}</span><i></i></div>
      <div class="pic p2" role="img" aria-label="{E(A_BREATH)}">{M_BREATH}</div>
      <h3>{t("You take a breath")}</h3>
      <p>{t("In for four, hold for two, out for four. Long enough for the urge to pass.")}</p>
    </li>
    <li>
      <div class="n"><span>{t("3 · Your call")}</span><i></i></div>
      <div class="pic p3" role="img" aria-label="{E(A_CHOICE)}">{M_CHOICE}</div>
      <h3>{t("You decide")}</h3>
      <p>{t("Walk away and it counts as a win. Or go in for a few minutes, and the pause comes back after.")}</p>
    </li>
  </ol>
  <div class="trio">
    <div><b>10</b><span>{t("seconds of breathing before a protected app opens.")}</span></div>
    <div><b>6</b><span>{t("kinds of pause, from a breath to a question to answer.")}</span></div>
    <div><b>0</b><span>{t("accounts. No sign up, no email, no password.")}</span></div>
  </div>
</div></section>

<section class="sec" id="research"><div class="wrap">
  <h2>{t("Does a pause work? <em>It has been tested.</em>")}</h2>
  <p class="intro">{t("In 2023, researchers published a six week study of 280 people using an app that works this way: a short wait before the app opens, then a way to change your mind.")}</p>
  <div class="trio">
    <div><b>36%</b><span>{t("of the time, people closed the app again after the pause.")}</span></div>
    <div><b>37%</b><span>{t("fewer attempts to open those apps by week six than in week one.")}</span></div>
    <div><b>57%</b><span>{t("fewer times those apps were actually opened after six weeks.")}</span></div>
  </div>
  <p class="fine">{t('A second experiment with 500 people looked at which part did the work. The way to back out helped most, and the wait helped too. Pausely gives you both: the pause, then "I changed my mind".')}</p>
  <p class="fine">{t("The study tested another app that pauses you the same way, not Pausely, and one of its three authors makes that app. Pausely has not been in a study of its own, so read these as what the method did there, not as a promise. Source: Grüning, Riedel and Lorenz-Spreen, {paper}, PNAS, 2023.").format(paper='<a href="https://doi.org/10.1073/pnas.2213114120" rel="noopener">Directing smartphone use through the self-nudge app one sec</a>')}</p>
</div></section>

<section class="sec" id="pauses"><div class="wrap">
  <h2>{t("Six kinds of pause. <em>Pick yours.</em>")}</h2>
  <p class="intro">{t("A breath is the pause everybody starts with, and it is free. With Premium you can pick another, or let Pausely choose a different one each time.")}</p>
  <ol class="strip six">
    <li>{shot("breathing", t("The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown."))}<h3>{t("Breathe")} <i class="tag free">{t("Free")}</i></h3><p>{t("Ten seconds, with a circle to follow.")}</p></li>
    <li>{shot("typing", t("The typing pause: Type this to continue, with twenty characters to type and a field that says Type here."))}<h3>{t("Type")} <i class="tag">Premium</i></h3><p>{t("Twenty characters. Hard to do on autopilot.")}</p></li>
    <li>{shot("intention", t("The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit."))}<h3>{t("Say why")} <i class="tag">Premium</i></h3><p>{t("One tap on the reason that fits.")}</p></li>
    <li>{shot("reminder", t("The reminder pause: a short line to read under the label On being here, with a bar that fills while you read, and Show me another."))}<h3>{t("Read a line")} <i class="tag">Premium</i></h3><p>{t("A reminder from Pausely, or one you wrote yourself.")}</p></li>
    <li>{shot("question", t("The question pause: One question. One try. Which of these rivers runs through the middle of the capital city? Four answers and an Answer button."))}<h3>{t("Answer a question")} <i class="tag">Premium</i></h3><p>{t("One question about where you live. One try.")}</p></li>
    <li>{shot("reflect", t("The reflection pause: you said Just checking, and Pausely asks What would make the next hour feel like it went well?"))}<h3>{t("Reflect")} <i class="tag">Premium</i></h3><p>{t("Say why you are here. Get one gentle question back.")}</p></li>
  </ol>
  <p class="strip-hint">{t("Swipe to see all six.")}</p>
  <p class="fine">{shots_note} {t("The Android app has the same pauses, though a new one can reach it a little later. The last two are written by AI and stay off until you turn AI pauses on.")} <a href="{BASE}{prefix}/privacy/#ai">{t("What they send")}</a></p>
  <p class="fine">{t("After any pause you choose: stop there, do something else, or go in for a few minutes. Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.")}{en_link("/how-it-works/", "Everything Pausely does")}</p>
</div></section>

<section class="sec" id="reels-count"><div class="wrap reels-split">
  <div class="reels-head">
    <h2>{t("How many reels <em>was that?</em>")}</h2>
    <p class="intro">{t("It is easy to lose count of short videos. Pausely keeps a rough count for you, and shows it while you are still scrolling.")}</p>
  </div>
  <div class="reels-art">{reels()}<p class="plat">{t("<b>This is Android.</b> On iPhone you get a banner every few minutes instead, with about how many short videos you watched.")}</p><p class="eg">{t("A made-up app playing stock clips from Mixkit. Example numbers.")}</p></div>
  <ul class="facts">
    <li><b>{t("On Android")}</b><span>{t("A small card floats over the apps you pick. It shows how long this visit has lasted and about how many videos went by. One tap hides it.")}</span></li>
    <li><b>{t("On iPhone")}</b><span>{t("iOS doesn't let one app draw over another, so Pausely sends a banner every few minutes: your time in the app today, and about how many short videos that comes to.")}</span></li>
    <li><b>{t("An estimate")}</b><span>{t("Some videos can be missed, and not every feed can be counted. The timer keeps going either way.")}</span></li>
    <li><b>{t("Yours to turn on")}</b><span>{t("Part of Premium, and off until you switch it on. The totals stay on your phone.")}</span></li>
  </ul>
</div></section>
{REELS_JS}

<section class="sec"><div class="wrap split">
  <div>
    <h2>{t("See the time <em>come back.</em>")}</h2>
    <p class="intro">{t("Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.")}</p>
    <ul class="facts">
      <li><b>{t("No account")}</b><span>{t("Nothing to sign up for.")}</span></li>
      <li><b>{t("Your apps stay private")}</b><span>{t("On iPhone, Pausely can't even read which apps you picked. Apple keeps that.")}</span></li>
      <li><b>{t("On your device")}</b><span>{t("Your time, your pauses and your journal stay on your phone.")}</span></li>
    </ul>
    <p class="fine"><a href="{BASE}{prefix}/privacy/">{t("What leaves the phone, exactly")}</a></p>
  </div>
  <div class="proof">{shot("progress", t("Pausely's Progress screen: 1 hour 48 minutes reclaimed this week, and a bar chart of the last seven days."))}<p class="eg">{t("The app's demo data.")}</p></div>
</div></section>

<div class="light">
<section class="sec" id="pricing"><div class="wrap">
  <h2>{t("Free to start. <em>Premium if you want more.</em>")}</h2>
  <div class="plans">
    <div><h3>{t("Free")}</h3><p class="price">{t("No charge, no trial clock")}</p><ul>
      <li>{t("Two apps protected")}</li>
      <li>{t("The breathing pause and one rule")}</li>
      <li>{t("Your whole progress screen")}</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">{t("Monthly · Yearly · Lifetime · Family")}</p><ul>
      <li>{t("Every app, website and category")}</li>
      <li>{t("Every kind of pause, and daily limits")}</li>
      <li>{t("Block everything, strict mode and Lock Pausely")}</li>
    </ul></div>
  </div>
  <p class="fine">{t("What protects you keeps protecting you if a subscription ends.")}{en_link("/pricing/", "Plans in full")}</p>
</div></section>

<section class="sec" id="faq"><div class="wrap">
  <h2>{t("Questions people ask first")}</h2>
  <div class="faq">{faq_html}</div>
  <p class="fine">{t('Something else? <a href="{support}">The full support page</a> covers setup, troubleshooting and how to reach us.').format(support=support + "#faq")}</p>
</div></section>{guides}
</div>

<section class="closing"><div class="wrap">
  <h2>{t("Take a breath <em>before the scroll.</em>")}</h2>
  <div class="cta-row">
    {store("home-closing")}
    <p class="cta-note">{t("iPhone, iPad and Android.<br>English and seven other languages.")}</p>
  </div>
</div></section>"""
    ld = [
        ORG,
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Pausely",
         "operatingSystem": "iOS, Android", "applicationCategory": "LifestyleApplication",
         "image": SITE + "/apple-touch-icon.png",
         "description": t("An app for iPhone, iPad and Android that puts a short pause in front of the apps you "
                          "choose, so opening them becomes a decision."),
         "inLanguage": lang,
         "url": SITE + home_path, "downloadUrl": [APP_STORE_URL, PLAY_URL],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": ORG},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq]},
    ]
    if lang == "en":
        ld.insert(0, {"@context": "https://schema.org", "@type": "WebSite", "name": APP, "alternateName": "Pausely app",
                      "url": SITE + "/"})
    alternates = [(c, i18n.HOMES[c][1]) for c in ["en"] + i18n.LANGS]
    return layout("home", home_path, t("Pausely: Stop Scrolling on Autopilot, Pause Before You Open"),
                  t("Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone, iPad "
                    "and Android. Breathe first, then decide. Free to start."),
                  body, ct="home" if lang == "en" else "home-" + lang, dark=True, jsonld=ld, alternates=alternates,
                  head=i18n.HEAD_CSS.get(lang, ""))


# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------

def how_it_works():
    def step(when, h, ps, cls, alt, pic):
        return (f'<li><div class="txt"><div class="when">{when}</div><h2>{h}</h2>'
                + "".join(f"<p>{p}</p>" for p in ps)
                + (f'</div><div class="pic {cls}">{pic}</div></li>' if cls == "shot" else
                   f'</div><div class="pic {cls}" role="img" aria-label="{alt}">{pic}</div></li>'))

    setup_pic = ('<div class="m-list"><div class="on">Protection<span>On</span></div>'
                 '<div>Your apps<span>2 chosen</span></div><div>Pause<span>Deep breath</span></div></div>')
    window_pic = ('<div class="mini m-shield"><div class="num">4:32</div>'
                  '<small>Then the pause comes back.</small></div>')
    steps = "".join([
        step("Setup, once", "Choose the apps that take your time",
             ["Pick them in Apple's own picker. Two are free, and Premium covers every app, website and whole category you choose.",
              "On iPhone and iPad, Pausely uses Apple's Screen Time, the same system behind iOS's built in app limits. It asks for that permission once, and you can take it back in Settings at any time.",
              "On Android it uses the Accessibility service to notice when one of your apps comes to the front. It explains what that lets it see before you say yes."],
             "shot", "", shot("home-apps", "Pausely's Home: Protection is on, today's pauses, and a row of your apps, each with its own switch.")),
        step("When you tap one", "The block screen comes first",
             ["Instead of the app, you see a number: how many times you have opened it today. No comment, no lecture. Only the number.",
              "Tap <kbd>Open Pausely</kbd> to take the pause, or <kbd>Never mind</kbd> to leave the app closed. iOS draws this screen, so the picture here comes from our App Store preview."],
             "shot", "", shot("block-screen", "The block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind.")),
        step("Ten seconds", "A pause before you go in",
             ["The breathing pause is the one everybody starts with: in for four seconds, hold for two, out for four.",
              "With Premium you can swap it for typing a short string, picking why you are opening the app, or reading a reminder. Or let Pausely pick a different one each time."],
             "shot", "", shot("breathing", "The breathing pause: a soft circle inside a ring, with the word Hold.")),
        step("Then", "You choose, on purpose",
             ["<kbd>I changed my mind</kbd> closes it there, and Pausely counts the win.",
              "Under <kbd>Continue for</kbd>, tap <kbd>1m</kbd> or <kbd>5m</kbd> and the app opens for that long. Or take the third way out: one of the things you said you would rather do, such as a walk, a book or a glass of water, with a timer when you start it."],
             "shot", "", shot("choice", "The choice screen: You paused. I changed my mind, Or walk for 10 minutes, Or read for 10 minutes, Continue for 1 or 5 minutes.")),
        step("If you go in", "The time is yours, and it ends",
             ["A countdown runs while the app is open: on the Lock Screen and in the Dynamic Island on iPhone, in a quiet notification on Android.",
              "When the time is up, the pause is back in front of the app. Nothing is taken from you. You are asked again."],
             "p6", "A drawing of a countdown: 4 minutes 32 seconds left, then the pause comes back.", window_pic),
        step("Over time", "Watch it add up",
             ["Progress shows pauses today, the times you walked away, the time saved, your streak and a chart of the week. All of it is free.",
              "Time per app shows today's minutes in the apps you chose. With Premium, Pausely also shows your patterns over four weeks."],
             "shot", "", shot("progress", "The Progress screen: 1 hour 48 minutes reclaimed this week, and the last seven days as bars.")),
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
      ("Time banners", "premium", "On iPhone and iPad. Every few minutes in an app you picked, a banner says how long you have spent in it today."),
      ("Short videos", "premium", "About how many short videos your time came to. An estimate, never a count."),
      ("Reels and time", "premium", "On Android. A small card floats over the apps you pick, with a timer for this visit and about how many reels went by. Some videos can be missed."),
      ("Widgets", "premium", "Home Screen widgets on both. On iPhone also the Lock Screen, Control Center buttons, Siri and Shortcuts."),
  ])}
</div></section>

<section class="sec"><div class="wrap">
  <h2>Setting it up takes <em>a few minutes.</em></h2>
  <ol class="setup">
    <li><span><b>Choose your apps.</b> On iPhone, Apple asks for Screen Time access on the same screen. On Android, Pausely asks for Accessibility access. It can't work without it.</span></li>
    <li><span><b>Try your pause once,</b> so you know what is coming.</span></li>
    <li><span><b>Add things you would rather do.</b> A walk, a book, a glass of water, or something of your own.</span></li>
    <li><span><b>Allow notifications if you want them.</b> Pausely says why it uses them first.</span></li>
    <li><span><b>Done.</b> Open one of your apps and meet the pause.</span></li>
  </ol>
  <div class="cta-row" style="margin-top:34px">{store("how-it-works")}<p class="cta-note">Free to start.<br>iPhone, iPad and Android.</p></div>
</div></section>
</main>"""
    return layout("how-it-works", "/how-it-works/", "How Pausely Works: A Pause Before the Apps You Overuse",
                  "Step by step: choose your apps, meet the block screen, take a ten second breath, then decide "
                  "whether to go in. Plus rules, daily limits and strict mode.", body, ct="how-it-works",
                  jsonld=[crumbs(("How it works", "/how-it-works/"))])


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
      <li>The countdown while an app is open</li>
      <li>On iPhone and iPad: Time per app</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">Everything in Free, plus</p><ul>
      <li>Every app, website and category you choose</li>
      <li>As many rules as you like, and daily limits</li>
      <li>Every kind of pause, and a pause that asks a little more when you keep reaching for the same app</li>
      <li>Block everything, strict mode and Lock Pausely</li>
      <li>Time banners on iPhone, the floating reels card on Android, and the short video estimate</li>
      <li>Your patterns, the mood insight and your week in words</li>
      <li>Room for six things to do instead</li>
      <li>Widgets, and on iPhone Control Center, Siri and Shortcuts</li>
      <li>The optional AI pauses, off until you turn them on</li>
    </ul></div>
  </div>

  <div class="table-scroll"><table class="price-table">
    <thead><tr><th>Premium plan</th><th>How it is billed</th><th>Good to know</th></tr></thead>
    <tbody>
      <tr><td>Monthly</td><td class="num">Every month</td><td>Cancel any time in your App Store or Google Play settings.</td></tr>
      <tr><td>Yearly</td><td class="num">Every year</td><td>Starts with a free trial where one is offered.</td></tr>
      <tr><td>Lifetime</td><td class="num">One payment</td><td>No renewal.</td></tr>
      <tr><td>Family Yearly</td><td class="num">Every year</td><td>On iPhone and iPad, shared through Apple's Family Sharing. Starts with a free trial where one is offered.</td></tr>
      <tr><td>Family Lifetime</td><td class="num">One payment</td><td>On iPhone and iPad. One payment for the whole family group.</td></tr>
    </tbody>
  </table></div>
  <p class="fine">The price for your country is shown in the app and in its store before you pay, in your own currency. Billing, refunds and cancellations are handled by Apple on iPhone and iPad, and by Google Play on Android. <a href="{BASE}/terms/#subscriptions">Subscription terms</a></p>
</div>

<section class="sec" style="margin-top:clamp(48px,7vw,90px);border-top:1px solid var(--line-d)"><div class="wrap">
  <h2>The small print, <em>in plain words.</em></h2>
  <div class="faq">
    <details open><summary>What happens if my subscription ends?</summary><div><p>What protects you keeps protecting you. Every app you chose and every rule keeps running and stays editable, and the pause you chose keeps standing in front of your apps. Adding more closes, and so do the extras that show you things, such as widgets and time banners.</p></div></details>
    <details><summary>How do the family plans work?</summary><div><p>On iPhone and iPad, Family Yearly and Family Lifetime are shared through Apple's Family Sharing. Each person gets Premium in their own copy of Pausely, on their own device. Nobody sees anyone else's apps, numbers or journal.</p></div></details>
    <details><summary>Can I restore Premium on a new phone?</summary><div><p>Yes. Open the Premium screen in Pausely and tap <kbd>Restore purchases</kbd>. Premium belongs to your Apple Account, or on Android to your Google account, not to the device.</p></div></details>
    <details><summary>Does Premium move between iPhone and Android?</summary><div><p>No. Pausely has no accounts of its own, so Premium stays with the store you bought it in: the App Store or Google Play.</p></div></details>
    <details><summary>Are there ads in Pausely?</summary><div><p>No. Pausely shows no ads, and Premium is the only thing it sells.</p></div></details>
  </div>
  <div class="cta-row" style="margin-top:34px">{store("pricing")}<p class="cta-note">Start free.<br>Upgrade inside the app if you want to.</p></div>
</div></section>
</main>"""
    return layout("pricing", "/pricing/", "Pausely Pricing: Free Plan and Premium",
                  "Pausely is free for two apps on iPhone, iPad and Android, with the breathing pause. Premium adds "
                  "every app, every pause, daily limits and strict mode.", body, ct="pricing",
                  jsonld=[crumbs(("Pricing", "/pricing/"))])


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
                  "making Screen Time limits hold.", body, ct="guides",
                  jsonld=[crumbs(("Guides", "/guides/"))])


def guide_page(g):
    from guides import GUIDES
    others = [o for o in GUIDES if o["slug"] != g["slug"]][:3]
    rel = "".join(
        f'<li><a href="{BASE}/guides/{o["slug"]}/"><b>{o["title"]}</b><i>{o["minutes"]} min read</i></a></li>'
        for o in others
    )
    ct = "guide-" + g["ct"]
    g_updated, g_updated_iso = g.get("updated", (UPDATED, UPDATED_ISO))
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
    <p class="byline">By the Pausely team · Updated {g_updated} · {g["minutes"]} min read</p>
  </header>
  <div class="prose">
{content}
{appbox}
  </div>
</article>
<div class="related"><h2>Keep reading</h2><ul class="toc-list">{rel}</ul></div>
</main>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
           "description": g["description"], "dateModified": g_updated_iso, "datePublished": g_updated_iso,
           "author": {"@type": "Organization", "name": "Pausely"},
           "publisher": ORG, "image": SITE + "/assets/og.png",
           "mainEntityOfPage": SITE + f'/guides/{g["slug"]}/'},
          crumbs(("Guides", "/guides/"), (g["title"], f'/guides/{g["slug"]}/'))]
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


# Pages that exist in more than one language, for the sitemap's alternates.
ALTERNATES = {i18n.HOMES[c][1]: [(x, i18n.HOMES[x][1]) for x in ["en"] + i18n.LANGS] for c in ["en"] + i18n.LANGS}


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
    for lang in i18n.LANGS:
        i18n.use(lang)
        try:
            path = i18n.HOMES[lang][1]
            out.append((path.lstrip("/") + "index.html", home(), path))
        finally:
            i18n.use("en")
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
