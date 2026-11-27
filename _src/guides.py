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
        "description": "Seven practical ways to stop doomscrolling on an iPhone, from moving one icon to setting "
                       "limits that hold, with exact steps and an honest note on what each one can't do.",
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
        "description": "Four ways to block TikTok on an iPhone: TikTok's own limit, a Screen Time limit, a full "
                       "block of the app and tiktok.com, and a pause before it opens. Exact steps for each.",
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
        "seo_title": "How to Block Instagram on iPhone (Without Deleting Your Account)",
        "description": "How to block or limit Instagram on an iPhone: its own daily limit, a Screen Time limit, "
                       "blocking instagram.com in Safari, and a pause before it opens. No account deletion needed.",
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
        "seo_title": "Screen Time Limits Not Working? How to Stop Tapping Ignore Limit",
        "description": "Why Screen Time app limits are so easy to ignore on iPhone, how to remove the Ignore Limit "
                       "button with a passcode, and what to do when a limit is the wrong tool.",
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
        "seo_title": "How to Block Apps at Night on iPhone (Downtime, Step by Step)",
        "description": "How to block apps at night on an iPhone with Downtime, how to keep your alarm and calls "
                       "working, why Sleep Focus alone doesn't block apps, and how to make the block hold.",
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
]
