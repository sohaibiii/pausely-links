# -*- coding: utf-8 -*-
"""English — the development language, and the fallback behind all seven others.

A key missing from another catalogue renders as the English here, never as an
identifier. That is the same rule the app follows (CLAUDE.md, Localization).

Every value is an HTML fragment. `{name}` placeholders are filled by
`gen.context()`: `{BASE}` and `{L}` build an in-language link, `{MAIL}` is the
support address, `{RESET}` is the app's own Settings path, `{K_*}` are single
app terms in a <kbd>, `{DATE}` is the localised date, and the rest are icons.
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Support",
"nav.about": "About",
"nav.privacy": "Privacy",
"nav.terms": "Terms",
"nav.data": "Your data",

"ui.skip": "Skip to content",
"ui.pages": "Pages",
"ui.footer": "Footer",
"ui.lang": "Language",
"ui.toc": "On this page",
"ui.rights": "All rights reserved.",
"ui.store_soon": "Coming soon to the App Store",
"ui.store_get": "Download on the App Store",
"ui.date": "12 November 2026",
"ui.last_updated": "Last updated: {DATE}",

# The app's own words, so this site names a screen the way the screen does.
"k.settings": "Settings",
"k.your_data": "Your data",
"k.reset_all": "Reset all data",
"k.restore": "Restore purchases",
"k.screen_time": "Screen Time",
"k.apps_with_st": "Apps with Screen Time access",
"k.notifications": "Notifications",
"k.ai_reflection": "AI reflection",
"k.what_is_sent": "What is sent",
"k.language": "Language",
"k.premium": "Premium",
"k.protection": "Protection",
"k.written_by": "Written by",
"k.time_per_app": "Time per app",
"k.time_banners": "Time banners",

"meta.support.title": "Pausely — Support",
"meta.support.desc": "Official support for Pausely, the app that puts a pause in front of the apps you chose. How it works, requirements, FAQ and contact.",
"meta.about.title": "Pausely — A breath before the scroll",
"meta.about.desc": "Pausely puts a small speed bump between you and the apps that eat your day. No account, and your apps, your time and your words stay on your phone.",
"meta.privacy.title": "Privacy Policy — Pausely",
"meta.privacy.desc": "What Pausely keeps on your device, what Meta's SDK reports so we can measure our ads, and what the optional AI reflection sends.",
"meta.terms.title": "Terms of Use — Pausely",
"meta.terms.desc": "Terms of Use (EULA) for Pausely: what the app is and is not, how Premium is billed, and what strict mode asks of you.",
"meta.data.title": "Delete your data — Pausely",
"meta.data.desc": "How to erase everything Pausely holds on your device, what happens to your subscription, and what Meta's SDK and the AI reflection leave elsewhere.",
"meta.nf.title": "Not found — Pausely",
"meta.nf.desc": "Page not found.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Support",
"s.h1": "Help with Pausely",
"s.sub": "A breath before the scroll. Pausely stands in front of the apps you chose and asks for ten seconds first. This page covers how it works, what it needs, and how to reach us.",
"s.cta": "Read the FAQ",
"s.meta": 'No account · your apps, your time and your words stay on your device · <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"s.how.h": "How Pausely works",
"s.how.b": """
<p class="lead">Pausely puts a small speed bump between you and the apps that eat your day.</p>
<p>You choose the apps you would rather use less. After that, tapping one of them does not open it straight away — Pausely stands in front of it first with a short pause: a breath, a sentence to type, or a question about why you are opening it. If you still want to go in, you can, for a timed window. When the window ends, the pause comes back.</p>
<p>The point is not to lock you out. It is to turn an automatic, thumb-driven habit into a decision you actually make. Given ten seconds to think, most people close the app instead — and Pausely counts that as a win.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Protection</b><span>One switch. While it is on, your chosen apps show Pausely's calm block screen instead of opening.</span></div></li>
  <li><span class="tile">{wind}</span><div><b>Three pauses</b><span>A breathing exercise, a typing challenge, or naming your intention. Setup picks the one that fits you; you can change it any time.</span></div></li>
  <li><span class="tile">{clock}</span><div><b>Rules</b><span>Protect certain apps at certain hours — a bedtime, a working day — with their own pause and their own window. A rule can also block completely until its hours are over.</span></div></li>
  <li><span class="tile">{lock}</span><div><b>Strict mode</b><span>Hold yourself to it for an hour, a day, or until a time you choose. While it runs, protection cannot be switched off and rules cannot be deleted — not even by you.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Alternatives and journal</b><span>Up to three healthy alternatives appear on the pause screen as a third way out, and there is a journal for the times you would rather write than scroll.</span></div></li>
  <li><span class="tile">{chart}</span><div><b>Progress</b><span>Pauses kept, time reclaimed, your streak and a weekly chart — plus Home Screen widgets and a Lock Screen countdown while a window is open.</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>The AI reflection, if you want it</b><span>Off until you switch it on. It turns "why are you opening this?" into a short exchange, and writes a weekly note about your week. On an iPhone with Apple Intelligence it can be written on the phone itself; otherwise OpenAI writes it — see <a href="{BASE}{L}/privacy/#ai">Privacy</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Requirements",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Device</th><td><strong>iPhone or iPad</strong> running <strong>iOS 17 or iPadOS 17</strong> or newer. One app, one layout, both devices.</td></tr>
<tr><th>Permission</th><td><strong>Screen Time</strong> access, granted once during setup through Apple's own prompt. Pausely uses Apple's Screen Time framework — the same system behind iOS's built-in app limits — and Apple, not Pausely, is what actually blocks an app.</td></tr>
<tr><th>Account</th><td>None. There is no sign-up, no email field and no password anywhere in the app.</td></tr>
<tr><th>Internet</th><td>Not needed. Every pause, rule, chart and journal entry works offline. When there is a connection, three things use it: Apple's own traffic when you buy or restore Premium; Meta's SDK, which reports installs, launches and purchases so we can measure our ads; and the AI reflection when OpenAI writes it — which is off until you switch it on.</td></tr>
<tr><th>Notifications</th><td>Optional, and made on the device. Pausely uses them to hand you from the block screen into the pause and to ask how an alternative went — and, only if you turn them on, for a reminder before your hardest hour and for {K_time_banners}. There is no push server.</td></tr>
<tr><th>Languages</th><td>English, German, Spanish, French, Japanese, Korean, Brazilian Portuguese and Simplified Chinese. Pausely follows your device's language, and you can pick a different one in {K_settings} → {K_language}.</td></tr>
</table></div>
""",

"s.start.h": "Getting started",
"s.start.b": """
<p>Setup is seven screens and takes under three minutes. It ends with protection already on and your first rule already written.</p>
<ol class="steps">
  <li><div><b>Say how much of the day your phone gets</b> — your own guess, nothing measured.</div></li>
  <li><div><b>Allow Screen Time access</b> when Apple asks. Pausely cannot work without it, and you can revoke it any time in {K_settings} → {K_screen_time}.</div></li>
  <li><div><b>Pick your apps</b> in Apple's picker. Pausely never learns their names — see <a href="{BASE}{L}/privacy/">Privacy</a>.</div></li>
  <li><div><b>Answer three questions</b> that choose the pause that fits you.</div></li>
  <li><div><b>Add up to three alternatives</b> — a walk, a book, a glass of water, or something of your own with a link into another app.</div></li>
  <li><div><b>Done.</b> Open one of your apps and meet the pause.</div></li>
</ol>
""",

"s.faq.h": "Frequently asked questions",
"s.faq.b": """
<dl class="faq">
<dt>Is Pausely free?</dt>
<dd>Yes. Free is a working product, not a demo: <strong>one rule</strong>, the <strong>breathing pause</strong> and your <strong>whole progress screen</strong> — pauses, wins, time reclaimed, the streak and the chart.</dd>
<dt>What does Premium add?</dt>
<dd>As many rules as you like, the other two pauses (type to proceed, set an intention), strict mode, the mood insight that compares how you feel after a session with how you feel after walking away, and the optional AI reflection with its weekly write-up. Premium is a monthly or yearly subscription — the yearly plan starts with a <strong>free trial</strong> — or a single lifetime purchase. Prices are shown in the app and in the App Store for your country, and billing is handled by Apple.</dd>
<dt>What happens if my subscription lapses?</dt>
<dd>Nothing you built is taken away. Every rule keeps running and stays editable, and the pause you chose keeps standing in front of your apps. Only the ability to add more closes. An app that stopped protecting your phone because a card expired would be letting you down at the exact moment you asked it not to.</dd>
<dt>Can I restore a purchase on a new device?</dt>
<dd>Yes. Open the Premium screen and tap {K_restore}. Premium belongs to your Apple ID, not to the device.</dd>
<dt>Why can't Pausely tell me which apps I blocked?</dt>
<dd>Because it genuinely does not know. Apple's Screen Time hands Pausely opaque tokens that are meaningless outside your device — no app names, no identifiers. Pausely can ask iOS to block them; it cannot read them.</dd>
<dt>I can't turn protection off. Is something broken?</dt>
<dd>Check whether <strong>strict mode</strong> is running — the home screen says so. While it runs, protection cannot be switched off and rules cannot be deleted, by design. It ends on its own at the time you chose.</dd>
<dt>Does Pausely see what I do in other apps?</dt>
<dd>No. It never sees your browsing, your messages or anything inside another app. iOS tells it how long the apps you chose have been open — for your daily goal, your limits and the time features — and Pausely keeps those minutes on your device and never sends them anywhere. Beyond that it records only its own events — that a pause was shown, and what you chose — and keeps those on your device too.</dd>
<dt>What is the AI reflection, and is it on?</dt>
<dd>It is off, until you switch it on. When you do, one pause becomes a short exchange: you type why you are opening the app, and a question comes back. It also writes a short note about your week. On an iPhone with Apple Intelligence, both can be written on the phone itself, and then nothing leaves it. When OpenAI writes them, those words go to Pausely's own server and on to OpenAI — never your journal, never your check-ins, never which apps you chose. {K_settings} → {K_ai_reflection} → {K_what_is_sent} lists every field, and switching it off stops all of it.</dd>
<dt>Does it work on iPad? On Mac?</dt>
<dd>iPad, yes — Pausely is one app for iPhone and iPad, with the same layout on both, and it works in Split View, Slide Over and Stage Manager. Mac, no: the Screen Time frameworks Pausely is built on are not available there.</dd>
<dt>Can I read the app in my own language?</dt>
<dd>Pausely speaks eight languages and follows your device's setting. To read it in a different one — without changing anything else on your device — open {K_settings} → {K_language}. Shields, widgets and the Lock Screen follow the same choice.</dd>
<dt>How do I erase everything?</dt>
<dd>{RESET}. That empties every pause, win, rule, journal entry and check-in, takes the blocks down and starts you at the beginning. It refuses while strict mode is running. Details on the <a href="{BASE}{L}/delete-data/">Your data</a> page.</dd>
</dl>
""",

"s.trouble.h": "Troubleshooting",
"s.trouble.b": """
<h3>An app opens without a pause</h3>
<ul>
  <li>Check the <strong>Protection</strong> switch on the home screen.</li>
  <li>Check that Screen Time access is still granted: {K_settings} → {K_screen_time} → {K_apps_with_st}. If it was revoked, Pausely shows a recovery screen with a button to ask again.</li>
  <li>If the app is only in a <strong>rule</strong>, the pause appears only during that rule's hours.</li>
  <li>An <strong>access window</strong> you opened earlier may still be running — the Lock Screen countdown shows how long is left.</li>
</ul>
<h3>The block screen appears but the pause never opens</h3>
<ul>
  <li>Tapping the block screen's button hands you to the app through a notification. If notifications are off for Pausely, iOS cannot deliver the hand-off — turn them on in {K_settings} → {K_notifications} → <kbd>Pausely</kbd>.</li>
  <li>Opening Pausely directly also opens the waiting pause.</li>
</ul>
<h3>Widgets are behind</h3>
<p>iOS refreshes widgets on its own schedule. Opening Pausely brings them up to date immediately.</p>
<h3>The app is in the wrong language</h3>
<p>Open {K_settings} → {K_language} and pick the one you want. Everything Pausely draws follows immediately. Apple's own app picker is drawn by iOS, not by Pausely, so it changes on the next launch.</p>
<h3>Premium isn't recognised</h3>
<p>Tap {K_restore} on the Premium screen, and make sure the device is signed into the same Apple ID that made the purchase. Refunds and billing questions are handled by Apple through <a href="https://support.apple.com/billing">Apple Support</a>.</p>
""",

"s.contact.h": "Contact",
"s.contact.b": """
<p>Questions, a bug, or something that should work and doesn't — write to us and a person will reply.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Include your device model, the iOS version, and what you expected to happen. Never send us your journal or check-ins — we do not need them and would rather not hold them.</span></div></div>
<p style="margin-top:16px" class="small">Billing, refunds and subscription changes are handled by Apple: <a href="https://apps.apple.com/account/subscriptions">manage subscriptions</a> · <a href="https://support.apple.com/billing">request a refund</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "About Pausely",
"a.h1": "A breath before the scroll.",
"a.sub": "Pick the apps you'd rather use less. From then on, opening one gets you a pause first — and a choice you actually make.",
"a.cta": "Support",
"a.meta": "No account · iPhone and iPad · iOS 17+ · eight languages",
"a.lead": "Pausely puts a small speed bump between you and the apps that eat your day. Not a lockout, not a guilt trip — ten seconds to decide whether you meant to open it.",

"a.f1.icon": "wind",
"a.f1.h": "A breath before the scroll.",
"a.f1.p": "Pausely stands in front of the apps you chose and asks for ten seconds first — a breathing exercise, a sentence to type, or a moment to name your intention.",
"a.f2.icon": "pause",
"a.f2.h": "Why are you opening it?",
"a.f2.p": "Turn a reflex into a decision — and make it on purpose. Most of the time, given the chance to think, people close the app instead.",
"a.f3.icon": "check",
"a.f3.h": "Walking away counts.",
"a.f3.p": "Keep the win, or go in for five minutes — no lockouts, no guilt trips. Your own alternatives sit on the pause screen as a third way out.",
"a.f4.icon": "chart",
"a.f4.h": "See the time come back.",
"a.f4.p": "Every pause you kept, every hour reclaimed, a streak and a weekly chart — with widgets for the Home Screen and a countdown on the Lock Screen.",
"a.f5.icon": "clock",
"a.f5.h": "Your apps. Your rules.",
"a.f5.p": "A switch and a pause for every app, with schedules for evenings and workdays. Strict mode holds you to it when you ask it to.",
"a.f6.icon": "eye-off",
"a.f6.h": "Your phone keeps what it knows.",
"a.f6.p": "No account. Your apps, your time, your pauses and your journal stay on your device — Pausely cannot even read which apps you picked; Apple keeps that. Meta's SDK tells us which of our ads brought you here, and the optional AI reflection sends what you type into it only when OpenAI writes it. <a href=\"{BASE}{L}/privacy/\">What leaves, exactly.</a>",

"a.price.h": "What it costs",
"a.price.b": """
<p>Free is a working product, not a demo, and nothing you set up is ever taken away — even if a subscription lapses.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Free</div><div class="price">$0</div><ul><li>One rule</li><li>The breathing pause</li><li>The whole progress screen — wins, time reclaimed, streak and chart</li><li>Widgets and the Lock Screen countdown</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Monthly · Yearly · Lifetime</div><ul><li>As many rules as you like</li><li>All three pauses</li><li>Strict mode</li><li>The mood insight</li><li>The optional AI reflection and its weekly note</li><li>Yearly starts with a free trial</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Prices are shown in the app and on the App Store for your country. Billing is handled by Apple. <a href="{BASE}{L}/terms/#subscriptions">Subscription terms.</a></p>
""",

"a.st.h": "Built on Apple's Screen Time",
"a.st.b": """
<p>Pausely uses the same framework that powers iOS's built-in app limits. Apple grants it only to apps it has reviewed for the purpose, and Apple — not Pausely — is what actually stands between you and the app. That is why Pausely can block an app without ever learning its name.</p>
<ul class="rows" style="margin-top:16px">
  <li><span class="tile">{tablet}</span><div><b>iPhone and iPad, one app</b><span>The same single-column layout on both, and it behaves in Split View, Slide Over and Stage Manager. iOS 17 or iPadOS 17 and newer.</span></div></li>
  <li><span class="tile">{globe}</span><div><b>Eight languages</b><span>English, German, Spanish, French, Japanese, Korean, Brazilian Portuguese and Simplified Chinese — including the block screen and the widgets. Choose one in {K_settings} → {K_language} without changing anything else on your device.</span></div></li>
</ul>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Privacy Policy",
"p.h1": "Your phone keeps what it knows.",
"p.sub": "Pausely has no account, and everything it records about you stays on your device. Two things leave it: what Meta's SDK reports so we can measure our ads, and — only if you switch it on and OpenAI writes it — what you type into the AI reflection. This page is about exactly where those lines are.",
"p.meta": "Effective {DATE} · applies to the Pausely app for iPhone, iPad and Android, and to this site",

"p.summary.h": "The short version",
"p.summary.b": """
<p class="lead">Pausely has no account. <strong>Everything it records — which apps you protect, how long you spend in them, your pauses, your journal — is written to your device and stays there.</strong> Pausely cannot even read which apps you chose; Apple's Screen Time keeps that.</p>
<p><strong>Two things leave your device</strong>, and this page lists every part of both:</p>
<ul>
  <li><strong>Meta's SDK</strong>, from Pausely 1.3, so we can tell which of our ads on Facebook and Instagram brought people to the app. It tells Meta when Pausely is installed or opened and when a plan is bought, with the kind of device and an identifier it makes up for this install. It never learns which apps you protect, how you use them or anything you write, and because Pausely never asks to track you, Meta gets no advertising identifier. <a href="{BASE}{L}/privacy/#ads">Details.</a></li>
  <li><strong>The AI reflection</strong>, which is off until you switch it on. On an iPhone with Apple Intelligence it can be written on the phone itself, and then nothing leaves. When OpenAI writes it, the words you type into that one pause go to Pausely's server and on to OpenAI, with four small facts about the moment. <a href="{BASE}{L}/privacy/#ai">Details.</a></li>
</ul>
<div class="callout"><span class="tile">{eye-off}</span><div>Your journal never leaves your device. Your check-ins never leave. The minutes you spend in other apps never leave. Which apps you chose never leaves — Pausely cannot read that even on your own device.</div></div>
<p style="margin-top:16px">In the terms of Apple's privacy labels: <strong>no tracking</strong>; <strong>identifiers, usage data, purchases, diagnostics and other data</strong>, collected by Meta's SDK to measure our ads; and <strong>user content</strong>, not linked to you, used only to make the AI reflection work. This policy applies to the Pausely app for iPhone, iPad and Android, published by {COMPANY}, and to this website.</p>
<p style="margin-top:16px"><strong>On Android</strong>, Pausely works the same way on Google's tools instead of Apple's: there is no Meta SDK, Google's ML Kit sends Google diagnostics about itself, and the AI reflection uses Gemini Nano in place of Apple Intelligence and Google Play Integrity in place of App Attest. <a href="{BASE}{L}/privacy/#android">Pausely on Android</a> sets out all of it.</p>
""",

"p.collect.h": "What we collect",
"p.collect.b": """
<p>"Collect", in Apple's sense and in ours, means transmitting data off the device and keeping it somewhere that is not transient. By that measure Pausely collects what Meta's SDK reports so we can measure our ads, and — only if you switch on the AI reflection and OpenAI writes it — the words you type into that one screen. Nothing else.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Collected?</th><th>What that means</th></tr>
<tr><td>Contact info</td><td>No</td><td>There is no account, no sign-in and no email field anywhere in the app.</td></tr>
<tr><td>Identifiers</td><td><strong>Yes — Meta's SDK</strong></td><td>An identifier the SDK makes up for this install of Pausely and sends with its events. Not your name, not your Apple ID and not the advertising identifier: Pausely never asks for App Tracking Transparency, so iOS does not hand one out. Pausely itself has no user ID and no device ID.</td></tr>
<tr><td>Usage data</td><td><strong>Yes — Meta's SDK</strong></td><td>That Pausely was installed, and each time it is opened and for how long. That is all of it: Pausely logs no event of its own, and nothing it counts — your pauses, your wins, the minutes you spend in other apps — is ever sent. Those stay on your device, for your own screens.</td></tr>
<tr><td>Purchases</td><td><strong>Yes — Meta's SDK</strong></td><td>When a plan is bought, a free trial starts or a subscription renews, the SDK notices it on your device and reports which plan, its price and its currency. Payment itself is Apple's, in the App Store sheet; Pausely never sees a card.</td></tr>
<tr><td>Diagnostics</td><td><strong>Yes — Meta's SDK</strong></td><td>Crash reports from Meta's own code. Pausely has no crash or performance reporter of its own.</td></tr>
<tr><td>Other data</td><td><strong>Yes — Meta's SDK</strong></td><td>Technical details sent with Meta's events, such as the kind of device, its iOS version, its language and its time zone.</td></tr>
<tr><td>User content</td><td><strong>Only the AI reflection</strong></td><td>Your journal, your check-ins and your custom alternatives are stored on the device and nowhere else. If — and only if — you switch the AI reflection on and OpenAI writes it, the words you type into <em>that one screen</em> are sent, so that a question can come back. Nothing else you write is ever sent.</td></tr>
<tr><td>Location, health, contacts, browsing, search</td><td>No</td><td>Pausely does not ask for your location, your health records or your contacts, and does not see your browsing or your searches. During a walk you chose instead of your phone it counts your steps with the phone's motion sensor, shows the number, and forgets it.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> none. Pausely never asks for permission to track you, so iOS keeps your device's advertising identifier from Meta's SDK, and the SDK tells Meta that tracking is not allowed. We do not link anything about you with data from other companies' apps or websites, and we share nothing with data brokers.</p>
""",

"p.device.h": "What stays on your device",
"p.device.b": """
<p>Pausely stores the following in its own private storage on your iPhone or iPad, protected by your device's passcode and encryption. None of it is uploaded, backed up by us, or visible to us.</p>
<ul>
  <li><strong>Your app selection</strong> — the apps you protect, and any you chose for {K_time_banners}, as opaque Screen Time tokens Pausely cannot read (see below).</li>
  <li><strong>Your rules and schedules</strong> — the names you give them, their hours and their pause.</li>
  <li><strong>Pause outcomes</strong> — that a pause was shown, when, and whether you walked away, went in, or chose an alternative. This is what the progress screen, the streak and the chart are made of.</li>
  <li><strong>Time in the apps you chose</strong> — minutes per day, as iOS counts them, for your daily goal, your limits, the short-video estimate and {K_time_banners}. Kept for up to sixty days.</li>
  <li><strong>What you write</strong> — journal entries, the words you type on the pause screen, mood check-ins after a session, and the names of custom alternatives.</li>
  <li><strong>Settings</strong> — your chosen pause, strict-mode state, alternatives, the apps you marked as mostly short videos, your language, and preferences.</li>
  <li><strong>Your Premium entitlement</strong> — a tier and an expiry date, so the app knows what to unlock.</li>
</ul>
<p>If you use iCloud Backup or an encrypted local backup, Apple may include Pausely's data in that backup under your own Apple ID and Apple's privacy terms. We have no access to it.</p>
""",

"p.screentime.h": "Screen Time: your apps and your time",
"p.screentime.b": """
<p>Pausely is built on Apple's Screen Time framework (Family Controls, Managed Settings and Device Activity). You grant it access once, through Apple's own prompt, and can revoke it at any time in {K_settings} → {K_screen_time}.</p>
<p>When you pick apps, Apple's picker returns <strong>tokens</strong>: values that identify the app to iOS but mean nothing to Pausely and nothing outside your device. Pausely stores those tokens so it can ask iOS to shield the apps you chose, and it never receives a bundle identifier. Where it needs to compare tokens between its own components it compares one-way hashes of them, never the tokens themselves. Apart from the sealed screen described below, the one place it can read an app's name is the block screen: iOS lets it see the name of the app you are standing in front of, so that the pause — and the AI reflection, if you use it — can say "Instagram" rather than "an app". That name stays on your device, except in the AI reflection's request when OpenAI writes it.</p>
<h3>How long you spend in them</h3>
<p>For your daily goal, your limits, the short-video estimate and {K_time_banners}, iOS tells Pausely each time the apps you chose pass another few minutes of use today. Pausely writes down minutes per day — on your device, never sent anywhere, and erased by {RESET}.</p>
<p>The {K_time_per_app} screen, and the minutes under an app's icon on the pause screen, are drawn by an extension Apple runs in a sealed sandbox. It sees app names and exact minutes, but it cannot use the network or hand anything back, so the rest of Pausely never learns them and nothing on that screen is kept.</p>
<p>The <strong>short-video</strong> figure is an estimate and always says "about": the minutes in the apps you marked, divided by the length you chose for one video. Pausely never sees a video, or anything else on your screen.</p>
<p>Pausely does not observe your browsing, your messages, or what you do inside any app. iOS itself draws the block screen and enforces the shield. Besides the minutes above, Pausely learns only that its own pause was shown and what you chose on it.</p>
""",
"p.ads.h": "Meta's SDK — measuring our ads",
"p.ads.b": """
<p class="lead">Pausely runs ads on Facebook and Instagram. <strong>From Pausely 1.3, the app includes Meta's software development kit (SDK)</strong> so we can tell which of those ads brought people to Pausely. It is the one piece of someone else's code in the app. It runs only inside the app itself — never in the parts that draw the block screen, count your time or draw the widgets — and Pausely never hands it anything of its own.</p>
<h3>What it sends to Meta</h3>
<ul>
  <li>That Pausely was <strong>installed</strong>, and each time it is <strong>opened</strong> and for how long.</li>
  <li>That a <strong>plan was bought</strong>, a free trial started or a subscription renewed — which plan, its price and its currency — as it notices on your device.</li>
  <li><strong>Technical details</strong> such as the kind of device, its iOS version, its language and its time zone.</li>
  <li>An <strong>identifier the SDK makes up</strong> for this install of Pausely. It is not your name, your Apple ID or your device's advertising identifier.</li>
  <li><strong>Crash reports</strong> from Meta's own code.</li>
  <li>If you open Pausely from one of its ads, the <strong>link</strong> the ad opened it with.</li>
</ul>
<p>Like any server, Meta's also sees the IP address these arrive from.</p>
<h3>What it never gets</h3>
<ul>
  <li><strong>Which apps you protect</strong>, or how long you spend in them.</li>
  <li><strong>Your pauses, rules, wins, journal and check-ins</strong>, or anything you type — including what you type into the AI reflection.</li>
  <li><strong>Any event of Pausely's own.</strong> The SDK reports only what is listed above, which it notices by itself; Pausely never tells it anything.</li>
  <li><strong>Your advertising identifier.</strong> Pausely never asks for permission to track you, so iOS does not hand it out, and the SDK tells Meta that tracking is not allowed.</li>
</ul>
<p>The SDK's features that would read what is on your screen — what you type into a text field, the labels of the buttons you tap, the layout of a screen — are switched off for Pausely, in the app and in Meta's settings, and they stay off.</p>
<p>Meta keeps what it receives under <a href="https://www.facebook.com/privacy/policy/">Meta's Privacy Policy</a>, which says how long it is kept and how to exercise your rights with Meta. The identifier lives in Pausely's storage on your device: deleting the app deletes it, and a new install starts with a new one.</p>
""",

"p.ai.h": "The AI reflection — only if you switch it on",
"p.ai.b": """
<p class="lead">This is an optional Premium feature. <strong>It is off when you install Pausely and stays off until you switch it on</strong>, and switching it off again stops all of it.</p>
<p>With it on, one pause becomes a short exchange: you type why you are opening the app, and a question comes back rather than a lecture. Once a week it also writes a short note about how your week went.</p>
<h3>Who writes it</h3>
<p>On an iPhone with <strong>Apple Intelligence</strong>, Apple's model can write the question and the weekly note <strong>on the phone itself</strong>. Then nothing listed below leaves your device: no request is made, and nothing is kept. That is how it starts wherever Apple Intelligence is available. Otherwise — or if you choose it at {K_settings} → {K_ai_reflection} → {K_written_by} — <strong>OpenAI</strong> writes it, and the rest of this section applies. If you chose Apple Intelligence and it cannot answer, the pause shows its plain question instead: your words never go somewhere you decided they should not.</p>
<h3>What is sent when OpenAI writes it</h3>
<ul>
  <li>The <strong>display name of the app you are opening</strong> — the name already on your screen at that moment.</li>
  <li><strong>Three numbers</strong>: how many times you have opened it today, the time on the clock, and how long your streak is.</li>
  <li><strong>The words you type into that screen</strong>, in that moment.</li>
</ul>
<p>The weekly note sends less: counts for the week and nothing else. No app names appear in it at all.</p>
<h3>What is never sent</h3>
<ul>
  <li><strong>Your journal.</strong> It is the one place you write for nobody, and it never leaves the device. On an iPhone with Apple Intelligence, Pausely can write a few lines about your week's entries — on the phone, and nowhere else.</li>
  <li><strong>Your check-ins</strong>, moods, or any note attached to them.</li>
  <li><strong>Your app selection</strong> — which apps you protect, or how many — and never a Screen Time token, a token hash or a bundle identifier.</li>
  <li><strong>How long you spend in any app.</strong></li>
  <li><strong>Your rules, schedules or strict-mode state.</strong></li>
  <li><strong>Anything that identifies you.</strong> There is no account, no user ID and no advertising identifier to send. The request carries an Apple App Attest assertion, which tells our server that it is talking to a genuine copy of Pausely — it is scoped to the app, not to you, and does not follow you between requests.</li>
</ul>
<h3>Where it goes, and how long it is kept</h3>
<p>Your words go to <strong>Pausely's own server</strong>, and on to <strong>OpenAI</strong>, which runs the model. Pausely never calls a model vendor's API from your device, and there is no API key inside the app to be extracted.</p>
<p><strong>Pausely's server stores nothing per request</strong> — no prompt, no reply, no context. To stop runaway use it keeps one number per device per day — how many reflections that device asked for, under a random device key — and deletes it after two days. Its logs record the shape of a request (a timestamp, how long it took, whether it succeeded) and never its contents. <strong>OpenAI keeps inputs and outputs for up to 30 days</strong> in its abuse-monitoring logs, and may examine them to check for abuse. <strong>OpenAI does not use any of it to train its models.</strong></p>
<p>Earlier versions of Pausely send the same words to <strong>Google</strong> instead, which keeps inputs and outputs for up to 24 hours, may examine prompts to check for abuse, and does not use them to train its models.</p>
<p>{K_settings} → {K_ai_reflection} → {K_what_is_sent} lists every field in the app itself, in the same words as this page.</p>
""",

"p.purchases.h": "Purchases",
"p.purchases.b": """
<p>Premium is sold through Apple's App Store using StoreKit. The transaction is between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Apple tells Pausely whether a purchase is active — nothing else — and Pausely tells Apple nothing about how you use the app. No usage data, no journal, no app selection and no identifier of ours travels with a purchase. Separately, Meta's SDK notices purchases on your device and reports them so we can measure our ads — see <a href="{BASE}{L}/privacy/#ads">Meta's SDK</a>.</p>
""",

"p.notifications.h": "Notifications, widgets and the Lock Screen",
"p.notifications.b": """
<p><strong>Notifications</strong> are optional and are made on your device. Pausely uses them to hand you from the block screen into the pause, and to ask how it went when the time for an alternative you chose — a walk, a book — is up. Two more come only if you turn them on: a reminder once a day shortly before your hardest hour, and {K_time_banners} (Premium), which tell you every few minutes how long you have spent today in apps you chose. A time banner never names the app — it says "this app" — because notifications also appear on the Lock Screen. No notification is sent from a server: there is no push server and no marketing.</p>
<p><strong>Widgets and Live Activities</strong> show counts, minutes and dates — today's wins, your streak, time reclaimed, your time today, the short-video estimate, and how long an access window has left. They deliberately do not have Screen Time access and never see which apps you blocked. A Lock Screen countdown names the <em>rule</em> you wrote ("Bedtime"), never the app, because a Lock Screen is readable by anyone holding the device. While an access window is open, the Dynamic Island also counts how long you have spent in that app through Pausely today; the Lock Screen does not show it.</p>
""",

"p.third.h": "Third parties",
"p.third.b": """
<p>Pausely contains <strong>one piece of third-party code: Meta's SDK</strong>, described <a href="{BASE}{L}/privacy/#ads">above</a>. There is no other analytics, advertising or crash-reporting code in the app. These parties are involved, and only these:</p>
<ul>
  <li><strong>Apple</strong> operates the App Store, processes purchases, enforces the Screen Time shield, runs Apple Intelligence on your iPhone if the AI reflection uses it, and — if you have opted in to sharing with developers — may share crash logs with us under its own policy.</li>
  <li><strong>Meta</strong> receives what its SDK reports so we can measure our ads, and nothing else.</li>
  <li><strong>Cloudflare</strong> hosts Pausely's server. When OpenAI writes the AI reflection, your words pass through it on their way to the model, and it stores none of them.</li>
  <li><strong>OpenAI</strong> runs the model behind the AI reflection when it writes it, and only for as long as you have that feature switched on. It receives what is listed above and nothing else, and it does not use it to train its models. Earlier versions of the app use <strong>Google</strong> for this instead.</li>
</ul>
<p>We do not sell or rent personal data to anyone, and we share nothing with data brokers.</p>
""",

"p.android.h": "Pausely on Android",
"p.android.b": """
<p class="lead">Pausely for Android, from Google Play, keeps the same promise: <strong>no account, and everything it records stays on your phone.</strong> It is built on Android's own tools rather than Apple's, so some things work differently, and this section sets out every one of them. Where it differs from the sections above, this is the one that applies on Android.</p>
<h3>What leaves your phone</h3>
<p>Two things, and the second only if you turn it on.</p>
<p><strong>Google's ML Kit diagnostics.</strong> Pausely for Android runs its on-phone AI with Google's ML Kit (Gemini Nano), and ML Kit sends Google diagnostics and usage statistics about itself: the phone's manufacturer, model and Android version, Pausely's package name and version, identifiers ML Kit uses for the installation and the device, performance figures, error codes and the languages set. It travels encrypted, and Google says it does not pass it on to third parties — see <a href="https://developers.google.com/ml-kit/android-data-disclosure">Google's ML Kit disclosure</a> and <a href="https://policies.google.com/privacy">Google's Privacy Policy</a>. It never contains what you type, which apps you chose, your time or your journal.</p>
<p><strong>The AI reflection, if you turn it on.</strong> It is off until you do, and works as described under <a href="{BASE}{L}/privacy/#ai">The AI reflection</a> above, with Google's tools in place of Apple's. On a phone that supports Gemini Nano it is written on the phone unless you choose otherwise, and then nothing about it leaves. Otherwise — or if you choose OpenAI at {K_settings} → {K_ai_reflection} → {K_written_by} — OpenAI writes it through Pausely's server, and the same things are sent as from an iPhone: the name of the app you are opening, how many times you have reached for it today, the time on your clock, your streak and the words you type into that pause. The weekly note sends only the week's counts. Your journal is only ever read by Gemini Nano, on the phone.</p>
<p>In place of Apple's App Attest, <strong>Google Play Integrity</strong> shows our server that a request comes from a genuine copy of Pausely, installed from Google Play, on a genuine phone. Pausely asks Google Play for a check tied to a random code made for this installation, and our server asks Google to confirm it. The code is not your account, your phone's ID or your advertising ID. Our server keeps it only as the key for that installation's daily count, which it deletes after two days, and turning the AI reflection off erases it from the phone. Pausely's server stores nothing else; OpenAI keeps what it receives for up to 30 days and does not train its models on it.</p>
<p>Nothing else leaves. Pausely for Android has <strong>no Meta SDK</strong>, no advertising and no analytics of its own, and never reads your advertising ID.</p>
<h3>The Accessibility service</h3>
<p>To put a pause in front of an app at the moment it opens, Pausely uses Android's Accessibility service. Only you can turn it on, in Android's settings, after Pausely has explained on its own screen what the service sees. Pausely is not an accessibility tool, and you can turn the service off at any time in Android's Accessibility settings; Pausely then stops pausing your apps. It sees:</p>
<ul>
  <li><strong>Which app is in front</strong>, including the focused app in split screen, so the pause appears before you use an app you chose. Apps you did not choose are ignored the moment they are checked.</li>
  <li><strong>The address of the site you open</strong> in Chrome, Samsung Internet, Firefox, Edge or Brave — only if you protect a website. Only its domain is compared with your list. For a site with a daily time limit, Pausely keeps that domain and how long it was in front for up to two days, on the phone. Page content, paths and searches are never read or kept.</li>
  <li>With <strong>Reels &amp; time</strong> — off until you turn it on, with its own consent — how long you spend in the apps you picked, and the layout and position of the video player, to estimate how many reels you watched. On YouTube Shorts it may compare the channel and sound labels on screen. Those labels and positions are held in memory for a moment and never saved; only today's minutes and reel totals are kept, on the phone. The count is an estimate and can miss videos.</li>
</ul>
<p>The service never reads your messages, what you type, your passwords or your notifications, and never taps, types or scrolls for you. Nothing it sees leaves your phone.</p>
<h3>Usage access, and what stays on the phone</h3>
<p>If you allow Usage access in Android's settings, Pausely reads how long the apps you chose were used, for your progress, your daily goal and your limits. On Android, Pausely knows the apps you chose by name rather than through Apple's sealed tokens, and keeps that list — with your rules, pauses, time, journal, check-ins, settings and Premium status — in its private storage on the phone. Android's app backup is turned off for Pausely, so none of it goes into a Google backup. The step counter, used only during a walk you chose instead, stays on the phone, and notifications are made on the phone; there is no push server.</p>
<h3>Purchases</h3>
<p>Premium is sold through Google Play. Payment is between you and Google, under Google's Privacy Policy, and Pausely never sees your card. Google Play tells Pausely whether a purchase is active, and Pausely sends nothing about purchases anywhere.</p>
<h3>In the terms of Google Play's Data safety section</h3>
<p><strong>Collected:</strong> device or other IDs and diagnostics, by Google's ML Kit, for analytics. Only when OpenAI writes the AI reflection, also what you type into it (user-generated content), the name of the app you are opening (installed apps) and a few counts (app interactions), for the feature to work, and the installation code (device or other IDs), for security. <strong>Shared:</strong> nothing. <strong>Encrypted in transit:</strong> yes. No account, no advertising ID, no location and no personal information.</p>
<h3>Deleting your data on Android</h3>
<p>{RESET} erases everything Pausely holds on the phone; it does not cancel a Google Play subscription, which you manage in Google Play. Clearing Pausely's storage in Android's app settings, or uninstalling it, does the same. Our server holds only an installation's daily count, for two days. What ML Kit has already sent is held by Google, under Google's Privacy Policy, and what OpenAI received it keeps for up to 30 days.</p>
""",

"p.delete.h": "Deleting your data",
"p.delete.b": """
<p>Everything Pausely holds is erasable from inside the app, without asking us:</p>
<div class="callout"><span class="tile">{trash}</span><div>{RESET}<br><span class="small">Empties every pause, win, rule, journal entry and check-in, takes the shields down, withdraws the schedules and starts you at the beginning. It refuses while strict mode is running — the one commitment you asked the app to hold you to — and it does not touch your subscription, which belongs to your Apple ID.</span></div></div>
<p style="margin-top:16px">Deleting the app removes all of its data from the device as well, including the identifier Meta's SDK made up for it. On our side there is nothing to delete: our server keeps no record of a request once it has answered it. What Meta's SDK has already sent is held by Meta, under <a href="https://www.facebook.com/privacy/policy/">Meta's Privacy Policy</a>. You are welcome to write to us anyway — see the <a href="{BASE}{L}/delete-data/">Your data</a> page.</p>
""",

"p.rights.h": "Your rights",
"p.rights.b": """
<p>Wherever you live — including under the GDPR, the UK GDPR and the CCPA/CPRA — you have rights to access, correct, export, restrict, object to and erase personal data a company holds about you, and to complain to a supervisory authority. Pausely holds no profile of you and keeps nothing after a reflection is answered, so there is nothing on our side to produce or delete; the data on your device is already in your hands, and the app's own controls exercise every one of those rights for you. What Meta's SDK sent is held by Meta, and <a href="https://www.facebook.com/privacy/policy/">Meta's Privacy Policy</a> explains how to exercise your rights there. If you have a question, or believe we hold something this page does not describe, write to {MAIL} and we will respond.</p>
""",

"p.children.h": "Children",
"p.children.b": """
<p>Pausely is a self-directed tool for the person using the device. It is not a parental-control product and does not manage another person's device. It is not directed at children under 13 (or the age of digital consent where you live), and we do not knowingly collect personal information from children.</p>
""",

"p.changes.h": "Changes to this policy",
"p.changes.b": """
<p>We may update this policy as the app changes. The date at the top moves when we do, and material changes will be noted in the app's release notes. The most recent change, on {DATE}, adds Pausely for Android — see <a href="{BASE}{L}/privacy/#android">Pausely on Android</a>. Before that came Pausely 1.3: Meta's SDK, which measures our ads, and new time features — {K_time_per_app}, {K_time_banners} and the short-video estimate — which, like the daily goal, count on your device how long you spend in the apps you choose. Before that, the AI reflection moved from Google to OpenAI, and gained the choice of Apple Intelligence on your iPhone. Continued use of Pausely after a change means you accept the revised policy.</p>
""",

"p.contact.h": "Contact",
"p.contact.b": """
<p>{COMPANY}, the publisher of Pausely, is the controller for anything covered here. Questions about privacy: {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Terms of Use",
"t.h1": "The agreement, in plain words.",
"t.sub": "What Pausely does, what it does not promise, how Premium is billed, and what strict mode asks of you.",
"t.meta": "Effective {DATE} · Pausely by {COMPANY}",

"t.acceptance.h": "1. Acceptance of Terms",
"t.acceptance.b": """
<p>These Terms of Use ("Terms") are an agreement between you and {COMPANY} ("we", "us"), the publisher of the Pausely app for iPhone and iPad ("Pausely" or "the app"). By installing or using Pausely you accept these Terms and our <a href="{BASE}{L}/privacy/">Privacy Policy</a>. If you do not agree, do not use the app.</p>
""",
"t.who.h": "2. Who may use Pausely",
"t.who.b": """
<p>You must be at least 13 years old, or the age of digital consent where you live, to use Pausely. Pausely is a tool you install for yourself, on your own device. It is not a parental-control product and must not be used to manage or monitor another person's device.</p>
""",
"t.what.h": "3. What Pausely is — and is not",
"t.what.b": """
<p>Pausely is a self-directed tool that adds a pause before apps you choose, records the outcomes on your device, and shows you your own progress. It is designed to make an automatic habit into a conscious choice.</p>
<p>Pausely is <strong>not</strong> a medical, psychological or therapeutic service, and nothing in it — including mood check-ins, journal prompts, insights and anything the AI reflection writes back — is advice, diagnosis or treatment. If you are struggling with compulsive use, anxiety, depression or anything else that affects your wellbeing, please speak to a qualified professional. In an emergency, call your local emergency number.</p>
<p>Pausely is also <strong>not a security or parental-control product</strong>. It is designed to be exactly as strong as you ask it to be: the app can be deleted, Screen Time access can be revoked in iOS Settings, and the shield exists only while the app is installed and authorised.</p>
""",
"t.screentime.h": "4. Screen Time, strict mode and your commitments",
"t.screentime.b": """
<p>Pausely relies on Apple's Screen Time framework. Apple enforces the shield; Pausely asks for it. Whether a shield appears, how quickly, and whether it persists across restarts and iOS updates is ultimately determined by iOS, and we cannot guarantee it in every circumstance.</p>
<p><strong>Strict mode</strong> is a commitment you make to yourself. While it runs, for the duration you chose, protection cannot be switched off, rules cannot be deleted and data cannot be reset — <em>including by you, and including by us</em>. We cannot end a strict-mode session early on request. Do not start one you are not prepared to keep, and do not start one on a device you may need unrestricted access to. Deleting the app ends every shield, as described in section 3.</p>
<p>A <strong>hard-block rule</strong> offers no way through during its hours. The same warning applies.</p>
""",
"t.data.h": "5. Your data and your device",
"t.data.b": """
<p>Everything Pausely records is stored on your device — see the <a href="{BASE}{L}/privacy/">Privacy Policy</a> for what leaves it, and when. You are responsible for your device, its passcode and its backups. If you delete the app, reset all data, or lose the device without a backup, your rules, journal and history are gone, and we have no copy to restore. Your Premium purchase is separate: it belongs to your Apple ID and can be restored on any device signed into it.</p>
<p>What you write into Pausely is yours. We claim no rights over it, and we receive none of it unless you switch on the AI reflection and OpenAI writes it, which sends only what section 6 and the Privacy Policy describe.</p>
""",
"t.ai.h": "6. The AI reflection",
"t.ai.b": """
<p>The AI reflection is an <strong>optional</strong> Premium feature that is <strong>off until you switch it on</strong>. With it on, it is written either on your iPhone by Apple Intelligence, which sends nothing, or by OpenAI, in which case the words you type into that one pause are sent to our server and on to OpenAI, which generates a response. Where both are available you choose at {K_settings} → {K_ai_reflection} → {K_written_by}. What is sent, what is never sent and how long anything is kept are set out in the <a href="{BASE}{L}/privacy/#ai">Privacy Policy</a>, and listed inside the app at {K_settings} → {K_ai_reflection} → {K_what_is_sent}.</p>
<p>The response is <strong>generated text</strong>. It may be wrong, unhelpful, or not what you expected, and it is <strong>not advice of any kind</strong> — see section 3. Do not type anything into it you would not want processed by a third party, and do not rely on it for any decision that matters. We do not guarantee the availability, latency or continuity of the feature, and we may change the model behind it, limit its use, or withdraw it, without that affecting the rest of the app.</p>
<p>You agree not to use the feature to generate unlawful, abusive or infringing content, or to attempt to extract the underlying model or its instructions. Switching the feature off stops all of it.</p>
""",
"t.subscriptions.h": "7. Premium, subscriptions and billing",
"t.subscriptions.b": """
<p>Pausely is free to download and use. <strong>Pausely Premium</strong> unlocks additional features and is sold in five forms, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Premium Monthly</strong> — an auto-renewing subscription, billed monthly.</li>
  <li><strong>Premium Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered.</li>
  <li><strong>Premium Lifetime</strong> — a one-time purchase that does not renew.</li>
  <li><strong>Premium Family Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered, for up to six people through Family Sharing.</li>
  <li><strong>Premium Family Lifetime</strong> — a one-time purchase that does not renew, for up to six people through Family Sharing.</li>
</ul>
<p>The two family plans are shared through Apple's <strong>Family Sharing</strong> with up to five other members of your family group. Each person gets Premium in their own copy of Pausely, on their own device; no rules, apps, history or other data are shared between them. The other three are for you alone and are not shared.</p>
<p>Payment is charged to your Apple ID at confirmation of purchase. A free trial converts to a paid subscription unless you cancel at least 24 hours before the trial ends. Subscriptions renew automatically at the same price and period unless auto-renew is turned off at least 24 hours before the end of the current period; renewal is charged within the 24 hours before that period ends. You can manage or cancel a subscription in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; cancellation takes effect at the end of the current period, and no partial refund is given for the unused part of a period. Refunds are handled by Apple under Apple's policies. Use {K_restore} in the app to recover Premium on a new device.</p>
<p><strong>If a subscription lapses</strong>, nothing you have already set up is removed: every rule keeps running and stays editable, and your chosen pause keeps working. Only the ability to add more Premium content closes. The set of Premium features may change over time; we will not remove a feature from an active subscription without notice.</p>
""",
"t.licence.h": "8. Licence and intellectual property",
"t.licence.b": """
<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to install and use Pausely on an iPhone or iPad you own or control, in accordance with these Terms and the App Store's usage rules. Pausely, its name, design, artwork, text and code are owned by {COMPANY} and protected by copyright and other laws. You may not copy, modify, distribute, sell, lease, reverse-engineer or create derivative works from the app except where the law expressly allows it.</p>
""",
"t.use.h": "9. Acceptable use",
"t.use.b": """
<p>You agree not to use Pausely in any way that is unlawful, that interferes with the app or Apple's services, that attempts to bypass the App Store's purchase mechanisms, or that installs it on a device you are not entitled to manage. You agree not to use it to restrict or monitor another person without their informed consent.</p>
""",
"t.termination.h": "10. Termination",
"t.termination.b": """
<p>You may stop using Pausely at any time by deleting it. We may suspend or end your licence if you breach these Terms. Sections 5, 6, 8, 11, 12 and 14 survive termination. Deleting the app does not cancel an active subscription — cancel it in your App Store settings.</p>
""",
"t.warranty.h": "11. Warranties and liability",
"t.warranty.b": """
<p>Pausely is provided "as is" and "as available", without warranties of any kind, express or implied, including that it will block any app in every circumstance, that it will be uninterrupted or error-free, that anything the AI reflection writes will be accurate or useful, or that it will change your habits. To the fullest extent permitted by law, {COMPANY} shall not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of data, arising from your use of or inability to use the app — including any consequence of a shield that did or did not appear, of a strict-mode session you chose to start, or of anything the AI reflection produced. Where liability cannot be excluded, it is limited to the amount you paid us for Premium in the twelve months before the claim. Nothing in these Terms limits rights you have as a consumer that cannot be waived.</p>
""",
"t.apple.h": "12. Apple",
"t.apple.b": """
<p>Pausely is distributed through the Apple App Store. These Terms are between you and {COMPANY}, not Apple. Apple has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to it, including product-liability, legal-compliance or intellectual-property claims. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them against you. Where these Terms are silent, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a> applies. You represent that you are not in a country subject to a U.S. government embargo or listed as a prohibited party, and you must comply with any applicable third-party terms when using the app.</p>
""",
"t.changes.h": "13. Changes to these Terms",
"t.changes.b": """
<p>We may update these Terms from time to time. The date at the top will change when we do, and material changes will be noted in the app's release notes. Continued use after an update means you accept the revised Terms.</p>
""",
"t.law.h": "14. Governing law",
"t.law.b": """
<p>These Terms are governed by the laws of Pakistan, where {COMPANY} operates, without regard to conflict-of-law provisions. Where the law of your country of residence gives you protections that cannot be contracted out of, those protections apply.</p>
""",
"t.contact.h": "15. Contact",
"t.contact.b": """
<p>Questions about these Terms: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Your data",
"d.h1": "Delete your data",
"d.sub": "Everything Pausely itself knows is on your device. Here is how to erase it, what happens to your subscription, and what is kept anywhere else.",
"d.meta": 'See also the <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"d.where.h": "What is stored where",
"d.where.b": """
<p class="lead">Pausely has no account, and its server keeps no record of anyone. Everything Pausely itself holds is on your device, and you can erase it without asking us.</p>
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Rules, pause history, streak, journal, check-ins, alternatives, settings</td><td>The app's private storage on your device</td><td>{RESET}, or delete the app</td></tr>
<tr><td>Minutes in the apps you chose — for your goal, your limits, the short-video estimate and time banners</td><td>The app's private storage on your device, for up to sixty days</td><td>{RESET}, or delete the app. Switching time banners off clears theirs</td></tr>
<tr><td>Your app selection</td><td>Opaque Screen Time tokens in the app's private storage</td><td>Same as above; revoking Screen Time access in iOS Settings also ends every shield</td></tr>
<tr><td>Widget snapshot</td><td>A small file of counts and dates on your device</td><td>Removed with the reset and with the app</td></tr>
<tr><td>Premium entitlement</td><td>Your Apple ID (Apple) and a copy of its status on your device</td><td>Managed in your App Store settings — see below</td></tr>
<tr><td>What Meta's SDK sent — installs, launches, purchases, the kind of device and the identifier it made up</td><td>Meta, under <a href="https://www.facebook.com/privacy/policy/">Meta's Privacy Policy</a>. The identifier itself is kept in the app's storage on your device</td><td>Deleting the app deletes the identifier, and a new install starts with a new one. For what Meta holds, see Meta's policy</td></tr>
<tr><td>What you typed into an AI reflection</td><td>Your device only, when Apple Intelligence wrote the reflection. When OpenAI wrote it: our server stores no prompt and no reply; OpenAI keeps inputs and outputs for up to 30 days (Google, for earlier versions: up to 24 hours)</td><td>Nothing to delete on our side. Switch the feature off in {K_settings} → {K_ai_reflection} and nothing more is ever sent</td></tr>
<tr><td>An account, a profile, anything with your name on it</td><td>—</td><td>There is none. We never had one to delete.</td></tr>
</table></div>
""",
"d.inapp.h": "Erase it in the app",
"d.inapp.b": """
<ol class="steps">
  <li><div>Open Pausely and go to {K_settings}.</div></li>
  <li><div>Tap {K_your_data}, then {K_reset_all}.</div></li>
  <li><div>Confirm. Every pause, win, rule, journal entry and check-in is erased, the shields come down, the schedules are withdrawn, and the app starts again from setup.</div></li>
</ol>
<div class="callout warm"><span class="tile">{lock}</span><div><strong>It refuses while strict mode is running.</strong> That is the one commitment you asked the app to hold you to. Wait for the session to end at the time you chose, then reset.</div></div>
""",
"d.uninstall.h": "Delete the app",
"d.uninstall.b": """
<p>Deleting Pausely from your device removes all of its data with it, including the Screen Time tokens, and ends every shield immediately. If the app is included in an iCloud or encrypted local backup, that copy belongs to your Apple ID and is governed by Apple's terms; we have no access to it.</p>
""",
"d.subscription.h": "Your subscription",
"d.subscription.b": """
<p>Neither resetting data nor deleting the app cancels a subscription — it belongs to your Apple ID, not to the app. Cancel it in <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; it stays active until the end of the current period. Refunds are handled by <a href="https://support.apple.com/billing">Apple Support</a>. A lifetime purchase does not renew and needs nothing cancelled.</p>
""",
"d.email.h": "Ask us",
"d.email.b": """
<p>If you would like written confirmation of what we hold about you, or have a question about what Meta's SDK sent, write to {MAIL} from any address. We will reply within 30 days. Please do not send us your journal, check-ins or screenshots of them — we do not need them to answer.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Nothing to see here.",
"nf.sub": "Which, for once, is not the point.",
"nf.cta": "Back to Support",
"nf.b": 'That page isn\'t here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.',

}
