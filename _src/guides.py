# -*- coding: utf-8 -*-
"""The guides. One search problem per page.

Each guide gives the free way first (the settings iOS already has), says plainly
where that stops working, and only then says what Pausely does about it. A guide
that is only an advert earns nothing, from readers or from search engines.

`body` is HTML and `{BASE}` is the site root. Names of iOS settings are written
the way iOS writes them; where Apple renamed one between versions, both names
are given. Menus inside other companies' apps move often, so those steps say
where to look and not only what to tap. No borrowed statistics, and no long
dashes anywhere (site_pages.check fails the build on one).
"""

GUIDES = [
    {
        "slug": "how-to-stop-doomscrolling",
        "ct": "stop-doomscrolling",
        "topic": "Habits",
        "minutes": 7,
        "title": "How to stop doomscrolling on iPhone: 7 things that work",
        "seo_title": "How to Stop Doomscrolling on iPhone: 7 Things That Work",
        "description": "Seven practical ways to stop doomscrolling on an iPhone, from moving one icon to setting limits that hold, with exact steps and what each one can't do.",
        "blurb": "Seven changes, lightest first. Most take under a minute and none of them need willpower at midnight.",
        "standfirst": "Doomscrolling is rarely a decision. Your thumb opens the app before you have noticed, and "
                      "twenty minutes go by. So the fixes that work are the ones that interrupt the opening, not "
                      "the ones that ask you to be stronger. Here are seven, lightest first.",
        "box_title": "A breath before the scroll",
        "box_text": "Pausely puts a ten second pause in front of the apps you choose, every time you open one. "
                    "Then you decide. Two apps are free.",
        "body": """
<h2>1. Move the app off your first Home Screen</h2>
<p>The cheapest fix there is. Most opens start with a thumb going to the place the icon has always been.</p>
<ol>
  <li>Press and hold the app's icon and tap <kbd>Edit Home Screen</kbd>.</li>
  <li>Drag it to your last page, or tap the minus and choose <kbd>Remove from Home Screen</kbd>. The app stays on the phone, in the App Library.</li>
</ol>
<p>Now opening it means searching for it by name, which is a small decision. <strong>Where it stops working:</strong> your thumb learns the new route within a week or two.</p>

<h2>2. Turn off the notifications that pull you in</h2>
<p>A lot of scrolling starts with a notification about something that could have waited.</p>
<ol>
  <li>Open <kbd>Settings</kbd>, tap <kbd>Notifications</kbd>, then the app.</li>
  <li>Turn off <kbd>Allow Notifications</kbd>. If that is too much, keep them on and turn off <kbd>Lock Screen</kbd> and <kbd>Banners</kbd>, so they wait quietly in Notification Center.</li>
</ol>
<p>If you still want to hear from the app once or twice a day, <kbd>Scheduled Summary</kbd> on the same screen delivers a batch at times you choose.</p>

<h2>3. Make the screen less interesting</h2>
<p>Feeds are designed around colour. In grey they are noticeably duller, and that is the point.</p>
<ol>
  <li>Open <kbd>Settings</kbd>, then <kbd>Accessibility</kbd>, then <kbd>Display &amp; Text Size</kbd>.</li>
  <li>Tap <kbd>Color Filters</kbd>, turn it on and choose <kbd>Grayscale</kbd>.</li>
</ol>
<p>To switch it quickly, go to <kbd>Accessibility</kbd>, then <kbd>Accessibility Shortcut</kbd>, and tick <kbd>Color Filters</kbd>. Three clicks of the side button now turn grey on and off. <strong>Where it stops working:</strong> photos and maps are worse in grey too, so most people end up turning it on only in the evening.</p>

<h2>4. Set a daily limit, and close the escape hatch</h2>
<p>Screen Time can give an app a daily allowance.</p>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>, and tick the apps.</li>
  <li>Tap <kbd>Next</kbd>, set the time and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time is used, iOS covers the app with a button that offers one more minute, a reminder in 15 minutes, or <kbd>Ignore Limit For Today</kbd>. One tap, and the limit is gone. <a href="{BASE}/guides/why-screen-time-limits-dont-work/">How to make a limit hold</a> has the fix.</p>

<h2>5. Give the evening a closing time</h2>
<p>Late evening is when most people scroll longest. Downtime closes the apps you choose between two times, every night.</p>
<ol>
  <li>In <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>Downtime</kbd>.</li>
  <li>Turn on <kbd>Scheduled</kbd> and set the hours.</li>
  <li>Go back and open <kbd>Always Allowed</kbd> to choose what stays open, such as Phone, Messages and your alarm.</li>
</ol>
<p>The steps for making this one firm are in <a href="{BASE}/guides/block-apps-at-night-on-iphone/">How to block apps at night</a>.</p>

<h2>6. Decide what you will do instead</h2>
<p>Closing an app leaves a gap, and the gap gets filled by the next app unless something else is ready. Pick two or three small things that take five to ten minutes: a walk round the block, a few pages of a book, a glass of water, a message to someone you like. Put the book where the phone usually sits.</p>
<p>This sounds too simple to matter. It is the step people skip, and the one that makes the others last.</p>

<h2>7. Put a pause in front of the app</h2>
<p>Everything above either hides the app or cuts it off after the time is spent. None of it catches the moment that matters, which is the half second when you open it without deciding to.</p>
<p>That is what Pausely is for. You choose the apps. After that, tapping one doesn't open it straight away. You see how many times you have opened it today, you breathe for ten seconds, and then you choose: <kbd>I changed my mind</kbd>, or continue for a few minutes. If you go in, the pause is back when the time is up.</p>
<p>It doesn't lock you out, and it doesn't lecture. It turns a reflex back into a choice. Two apps and the breathing pause are free.</p>

<div class="note"><b>If you only do one thing:</b> do number 1 tonight. It takes thirty seconds and costs nothing.</div>
""",
    },
    {
        "slug": "how-to-block-tiktok-on-iphone",
        "ct": "block-tiktok",
        "topic": "Blocking apps",
        "minutes": 6,
        "title": "How to block TikTok on iPhone (4 ways, lightest to firmest)",
        "seo_title": "How to Block TikTok on iPhone: 4 Ways That Work",
        "description": "Four ways to block TikTok on an iPhone: TikTok's own limit, a Screen Time limit, a full block of the app and tiktok.com, and a pause before it opens.",
        "blurb": "From TikTok's own timer to a full block of the app and the website, and where each one gives way.",
        "standfirst": "TikTok lives in two places on your phone: the app, and tiktok.com in Safari. Here are four "
                      "ways to block it, from a soft reminder to a block with no way round, with the steps for "
                      "each and the point where it stops holding.",
        "box_title": "Not ready to delete it?",
        "box_text": "Pausely leaves TikTok on your phone and asks for ten seconds every time you open it. Most "
                    "days that is the difference. Two apps are free.",
        "body": """
<p>Before you start, decide what you want. If you want TikTok gone, go to option 3. If you still enjoy it and only want to stop losing whole evenings, options 1, 2 and 4 are closer.</p>

<h2>Option 1: TikTok's own screen time limit</h2>
<p>TikTok has a daily limit built in. Open your profile, tap the menu at the top, and go to <kbd>Settings and privacy</kbd>. Look for <kbd>Screen time</kbd> (TikTok moves this section from time to time), then <kbd>Daily screen time</kbd>, and set a number of minutes. The same section has break reminders and sleep reminders.</p>
<p><strong>Where it stops working.</strong> When the time is up, TikTok asks for a passcode you set yourself. You know the passcode. It is a reminder, not a block.</p>

<h2>Option 2: A Screen Time limit on the app</h2>
<p>This uses Screen Time, which is already on your iPhone, so the limit sits outside TikTok.</p>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Open the <kbd>Social</kbd> category and tick TikTok.</li>
  <li>Scroll to the bottom of the same list, open <kbd>Websites</kbd>, tap <kbd>Add Website</kbd> and type <kbd>tiktok.com</kbd>. Now one limit covers the app and the site together.</li>
  <li>Tap <kbd>Next</kbd>, set the time (the smallest is 1 minute a day) and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time runs out, iOS covers the app and offers one more minute, a reminder in 15 minutes, or <kbd>Ignore Limit For Today</kbd>. That last one is a single tap. To remove it, set a Screen Time passcode and turn on <kbd>Block at End of Limit</kbd>. It only really holds if someone else chooses the passcode.</p>

<h2>Option 3: Remove it completely</h2>
<p>Three steps: delete the app, stop it coming back, and block the website.</p>
<ol>
  <li>Press and hold the TikTok icon, tap <kbd>Remove App</kbd>, then <kbd>Delete App</kbd>. Your account and your videos stay on TikTok's side.</li>
  <li>In <kbd>Settings</kbd>, go to <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on. Tap <kbd>iTunes &amp; App Store Purchases</kbd>, then <kbd>Installing Apps</kbd>, and choose <kbd>Don't Allow</kbd>. The App Store disappears from your Home Screen until you change this back.</li>
  <li>Still in <kbd>Content &amp; Privacy Restrictions</kbd>, tap <kbd>Content Restrictions</kbd> (on newer versions of iOS this row is called <kbd>App Store, Media, Web &amp; Games</kbd>), then <kbd>Web Content</kbd>, and choose <kbd>Limit Adult Websites</kbd>. Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and enter <kbd>tiktok.com</kbd>.</li>
</ol>
<p><strong>Two side effects to know about.</strong> <kbd>Limit Adult Websites</kbd> also turns on Apple's adult content filter and removes Private Browsing from Safari. And with <kbd>Installing Apps</kbd> off you can't install anything else either, so you will be switching it back on now and then. That moment is when TikTok tends to return.</p>

<h2>Option 4: Keep it, with a pause in front</h2>
<p>For most people the trouble is not TikTok itself. It is opening TikTok forty times a day without deciding to. A block treats every open the same. A pause sorts the ones you meant from the ones you didn't.</p>
<p>With Pausely, tapping TikTok shows you how many times you have opened it today, then asks for a ten second breath. After it you choose: <kbd>I changed my mind</kbd>, or continue for a few minutes. When the time is up, the pause comes back.</p>
<p>If you want it firmer, Premium adds a daily limit that rests the app until tomorrow, rules that block it at the hours you choose, and tiktok.com in Safari.</p>

<h2>Which one should you pick?</h2>
<table>
  <thead><tr><th>You want</th><th>Use</th></tr></thead>
  <tbody>
    <tr><td>A nudge, nothing more</td><td>Option 1</td></tr>
    <tr><td>A daily allowance, set by someone you trust</td><td>Option 2 with a passcode</td></tr>
    <tr><td>TikTok gone from this phone</td><td>Option 3</td></tr>
    <tr><td>To keep it, and open it on purpose</td><td>Option 4</td></tr>
  </tbody>
</table>
""",
    },
    {
        "slug": "how-to-block-instagram-on-iphone",
        "ct": "block-instagram",
        "topic": "Blocking apps",
        "minutes": 6,
        "title": "How to block Instagram on iPhone without deleting your account",
        "seo_title": "How to Block Instagram on iPhone (No Account Deletion)",
        "description": "How to block or limit Instagram on an iPhone: its own daily limit, a Screen Time limit, blocking instagram.com in Safari, and a pause before it opens.",
        "blurb": "Keep the account and the messages. Lose the forty automatic opens a day.",
        "standfirst": "Most people don't want to leave Instagram. They want their messages and their friends' "
                      "photos, without the hour of Reels that comes attached. Here is how to block or limit it "
                      "on an iPhone and keep your account exactly as it is.",
        "box_title": "Open Instagram on purpose",
        "box_text": "Pausely asks for a ten second breath every time you open Instagram, then lets you choose. "
                    "Your account is untouched. Two apps are free.",
        "body": """
<p>None of these steps deletes or deactivates your account. Your profile, followers and messages stay where they are.</p>

<h2>Option 1: Instagram's own daily limit</h2>
<p>Open your profile, tap the menu at the top right, and look for <kbd>Time management</kbd>. On older versions it is under <kbd>Your activity</kbd>, then <kbd>Time spent</kbd>. There you can set a <kbd>Daily limit</kbd>, and a sleep mode that quiets notifications at night.</p>
<p><strong>Where it stops working.</strong> When you reach the limit, Instagram shows a reminder you can dismiss in one tap. It tells you the time. It doesn't stop you.</p>

<h2>Option 2: A Screen Time limit</h2>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Open the <kbd>Social</kbd> category and tick Instagram.</li>
  <li>At the bottom of the same list, open <kbd>Websites</kbd>, tap <kbd>Add Website</kbd> and type <kbd>instagram.com</kbd>, so the limit covers Safari too.</li>
  <li>Tap <kbd>Next</kbd>, set the time and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> The cover that appears when your time is used has <kbd>Ignore Limit For Today</kbd> on it. A Screen Time passcode chosen by someone else, with <kbd>Block at End of Limit</kbd> switched on, closes that door.</p>

<h2>Option 3: Delete the app and use the website</h2>
<p>A popular middle path. Press and hold the icon, tap <kbd>Remove App</kbd>, then <kbd>Delete App</kbd>. Your account is not affected. When you need to check something, sign in at instagram.com in Safari.</p>
<p>The website does messages and the feed, and it is a little slower and clumsier than the app. That clumsiness is the feature: people tend to check and leave. <strong>Where it stops working:</strong> Reels play on the website too, and the app is twenty seconds away in the App Store.</p>

<h2>Option 4: Block instagram.com in Safari</h2>
<p>If you have deleted the app and the website has become the new habit:</p>
<ol>
  <li>Open <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on.</li>
  <li>Tap <kbd>Content Restrictions</kbd>. On newer versions of iOS this row is called <kbd>App Store, Media, Web &amp; Games</kbd>.</li>
  <li>Tap <kbd>Web Content</kbd> and choose <kbd>Limit Adult Websites</kbd>.</li>
  <li>Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and enter <kbd>instagram.com</kbd>.</li>
</ol>
<p>This also turns on Apple's adult content filter and removes Private Browsing from Safari, which surprises some people.</p>

<h2>Option 5: Keep the app, and put a pause in front of it</h2>
<p>The options above are all or nothing, and Instagram is rarely all bad. You open it to answer a message and surface forty minutes later. The message was fine. The opening without thinking was the problem.</p>
<p>Pausely works on that moment. Tap Instagram and you see how many times you have opened it today, then a ten second breath. After it you choose: <kbd>I changed my mind</kbd>, or continue for a few minutes to answer that message. When the time is up, the pause is back, which is usually when you notice you had drifted into Reels.</p>
<p>With Premium you can also see about how many short videos your time came to. It is an estimate, and it tends to land.</p>

<div class="note"><b>A note on messages.</b> If people reach you on Instagram, tell the ones who matter where else to find you before you block anything. It removes the best excuse for opening it.</div>
""",
    },
    {
        "slug": "why-screen-time-limits-dont-work",
        "ct": "screen-time-limits",
        "topic": "Screen Time",
        "minutes": 5,
        "title": "Why you keep tapping Ignore Limit, and how to make a Screen Time limit hold",
        "seo_title": "Screen Time Limits Not Working? Stop Tapping Ignore Limit",
        "description": "Why Screen Time limits are so easy to ignore on iPhone, how to remove the Ignore Limit button with a passcode, and what to use when a limit is the wrong tool.",
        "blurb": "The Ignore Limit button is one tap. Here is how to remove it, and why a limit may be the wrong tool anyway.",
        "standfirst": "You set a one hour limit. The hour ends, a grey screen appears, and your thumb has tapped "
                      "Ignore Limit For Today before you have read it. You are not unusually weak. The limit was "
                      "built with a door in it. Here is how to close the door.",
        "box_title": "A pause at the start, not a wall at the end",
        "box_text": "Pausely asks for ten seconds every time you open an app you chose, before any time is spent. "
                    "Two apps are free.",
        "body": """
<h2>Why the limit gives way</h2>
<p>A Screen Time limit does nothing at all until your time is used. Then it interrupts you at the worst possible moment, when you are mid scroll and want to continue, and offers three buttons: <kbd>One More Minute</kbd>, <kbd>Remind Me in 15 Minutes</kbd> and <kbd>Ignore Limit For Today</kbd>.</p>
<p>The person tapping that button is the tired, mid scroll version of you, and the calm version who set the limit isn't in the room. After a week the tap is automatic, and the limit has become one more thing you dismiss.</p>

<h2>Fix 1: Take the button away</h2>
<p>iOS can remove the ignore option, but only when Screen Time has a passcode.</p>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>.</li>
  <li>Tap <kbd>Lock Screen Time Settings</kbd> (older versions call it <kbd>Use Screen Time Passcode</kbd>) and set a four digit code.</li>
  <li>Go to <kbd>App Limits</kbd>, tap your limit, and turn on <kbd>Block at End of Limit</kbd>.</li>
</ol>
<p>Now the cover offers <kbd>Ask For More Time</kbd>, which gives one more minute and then needs the passcode.</p>
<p><strong>The catch.</strong> You know the passcode. Typing four digits is slower than one tap, and that helps a little, but not for long. It works properly when somebody else sets the code and doesn't tell you: a partner, a friend, a sibling. If you live alone, write it on paper and put the paper somewhere annoying to reach.</p>

<h2>Fix 2: Make the limit smaller than you think</h2>
<p>A two hour limit is spent by early evening, exactly when you most want the app, and that is when you override it. Try a short limit that you expect to hit early, such as 20 minutes, and treat hitting it as the signal that today's ration is done. Limits reset at midnight.</p>

<h2>Fix 3: Use a schedule instead of a budget</h2>
<p>Budgets need you to keep track. Schedules don't. Downtime closes the apps you choose between two times every day, such as 10 p.m. to 7 a.m. Find it in <kbd>Settings</kbd>, <kbd>Screen Time</kbd>, <kbd>Downtime</kbd>. With a passcode set, turn on <kbd>Block at Downtime</kbd> so it can't be waved away. <a href="{BASE}/guides/block-apps-at-night-on-iphone/">The full steps are here.</a></p>

<h2>When a limit is the wrong tool</h2>
<p>A limit measures minutes. But for many people the trouble is not the total. It is the number of times they open the app without meaning to: in a queue, between tasks, in the middle of a sentence. Twenty opens of two minutes each stay well inside most limits, and still break up a whole day.</p>
<p>For that, the interruption has to come at the start, before the feed loads, when stopping is easy.</p>
<p>That is how Pausely works. You choose the apps. Each time you tap one you see how many times you have opened it today, and you breathe for ten seconds. Then you choose: <kbd>I changed my mind</kbd>, or continue for a few minutes. There is no ignore button to learn, because the pause is short enough that you don't need one.</p>
<p>And if you do want a hard stop as well, Premium has daily limits that rest an app until tomorrow, and a strict mode that can't be undone until the time you chose, not even by you.</p>

<table>
  <thead><tr><th></th><th>Screen Time limit</th><th>Pausely</th></tr></thead>
  <tbody>
    <tr><td>When it steps in</td><td>After your time is used</td><td>Every time you open the app</td></tr>
    <tr><td>What it asks</td><td>Nothing, or a passcode</td><td>Ten seconds, then a choice</td></tr>
    <tr><td>How you get past it</td><td>One tap on Ignore Limit</td><td>By deciding to go in, for a set time</td></tr>
    <tr><td>Cost</td><td>Free, built in</td><td>Free for two apps</td></tr>
  </tbody>
</table>
<p>They also work together. Pausely is built on the same Screen Time system, and nothing stops you using both.</p>
""",
    },
    {
        "slug": "block-apps-at-night-on-iphone",
        "ct": "block-at-night",
        "topic": "Screen Time",
        "minutes": 5,
        "title": "How to block apps at night on iPhone",
        "seo_title": "How to Block Apps at Night on iPhone: Downtime Step by Step",
        "description": "How to block apps at night on an iPhone with Downtime, keep your alarm and calls working, and make the block hold. Why Sleep Focus alone doesn't block apps.",
        "blurb": "Downtime, step by step, with your alarm and calls still working, and how to stop yourself overriding it.",
        "standfirst": "The last scroll of the day is the longest one, because nothing is waiting to interrupt it. "
                      "Your iPhone can close chosen apps at a set time every night. Here is how to set it up so "
                      "your alarm still rings and the block is still there at 11.30 p.m.",
        "box_title": "A bedtime rule that asks first",
        "box_text": "In Pausely, a rule protects the apps you choose during the hours you set, with a pause or a "
                    "full block. One rule is free.",
        "body": """
<h2>First: Sleep Focus doesn't block apps</h2>
<p>Many people turn on Sleep Focus and expect their apps to close. It doesn't do that. Sleep Focus silences notifications and dims the Lock Screen. Every app still opens normally. It is worth having, and it is not a block. For a block you need Downtime.</p>

<h2>Set up Downtime</h2>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>Downtime</kbd> and turn on <kbd>Scheduled</kbd>.</li>
  <li>Choose <kbd>Every Day</kbd>, or <kbd>Customize Days</kbd> if weekends are different, and set <kbd>From</kbd> and <kbd>To</kbd>. Starting 30 to 60 minutes before you want to be asleep works well.</li>
</ol>
<p>During those hours every app is covered except Phone and the ones you allow in the next step. iOS gives a reminder five minutes before it starts.</p>

<h2>Choose what stays open</h2>
<ol>
  <li>Go back to <kbd>Screen Time</kbd> and tap <kbd>Always Allowed</kbd>.</li>
  <li>Tap the plus beside anything you need at night: Clock for your alarm, Messages, Maps, your music or audiobook app, a meditation app.</li>
  <li>Under <kbd>Contacts</kbd> on the same screen, choose who can reach you during Downtime.</li>
</ol>
<p>Be honest with this list. If you allow the browser, the feeds are all still there on the web.</p>
<p>Shopping apps belong off the list too if late night orders are the problem rather than the feeds. We also make On Ice, a shopping blocker, and wrote a guide on <a href="https://getonice.com/guides/how-to-stop-late-night-online-shopping/">how to stop late night online shopping</a>.</p>

<h2>Make it hold</h2>
<p>Out of the box, a covered app has an <kbd>Ignore Limit</kbd> button under it, with <kbd>Ignore Limit For Today</kbd> one tap further in. To remove it:</p>
<ol>
  <li>In <kbd>Screen Time</kbd>, tap <kbd>Lock Screen Time Settings</kbd> (older versions call it <kbd>Use Screen Time Passcode</kbd>) and set a code.</li>
  <li>Go back into <kbd>Downtime</kbd> and turn on <kbd>Block at Downtime</kbd>.</li>
</ol>
<p>Now getting past it needs the passcode. As with every Screen Time passcode, it holds best when someone else chose it.</p>

<h2>Three small things that help more than they should</h2>
<ul>
  <li><strong>Charge the phone outside the bedroom.</strong> Or at least out of reach of the bed. A cheap alarm clock removes the last reason to keep it close.</li>
  <li><strong>Put something by the bed.</strong> A book, a notebook, a puzzle. The half hour needs filling with something.</li>
  <li><strong>Start Downtime earlier than feels necessary.</strong> If it begins at the moment you want to be asleep, you will meet it mid scroll and argue with it.</li>
</ul>

<h2>If Downtime is too blunt</h2>
<p>Downtime covers everything outside your allowed list, on one schedule, and its only answer is the passcode. Some nights you do need the app for two minutes, and that is when people turn the whole thing off and forget to turn it back on.</p>
<p>A rule in Pausely is narrower. You pick the apps and the hours, and choose what happens when you tap one in that time: a pause first, such as ten seconds of breathing and then a choice, or a full block until the hours are over. Outside those hours the same apps can keep their ordinary pause.</p>
<p>One rule is free. If you want the night to be something you can't talk yourself out of, Premium has strict mode, which holds until a time you pick and can't be undone before then, not even by you.</p>
""",
    },
    {
        "slug": "how-to-block-apps-on-iphone",
        "ct": "block-apps",
        "topic": "Blocking apps",
        "minutes": 7,
        "updated": ("28 November 2026", "2026-11-28"),
        "title": "How to block apps on iPhone: 5 ways, from a nudge to a full block",
        "seo_title": "How to Block Apps on iPhone: 5 Ways, Step by Step",
        "description": "How to block apps on an iPhone with Screen Time: a daily limit, a schedule, hiding apps completely, Face ID locks, and a pause before an app opens.",
        "blurb": "A daily limit, a bedtime schedule, hiding an app completely, and where each one gives way.",
        "standfirst": "Your iPhone can already block apps. It has four different ways to do it, hidden in "
                      "Screen Time and on the Home Screen, and each one blocks something slightly different. Here "
                      "they are, lightest first, with the steps and the point where each one stops holding.",
        "box_title": "Block the reflex, not the app",
        "box_text": "Pausely puts a ten second pause in front of the apps you choose. Then you decide whether to "
                    "go in. Two apps are free.",
        "body": """
<div class="note"><b>The short answer.</b> Open <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>App Limits</kbd> and <kbd>Add Limit</kbd>. Tick the app, set 1 minute, and tap <kbd>Add</kbd>. To stop yourself switching it off, set a Screen Time passcode and turn on <kbd>Block at End of Limit</kbd>. The rest of this page explains the other ways, and which one fits.</div>

<h2>Before you start: turn on Screen Time</h2>
<p>Every built-in block lives in Screen Time. Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd>. It takes a few seconds and changes nothing else.</p>

<h2>Option 1: A daily limit (App Limits)</h2>
<p>Best when you want to keep using an app, just less.</p>
<ol>
  <li>In <kbd>Screen Time</kbd>, tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Open a category, for example <kbd>Social</kbd> or <kbd>Entertainment</kbd>, and tick the apps. Ticking the category itself covers every app in it, including ones you install later.</li>
  <li>To cover the website version too, scroll to the bottom, open <kbd>Websites</kbd>, tap <kbd>Add Website</kbd> and type its address.</li>
  <li>Tap <kbd>Next</kbd>, set the time (the smallest is 1 minute a day) and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time is used, iOS covers the app with a screen that offers one more minute, a reminder in 15 minutes, or <kbd>Ignore Limit For Today</kbd>. One tap and the limit is gone for the day. <a href="{BASE}/guides/why-screen-time-limits-dont-work/">How to make a limit hold</a> shows how to remove that button.</p>

<h2>Option 2: A schedule (Downtime)</h2>
<p>Best when the problem has a time of day, usually late evening.</p>
<ol>
  <li>In <kbd>Screen Time</kbd>, tap <kbd>Downtime</kbd> and turn on <kbd>Scheduled</kbd>.</li>
  <li>Choose the days and set <kbd>From</kbd> and <kbd>To</kbd>.</li>
  <li>Go back and open <kbd>Always Allowed</kbd> to choose what stays open, such as Messages, Maps and Clock for your alarm.</li>
</ol>
<p>During those hours every app outside the allowed list is covered. <strong>Where it stops working:</strong> the same <kbd>Ignore Limit</kbd> button appears, and Downtime covers everything at once, so one urgent app at 11 p.m. tempts you to turn the whole thing off. The full set-up is in <a href="{BASE}/guides/block-apps-at-night-on-iphone/">How to block apps at night</a>.</p>

<h2>Option 3: Hide apps completely (Content &amp; Privacy Restrictions)</h2>
<p>Best when you want an app gone, with no button to bring it back. This is the strongest block iOS has, and the bluntest.</p>
<p><strong>For Apple's own apps</strong>, such as Safari, Camera or FaceTime:</p>
<ol>
  <li>In <kbd>Screen Time</kbd>, tap <kbd>Content &amp; Privacy Restrictions</kbd> and turn the switch on.</li>
  <li>Tap <kbd>Allowed Apps</kbd> (on newer versions of iOS it is <kbd>Allowed Apps &amp; Features</kbd>) and turn off the ones you want hidden.</li>
</ol>
<p>They vanish from the Home Screen and the App Library until you turn them back on.</p>
<p><strong>For apps from the App Store</strong>, iOS can only hide them all together. In <kbd>Content &amp; Privacy Restrictions</kbd>, tap <kbd>Content Restrictions</kbd> (newer versions call it <kbd>App Store, Media, Web &amp; Games</kbd>), then <kbd>Apps</kbd>, and choose <kbd>Don't Allow Apps</kbd>. Every app you installed disappears, which is rarely what an adult wants. To remove one app and keep it away, delete it and turn off installing instead: in <kbd>Content &amp; Privacy Restrictions</kbd>, tap <kbd>iTunes &amp; App Store Purchases</kbd>, then <kbd>Installing Apps</kbd>, and choose <kbd>Don't Allow</kbd>.</p>
<p><strong>Where it stops working.</strong> Anyone who knows the Screen Time passcode can undo it in seconds, and with installing switched off you will be switching it back on every time you need a new app. That moment is when the old app tends to come back.</p>

<h2>Option 4: Lock an app with Face ID</h2>
<p>On iOS 18 and later, press and hold an app's icon and tap <kbd>Require Face ID</kbd>. You can also choose <kbd>Hide and Require Face ID</kbd>, which moves it into a hidden folder at the bottom of the App Library.</p>
<p>This is a privacy feature, not a block. It stops other people opening the app. It doesn't stop you, because your face opens it in under a second. Hiding the icon helps a little, for the same reason moving an icon off your first Home Screen helps: your thumb has further to go.</p>

<h2>Option 5: A pause before the app opens</h2>
<p>Options 1 to 3 either cut you off after the time is spent or remove the app altogether. Most of the time neither is what you want. You want to keep the app for the things it is good for, and stop opening it on autopilot.</p>
<p>That is the moment Pausely works on. You choose the apps. Tap one and it doesn't open straight away: you see how many times you have opened it today, you breathe for ten seconds, and then you choose. <kbd>I changed my mind</kbd> closes it. Continuing gives you a few minutes, and when they are up the pause comes back.</p>
<p>If you want something firmer, a rule in Pausely can block chosen apps during the hours you set, and Premium adds a daily limit that rests an app until tomorrow and a strict mode that can't be switched off early, not even by you.</p>

<h2>Which one should you pick?</h2>
<table>
  <thead><tr><th>You want</th><th>Use</th></tr></thead>
  <tbody>
    <tr><td>Less time in an app, not none</td><td>Option 1, a daily limit</td></tr>
    <tr><td>No apps after a certain time</td><td>Option 2, Downtime</td></tr>
    <tr><td>An app gone from the phone</td><td>Option 3, with a passcode someone else keeps</td></tr>
    <tr><td>Other people kept out of an app</td><td>Option 4, Face ID</td></tr>
    <tr><td>To open an app on purpose, not by reflex</td><td>Option 5, a pause</td></tr>
  </tbody>
</table>
<p>They also combine. A lot of people use Downtime for the night and a pause for the day.</p>
""",
    },
    {
        "slug": "how-to-block-youtube-on-iphone",
        "ct": "block-youtube",
        "topic": "Blocking apps",
        "minutes": 6,
        "updated": ("28 November 2026", "2026-11-28"),
        "title": "How to block YouTube on iPhone: the app, the website and Shorts",
        "seo_title": "How to Block YouTube on iPhone: App, Website and Shorts",
        "description": "Four ways to block or limit YouTube on an iPhone: YouTube's own reminders, a Screen Time limit on the app and youtube.com, a full block, and a pause first.",
        "blurb": "YouTube's own reminders, a limit that covers the app and the website, a full block, and what to do about Shorts.",
        "standfirst": "YouTube is harder to block than most apps, because it lives in three places: the app, "
                      "youtube.com in Safari, and videos that play inside other apps. Here are four ways to deal "
                      "with it, from a gentle reminder to a block with no way round.",
        "box_title": "Watch the video you came for",
        "box_text": "Pausely asks for a ten second breath every time you open YouTube, then lets you choose. "
                    "Two apps are free.",
        "body": """
<p>First decide what you want. If YouTube is useful to you (recipes, lessons, a band you love) and the trouble is the hour that follows, options 1, 2 and 4 fit better than a full block.</p>

<h2>Option 1: YouTube's own reminders</h2>
<p>The YouTube app can remind you to stop. Tap your profile picture, then the settings gear, then <kbd>General</kbd>. Look for <kbd>Remind me to take a break</kbd> and <kbd>Remind me when it's bedtime</kbd> (YouTube moves these menus from time to time). Choose how often, or what time.</p>
<p><strong>Where it stops working.</strong> The reminder pauses the video and shows a message. One tap and you are back. It is a clock on the wall, not a door.</p>

<h2>Option 2: A Screen Time limit on the app and the website</h2>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Find YouTube, usually under <kbd>Entertainment</kbd>, and tick it.</li>
  <li>Scroll to the bottom, open <kbd>Websites</kbd>, tap <kbd>Add Website</kbd> and type <kbd>youtube.com</kbd>. Add <kbd>m.youtube.com</kbd> as well. Now one limit covers the app and the site.</li>
  <li>Tap <kbd>Next</kbd>, set the time and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time runs out, the cover offers <kbd>Ignore Limit For Today</kbd>, which is one tap. Setting a Screen Time passcode and turning on <kbd>Block at End of Limit</kbd> removes it. It holds best if someone else chooses the passcode.</p>

<h2>Option 3: Block YouTube completely</h2>
<p>Three steps: delete the app, stop it coming back, and block the website.</p>
<ol>
  <li>Press and hold the YouTube icon, tap <kbd>Remove App</kbd>, then <kbd>Delete App</kbd>. Your account, playlists and subscriptions stay on YouTube's side.</li>
  <li>In <kbd>Settings</kbd>, go to <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on. Tap <kbd>iTunes &amp; App Store Purchases</kbd>, then <kbd>Installing Apps</kbd>, and choose <kbd>Don't Allow</kbd>.</li>
  <li>Still in <kbd>Content &amp; Privacy Restrictions</kbd>, tap <kbd>Content Restrictions</kbd> (on newer versions of iOS this row is called <kbd>App Store, Media, Web &amp; Games</kbd>), then <kbd>Web Content</kbd>, and choose <kbd>Limit Adult Websites</kbd>. Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and enter <kbd>youtube.com</kbd>, then <kbd>m.youtube.com</kbd>.</li>
</ol>
<p><strong>Side effects to know about.</strong> <kbd>Limit Adult Websites</kbd> also turns on Apple's adult content filter and removes Private Browsing from Safari. With <kbd>Installing Apps</kbd> off you can't install anything else either. And videos embedded in other apps or websites may still play, because they are not opened from youtube.com in Safari.</p>

<h2>What about Shorts?</h2>
<p>Many people are happy with long videos and lose their evenings to Shorts. Screen Time can't tell the two apart: to iOS it is all one app. There is no setting on an iPhone that blocks Shorts and keeps the rest.</p>
<p>What helps is changing where you start. Open YouTube from a link, a playlist or the <kbd>Subscriptions</kbd> tab rather than the home feed, and turn off autoplay in the app's settings, so one video doesn't roll into the next. If Shorts are the main problem, a pause on the whole app (option 4) catches the moment you open it for no reason, which is usually how Shorts begin.</p>

<h2>Option 4: Keep YouTube, with a pause in front</h2>
<p>With Pausely, tapping YouTube shows you how many times you have opened it today, then asks for a ten second breath. After it you choose: <kbd>I changed my mind</kbd>, or continue for a few minutes. When the time is up, the pause comes back, which is often the moment you notice you had drifted from the video you came for.</p>
<p>If you want it firmer, Premium adds a daily limit that rests the app until tomorrow, and rules that block it during the hours you choose.</p>

<h2>Which one should you pick?</h2>
<table>
  <thead><tr><th>You want</th><th>Use</th></tr></thead>
  <tbody>
    <tr><td>A reminder to stop</td><td>Option 1</td></tr>
    <tr><td>A daily allowance, app and website together</td><td>Option 2 with a passcode</td></tr>
    <tr><td>YouTube gone from this phone</td><td>Option 3</td></tr>
    <tr><td>To keep it for what it is good at</td><td>Option 4</td></tr>
  </tbody>
</table>
""",
    },
    {
        "slug": "what-to-do-instead-of-doomscrolling",
        "ct": "instead-of-doomscrolling",
        "topic": "Habits",
        "minutes": 6,
        "updated": ("28 November 2026", "2026-11-28"),
        "title": "What to do instead of doomscrolling: 21 ideas, sorted by how long you have",
        "seo_title": "What to Do Instead of Doomscrolling: 21 Real Ideas",
        "description": "21 things to do instead of doomscrolling, sorted by whether you have one minute, ten minutes or a whole evening, and how to make the swap actually happen.",
        "blurb": "Twenty-one swaps, sorted by the time you have, and the small trick that makes one of them happen.",
        "standfirst": "Closing the app is the easy half. The hard half is the empty minute after it, which the next "
                      "app fills unless something else is already waiting. Here are 21 things to put in that "
                      "minute, sorted by how much time you actually have.",
        "box_title": "A pause that offers something else",
        "box_text": "When you open an app you chose, Pausely asks for a ten second breath and can suggest "
                    "something else instead. Two apps are free.",
        "body": """
<h2>Why \"just stop\" doesn't work</h2>
<p>Scrolling usually fills a gap: waiting, boredom, tiredness, putting off something harder. If you take the phone away and leave the gap, the gap wins. So the trick is not more willpower. It is having the next thing decided before the gap arrives.</p>
<p>Pick two or three ideas from the lists below, one for each kind of moment you scroll in. You don't need all 21.</p>

<h2>If you have one minute</h2>
<p>For queues, lifts, the kettle, the gap between meetings.</p>
<ol>
  <li><strong>Breathe slowly five times.</strong> In through the nose, longer out. It is the quickest reset there is.</li>
  <li><strong>Look at something far away.</strong> Out of a window, down the street. Your eyes have been at arm's length all day.</li>
  <li><strong>Stand up and stretch.</strong> Neck, shoulders, the back you have been curling over the phone.</li>
  <li><strong>Drink a glass of water.</strong> Half of the restless feeling is sometimes just thirst.</li>
  <li><strong>Send one real message.</strong> Not a reaction. A sentence to someone you like.</li>
  <li><strong>Write down the thing on your mind.</strong> One line on paper or in a notes app, so it stops circling.</li>
</ol>

<h2>If you have ten minutes</h2>
<p>For breaks, the bus, the time before you start something.</p>
<ol start="7">
  <li><strong>Walk round the block.</strong> No podcast needed. This is the single best swap on the list.</li>
  <li><strong>Read a few pages of a book.</strong> Keep one where the phone usually sits.</li>
  <li><strong>Tidy one small thing.</strong> A drawer, the sink, your desk. It ends with something visibly better.</li>
  <li><strong>Listen to one album track, properly.</strong> Eyes closed, nothing else.</li>
  <li><strong>Do a short practice.</strong> Ten minutes of a language, an instrument, a sketch.</li>
  <li><strong>Call someone instead of watching them.</strong> Their stories, live, are better than their posts.</li>
  <li><strong>Start the task you were avoiding, for two minutes.</strong> Often the scrolling was putting this off. Two minutes is usually enough to get past the start.</li>
</ol>

<h2>If it is the evening</h2>
<p>For the long scroll on the sofa or in bed, which is the one that costs the most.</p>
<ol start="14">
  <li><strong>Put the phone on charge in another room</strong> and come back without it.</li>
  <li><strong>Watch one thing on purpose.</strong> A film or an episode you chose, on the big screen, then stop. Choosing is the difference.</li>
  <li><strong>Cook something slightly more than you need to.</strong></li>
  <li><strong>Have a bath or a long shower.</strong> No phone in the bathroom.</li>
  <li><strong>Play a game with real pieces.</strong> Cards, a puzzle, a board game, even alone.</li>
  <li><strong>Write tomorrow's three things.</strong> It quietens the urge to check everything now.</li>
  <li><strong>Stretch on the floor for ten minutes.</strong> It is hard to scroll lying on your back with your arms out.</li>
  <li><strong>Go to bed early with a book.</strong> If you are scrolling because you are tired, the answer is sleep, not a better feed.</li>
</ol>

<h2>How to make the swap actually happen</h2>
<p>Ideas on a list don't help at 11 p.m. Three small things do.</p>
<ul>
  <li><strong>Decide in advance, with a when.</strong> \"When I sit on the sofa after dinner, I pick up the book\" works better than \"I'll read more\". The moment triggers the plan.</li>
  <li><strong>Put the alternative where the phone was.</strong> Book on the pillow, shoes by the door, water on the desk. Make the new thing the easy thing.</li>
  <li><strong>Add friction to the old thing.</strong> Move the app off your first Home Screen, or set a limit. Our guide on <a href="{BASE}/guides/how-to-stop-doomscrolling/">how to stop doomscrolling</a> has seven ways, and <a href="{BASE}/guides/how-to-block-apps-on-iphone/">how to block apps on iPhone</a> covers the built-in blocks.</li>
</ul>
<p>And be kind about slips. Missing one evening doesn't undo a week. Pick it up the next day.</p>

<h2>Let the phone remind you</h2>
<p>The hardest moment to change is the one you don't notice: the thumb opening the app before you have decided anything. Pausely puts a pause there. Tap an app you chose and you see how many times you have opened it today, then breathe for ten seconds. Instead of going in, the pause can offer something else, like <kbd>Or walk for 10 minutes</kbd>. Some days you go in anyway, for a few minutes. Plenty of days you don't.</p>
<div class="note"><b>If you only try one thing:</b> number 7. Next time you reach for the phone with nothing to do, walk round the block instead, and see how you feel when you get back.</div>
""",
    },
]
