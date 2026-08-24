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

## Editing

Everything is rendered by one script from one file — edit `_src/gen.py`, then:

```
python3 _src/gen.py
```

and commit the regenerated `index.html` files alongside it. The colours, radii and type are
Pausely's own tokens (`Core/DesignSystem/Theme.swift` in the app repo), dark-first with a light
counterpart, so the pages read as the same product as the app.

Once App Store Connect has assigned the app its Apple ID, set `APP_STORE_URL` at the top of
`_src/gen.py` and regenerate — every "App Store" button turns from *coming soon* into a link.
