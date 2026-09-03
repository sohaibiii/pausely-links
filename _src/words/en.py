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
"ui.date": "3 September 2026",
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

"meta.support.title": "Pausely — Support",
"meta.support.desc": "Official support for Pausely, the app that puts a pause in front of the apps you chose. How it works, requirements, FAQ and contact.",
"meta.about.title": "Pausely — A breath before the scroll",
"meta.about.desc": "Pausely puts a small speed bump between you and the apps that eat your day. No account, and nothing leaves your phone unless you ask it to.",
"meta.privacy.title": "Privacy Policy — Pausely",
"meta.privacy.desc": "What Pausely keeps on your device, the one optional feature that sends anything at all, and what it sends.",
"meta.terms.title": "Terms of Use — Pausely",
"meta.terms.desc": "Terms of Use (EULA) for Pausely: what the app is and is not, how Premium is billed, and what strict mode asks of you.",
"meta.data.title": "Delete your data — Pausely",
"meta.data.desc": "How to erase everything Pausely holds — all of it on your device — and what happens to your subscription.",
"meta.nf.title": "Not found — Pausely",
"meta.nf.desc": "Page not found.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Support",
"s.h1": "Help with Pausely",
"s.sub": "A breath before the scroll. Pausely stands in front of the apps you chose and asks for ten seconds first. This page covers how it works, what it needs, and how to reach us.",
"s.cta": "Read the FAQ",
"s.meta": 'No account · nothing leaves your device unless you ask it to · <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

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
  <li><span class="tile">{sparkle}</span><div><b>The AI reflection, if you want it</b><span>Off until you switch it on. It turns "why are you opening this?" into a short exchange, and writes a weekly note about your week. It is the one part of Pausely that uses the network — see <a href="{BASE}{L}/privacy/#ai">Privacy</a>.</span></div></li>
</ul>
""",

"s.requirements.h": "Requirements",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Device</th><td><strong>iPhone or iPad</strong> running <strong>iOS 17 or iPadOS 17</strong> or newer. One app, one layout, both devices.</td></tr>
<tr><th>Permission</th><td><strong>Screen Time</strong> access, granted once during setup through Apple's own prompt. Pausely uses Apple's Screen Time framework — the same system behind iOS's built-in app limits — and Apple, not Pausely, is what actually blocks an app.</td></tr>
<tr><th>Account</th><td>None. There is no sign-up, no email field and no password anywhere in the app.</td></tr>
<tr><th>Internet</th><td>Not needed. Every pause, rule, chart and journal entry works offline. Two things use the network: Apple's own traffic when you buy or restore Premium, and the AI reflection — which is off until you switch it on.</td></tr>
<tr><th>Notifications</th><td>Optional, and local to the device. Pausely uses them to hand you from the block screen into the pause, and to ask afterwards how a session left you feeling. There is no push server.</td></tr>
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
<dd>No. It never observes your browsing, messages or activity inside any app. It records only its own events — that a pause was shown, and what you chose — and keeps those on your device.</dd>
<dt>What is the AI reflection, and is it on?</dt>
<dd>It is off, until you switch it on. When you do, one pause becomes a short exchange: you type why you are opening the app, and a question comes back. It also writes a short note about your week. Those words go to Pausely's own server and on to Google, which runs the model — never your journal, never your check-ins, never which apps you chose. {K_settings} → {K_ai_reflection} → {K_what_is_sent} lists every field, and switching it off returns the app to making no network calls at all.</dd>
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
"a.f6.h": "Nothing leaves your device.",
"a.f6.p": 'No account, no analytics, no advertising. Pausely cannot even read which apps you picked — Apple keeps that. One optional feature sends anything at all, and it starts switched off. <a href="{BASE}{L}/privacy/">How that works.</a>',

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
"p.sub": "Pausely has no account and no analytics. Everything it records stays on your device — with one optional feature, switched off until you ask for it, that sends the words you type into a single screen. This page is about exactly where that line is.",
"p.meta": "Effective {DATE} · applies to the Pausely app for iPhone and iPad, and to this site",

"p.summary.h": "The short version",
"p.summary.b": """
<p class="lead">Pausely has no account, no analytics, no advertising and no third-party code of any kind. <strong>With the AI reflection switched off — which is how every install starts — it makes no network calls at all</strong>, and everything it knows is written to your device and stays there.</p>
<p><strong>Switching the AI reflection on is the one thing that changes that</strong>, and it changes only one thing: the words you type into that one pause leave your device, together with four small facts about the moment. Your journal never leaves. Your check-ins never leave. Which apps you chose never leaves — Pausely cannot read that even on your own device.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Pausely does not know which apps you chose to pause. Apple's Screen Time gives it opaque tokens that only your device can interpret. There is no app name, no identifier, and nothing to send.</div></div>
<p style="margin-top:16px">This policy applies to the Pausely app for iPhone and iPad, published by {COMPANY}, and to this website. It says the same thing as the privacy label on Pausely's App Store page: <strong>User content, not linked to your identity, used only to make the app work — and no tracking.</strong> That single label exists because of the AI reflection; every other category is <em>Data Not Collected</em>.</p>
""",

"p.collect.h": "What we collect",
"p.collect.b": """
<p>"Collect", in Apple's sense and in ours, means transmitting data off the device and keeping it somewhere that is not transient. By that measure Pausely collects one thing, in one case, and only if you asked for it.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Collected?</th><th>What that means</th></tr>
<tr><td>Contact info</td><td>No</td><td>There is no account, no sign-in and no email field anywhere in the app.</td></tr>
<tr><td>Identifiers</td><td>No</td><td>No user ID, no device ID, no advertising identifier. Pausely never asks for App Tracking Transparency because it has nothing to ask about.</td></tr>
<tr><td>Usage data</td><td>No</td><td>No analytics SDK and no product-interaction events. Nothing is counted anywhere except on your device, for your own progress screen.</td></tr>
<tr><td>User content</td><td><strong>Only the AI reflection</strong></td><td>Your journal, your check-ins and your custom alternatives are stored on the device and nowhere else. If — and only if — you switch the AI reflection on, the words you type into <em>that one screen</em> are sent, so that a question can come back. Nothing else you write is ever sent.</td></tr>
<tr><td>Purchases</td><td>No</td><td>Payment is Apple's, in the App Store sheet. Pausely never sees a card and sends nothing about the purchase anywhere.</td></tr>
<tr><td>Location, health, contacts, browsing, search, diagnostics</td><td>No</td><td>Pausely does not link the frameworks that would read them and has no crash or performance reporter of its own.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> none. Pausely does not link anything about you with data from other companies' apps or websites, and shares nothing with data brokers or advertisers. There is no advertising in the app and no SDK that could carry any.</p>
""",

"p.device.h": "What stays on your device",
"p.device.b": """
<p>Pausely stores the following in its own private storage on your iPhone or iPad, protected by your device's passcode and encryption. None of it is uploaded, backed up by us, or visible to us.</p>
<ul>
  <li><strong>Your app selection</strong> — as opaque Screen Time tokens Pausely cannot read (see below).</li>
  <li><strong>Your rules and schedules</strong> — the names you give them, their hours and their pause.</li>
  <li><strong>Pause outcomes</strong> — that a pause was shown, when, and whether you walked away, went in, or chose an alternative. This is what the progress screen, the streak and the chart are made of.</li>
  <li><strong>What you write</strong> — journal entries, the words you type on the pause screen, mood check-ins after a session, and the names of custom alternatives.</li>
  <li><strong>Settings</strong> — your chosen pause, strict-mode state, alternatives, your language, and preferences.</li>
  <li><strong>Your Premium entitlement</strong> — a tier and an expiry date, so the app knows what to unlock.</li>
</ul>
<p>If you use iCloud Backup or an encrypted local backup, Apple may include Pausely's data in that backup under your own Apple ID and Apple's privacy terms. We have no access to it.</p>
""",

"p.screentime.h": "Screen Time and your app selection",
"p.screentime.b": """
<p>Pausely is built on Apple's Screen Time framework (Family Controls, Managed Settings and Device Activity). You grant it access once, through Apple's own prompt, and can revoke it at any time in {K_settings} → {K_screen_time}.</p>
<p>When you pick apps, Apple's picker returns <strong>tokens</strong>: values that identify the app to iOS but mean nothing to Pausely and nothing outside your device. Pausely stores those tokens so it can ask iOS to shield the apps you chose. It never receives a bundle identifier or an app name, and it could not report one if it wanted to. Where it needs to compare tokens between its own components it compares one-way hashes of them, never the tokens themselves.</p>
<p>Pausely does not observe your browsing, your messages, or what you do inside any app. iOS itself draws the block screen and enforces the shield. Pausely learns only that its own pause was shown and what you chose on it.</p>
""",

"p.ai.h": "The AI reflection — the one thing that leaves",
"p.ai.b": """
<p class="lead">This is an optional Premium feature. <strong>It is off when you install Pausely and stays off until you switch it on</strong>, and switching it off again returns the app to making no network calls at all.</p>
<p>With it on, one pause becomes a short exchange: you type why you are opening the app, and a question comes back rather than a lecture. Once a week it also writes a short note about how your week went.</p>
<h3>What is sent</h3>
<ul>
  <li>The <strong>display name of the app you are opening</strong> — the name already on your screen at that moment.</li>
  <li><strong>Three numbers</strong>: how many times you have opened it today, the time on the clock, and how long your streak is.</li>
  <li><strong>The words you type into that screen</strong>, in that moment.</li>
</ul>
<p>The weekly note sends less: counts for the week and nothing else. No app names appear in it at all.</p>
<h3>What is never sent</h3>
<ul>
  <li><strong>Your journal.</strong> It is the one place you write for nobody, and it never leaves the device.</li>
  <li><strong>Your check-ins</strong>, moods, or any note attached to them.</li>
  <li><strong>Your app selection</strong> — which apps you protect, or how many — and never a Screen Time token, a token hash or a bundle identifier.</li>
  <li><strong>Your rules, schedules or strict-mode state.</strong></li>
  <li><strong>Anything that identifies you.</strong> There is no account, no user ID and no advertising identifier to send. The request carries an Apple App Attest assertion, which tells our server that it is talking to a genuine copy of Pausely — it is scoped to the app, not to you, and does not follow you between requests.</li>
</ul>
<h3>Where it goes, and how long it is kept</h3>
<p>Your words go to <strong>Pausely's own server</strong>, and on to <strong>Google</strong>, which runs the model. Pausely never calls a model vendor's API from your device, and there is no API key inside the app to be extracted.</p>
<p><strong>Pausely's server stores nothing per request</strong> — no prompt, no reply, no context. Its logs record the shape of a request (a timestamp, how long it took, whether it succeeded) and never its contents. <strong>Google keeps inputs and outputs for up to 24 hours</strong> to reduce latency, and may examine prompts to check for abuse, under its standard Cloud terms. <strong>Google does not use any of it to train its models.</strong></p>
<p>{K_settings} → {K_ai_reflection} → {K_what_is_sent} lists every field in the app itself, in the same words as this page.</p>
""",

"p.purchases.h": "Purchases",
"p.purchases.b": """
<p>Premium is sold through Apple's App Store using StoreKit. The transaction is between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Apple tells Pausely whether a purchase is active — nothing else — and Pausely tells Apple nothing about how you use the app. No usage data, no journal, no app selection and no identifier of ours travels with a purchase.</p>
""",

"p.notifications.h": "Notifications, widgets and the Lock Screen",
"p.notifications.b": """
<p><strong>Notifications</strong> are optional and are generated on your device. Pausely uses them to hand you from the block screen into the pause, and to ask afterwards how a session left you feeling. No notification is sent from a server — there is no push server, no tips, no streak nudges and no marketing.</p>
<p><strong>Widgets and the Live Activity</strong> show counts and dates — today's wins, your streak, time reclaimed, and how long an access window has left. They deliberately do not have Screen Time access and never see which apps you blocked. A Lock Screen countdown names the <em>rule</em> you wrote ("Bedtime"), never the app, because a Lock Screen is readable by anyone holding the device.</p>
""",

"p.third.h": "Third parties",
"p.third.b": """
<p>Pausely contains <strong>no third-party code</strong>: no analytics, no advertising, no crash reporter, no SDKs. Two other parties are involved, and only these two:</p>
<ul>
  <li><strong>Apple</strong> operates the App Store, processes purchases, enforces the Screen Time shield, and — if you have opted in to sharing with developers — may share crash logs with us under its own policy.</li>
  <li><strong>Google</strong> runs the model behind the AI reflection, and only for as long as you have that feature switched on. It receives what is listed above and nothing else, and it does not use it to train its models.</li>
</ul>
<p>We do not sell or rent personal data to anyone, and we share nothing with data brokers or advertisers.</p>
""",

"p.delete.h": "Deleting your data",
"p.delete.b": """
<p>Everything Pausely holds is erasable from inside the app, without asking us:</p>
<div class="callout"><span class="tile">{trash}</span><div>{RESET}<br><span class="small">Empties every pause, win, rule, journal entry and check-in, takes the shields down, withdraws the schedules and starts you at the beginning. It refuses while strict mode is running — the one commitment you asked the app to hold you to — and it does not touch your subscription, which belongs to your Apple ID.</span></div></div>
<p style="margin-top:16px">Deleting the app removes all of its data from the device as well. On our side there is nothing to delete: the server keeps no record of a request once it has answered it. You are welcome to write to us anyway — see the <a href="{BASE}{L}/delete-data/">Your data</a> page.</p>
""",

"p.rights.h": "Your rights",
"p.rights.b": """
<p>Wherever you live — including under the GDPR, the UK GDPR and the CCPA/CPRA — you have rights to access, correct, export, restrict and erase personal data a company holds about you, and to complain to a supervisory authority. Pausely holds no profile of you and keeps nothing after a reflection is answered, so there is nothing on our side to produce or delete; the data on your device is already in your hands, and the app's own controls exercise every one of those rights for you. If you believe otherwise, write to {MAIL} and we will respond.</p>
""",

"p.children.h": "Children",
"p.children.b": """
<p>Pausely is a self-directed tool for the person using the device. It is not a parental-control product and does not manage another person's device. It is not directed at children under 13 (or the age of digital consent where you live), and we do not knowingly collect personal information from anyone — of any age.</p>
""",

"p.changes.h": "Changes to this policy",
"p.changes.b": """
<p>We may update this policy as the app changes. The date at the top moves when we do, and material changes will be noted in the app's release notes. The last substantive change was the arrival of the AI reflection, which added the one case in which anything leaves your device. Continued use of Pausely after a change means you accept the revised policy.</p>
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
<p>Everything Pausely records is stored on your device — see the <a href="{BASE}{L}/privacy/">Privacy Policy</a> for the single, optional exception. You are responsible for your device, its passcode and its backups. If you delete the app, reset all data, or lose the device without a backup, your rules, journal and history are gone, and we have no copy to restore. Your Premium purchase is separate: it belongs to your Apple ID and can be restored on any device signed into it.</p>
<p>What you write into Pausely is yours. We claim no rights over it, and we receive none of it unless you switch on the AI reflection, which sends only what section 6 and the Privacy Policy describe.</p>
""",
"t.ai.h": "6. The AI reflection",
"t.ai.b": """
<p>The AI reflection is an <strong>optional</strong> Premium feature that is <strong>off until you switch it on</strong>. With it on, the words you type into that one pause are sent to our server and on to Google, which generates a response. What is sent, what is never sent and how long anything is kept are set out in the <a href="{BASE}{L}/privacy/#ai">Privacy Policy</a>, and listed inside the app at {K_settings} → {K_ai_reflection} → {K_what_is_sent}.</p>
<p>The response is <strong>generated text</strong>. It may be wrong, unhelpful, or not what you expected, and it is <strong>not advice of any kind</strong> — see section 3. Do not type anything into it you would not want processed by a third party, and do not rely on it for any decision that matters. We do not guarantee the availability, latency or continuity of the feature, and we may change the model behind it, limit its use, or withdraw it, without that affecting the rest of the app.</p>
<p>You agree not to use the feature to generate unlawful, abusive or infringing content, or to attempt to extract the underlying model or its instructions. Switching the feature off stops all of it and returns the app to making no network calls at all.</p>
""",
"t.subscriptions.h": "7. Premium, subscriptions and billing",
"t.subscriptions.b": """
<p>Pausely is free to download and use. <strong>Pausely Premium</strong> unlocks additional features and is sold in three forms, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Premium Monthly</strong> — an auto-renewing subscription, billed monthly.</li>
  <li><strong>Premium Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered.</li>
  <li><strong>Premium Lifetime</strong> — a one-time purchase that does not renew.</li>
</ul>
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
"d.sub": "Everything Pausely knows is on your device. Here is how to erase it, what happens to your subscription, and what — nothing — is left on our side.",
"d.meta": 'See also the <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"d.where.h": "What is stored where",
"d.where.b": """
<p class="lead">Pausely has no account, and its server keeps no record of anyone. Everything it holds is on your device, and you can erase it without asking us.</p>
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Rules, pause history, streak, journal, check-ins, alternatives, settings</td><td>The app's private storage on your device</td><td>{RESET}, or delete the app</td></tr>
<tr><td>Your app selection</td><td>Opaque Screen Time tokens in the app's private storage</td><td>Same as above; revoking Screen Time access in iOS Settings also ends every shield</td></tr>
<tr><td>Widget snapshot</td><td>A small file of counts and dates on your device</td><td>Removed with the reset and with the app</td></tr>
<tr><td>Premium entitlement</td><td>Your Apple ID (Apple) and a copy of its status on your device</td><td>Managed in your App Store settings — see below</td></tr>
<tr><td>What you typed into an AI reflection</td><td>Nowhere, once it has been answered. Our server stores no prompt and no reply; Google keeps inputs and outputs for up to 24 hours</td><td>Nothing to delete. Switch the feature off in {K_settings} → {K_ai_reflection} and nothing more is ever sent</td></tr>
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
<p>If you would like written confirmation that we hold nothing about you, or you believe we do, write to {MAIL} from any address. We will reply within 30 days. Please do not send us your journal, check-ins or screenshots of them — we do not need them to answer.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Nothing to see here.",
"nf.sub": "Which, for once, is not the point.",
"nf.cta": "Back to Support",
"nf.b": 'That page isn\'t here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.',

}
