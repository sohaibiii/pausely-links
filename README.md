# pausely-links

The pages Pausely's App Store listing points at, hosted with GitHub Pages at
https://sohaibiii.github.io/pausely-links/

| Page | URL | App Store Connect field |
|---|---|---|
| Home | `/` | Marketing URL |
| How it works | `/how-it-works/` | |
| Pricing | `/pricing/` | |
| Guides | `/guides/` and `/guides/<slug>/` | |
| Support | `/support/` (English), `/<lang>/` (the seven others) | Support URL |
| About | `/about/` | |
| Privacy Policy | `/privacy/` | Privacy Policy URL |
| Terms of Use (EULA) | `/terms/` | EULA / linked from the paywall |
| Delete your data | `/delete-data/` | (linked from Privacy) |

The home page keeps an `id="faq"` section and a link to Support, so the `/` and `/#faq` links in
shipped builds of the app still land on answers.

## The marketing pages

Home, How it works, Pricing and the guides are English only for now. `_src/site_pages.py` holds
their markup and words, `_src/guides.py` the guides, `assets/site.css` their styles. `gen.py` calls
`site_pages.build()` at the end of its run, so the two commands under Editing still rebuild
everything.

Rules these pages keep, and `site_pages.check` fails the build on the ones a machine can see:

- Only features the app has, named the way its screens name them.
- Screens of the app are real screenshots (`assets/img/`, the app's demo data); the simpler pictures are drawings in the app's own words.
- The demo in the hero (`assets/video/demo.mp4`) is cut from the App Store preview, with two scenes added: tapping TikTok on the Home Screen, and the typing pause. TikTok is named and shown as the app being paused, and the footer says Pausely is not affiliated with it.
- No borrowed statistics, studies, press or reviews.
- The app is on iPhone, iPad and Android (Google Play, `com.social.pausely`), and they are not the same app. Anything only one of them does says which: the floating reels card is Android's, the Dynamic Island and Screen Time are the iPhone's. Nothing is promised for a Mac.
- The reels card on the home page is Android's "Reels & time" badge, in its words and in the corner it starts in, over a made-up short-video app called Clips (the name the app's own examples use). The player has the layout every such app shares and no real app's name or logo. The clips are Mixkit stock footage (Stock Video Free License), never somebody's real post, and the names and numbers on them are invented. Its count is an estimate and the page says so.
- No claim that the app sends nothing anywhere. The Privacy Policy says exactly what leaves.
- No prices. Yearly changes on 1 December 2026, and the App Store shows the real one.
- No long dashes in copy.

Two switches:

- `DOMAIN` at the top of `_src/gen.py`. Set it to the custom domain (for example
  `"getpausely.app"`) and rebuild: every link, the sitemap and a `CNAME` file follow.
- `PROVIDER_TOKEN` at the top of `_src/site_pages.py`. Paste the provider id from App Store
  Connect and every App Store button reports which page sent the download (campaign links).

## Languages

Every page exists in the **eight languages Pausely ships in**, and a row of tabs under the
navigation switches between them without leaving the page you are on. English lives at the root and
each other language under its own code, so `/de/privacy/` is the German privacy policy and the link
somebody was given keeps both its page *and* its language:

`en` · `/de` · `/es` · `/fr` · `/ja` · `/ko` · `/pt-BR` · `/zh-Hans`

The App Store fields above should still point at the **English** URLs. Apple shows the listing in
the reader's own language, and the tabs let them carry that through to these pages; a hard-coded
`/de/` URL would trap an English reader in German.

Each page declares `hreflang` alternates for all eight plus `x-default`, and `sitemap.xml` repeats
them — without that, a search engine treats eight translations of the privacy policy as eight
competing pages rather than one page in eight languages, and picks a winner on its own.

Wording that names a screen in the app — <kbd>Settings</kbd> → <kbd>Your data</kbd> →
<kbd>Reset all data</kbd>, <kbd>Restore purchases</kbd> — is taken from the app's own catalogue
(`Core/Resources/Localizable.xcstrings`), so a page never tells somebody to tap a button whose
label is written differently on their screen.

## Hosting

The pages are served at https://getpausely.app by a Cloudflare Worker named `pausely-site`.
Cloudflare is connected to this repository and publishes `main` after every push, with no build
step: it uploads the committed files as they are. `wrangler.jsonc` names the Worker and its
settings, and `.assetsignore` lists the files that are not part of the website (`_src`, this README
and so on).

`_worker/index.js` runs for one path only, `/assets/video/`. Cloudflare's static assets answer a
byte-range request with the whole file, and Safari on iPhone will not play a video served that way,
so that script returns the requested bytes of the demo video. Every other page and file is served
without it.

GitHub Pages stays switched on, and the `CNAME` file stays, for one reason: shipped builds of the
app open `https://sohaibiii.github.io/pausely-links/...`, and GitHub forwards those addresses to
getpausely.app only while both are in place. Do not turn Pages off or delete `CNAME`.

## Editing

`_src/gen.py` owns the markup; `_src/words/<lang>.py` owns the words. English is the fallback behind
all seven others, so a key that has not been translated yet renders as English, never as an
identifier — the same rule the app follows.

```
python3 _src/check.py     # the eight catalogues agree
python3 _src/gen.py       # rewrite every page
```

Run **both**, and commit the regenerated HTML alongside the source. `check.py` is the half no reader
of that language can proofread for us: it holds every catalogue to the same key set, the same
`{placeholders}`, the same link targets and balanced tags. A translation that quietly drops a link,
or invents a placeholder that then renders as a literal brace, is a defect nobody here would ever
see.

To add a language: add it to `LANGUAGES` and `NATIVE_NAME` in `_src/gen.py`, add
`_src/words/<code>.py` (underscores for a hyphen: `pt_BR.py`), translate, then run the two commands
above. Keep the list and its order in step with `AppLanguage` in the app.

The colours, radii and type are Pausely's own tokens (`Core/DesignSystem/Theme.swift` in the app
repo), dark-first with a light counterpart, so the pages read as the same product as the app.

Once App Store Connect has assigned the app its Apple ID, set `APP_STORE_URL` at the top of
`_src/gen.py` and regenerate — every "App Store" button turns from *coming soon* into a link.
