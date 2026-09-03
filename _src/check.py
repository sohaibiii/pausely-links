# -*- coding: utf-8 -*-
"""Holds the eight catalogues in `_src/words/` to the same shape.

    python3 _src/check.py

This is the half of a translation nobody here can proofread. A German reader
will notice a clumsy sentence; nobody will notice that the French privacy
policy quietly lost its link to the data page, or that a `{RESET}` became a
`{RESETT}` and now renders as a literal brace. So the machine checks the shape
and leaves the prose to the translator:

  * every key English has, each language has — a missing one would silently
    render as English, which is fine at runtime and a lie in a review;
  * no key a language has that English does not, which is always a typo;
  * the same `{placeholders}` in every translation as in its English, because
    an invented one is a crash and a dropped one is a missing link;
  * the same link targets, in the same number;
  * balanced tags, because one unclosed <p> takes the rest of the page with it.

Exits non-zero on any of those. Values that are identical to English are only
listed, not failed: "Premium" is "Premium" in most of them.
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from gen import LANGUAGES, NATIVE_NAME  # noqa: E402
import words.en as english  # noqa: E402

EN = english.COPY

# Keys that name an icon rather than say anything, so they stay English.
NOT_TRANSLATED = {k for k in EN if k.endswith(".icon")}

PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_\-]*)\}")
HREF = re.compile(r'href="([^"]*)"')
TAG = re.compile(r"<(/?)([a-z0-9]+)(?=[\s/>])")
VOID = {"br", "img", "input", "hr", "meta", "link", "path", "circle", "rect", "stop", "svg", "use"}


def shape(value):
    opens, closes = Counter(), Counter()
    for slash, tag in TAG.findall(value):
        if tag in VOID:
            continue
        (closes if slash else opens)[tag] += 1
    return {
        "placeholders": Counter(PLACEHOLDER.findall(value)),
        "hrefs": Counter(HREF.findall(value)),
        "unclosed": {t: opens[t] - closes[t] for t in set(opens) | set(closes)
                     if opens[t] != closes[t]},
    }


def main():
    failures = []
    for code, _ in LANGUAGES:
        if code == "en":
            continue
        module = __import__("words." + code.replace("-", "_"), fromlist=["COPY"])
        catalogue = module.COPY
        name = f"{code} ({NATIVE_NAME[code]})"

        missing = sorted((set(EN) - NOT_TRANSLATED) - set(catalogue))
        unknown = sorted(set(catalogue) - set(EN))
        for key in missing:
            failures.append(f"{name}: missing key {key!r}")
        for key in unknown:
            failures.append(f"{name}: unknown key {key!r} — not in English")

        same = []
        for key in sorted(set(EN) & set(catalogue)):
            want, got = shape(EN[key]), shape(catalogue[key])
            if want["placeholders"] != got["placeholders"]:
                failures.append(
                    f"{name}: {key!r} placeholders differ — English has "
                    f"{sorted(want['placeholders'].elements())}, this has "
                    f"{sorted(got['placeholders'].elements())}"
                )
            if want["hrefs"] != got["hrefs"]:
                failures.append(
                    f"{name}: {key!r} links differ — English has "
                    f"{sorted(want['hrefs'].elements())}, this has "
                    f"{sorted(got['hrefs'].elements())}"
                )
            if got["unclosed"]:
                failures.append(f"{name}: {key!r} has unbalanced tags {got['unclosed']}")
            if EN[key].strip() == catalogue[key].strip():
                same.append(key)

        note = f" · {len(same)} identical to English" if same else ""
        print(f"{name}: {len(catalogue)} keys{note}")
        if same:
            print("   " + ", ".join(same))

    # "Pausely" is a name, not a word — the same rule the app holds itself to.
    for code, _ in LANGUAGES:
        module = __import__("words." + code.replace("-", "_"), fromlist=["COPY"])
        for key, value in module.COPY.items():
            for wrong in ("Pausley", "pausely "):
                if wrong in value:
                    failures.append(f"{code}: {key!r} misspells the app's name")

    if failures:
        print("\n".join(["", "FAILED:"] + ["  " + f for f in failures]))
        return 1
    print("\nAll catalogues agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
