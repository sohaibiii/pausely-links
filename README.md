# pausely-links

The pages Pausely's App Store listing points at, hosted with GitHub Pages at
https://sohaibiii.github.io/pausely-links/

| Page | URL | App Store Connect field |
|---|---|---|
| Support | `/` | Support URL |
| About | `/about/` | Marketing URL |
| Privacy Policy | `/privacy/` | Privacy Policy URL |
| Terms of Use (EULA) | `/terms/` | EULA / linked from the paywall |
| Delete your data | `/delete-data/` | — (linked from Privacy) |

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
