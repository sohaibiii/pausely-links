# -*- coding: utf-8 -*-
"""The home page in German, Japanese and Spanish.

The English home page in `site_pages.py` wraps every visible English string in
`t()`. While one of the languages below is being built, `t()` returns its
translation, and a string with no translation stops the build, so an English
sentence can never slip onto a translated page unnoticed.

Rules, same as the support pages in `words/`:
  * the app's own words come from the app's Localizable.xcstrings, copied as
    they are (Pausely öffnen / Doch nicht, Pauselyを開く / やめておく,
    Abrir Pausely / Déjalo, Du hast pausiert., ひと呼吸、置けました。...);
  * German says du, Japanese uses です・ます and calls a pause 一呼吸 like the
    app does, Spanish is neutral and says tú;
  * the recording and screenshots are of the English app, and the page says so;
  * no long dashes.

These translations were written without a native speaker's review.
"""

# code: (URL prefix, home page path, og:locale)
HOMES = {
    "en": ("", "/", "en_US"),
    "de": ("/de", "/de/home/", "de_DE"),
    "es": ("/es", "/es/home/", "es_ES"),
    "ja": ("/ja", "/ja/home/", "ja_JP"),
}
LANGS = ["de", "es", "ja"]

_state = {"lang": "en"}


def current():
    return _state["lang"]


def use(lang):
    _state["lang"] = lang


def t(s):
    lang = _state["lang"]
    if lang == "en":
        return s
    try:
        return T[lang][s]
    except KeyError:
        raise SystemExit(f"i18n: no {lang} translation for {s!r}")


# Japanese has no spaces, so a heading would break anywhere, even inside a word.
# Phrases in <span class="nw"> stay whole.
HEAD_CSS = {"ja": "<style>.nw{display:inline-block}h1,h2,h3{word-break:auto-phrase;letter-spacing:0}"
                  ".hero h1{font-size:clamp(36px,5.4vw,68px);line-height:1.1}</style>\n"}


def faq():
    """The home page's questions, in order, for a translated page."""
    return FAQ[_state["lang"]]


T = {}
FAQ = {}

# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------

T["de"] = {
    # Page frame
    "Get the app": "App laden",
    "Pages": "Seiten",
    "Skip to content": "Zum Inhalt springen",
    "Download on the": "Laden im",
    "This page in:": "Diese Seite auf:",
    "Support in other languages:": "Hilfe in anderen Sprachen:",
    "The app": "Die App",
    "Download on the App Store": "Im App Store laden",
    "Help and legal": "Hilfe und Rechtliches",
    "A breath before the scroll. Made by {company}. Write to {email} and a person will reply.":
        "Ein Atemzug vor dem Scrollen. Von {company}. Schreib an {email}, und ein Mensch antwortet dir.",
    "Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed by them or by any other app named or shown here.":
        "Bildschirme der App zeigen ihre Demodaten, die einfacheren Bilder sind Zeichnungen. Apple, iPhone, iPad, Safari, Bildschirmzeit und App Store sind Marken von Apple Inc. TikTok und Instagram sind Marken ihrer Inhaber. Pausely steht in keiner Verbindung zu ihnen oder zu einer anderen hier genannten oder gezeigten App und wird von keiner davon unterstützt oder empfohlen.",
    "Pausely: a pause before the apps you open without thinking.":
        "Pausely: eine Pause vor den Apps, die du öffnest, ohne nachzudenken.",
    # Cookie banner
    "Cookie choices": "Cookie-Einstellungen",
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "Diese Website zählt Besuche mit Google Analytics. Ist ein Cookie dafür für dich in Ordnung?",
    "What it collects": "Was erfasst wird",
    "No thanks": "Nein danke",
    "OK": "OK",
    # Title and description
    "Pausely: Stop Scrolling on Autopilot, Pause Before You Open":
        "Pausely: Schluss mit Scrollen auf Autopilot. Erst Pause, dann öffnen",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone and iPad. Breathe first, then decide. Free to start, no account.":
        "Pausely setzt eine zehn Sekunden lange Pause vor die Apps, die du öffnest, ohne nachzudenken. Für iPhone und iPad. Erst atmen, dann entscheiden. Kostenlos starten, kein Konto.",
    "An app for iPhone and iPad that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "Eine App für iPhone und iPad, die eine kurze Pause vor die Apps setzt, die du auswählst. So wird das Öffnen zu einer Entscheidung.",
    # Hero
    "For iPhone and iPad": "Für iPhone und iPad",
    "Stop scrolling <em>on autopilot.</em>": "Schluss mit Scrollen <em>auf Autopilot.</em>",
    "Pausely puts a short pause in front of TikTok, Instagram or any app you open without thinking. Breathe first. Then decide if you still want to go in.":
        "Pausely setzt eine kurze Pause vor TikTok, Instagram oder jede App, die du öffnest, ohne nachzudenken. Erst atmen. Dann entscheiden, ob du wirklich rein willst.",
    "Free to start.<br>No account.": "Kostenlos starten.<br>Kein Konto.",
    "A screen recording style demo: someone taps TikTok on the Home Screen. Pausely steps in and shows 12 opens today. A breathing pause follows, then a pause where you type a short code, then the choice screen: You paused.":
        "Eine Demo im Stil einer Bildschirmaufnahme der englischen App: Jemand tippt auf dem Home-Bildschirm auf TikTok. Pausely geht dazwischen und zeigt 12 Öffnungen heute. Es folgt eine Atempause, dann eine Pause, in der man einen kurzen Code abtippt, dann der Auswahlbildschirm: Du hast pausiert.",
    # How it works
    "One pause. <em>Then you choose.</em>": "Eine Pause. <em>Dann entscheidest du.</em>",
    "1 · You tap an app": "1 · Du tippst auf eine App",
    "Pausely steps in first": "Pausely kommt zuerst",
    "The app doesn't open straight away. You see how many times you have opened it today.":
        "Die App öffnet sich nicht sofort. Du siehst, wie oft du sie heute schon geöffnet hast.",
    "2 · Ten seconds": "2 · Zehn Sekunden",
    "You take a breath": "Du atmest durch",
    "In for four, hold for two, out for four. Long enough for the urge to pass.":
        "Vier ein, zwei halten, vier aus. Lang genug, damit der Impuls vorbeigeht.",
    "3 · Your call": "3 · Deine Wahl",
    "You decide": "Du entscheidest",
    "Walk away and it counts as a win. Or go in for a few minutes, and the pause comes back after.":
        "Gehst du weg, zählt das als Erfolg. Oder du gehst für ein paar Minuten rein, und danach kommt die Pause wieder.",
    "seconds of breathing before a protected app opens.": "Sekunden atmen, bevor sich eine geschützte App öffnet.",
    "kinds of pause, from a breath to a question to answer.": "Arten von Pausen, vom Atemzug bis zur Frage, die du beantwortest.",
    "accounts. No sign up, no email, no password.": "Konten. Keine Anmeldung, keine E-Mail, kein Passwort.",
    # Drawings (the app's own words)
    "Opens today": "Heute geöffnet",
    "Open Pausely": "Pausely öffnen",
    "Never mind": "Doch nicht",
    "Breathe in": "Einatmen",
    "Ten seconds of breathing before you continue.": "Zehn Sekunden atmen, bevor du weitermachst.",
    "You paused.": "Du hast pausiert.",
    "I changed my mind": "Ich hab’s mir anders überlegt",
    "Or walk for 10 minutes": "Oder Spazieren für 10 Min.",
    "Continue for 5m": "Weitermachen für 5 Min.",
    "A drawing of the block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind.":
        "Eine Zeichnung des Sperrbildschirms der App: die Zahl 12, Heute geöffnet. Tasten: Pausely öffnen, Doch nicht.",
    "A drawing of the breathing pause: a soft circle and the words Breathe in.":
        "Eine Zeichnung der Atempause: ein weicher Kreis und das Wort Einatmen.",
    "A drawing of the choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Continue for 5 minutes.":
        "Eine Zeichnung des Auswahlbildschirms: Du hast pausiert. Tasten: Ich hab’s mir anders überlegt, Oder Spazieren für 10 Min., Weitermachen für 5 Min.",
    # Real app strip
    "The real app, <em>on your iPhone.</em>": "Die echte App, <em>auf deinem iPhone.</em>",
    "A breath is the pause everybody starts with. With Premium you can pick another, or let Pausely choose a different one each time.":
        "Ein Atemzug ist die Pause, mit der alle anfangen. Mit Premium wählst du eine andere oder lässt Pausely jedes Mal eine andere aussuchen.",
    "These screens show the English version. The app itself is in your language.":
        "Die Bildschirme zeigen die englische Version. Die App selbst ist auf Deutsch.",
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "Die Atempause in Pausely, englische Version: ein weicher Kreis in einem Ring, mit dem Wort Hold (Halten) und einem Countdown.",
    "Breathe": "Atmen",
    "Ten seconds, with a circle to follow.": "Zehn Sekunden, mit einem Kreis zum Mitatmen.",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "Die Tipp-Pause, englische Version: zwanzig Zeichen zum Abtippen und ein Eingabefeld.",
    "Or type": "Oder tippen",
    "Twenty characters. Hard to do on autopilot.": "Zwanzig Zeichen. Auf Autopilot kaum zu schaffen.",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "Die Absichts-Pause, englische Version: Warum öffnest du diese App? Zwölf Kacheln wie Jemandem antworten, Nur kurz schauen, Langeweile und Aus Gewohnheit.",
    "Or say why": "Oder sag, warum",
    "One tap on the reason that fits.": "Ein Tipp auf den Grund, der passt.",
    "The choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Or read for 10 minutes, and Continue for 1 or 5 minutes.":
        "Der Auswahlbildschirm, englische Version: Du hast pausiert. Tasten: Ich hab’s mir anders überlegt, spazieren oder lesen für 10 Minuten, und Weitermachen für 1 oder 5 Minuten.",
    "Then choose": "Dann wählen",
    "Stop here, do something else, or go in for a minute.": "Hier aufhören, etwas anderes tun oder kurz reingehen.",
    "Swipe to see all four.": "Wische, um alle vier zu sehen.",
    "Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "Lieber strenger? Regeln, Tageslimits, Alles blockieren und der strenge Modus sind da, wenn du sie brauchst.",
    # Progress
    "See the time <em>come back.</em>": "Sieh, wie die Zeit <em>zurückkommt.</em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "Jedes Mal, wenn du weggehst, zählt Pausely mit. Der Fortschritt ist kostenlos, und deine Zahlen bleiben auf deinem iPhone.",
    "No account": "Kein Konto",
    "Nothing to sign up for.": "Keine Anmeldung nötig.",
    "Your apps stay private": "Deine Apps bleiben privat",
    "Pausely can't read which apps you picked. Apple keeps that.":
        "Pausely kann nicht lesen, welche Apps du gewählt hast. Das behält Apple für sich.",
    "On your device": "Auf deinem Gerät",
    "Your time, your pauses and your journal stay on your phone.":
        "Deine Zeit, deine Pausen und dein Tagebuch bleiben auf deinem iPhone.",
    "What leaves the phone, exactly": "Was das iPhone verlässt, ganz genau",
    "Pausely's Progress screen: 1 hour 48 minutes reclaimed this week, and a bar chart of the last seven days.":
        "Der Fortschritt in Pausely, englische Version: 1 Std. 48 Min. diese Woche zurückgewonnen und ein Balkendiagramm der letzten sieben Tage.",
    "The app's demo data.": "Demodaten der App.",
    # Pricing
    "Free to start. <em>Premium if you want more.</em>": "Kostenlos starten. <em>Premium, wenn du mehr willst.</em>",
    "Free": "Kostenlos",
    "No charge, no trial clock": "Ohne Kosten, ohne Testzeit",
    "Two apps protected": "Zwei Apps geschützt",
    "The breathing pause and one rule": "Die Atempause und eine Regel",
    "Your whole progress screen": "Dein ganzer Fortschritt",
    "Monthly · Yearly · Lifetime · Family": "Monatlich · Jährlich · Einmalkauf · Familie",
    "Every app, website and category": "Jede App, Website und Kategorie",
    "Every kind of pause, and daily limits": "Jede Art von Pause und Tageslimits",
    "Block everything, strict mode and Lock Pausely": "Alles blockieren, strenger Modus und Pausely-Sperre",
    "What protects you keeps protecting you if a subscription ends.":
        "Was dich schützt, schützt dich weiter, auch wenn ein Abo endet.",
    # FAQ frame and closing
    "Questions people ask first": "Häufige Fragen",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "Noch etwas? <a href=\"{support}\">Die Hilfeseite</a> erklärt Einrichtung, Problemlösung und wie du uns erreichst.",
    "Take a breath <em>before the scroll.</em>": "Atme durch, <em>bevor du scrollst.</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone und iPad, ab iOS 17.<br>Auf Deutsch und in sieben weiteren Sprachen.",
}

FAQ["de"] = [
    ("Sperrt mich Pausely aus meinen Apps aus?",
     "Nein. Eine normale Pause ist ein Moment, keine Mauer. Danach entscheidest du: <kbd>Ich hab’s mir anders "
     "überlegt</kbd> oder für ein paar Minuten weiter in die App. Kein Durchkommen gibt es nur bei Dingen, die du "
     "selbst eingerichtet hast, etwa ein aufgebrauchtes Tageslimit, eine von dir gestartete Sperre oder eine Regel, "
     "die eine App zu bestimmten Zeiten blockiert. Jede davon endet von selbst."),
    ("Was ist anders als bei den Bildschirmzeit-Limits?",
     "Ein Bildschirmzeit-Limit wartet, bis deine Zeit aufgebraucht ist, und bietet dann <kbd>Limit ignorieren</kbd> "
     "an. Pausely kommt jedes Mal, wenn du die App öffnest, bevor das Scrollen beginnt, und bittet zuerst um einen "
     "Atemzug."),
    ("Mit welchen Apps funktioniert es?",
     "Mit jeder App auf deinem iPhone oder iPad. Du wählst sie in Apples eigener Bildschirmzeit-Auswahl, also mit "
     "genau den Apps, die dir Zeit nehmen. Pausely erfährt nie ihre Namen. Apple gibt der App stattdessen private "
     "Codes."),
    ("Sieht Pausely, was ich in anderen Apps mache?",
     "Nein. Pausely sieht nie, was du im Web aufrufst, deine Nachrichten oder irgendetwas in einer anderen App. iOS "
     "teilt Pausely mit, wie lange die gewählten Apps geöffnet waren, und diese Minuten bleiben auf deinem Gerät."),
    ("Ist Pausely kostenlos?",
     "Ja, und kostenlos ist ein vollwertiges Produkt, keine Demo: zwei geschützte Apps, eine Regel, die Atempause, "
     "dein ganzer Fortschritt, die heutige Zeit in jeder gewählten App und der Countdown auf dem Sperrbildschirm und "
     "in der Dynamic Island."),
    ("Brauche ich ein Konto?",
     "Nein. In der ganzen App gibt es keine Anmeldung, kein E-Mail-Feld und kein Passwort."),
    ("Welche Geräte brauche ich?",
     "Ein iPhone oder iPad mit iOS 17 oder iPadOS 17 oder neuer. Eine Mac-Version gibt es nicht, weil die "
     "Bildschirmzeit-Frameworks, auf denen Pausely aufbaut, dort nicht verfügbar sind."),
]

# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------

T["es"] = {
    "Get the app": "Descargar la app",
    "Pages": "Páginas",
    "Skip to content": "Ir al contenido",
    "Download on the": "Descárgalo en el",
    "This page in:": "Esta página en:",
    "Support in other languages:": "Ayuda en otros idiomas:",
    "The app": "La app",
    "Download on the App Store": "Descárgalo en el App Store",
    "Help and legal": "Ayuda y aspectos legales",
    "A breath before the scroll. Made by {company}. Write to {email} and a person will reply.":
        "Una respiración antes del scroll. Hecho por {company}. Escribe a {email} y te responderá una persona.",
    "Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed by them or by any other app named or shown here.":
        "Las pantallas de la app muestran sus datos de demostración, y las imágenes más sencillas son dibujos. Apple, iPhone, iPad, Safari, Tiempo de uso y App Store son marcas comerciales de Apple Inc. TikTok e Instagram son marcas de sus propietarios. Pausely no está afiliada, patrocinada ni respaldada por ellos ni por ninguna otra app nombrada o mostrada aquí.",
    "Pausely: a pause before the apps you open without thinking.":
        "Pausely: una pausa antes de las apps que abres sin pensar.",
    "Cookie choices": "Preferencias de cookies",
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "Esta web cuenta las visitas con Google Analytics. ¿Te parece bien una cookie para eso?",
    "What it collects": "Qué recoge",
    "No thanks": "No, gracias",
    "OK": "Vale",
    "Pausely: Stop Scrolling on Autopilot, Pause Before You Open":
        "Pausely: deja de hacer scroll en piloto automático y haz una pausa antes de abrir",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone and iPad. Breathe first, then decide. Free to start, no account.":
        "Pausely pone una pausa de diez segundos delante de las apps que abres sin pensar, en iPhone y iPad. Primero respira, luego decide. Gratis para empezar, sin cuenta.",
    "An app for iPhone and iPad that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "Una app para iPhone y iPad que pone una pausa breve delante de las apps que eliges, para que abrirlas sea una decisión.",
    "For iPhone and iPad": "Para iPhone y iPad",
    "Stop scrolling <em>on autopilot.</em>": "Deja el scroll <em>en piloto automático.</em>",
    "Pausely puts a short pause in front of TikTok, Instagram or any app you open without thinking. Breathe first. Then decide if you still want to go in.":
        "Pausely pone una pausa breve delante de TikTok, Instagram o cualquier app que abras sin pensar. Primero respira. Luego decide si de verdad quieres entrar.",
    "Free to start.<br>No account.": "Gratis para empezar.<br>Sin cuenta.",
    "A screen recording style demo: someone taps TikTok on the Home Screen. Pausely steps in and shows 12 opens today. A breathing pause follows, then a pause where you type a short code, then the choice screen: You paused.":
        "Una demo con aspecto de grabación de pantalla de la app en inglés: alguien toca TikTok en la pantalla de inicio. Pausely se adelanta y muestra 12 aperturas hoy. Sigue una pausa para respirar, luego una pausa en la que escribes un código corto y después la pantalla de elección: Has hecho una pausa.",
    "One pause. <em>Then you choose.</em>": "Una pausa. <em>Luego eliges tú.</em>",
    "1 · You tap an app": "1 · Tocas una app",
    "Pausely steps in first": "Pausely llega primero",
    "The app doesn't open straight away. You see how many times you have opened it today.":
        "La app no se abre al instante. Ves cuántas veces la has abierto hoy.",
    "2 · Ten seconds": "2 · Diez segundos",
    "You take a breath": "Respiras",
    "In for four, hold for two, out for four. Long enough for the urge to pass.":
        "Inspira cuatro, mantén dos, espira cuatro. Lo justo para que pasen las ganas.",
    "3 · Your call": "3 · Tú decides",
    "You decide": "Decides",
    "Walk away and it counts as a win. Or go in for a few minutes, and the pause comes back after.":
        "Si te apartas, cuenta como un logro. O entras unos minutos, y después la pausa vuelve.",
    "seconds of breathing before a protected app opens.": "segundos de respiración antes de que se abra una app protegida.",
    "kinds of pause, from a breath to a question to answer.": "tipos de pausa, desde una respiración hasta una pregunta que responder.",
    "accounts. No sign up, no email, no password.": "cuentas. Sin registro, sin email, sin contraseña.",
    "Opens today": "Aperturas hoy",
    "Open Pausely": "Abrir Pausely",
    "Never mind": "Déjalo",
    "Breathe in": "Inspira",
    "Ten seconds of breathing before you continue.": "Diez segundos de respiración antes de continuar.",
    "You paused.": "Has hecho una pausa.",
    "I changed my mind": "He cambiado de idea",
    "Or walk for 10 minutes": "O Caminar durante 10 min",
    "Continue for 5m": "Continuar durante 5 min",
    "A drawing of the block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind.":
        "Un dibujo de la pantalla de bloqueo de la app: el número 12, Aperturas hoy. Botones: Abrir Pausely, Déjalo.",
    "A drawing of the breathing pause: a soft circle and the words Breathe in.":
        "Un dibujo de la pausa para respirar: un círculo suave y la palabra Inspira.",
    "A drawing of the choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Continue for 5 minutes.":
        "Un dibujo de la pantalla de elección: Has hecho una pausa. Botones: He cambiado de idea, O Caminar durante 10 min, Continuar durante 5 min.",
    "The real app, <em>on your iPhone.</em>": "La app real, <em>en tu iPhone.</em>",
    "A breath is the pause everybody starts with. With Premium you can pick another, or let Pausely choose a different one each time.":
        "Una respiración es la pausa con la que empieza todo el mundo. Con Premium puedes elegir otra, o dejar que Pausely elija una distinta cada vez.",
    "These screens show the English version. The app itself is in your language.":
        "Estas pantallas muestran la versión en inglés. La app en sí está en español.",
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "La pausa para respirar de Pausely, versión en inglés: un círculo suave dentro de un anillo, con la palabra Hold (Mantén) y una cuenta atrás.",
    "Breathe": "Respira",
    "Ten seconds, with a circle to follow.": "Diez segundos, con un círculo que seguir.",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "La pausa de escritura, versión en inglés: veinte caracteres que escribir y un campo de texto.",
    "Or type": "O escribe",
    "Twenty characters. Hard to do on autopilot.": "Veinte caracteres. Difícil en piloto automático.",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "La pausa de intención, versión en inglés: ¿Por qué abres esta app? Doce opciones como Responder a alguien, Solo miraba, Aburrimiento y Por costumbre.",
    "Or say why": "O di por qué",
    "One tap on the reason that fits.": "Un toque en el motivo que encaje.",
    "The choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Or read for 10 minutes, and Continue for 1 or 5 minutes.":
        "La pantalla de elección, versión en inglés: Has hecho una pausa. Botones: He cambiado de idea, caminar o leer durante 10 minutos, y continuar durante 1 o 5 minutos.",
    "Then choose": "Luego elige",
    "Stop here, do something else, or go in for a minute.": "Para aquí, haz otra cosa o entra un minuto.",
    "Swipe to see all four.": "Desliza para ver las cuatro.",
    "Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "¿Lo quieres más firme? Reglas, límites diarios, Bloquear todo y el modo estricto están ahí cuando los necesites.",
    "See the time <em>come back.</em>": "Mira cómo <em>vuelve el tiempo.</em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "Cada vez que te apartas, Pausely lo cuenta. La pantalla de progreso es gratis, y tus cifras se quedan en tu iPhone.",
    "No account": "Sin cuenta",
    "Nothing to sign up for.": "Nada en lo que registrarse.",
    "Your apps stay private": "Tus apps siguen siendo privadas",
    "Pausely can't read which apps you picked. Apple keeps that.":
        "Pausely no puede leer qué apps elegiste. Eso lo guarda Apple.",
    "On your device": "En tu dispositivo",
    "Your time, your pauses and your journal stay on your phone.":
        "Tu tiempo, tus pausas y tu diario se quedan en tu iPhone.",
    "What leaves the phone, exactly": "Qué sale del iPhone, exactamente",
    "Pausely's Progress screen: 1 hour 48 minutes reclaimed this week, and a bar chart of the last seven days.":
        "La pantalla de progreso de Pausely, versión en inglés: 1 h 48 min recuperados esta semana y un gráfico de barras de los últimos siete días.",
    "The app's demo data.": "Datos de demostración de la app.",
    "Free to start. <em>Premium if you want more.</em>": "Gratis para empezar. <em>Premium si quieres más.</em>",
    "Free": "Gratis",
    "No charge, no trial clock": "Sin coste, sin periodo de prueba",
    "Two apps protected": "Dos apps protegidas",
    "The breathing pause and one rule": "La pausa para respirar y una regla",
    "Your whole progress screen": "Toda tu pantalla de progreso",
    "Monthly · Yearly · Lifetime · Family": "Mensual · Anual · De por vida · Familia",
    "Every app, website and category": "Todas las apps, webs y categorías",
    "Every kind of pause, and daily limits": "Todos los tipos de pausa y límites diarios",
    "Block everything, strict mode and Lock Pausely": "Bloquear todo, modo estricto y Bloqueo de Pausely",
    "What protects you keeps protecting you if a subscription ends.":
        "Lo que te protege sigue protegiéndote aunque termine una suscripción.",
    "Questions people ask first": "Preguntas frecuentes",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "¿Algo más? <a href=\"{support}\">La página de ayuda</a> explica la configuración, la solución de problemas y cómo contactarnos.",
    "Take a breath <em>before the scroll.</em>": "Respira <em>antes del scroll.</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone y iPad, iOS 17 o posterior.<br>En español y en otros siete idiomas.",
}

FAQ["es"] = [
    ("¿Pausely me deja sin acceso a mis apps?",
     "No. Una pausa normal es un momento, no un muro. Después eliges: <kbd>He cambiado de idea</kbd>, o seguir en la "
     "app unos minutos. Lo único que no tiene paso son cosas que configuras tú, como un límite diario ya agotado, un "
     "bloqueo que has iniciado o una regla que bloquea una app a ciertas horas. Cada una termina sola."),
    ("¿En qué se diferencia de los límites de Tiempo de uso?",
     "Un límite de Tiempo de uso espera a que se acabe tu tiempo y luego ofrece <kbd>Ignorar límite</kbd>. Pausely "
     "aparece cada vez que abres la app, antes de que empiece el scroll, y te pide primero una respiración."),
    ("¿Con qué apps funciona?",
     "Con cualquier app de tu iPhone o iPad. Las eliges en el selector de Tiempo de uso de Apple, así que funciona con "
     "las que se llevan tu tiempo. Pausely nunca sabe sus nombres: Apple le da códigos privados en su lugar."),
    ("¿Pausely ve lo que hago en otras apps?",
     "No. Nunca ve lo que navegas, tus mensajes ni nada dentro de otra app. iOS le dice cuánto tiempo han estado "
     "abiertas las apps que elegiste, y Pausely guarda esos minutos en tu dispositivo."),
    ("¿Pausely es gratis?",
     "Sí, y la versión gratis es un producto completo, no una demo: dos apps protegidas, una regla, la pausa para "
     "respirar, toda tu pantalla de progreso, el tiempo de hoy en cada app elegida y la cuenta atrás en la pantalla "
     "bloqueada y en la Dynamic Island."),
    ("¿Necesito una cuenta?",
     "No. En toda la app no hay registro, ni campo de email, ni contraseña."),
    ("¿Qué dispositivos necesito?",
     "Un iPhone o iPad con iOS 17 o iPadOS 17, o posterior. No hay versión para Mac, porque los frameworks de Tiempo "
     "de uso en los que se basa Pausely no están disponibles allí."),
]

# ---------------------------------------------------------------------------
# Japanese
# ---------------------------------------------------------------------------

T["ja"] = {
    "Get the app": "アプリを入手",
    "Pages": "ページ",
    "Skip to content": "本文へスキップ",
    "Download on the": "ダウンロード",
    "This page in:": "このページの他の言語：",
    "Support in other languages:": "他の言語のヘルプ：",
    "The app": "アプリ",
    "Download on the App Store": "App Storeでダウンロード",
    "Help and legal": "ヘルプと規約",
    "A breath before the scroll. Made by {company}. Write to {email} and a person will reply.":
        "スクロールの前に、ひと呼吸。{company}が作っています。{email}までご連絡ください。人が返信します。",
    "Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, Screen Time and App Store are trademarks of Apple Inc. TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed by them or by any other app named or shown here.":
        "アプリの画面はデモデータを表示しており、簡単な絵はイラストです。Apple、iPhone、iPad、Safari、スクリーンタイム、App StoreはApple Inc.の商標です。TikTokとInstagramは各所有者の商標です。Pauselyは、これらの企業やここに名前や画面が出てくる他のアプリとは提携しておらず、後援や推奨も受けていません。",
    "Pausely: a pause before the apps you open without thinking.":
        "Pausely：何となく開いてしまうアプリの前に、ひと呼吸。",
    "Cookie choices": "Cookieの設定",
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "このサイトはGoogleアナリティクスで訪問数を数えています。そのためのCookieを使ってもよろしいですか？",
    "What it collects": "収集する内容",
    "No thanks": "いいえ",
    "OK": "OK",
    "Pausely: Stop Scrolling on Autopilot, Pause Before You Open":
        "Pausely：無意識のスクロールをやめて、開く前にひと呼吸",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone and iPad. Breathe first, then decide. Free to start, no account.":
        "Pauselyは、何となく開いてしまうアプリの前に10秒のひと呼吸を置くiPhone・iPadアプリです。まず呼吸して、それから決める。無料で始められて、アカウントも不要です。",
    "An app for iPhone and iPad that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "選んだアプリの前に短いひと呼吸を置き、開くことを自分の決断に変えるiPhone・iPadアプリ。",
    "For iPhone and iPad": "iPhone・iPad向け",
    "Stop scrolling <em>on autopilot.</em>": "<span class=\"nw\">無意識の</span><span class=\"nw\">スクロールに、</span><em class=\"nw\">ひと呼吸を。</em>",
    "Pausely puts a short pause in front of TikTok, Instagram or any app you open without thinking. Breathe first. Then decide if you still want to go in.":
        "Pauselyは、TikTokやInstagramなど、何となく開いてしまうアプリの前に短いひと呼吸を置きます。まず呼吸して、それでも開きたいかを決めましょう。",
    "Free to start.<br>No account.": "無料で始められます。<br>アカウント不要。",
    "A screen recording style demo: someone taps TikTok on the Home Screen. Pausely steps in and shows 12 opens today. A breathing pause follows, then a pause where you type a short code, then the choice screen: You paused.":
        "英語版アプリの画面収録風デモ：ホーム画面でTikTokをタップすると、Pauselyが先に現れ、今日開いた回数12回を表示します。続いて呼吸の一呼吸、短いコードを入力する一呼吸、そして選択画面「ひと呼吸、置けました。」が出ます。",
    "One pause. <em>Then you choose.</em>": "ひと呼吸して、<em>それから選ぶ。</em>",
    "1 · You tap an app": "1 · アプリをタップ",
    "Pausely steps in first": "先にPauselyが現れる",
    "The app doesn't open straight away. You see how many times you have opened it today.":
        "アプリはすぐには開きません。今日そのアプリを何回開いたかが表示されます。",
    "2 · Ten seconds": "2 · 10秒",
    "You take a breath": "ひと呼吸する",
    "In for four, hold for two, out for four. Long enough for the urge to pass.":
        "4秒吸って、2秒止めて、4秒吐く。衝動が過ぎるには十分な長さです。",
    "3 · Your call": "3 · あなたが決める",
    "You decide": "自分で選ぶ",
    "Walk away and it counts as a win. Or go in for a few minutes, and the pause comes back after.":
        "開かずに離れれば、それがひとつの勝ち。数分だけ使うこともでき、そのあとまたひと呼吸が戻ってきます。",
    "seconds of breathing before a protected app opens.": "秒の呼吸。保護したアプリが開く前に。",
    "kinds of pause, from a breath to a question to answer.": "種類の一呼吸。呼吸から、答える質問まで。",
    "accounts. No sign up, no email, no password.": "アカウント。登録も、メールも、パスワードもなし。",
    "Opens today": "今日開いた回数",
    "Open Pausely": "Pauselyを開く",
    "Never mind": "やめておく",
    "Breathe in": "吸って",
    "Ten seconds of breathing before you continue.": "続ける前に、10秒の呼吸を。",
    "You paused.": "ひと呼吸、置けました。",
    "I changed my mind": "やっぱりやめる",
    "Or walk for 10 minutes": "代わりに10分歩く",
    "Continue for 5m": "5分続ける",
    "A drawing of the block screen: the number 12, Opens today. Buttons: Open Pausely, Never mind.":
        "アプリのブロック画面のイラスト：数字の12と「今日開いた回数」。ボタンは「Pauselyを開く」と「やめておく」。",
    "A drawing of the breathing pause: a soft circle and the words Breathe in.":
        "呼吸の一呼吸のイラスト：やわらかな円と「吸って」の文字。",
    "A drawing of the choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Continue for 5 minutes.":
        "選択画面のイラスト：「ひと呼吸、置けました。」ボタンは「やっぱりやめる」「代わりに10分歩く」「5分続ける」。",
    "The real app, <em>on your iPhone.</em>": "<span class=\"nw\">本物のアプリを、</span><em><span class=\"nw\">あなたの</span><span class=\"nw\">iPhoneで。</span></em>",
    "A breath is the pause everybody starts with. With Premium you can pick another, or let Pausely choose a different one each time.":
        "最初の一呼吸は、だれでも呼吸から。Premiumなら別の一呼吸を選んだり、毎回Pauselyに違うものを選ばせたりできます。",
    "These screens show the English version. The app itself is in your language.":
        "画面は英語版です。アプリ自体は日本語で表示されます。",
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "Pauselyの呼吸の一呼吸（英語版）：リングの中のやわらかな円、Hold（止めて）の文字とカウントダウン。",
    "Breathe": "呼吸する",
    "Ten seconds, with a circle to follow.": "円に合わせて10秒。",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "入力の一呼吸（英語版）：入力する20文字と入力欄。",
    "Or type": "入力する",
    "Twenty characters. Hard to do on autopilot.": "20文字。無意識ではなかなか打てません。",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "意図の一呼吸（英語版）：「なぜ、このアプリを開くのですか？」と、「誰かに返信する」「ちょっと見るだけ」「退屈」「つい癖で」など12個の選択肢。",
    "Or say why": "理由を選ぶ",
    "One tap on the reason that fits.": "当てはまる理由をワンタップ。",
    "The choice screen: You paused. Buttons: I changed my mind, Or walk for 10 minutes, Or read for 10 minutes, and Continue for 1 or 5 minutes.":
        "選択画面（英語版）：「ひと呼吸、置けました。」ボタンは「やっぱりやめる」、10分の散歩か読書、1分または5分続ける。",
    "Then choose": "そして選ぶ",
    "Stop here, do something else, or go in for a minute.": "ここでやめるか、別のことをするか、1分だけ使うか。",
    "Swipe to see all four.": "スワイプして4つすべてを見る。",
    "Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "もっとしっかり止めたいなら、ルール、1日の上限、すべてブロック、厳格モードも使えます。",
    "See the time <em>come back.</em>": "<span class=\"nw\">時間が</span><em><span class=\"nw\">戻ってくるのが</span><span class=\"nw\">見える。</span></em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "開かずに離れるたびに、Pauselyが数えます。記録の画面は無料で、数字はあなたのiPhoneの中にとどまります。",
    "No account": "アカウント不要",
    "Nothing to sign up for.": "登録するものはありません。",
    "Your apps stay private": "選んだアプリは非公開",
    "Pausely can't read which apps you picked. Apple keeps that.":
        "Pauselyは、どのアプリを選んだかを読み取れません。その情報はAppleが保持します。",
    "On your device": "デバイスの中に",
    "Your time, your pauses and your journal stay on your phone.":
        "使用時間、一呼吸の記録、日記はあなたのiPhoneの中にとどまります。",
    "What leaves the phone, exactly": "iPhoneの外に出る情報を正確に",
    "Pausely's Progress screen: 1 hour 48 minutes reclaimed this week, and a bar chart of the last seven days.":
        "Pauselyの記録画面（英語版）：今週1時間48分を取り戻したことと、過去7日間の棒グラフ。",
    "The app's demo data.": "アプリのデモデータです。",
    "Free to start. <em>Premium if you want more.</em>": "<span class=\"nw\">無料で始めて、</span><em><span class=\"nw\">もっと欲しければ</span><span class=\"nw\">Premium。</span></em>",
    "Free": "無料",
    "No charge, no trial clock": "料金なし、試用期限なし",
    "Two apps protected": "アプリ2つを保護",
    "The breathing pause and one rule": "呼吸の一呼吸とルールひとつ",
    "Your whole progress screen": "記録の画面すべて",
    "Monthly · Yearly · Lifetime · Family": "月額 · 年額 · 買い切り · ファミリー",
    "Every app, website and category": "すべてのアプリ、ウェブサイト、カテゴリ",
    "Every kind of pause, and daily limits": "すべての種類の一呼吸と、1日の上限",
    "Block everything, strict mode and Lock Pausely": "すべてブロック、厳格モード、Pauselyロック",
    "What protects you keeps protecting you if a subscription ends.":
        "サブスクリプションが終わっても、設定した保護はそのまま続きます。",
    "Questions people ask first": "よくある質問",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "ほかにも質問があれば、<a href=\"{support}\">ヘルプページ</a>で設定方法、トラブルの解決、お問い合わせ先をご覧いただけます。",
    "Take a breath <em>before the scroll.</em>": "スクロールの前に、<em>ひと呼吸。</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone・iPad、iOS 17以降。<br>日本語を含む8言語に対応。",
}

FAQ["ja"] = [
    ("Pauselyを使うと、アプリが開けなくなりますか？",
     "いいえ。ふだんの一呼吸は壁ではなく、ほんの一瞬です。そのあと<kbd>やっぱりやめる</kbd>か、数分だけアプリを"
     "使うかを選べます。通れなくなるのは、自分で設定したものだけです。たとえば使い切った1日の上限、自分で始めた"
     "ブロック、決まった時間にアプリをブロックするルールなど。どれも時間が来れば自然に終わります。"),
    ("スクリーンタイムの制限とは何が違いますか？",
     "スクリーンタイムの制限は、時間を使い切るまで待ち、そのあと<kbd>制限を無視</kbd>を表示します。Pauselyは"
     "アプリを開くたびに、スクロールが始まる前に現れて、まずひと呼吸を促します。"),
    ("どのアプリで使えますか？",
     "iPhoneやiPadのどのアプリでも使えます。Apple純正のスクリーンタイムの選択画面で選ぶので、時間を取られている"
     "アプリならどれでも対象にできます。Pauselyがアプリの名前を知ることはなく、Appleからは非公開のコードだけが"
     "渡されます。"),
    ("Pauselyは他のアプリでの操作を見ていますか？",
     "いいえ。閲覧履歴やメッセージ、他のアプリの中身を見ることはありません。iOSが伝えるのは、選んだアプリが"
     "開いていた時間だけで、その時間はデバイスの中に保存されます。"),
    ("Pauselyは無料ですか？",
     "はい。無料版はお試しではなく、きちんと使える製品です。アプリ2つの保護、ルールひとつ、呼吸の一呼吸、"
     "記録の画面すべて、選んだアプリごとの今日の使用時間、ロック画面とDynamic Islandのカウントダウンが使えます。"),
    ("アカウントは必要ですか？",
     "いいえ。アプリのどこにも登録、メールアドレスの入力欄、パスワードはありません。"),
    ("どのデバイスで使えますか？",
     "iOS 17またはiPadOS 17以降のiPhoneかiPadです。Mac版はありません。Pauselyの土台であるスクリーンタイムの"
     "フレームワークがMacでは使えないためです。"),
]
