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
    # Hero
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
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "Die Atempause in Pausely, englische Version: ein weicher Kreis in einem Ring, mit dem Wort Hold (Halten) und einem Countdown.",
    "Breathe": "Atmen",
    "Ten seconds, with a circle to follow.": "Zehn Sekunden, mit einem Kreis zum Mitatmen.",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "Die Tipp-Pause, englische Version: zwanzig Zeichen zum Abtippen und ein Eingabefeld.",
    "Twenty characters. Hard to do on autopilot.": "Zwanzig Zeichen. Auf Autopilot kaum zu schaffen.",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "Die Absichts-Pause, englische Version: Warum öffnest du diese App? Zwölf Kacheln wie Jemandem antworten, Nur kurz schauen, Langeweile und Aus Gewohnheit.",
    "One tap on the reason that fits.": "Ein Tipp auf den Grund, der passt.",
    # Progress
    "See the time <em>come back.</em>": "Sieh, wie die Zeit <em>zurückkommt.</em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "Jedes Mal, wenn du weggehst, zählt Pausely mit. Der Fortschritt ist kostenlos, und deine Zahlen bleiben auf deinem iPhone.",
    "No account": "Kein Konto",
    "Nothing to sign up for.": "Keine Anmeldung nötig.",
    "Your apps stay private": "Deine Apps bleiben privat",
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
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "La pausa para respirar de Pausely, versión en inglés: un círculo suave dentro de un anillo, con la palabra Hold (Mantén) y una cuenta atrás.",
    "Breathe": "Respira",
    "Ten seconds, with a circle to follow.": "Diez segundos, con un círculo que seguir.",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "La pausa de escritura, versión en inglés: veinte caracteres que escribir y un campo de texto.",
    "Twenty characters. Hard to do on autopilot.": "Veinte caracteres. Difícil en piloto automático.",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "La pausa de intención, versión en inglés: ¿Por qué abres esta app? Doce opciones como Responder a alguien, Solo miraba, Aburrimiento y Por costumbre.",
    "One tap on the reason that fits.": "Un toque en el motivo que encaje.",
    "See the time <em>come back.</em>": "Mira cómo <em>vuelve el tiempo.</em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "Cada vez que te apartas, Pausely lo cuenta. La pantalla de progreso es gratis, y tus cifras se quedan en tu iPhone.",
    "No account": "Sin cuenta",
    "Nothing to sign up for.": "Nada en lo que registrarse.",
    "Your apps stay private": "Tus apps siguen siendo privadas",
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
    "The breathing pause in Pausely: a soft circle inside a ring, with the word Hold and a countdown.":
        "Pauselyの呼吸の一呼吸（英語版）：リングの中のやわらかな円、Hold（止めて）の文字とカウントダウン。",
    "Breathe": "呼吸する",
    "Ten seconds, with a circle to follow.": "円に合わせて10秒。",
    "The typing pause: Type this to continue, with twenty characters to type and a field that says Type here.":
        "入力の一呼吸（英語版）：入力する20文字と入力欄。",
    "Twenty characters. Hard to do on autopilot.": "20文字。無意識ではなかなか打てません。",
    "The intention pause: Why are you opening this app? Twelve tiles such as Reply to someone, Just checking, Bored and Out of habit.":
        "意図の一呼吸（英語版）：「なぜ、このアプリを開くのですか？」と、「誰かに返信する」「ちょっと見るだけ」「退屈」「つい癖で」など12個の選択肢。",
    "One tap on the reason that fits.": "当てはまる理由をワンタップ。",
    "See the time <em>come back.</em>": "<span class=\"nw\">時間が</span><em><span class=\"nw\">戻ってくるのが</span><span class=\"nw\">見える。</span></em>",
    "Every time you walk away, Pausely counts it. The progress screen is free, and your numbers stay on your phone.":
        "開かずに離れるたびに、Pauselyが数えます。記録の画面は無料で、数字はあなたのiPhoneの中にとどまります。",
    "No account": "アカウント不要",
    "Nothing to sign up for.": "登録するものはありません。",
    "Your apps stay private": "選んだアプリは非公開",
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

# ---------------------------------------------------------------------------
# Added 28 Nov 2026 with the English home page's Android, research, six
# pauses and reels sections.
# ---------------------------------------------------------------------------

_LEGAL = ("Screens of the app show its demo data, and the simpler pictures are drawings. Apple, iPhone, iPad, Safari, "
          "Screen Time and App Store are trademarks of Apple Inc. Android and Google Play are trademarks of Google LLC. "
          "TikTok and Instagram are trademarks of their owners. Pausely is not affiliated with, sponsored by or endorsed "
          "by them or by any other app named or shown here.")
_STUDY = ("The study tested another app that pauses you the same way, not Pausely, and one of its three authors makes "
          "that app. Pausely has not been in a study of its own, so read these as what the method did there, not as a "
          "promise. Source: Grüning, Riedel and Lorenz-Spreen, {paper}, PNAS, 2023.")
_SECOND = ('A second experiment with 500 people looked at which part did the work. The way to back out helped most, and '
           'the wait helped too. Pausely gives you both: the pause, then "I changed my mind".')
_REELS_ALT = ("An Android phone playing short videos in a made-up app. In the top right corner Pausely's floating card "
              "reads 00:42, 12 reels, this visit, estimated. Example numbers.")

T["de"].update({
    "For iPhone, iPad and Android": "Für iPhone, iPad und Android",
    "Get it on": "Jetzt bei",
    "Get it on Google Play": "Jetzt bei Google Play",
    _LEGAL: "Bildschirme der App zeigen ihre Demodaten, die einfacheren Bilder sind Zeichnungen. Apple, iPhone, iPad, Safari, Bildschirmzeit und App Store sind Marken von Apple Inc. Android und Google Play sind Marken von Google LLC. TikTok und Instagram sind Marken ihrer Inhaber. Pausely steht in keiner Verbindung zu ihnen oder zu einer anderen hier genannten oder gezeigten App und wird von keiner davon unterstützt oder empfohlen.",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone, iPad and Android. Breathe first, then decide. Free to start.":
        "Pausely setzt eine zehn Sekunden lange Pause vor die Apps, die du öffnest, ohne nachzudenken. Für iPhone, iPad und Android. Erst atmen, dann entscheiden. Kostenlos starten.",
    "An app for iPhone, iPad and Android that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "Eine App für iPhone, iPad und Android, die eine kurze Pause vor die Apps setzt, die du auswählst. So wird das Öffnen zu einer Entscheidung.",
    # Research
    "Does a pause work? <em>It has been tested.</em>": "Hilft eine Pause? <em>Das wurde untersucht.</em>",
    "In 2023, researchers published a six week study of 280 people using an app that works this way: a short wait before the app opens, then a way to change your mind.":
        "2023 haben Forschende eine sechswöchige Studie mit 280 Menschen veröffentlicht, die eine App nach diesem Prinzip nutzten: eine kurze Wartezeit, bevor sich die App öffnet, dann die Möglichkeit, es sich anders zu überlegen.",
    "of the time, people closed the app again after the pause.": "der Fälle schlossen die Leute die App nach der Pause wieder.",
    "fewer attempts to open those apps by week six than in week one.": "weniger Versuche, diese Apps zu öffnen, in Woche sechs als in Woche eins.",
    "fewer times those apps were actually opened after six weeks.": "seltener wurden diese Apps nach sechs Wochen tatsächlich geöffnet.",
    _SECOND: "Ein zweites Experiment mit 500 Menschen untersuchte, welcher Teil wirkt. Die Möglichkeit, abzubrechen, half am meisten, die Wartezeit half ebenfalls. Pausely bietet beides: die Pause, dann „Ich hab’s mir anders überlegt“.",
    _STUDY: "Die Studie hat eine andere App getestet, die auf dieselbe Weise pausiert, nicht Pausely, und einer der drei Autoren entwickelt diese App. Pausely war noch in keiner eigenen Studie. Lies die Zahlen also als das, was die Methode dort bewirkt hat, nicht als Versprechen. Quelle: Grüning, Riedel und Lorenz-Spreen, {paper}, PNAS, 2023.",
    # Six pauses
    "Six kinds of pause. <em>Pick yours.</em>": "Sechs Arten von Pausen. <em>Wähl deine.</em>",
    "A breath is the pause everybody starts with, and it is free. With Premium you can pick another, or let Pausely choose a different one each time.":
        "Ein Atemzug ist die Pause, mit der alle anfangen, und sie ist kostenlos. Mit Premium wählst du eine andere oder lässt Pausely jedes Mal eine andere aussuchen.",
    "Type": "Tippen",
    "Say why": "Sag, warum",
    "Read a line": "Einen Satz lesen",
    "A reminder from Pausely, or one you wrote yourself.": "Eine Erinnerung von Pausely oder eine, die du selbst geschrieben hast.",
    "Answer a question": "Eine Frage beantworten",
    "One question about where you live. One try.": "Eine Frage über dein Land. Ein Versuch.",
    "Reflect": "Nachdenken",
    "Say why you are here. Get one gentle question back.": "Sag, warum du hier bist, und bekomm eine sanfte Frage zurück.",
    "The reminder pause: a short line to read under the label On being here, with a bar that fills while you read, and Show me another.":
        "Die Erinnerungs-Pause, englische Version: ein kurzer Satz zum Lesen, ein Balken, der sich beim Lesen füllt, und eine Taste für einen anderen Satz.",
    "The question pause: One question. One try. Which of these rivers runs through the middle of the capital city? Four answers and an Answer button.":
        "Die Frage-Pause, englische Version: Eine Frage, ein Versuch. Welcher dieser Flüsse fließt mitten durch die Hauptstadt? Vier Antworten und eine Taste zum Antworten.",
    "The reflection pause: you said Just checking, and Pausely asks What would make the next hour feel like it went well?":
        "Die Nachdenk-Pause, englische Version: Du hast Nur kurz schauen gewählt, und Pausely fragt, was die nächste Stunde zu einer guten Stunde machen würde.",
    "Swipe to see all six.": "Wische, um alle sechs zu sehen.",
    "Screens from the English iPhone app, showing its demo data. The app itself is in your language.":
        "Bildschirme der englischen iPhone-App mit ihren Demodaten. Die App selbst ist auf Deutsch.",
    "The Android app has the same pauses, though a new one can reach it a little later. The last two are written by AI and stay off until you turn AI pauses on.":
        "Die Android-App hat dieselben Pausen, eine neue kommt dort manchmal etwas später an. Die letzten beiden schreibt eine KI, und sie bleiben aus, bis du die KI-Pausen einschaltest.",
    "What they send": "Was dabei gesendet wird",
    "After any pause you choose: stop there, do something else, or go in for a few minutes. Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "Nach jeder Pause entscheidest du: aufhören, etwas anderes tun oder für ein paar Minuten reingehen. Lieber strenger? Regeln, Tageslimits, Alles blockieren und der strenge Modus sind da, wenn du sie brauchst.",
    # Reels
    "How many reels <em>was that?</em>": "Wie viele Reels <em>waren das?</em>",
    "It is easy to lose count of short videos. Pausely keeps a rough count for you, and shows it while you are still scrolling.":
        "Bei Kurzvideos verliert man leicht den Überblick. Pausely zählt ungefähr für dich mit und zeigt es dir, während du noch scrollst.",
    _REELS_ALT: "Ein Android-Handy spielt Kurzvideos in einer erfundenen App. Oben rechts zeigt die schwebende Karte von Pausely 00:42, 12 Reels, dieser Besuch, geschätzt. Beispielzahlen.",
    "Dislike": "Mag ich nicht", "Share": "Teilen", "Follow": "Folgen", "Original sound": "Originalton",
    "The easiest weeknight dinner": "Das einfachste Abendessen unter der Woche",
    "He heard the word walk": "Er hat das Wort Gassi gehört",
    "Found this beach by accident": "Diesen Strand zufällig gefunden",
    "Sprinkles, in slow motion": "Streusel in Zeitlupe",
    "Day 12 of painting every day": "Tag 12: jeden Tag malen",
    "Home": "Start", "Clips": "Clips", "Following": "Abos", "You": "Du",
    "reels": "Reels",
    "This visit · estimated": "Dieser Besuch · geschätzt",
    "<b>This is Android.</b> On iPhone you get a banner every few minutes instead, with about how many short videos you watched.":
        "<b>Das ist Android.</b> Auf dem iPhone bekommst du stattdessen alle paar Minuten ein Banner mit ungefähr der Zahl der Kurzvideos, die du gesehen hast.",
    "A made-up app playing stock clips from Mixkit. Example numbers.": "Eine erfundene App mit Stock-Clips von Mixkit. Beispielzahlen.",
    "On Android": "Auf Android",
    "A small card floats over the apps you pick. It shows how long this visit has lasted and about how many videos went by. One tap hides it.":
        "Eine kleine Karte schwebt über den Apps, die du auswählst. Sie zeigt, wie lange dieser Besuch schon dauert und ungefähr wie viele Videos vorbeigezogen sind. Ein Tipp blendet sie aus.",
    "On iPhone": "Auf dem iPhone",
    "iOS doesn't let one app draw over another, so Pausely sends a banner every few minutes: your time in the app today, and about how many short videos that comes to.":
        "iOS lässt keine App über einer anderen zeichnen. Deshalb schickt Pausely alle paar Minuten ein Banner: deine heutige Zeit in der App und ungefähr wie viele Kurzvideos das sind.",
    "An estimate": "Eine Schätzung",
    "Some videos can be missed, and not every feed can be counted. The timer keeps going either way.":
        "Manche Videos können fehlen, und nicht jeder Feed lässt sich zählen. Der Timer läuft in jedem Fall weiter.",
    "Yours to turn on": "Du schaltest es ein",
    "Part of Premium, and off until you switch it on. The totals stay on your phone.":
        "Teil von Premium und aus, bis du es einschaltest. Die Summen bleiben auf deinem Handy.",
    "On iPhone, Pausely can't even read which apps you picked. Apple keeps that.":
        "Auf dem iPhone kann Pausely nicht einmal lesen, welche Apps du gewählt hast. Das behält Apple für sich.",
    "iPhone, iPad and Android.<br>English and seven other languages.": "iPhone, iPad und Android.<br>Auf Deutsch und in sieben weiteren Sprachen.",
})

T["es"].update({
    "For iPhone, iPad and Android": "Para iPhone, iPad y Android",
    "Get it on": "Disponible en",
    "Get it on Google Play": "Disponible en Google Play",
    _LEGAL: "Las pantallas de la app muestran sus datos de demostración, y las imágenes más sencillas son dibujos. Apple, iPhone, iPad, Safari, Tiempo de uso y App Store son marcas comerciales de Apple Inc. Android y Google Play son marcas comerciales de Google LLC. TikTok e Instagram son marcas de sus propietarios. Pausely no está afiliada, patrocinada ni respaldada por ellos ni por ninguna otra app nombrada o mostrada aquí.",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone, iPad and Android. Breathe first, then decide. Free to start.":
        "Pausely pone una pausa de diez segundos delante de las apps que abres sin pensar, en iPhone, iPad y Android. Primero respira, luego decide. Gratis para empezar.",
    "An app for iPhone, iPad and Android that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "Una app para iPhone, iPad y Android que pone una pausa breve delante de las apps que eliges, para que abrirlas sea una decisión.",
    "Does a pause work? <em>It has been tested.</em>": "¿Funciona una pausa? <em>Se ha estudiado.</em>",
    "In 2023, researchers published a six week study of 280 people using an app that works this way: a short wait before the app opens, then a way to change your mind.":
        "En 2023, unos investigadores publicaron un estudio de seis semanas con 280 personas que usaban una app que funciona así: una breve espera antes de que se abra la app y, después, la opción de cambiar de idea.",
    "of the time, people closed the app again after the pause.": "de las veces, la gente volvió a cerrar la app tras la pausa.",
    "fewer attempts to open those apps by week six than in week one.": "menos intentos de abrir esas apps en la sexta semana que en la primera.",
    "fewer times those apps were actually opened after six weeks.": "menos veces se abrieron de verdad esas apps tras seis semanas.",
    _SECOND: "Un segundo experimento con 500 personas analizó qué parte funcionaba. La opción de echarse atrás fue lo que más ayudó, y la espera también ayudó. Pausely te da las dos cosas: la pausa y, después, «He cambiado de idea».",
    _STUDY: "El estudio probó otra app que hace una pausa de la misma manera, no Pausely, y uno de sus tres autores desarrolla esa app. Pausely no ha tenido un estudio propio, así que lee estas cifras como lo que el método logró allí, no como una promesa. Fuente: Grüning, Riedel y Lorenz-Spreen, {paper}, PNAS, 2023.",
    "Six kinds of pause. <em>Pick yours.</em>": "Seis tipos de pausa. <em>Elige la tuya.</em>",
    "A breath is the pause everybody starts with, and it is free. With Premium you can pick another, or let Pausely choose a different one each time.":
        "Una respiración es la pausa con la que empieza todo el mundo, y es gratis. Con Premium puedes elegir otra, o dejar que Pausely elija una distinta cada vez.",
    "Type": "Escribe",
    "Say why": "Di por qué",
    "Read a line": "Lee una frase",
    "A reminder from Pausely, or one you wrote yourself.": "Un recordatorio de Pausely, o uno que hayas escrito tú.",
    "Answer a question": "Responde una pregunta",
    "One question about where you live. One try.": "Una pregunta sobre tu país. Un intento.",
    "Reflect": "Reflexiona",
    "Say why you are here. Get one gentle question back.": "Di por qué estás aquí y recibe una pregunta amable a cambio.",
    "The reminder pause: a short line to read under the label On being here, with a bar that fills while you read, and Show me another.":
        "La pausa de recordatorio, versión en inglés: una frase corta para leer, una barra que se llena mientras lees y un botón para ver otra.",
    "The question pause: One question. One try. Which of these rivers runs through the middle of the capital city? Four answers and an Answer button.":
        "La pausa de pregunta, versión en inglés: una pregunta, un intento. ¿Cuál de estos ríos atraviesa el centro de la capital? Cuatro respuestas y un botón para responder.",
    "The reflection pause: you said Just checking, and Pausely asks What would make the next hour feel like it went well?":
        "La pausa de reflexión, versión en inglés: elegiste Solo miraba, y Pausely pregunta qué haría que la próxima hora fuera una buena hora.",
    "Swipe to see all six.": "Desliza para ver las seis.",
    "Screens from the English iPhone app, showing its demo data. The app itself is in your language.":
        "Pantallas de la app de iPhone en inglés, con sus datos de demostración. La app en sí está en español.",
    "The Android app has the same pauses, though a new one can reach it a little later. The last two are written by AI and stay off until you turn AI pauses on.":
        "La app de Android tiene las mismas pausas, aunque una nueva puede llegar un poco más tarde. Las dos últimas las escribe una IA y están desactivadas hasta que actives las pausas con IA.",
    "What they send": "Qué envían",
    "After any pause you choose: stop there, do something else, or go in for a few minutes. Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "Después de cualquier pausa eliges tú: parar ahí, hacer otra cosa o entrar unos minutos. ¿Lo quieres más firme? Reglas, límites diarios, Bloquear todo y el modo estricto están ahí cuando los necesites.",
    "How many reels <em>was that?</em>": "¿Cuántos reels <em>han sido?</em>",
    "It is easy to lose count of short videos. Pausely keeps a rough count for you, and shows it while you are still scrolling.":
        "Es fácil perder la cuenta de los vídeos cortos. Pausely lleva una cuenta aproximada por ti y te la enseña mientras sigues deslizando.",
    _REELS_ALT: "Un móvil Android reproduce vídeos cortos en una app inventada. En la esquina superior derecha, la tarjeta flotante de Pausely muestra 00:42, 12 reels, esta visita, estimado. Cifras de ejemplo.",
    "Dislike": "No me gusta", "Share": "Compartir", "Follow": "Seguir", "Original sound": "Sonido original",
    "The easiest weeknight dinner": "La cena más fácil entre semana",
    "He heard the word walk": "Ha oído la palabra paseo",
    "Found this beach by accident": "Encontré esta playa por casualidad",
    "Sprinkles, in slow motion": "Virutas de colores, a cámara lenta",
    "Day 12 of painting every day": "Día 12 pintando cada día",
    "Home": "Inicio", "Clips": "Clips", "Following": "Siguiendo", "You": "Tú",
    "reels": "reels",
    "This visit · estimated": "Esta visita · estimado",
    "<b>This is Android.</b> On iPhone you get a banner every few minutes instead, with about how many short videos you watched.":
        "<b>Esto es Android.</b> En iPhone, en su lugar, recibes un aviso cada pocos minutos con cuántos vídeos cortos has visto, más o menos.",
    "A made-up app playing stock clips from Mixkit. Example numbers.": "Una app inventada con clips de stock de Mixkit. Cifras de ejemplo.",
    "On Android": "En Android",
    "A small card floats over the apps you pick. It shows how long this visit has lasted and about how many videos went by. One tap hides it.":
        "Una pequeña tarjeta flota sobre las apps que eliges. Muestra cuánto dura esta visita y cuántos vídeos han pasado, más o menos. Un toque la oculta.",
    "On iPhone": "En iPhone",
    "iOS doesn't let one app draw over another, so Pausely sends a banner every few minutes: your time in the app today, and about how many short videos that comes to.":
        "iOS no deja que una app se dibuje sobre otra, así que Pausely envía un aviso cada pocos minutos: tu tiempo de hoy en la app y a cuántos vídeos cortos equivale, más o menos.",
    "An estimate": "Una estimación",
    "Some videos can be missed, and not every feed can be counted. The timer keeps going either way.":
        "Algunos vídeos pueden escaparse y no todos los feeds se pueden contar. El temporizador sigue en marcha igualmente.",
    "Yours to turn on": "Lo activas tú",
    "Part of Premium, and off until you switch it on. The totals stay on your phone.":
        "Forma parte de Premium y está desactivado hasta que lo actives. Los totales se quedan en tu móvil.",
    "On iPhone, Pausely can't even read which apps you picked. Apple keeps that.":
        "En iPhone, Pausely ni siquiera puede leer qué apps elegiste. Eso lo guarda Apple.",
    "iPhone, iPad and Android.<br>English and seven other languages.": "iPhone, iPad y Android.<br>En español y en otros siete idiomas.",
})

T["ja"].update({
    "For iPhone, iPad and Android": "iPhone・iPad・Android向け",
    "Get it on": "今すぐ手に入れよう",
    "Get it on Google Play": "Google Playで手に入れよう",
    _LEGAL: "アプリの画面はデモデータを表示しており、簡単な絵はイラストです。Apple、iPhone、iPad、Safari、スクリーンタイム、App StoreはApple Inc.の商標です。AndroidとGoogle PlayはGoogle LLCの商標です。TikTokとInstagramは各所有者の商標です。Pauselyは、これらの企業やここに名前や画面が出てくる他のアプリとは提携しておらず、後援や推奨も受けていません。",
    "Pausely puts a ten second pause in front of the apps you open without thinking, on iPhone, iPad and Android. Breathe first, then decide. Free to start.":
        "Pauselyは、何となく開いてしまうアプリの前に10秒のひと呼吸を置くアプリです。iPhone、iPad、Androidに対応。まず呼吸して、それから決める。無料で始められます。",
    "An app for iPhone, iPad and Android that puts a short pause in front of the apps you choose, so opening them becomes a decision.":
        "選んだアプリの前に短いひと呼吸を置き、開くことを自分の決断に変えるiPhone・iPad・Androidアプリ。",
    "Does a pause work? <em>It has been tested.</em>": "<span class=\"nw\">ひと呼吸に</span><span class=\"nw\">効果はある？</span><em class=\"nw\">研究があります。</em>",
    "In 2023, researchers published a six week study of 280 people using an app that works this way: a short wait before the app opens, then a way to change your mind.":
        "2023年、研究者たちは、同じ仕組みのアプリを使う280人を6週間追った研究を発表しました。アプリが開く前に短く待たされ、そのあと考え直す選択肢が出る仕組みです。",
    "of the time, people closed the app again after the pause.": "の場面で、ひと呼吸のあとにアプリを閉じました。",
    "fewer attempts to open those apps by week six than in week one.": "減少。6週目には、1週目よりアプリを開こうとする回数が減りました。",
    "fewer times those apps were actually opened after six weeks.": "減少。6週間後、実際にアプリが開かれた回数が減りました。",
    _SECOND: "500人を対象にした2つめの実験では、どの部分が効いているかを調べました。いちばん効いたのは引き返す選択肢で、待つことにも効果がありました。Pauselyはその両方を備えています。ひと呼吸と、そのあとの「やっぱりやめる」です。",
    _STUDY: "この研究で試されたのはPauselyではなく、同じように一呼吸を置く別のアプリで、著者3人のうち1人がそのアプリの開発者です。Pausely自体の研究はまだありません。ここの数字は、その方法が研究の中で示した結果であって、約束ではありません。出典：Grüning、Riedel、Lorenz-Spreen、{paper}、PNAS、2023年。",
    "Six kinds of pause. <em>Pick yours.</em>": "<span class=\"nw\">6種類の一呼吸。</span><em class=\"nw\">好きなものを。</em>",
    "A breath is the pause everybody starts with, and it is free. With Premium you can pick another, or let Pausely choose a different one each time.":
        "最初の一呼吸は、だれでも呼吸から。これは無料です。Premiumなら別の一呼吸を選んだり、毎回Pauselyに違うものを選ばせたりできます。",
    "Type": "入力する",
    "Say why": "理由を選ぶ",
    "Read a line": "ひと言を読む",
    "A reminder from Pausely, or one you wrote yourself.": "Pauselyからのひと言か、自分で書いたひと言を。",
    "Answer a question": "質問に答える",
    "One question about where you live. One try.": "あなたの国についての質問がひとつ。チャンスは1回。",
    "Reflect": "振り返る",
    "Say why you are here. Get one gentle question back.": "ここに来た理由を伝えると、やさしい質問がひとつ返ってきます。",
    "The reminder pause: a short line to read under the label On being here, with a bar that fills while you read, and Show me another.":
        "ひと言の一呼吸（英語版）：読むための短いひと言、読んでいるあいだに満ちていくバー、別のひと言を表示するボタン。",
    "The question pause: One question. One try. Which of these rivers runs through the middle of the capital city? Four answers and an Answer button.":
        "質問の一呼吸（英語版）：質問はひとつ、チャンスは1回。首都の中心を流れる川はどれ？4つの答えと回答ボタン。",
    "The reflection pause: you said Just checking, and Pausely asks What would make the next hour feel like it went well?":
        "振り返りの一呼吸（英語版）：「ちょっと見るだけ」を選ぶと、Pauselyが「この先の1時間をよい時間にするには？」と尋ねます。",
    "Swipe to see all six.": "スワイプして6つすべてを見る。",
    "Screens from the English iPhone app, showing its demo data. The app itself is in your language.":
        "英語版iPhoneアプリの画面で、デモデータを表示しています。アプリ自体は日本語で表示されます。",
    "The Android app has the same pauses, though a new one can reach it a little later. The last two are written by AI and stay off until you turn AI pauses on.":
        "Androidアプリにも同じ一呼吸があります。新しいものは少し遅れて届くことがあります。最後の2つはAIが書くもので、AIの一呼吸をオンにするまでオフのままです。",
    "What they send": "送信される内容",
    "After any pause you choose: stop there, do something else, or go in for a few minutes. Want it firmer? Rules, daily limits, Block everything and strict mode are there when you ask.":
        "どの一呼吸のあとも、選ぶのはあなたです。そこでやめるか、別のことをするか、数分だけ使うか。もっとしっかり止めたいなら、ルール、1日の上限、すべてブロック、厳格モードも使えます。",
    "How many reels <em>was that?</em>": "<span class=\"nw\">いま、リールを</span><em class=\"nw\">何本見た？</em>",
    "It is easy to lose count of short videos. Pausely keeps a rough count for you, and shows it while you are still scrolling.":
        "ショート動画は、見た本数を忘れがちです。Pauselyがおおよその数を数えて、スクロールしているあいだに表示します。",
    _REELS_ALT: "架空のアプリでショート動画を再生しているAndroidスマートフォン。右上にPauselyのフローティングカードがあり、00:42、12本、今回の利用、推定と表示されています。数字は例です。",
    "Dislike": "低評価", "Share": "共有", "Follow": "フォロー", "Original sound": "オリジナル音源",
    "The easiest weeknight dinner": "平日のいちばん簡単な夕ごはん",
    "He heard the word walk": "「散歩」って聞こえたみたい",
    "Found this beach by accident": "偶然見つけたビーチ",
    "Sprinkles, in slow motion": "スローモーションのスプリンクル",
    "Day 12 of painting every day": "毎日お絵かき12日目",
    "Home": "ホーム", "Clips": "クリップ", "Following": "フォロー中", "You": "マイページ",
    "reels": "本",
    "This visit · estimated": "今回の利用 · 推定",
    "<b>This is Android.</b> On iPhone you get a banner every few minutes instead, with about how many short videos you watched.":
        "<b>これはAndroidです。</b>iPhoneでは代わりに数分ごとにバナーが届き、見たショート動画のおおよその本数を伝えます。",
    "A made-up app playing stock clips from Mixkit. Example numbers.": "Mixkitのストック動画を再生する架空のアプリです。数字は例です。",
    "On Android": "Androidでは",
    "A small card floats over the apps you pick. It shows how long this visit has lasted and about how many videos went by. One tap hides it.":
        "選んだアプリの上に小さなカードが浮かび、今回の利用時間と、流れていった動画のおおよその本数を表示します。タップひとつで隠せます。",
    "On iPhone": "iPhoneでは",
    "iOS doesn't let one app draw over another, so Pausely sends a banner every few minutes: your time in the app today, and about how many short videos that comes to.":
        "iOSでは、アプリが別のアプリの上に表示することはできません。そのためPauselyは数分ごとにバナーを送り、今日そのアプリで過ごした時間と、それがショート動画何本分くらいかを伝えます。",
    "An estimate": "あくまで推定",
    "Some videos can be missed, and not every feed can be counted. The timer keeps going either way.":
        "数え漏れる動画もあり、数えられないフィードもあります。それでもタイマーは動き続けます。",
    "Yours to turn on": "オンにするのはあなた",
    "Part of Premium, and off until you switch it on. The totals stay on your phone.":
        "Premiumの機能で、オンにするまではオフのままです。合計はスマートフォンの中にとどまります。",
    "On iPhone, Pausely can't even read which apps you picked. Apple keeps that.":
        "iPhoneでは、Pauselyはどのアプリを選んだかさえ読み取れません。その情報はAppleが保持します。",
    "iPhone, iPad and Android.<br>English and seven other languages.": "iPhone・iPad・Android対応。<br>日本語を含む8言語に対応。",
})

# The FAQ answers that differ between iPhone and Android, as in the English FAQ.
def _replace(lang, question, answer):
    for i, (q, _) in enumerate(FAQ[lang]):
        if q == question:
            FAQ[lang][i] = (q, answer)
            return
    raise SystemExit(f"i18n: no {lang} FAQ question {question!r}")


_replace("de", "Mit welchen Apps funktioniert es?",
         "Mit jeder App auf deinem Handy, also mit genau den Apps, die dir Zeit nehmen. Auf iPhone und iPad wählst du "
         "sie in Apples eigener Bildschirmzeit-Auswahl, und Pausely erfährt nie ihre Namen: Apple gibt der App "
         "stattdessen private Codes. Auf Android wählst du sie aus der Liste der Apps auf deinem Handy.")
_replace("de", "Sieht Pausely, was ich in anderen Apps mache?",
         "Auf iPhone und iPad nicht. Pausely sieht nie, was du im Web aufrufst, deine Nachrichten oder irgendetwas in "
         "einer anderen App. iOS teilt Pausely mit, wie lange die gewählten Apps geöffnet waren, und diese Minuten "
         "bleiben auf deinem Gerät. Auf Android nutzt Pausely die Bedienungshilfen, um zu sehen, welche App im "
         "Vordergrund ist. Es liest nie deine Nachrichten oder was du tippst, und es tippt nie für dich. In Chrome und "
         "einigen anderen Browsern sieht es auch die Adresse der Website, die du öffnest, damit es die gewählten "
         "Websites pausieren kann. Es fragt vorher und erklärt das alles, bevor du zustimmst.")
_replace("de", "Ist Pausely kostenlos?",
         "Ja, und kostenlos ist ein vollwertiges Produkt, keine Demo: zwei geschützte Apps, eine Regel, die Atempause "
         "und dein ganzer Fortschritt. Auf iPhone und iPad gehören auch die heutige Zeit in jeder gewählten App und "
         "der Countdown auf dem Sperrbildschirm und in der Dynamic Island dazu.")
_replace("de", "Welche Geräte brauche ich?",
         "Ein iPhone oder iPad mit iOS 17 oder iPadOS 17 oder neuer, oder ein Android-Handy mit Android 8 oder neuer. "
         "Eine Mac-Version gibt es nicht.")

_replace("es", "¿Con qué apps funciona?",
         "Con cualquier app de tu móvil, así que funciona con las que se llevan tu tiempo. En iPhone y iPad las eliges "
         "en el selector de Tiempo de uso de Apple, y Pausely nunca sabe sus nombres: Apple le da códigos privados en "
         "su lugar. En Android las eliges de la lista de apps de tu móvil.")
_replace("es", "¿Pausely ve lo que hago en otras apps?",
         "En iPhone y iPad, no. Nunca ve lo que navegas, tus mensajes ni nada dentro de otra app. iOS le dice cuánto "
         "tiempo han estado abiertas las apps que elegiste, y Pausely guarda esos minutos en tu dispositivo. En "
         "Android, Pausely usa el servicio de accesibilidad para ver qué app está en primer plano. Nunca lee tus "
         "mensajes ni lo que escribes, y nunca toca ni escribe por ti. En Chrome y algunos otros navegadores también ve "
         "la dirección de la web que abres, para poder pausar las webs que elegiste. Te lo pregunta antes y te lo "
         "explica todo antes de que digas que sí.")
_replace("es", "¿Pausely es gratis?",
         "Sí, y la versión gratis es un producto completo, no una demo: dos apps protegidas, una regla, la pausa para "
         "respirar y toda tu pantalla de progreso. En iPhone y iPad también incluye el tiempo de hoy en cada app "
         "elegida y la cuenta atrás en la pantalla bloqueada y en la Dynamic Island.")
_replace("es", "¿Qué dispositivos necesito?",
         "Un iPhone o iPad con iOS 17 o iPadOS 17 o posterior, o un móvil Android con Android 8 o posterior. No hay "
         "versión para Mac.")

_replace("ja", "どのアプリで使えますか？",
         "スマートフォンのどのアプリでも使えるので、時間を取られているアプリならどれでも対象にできます。iPhoneとiPadでは"
         "Apple純正のスクリーンタイムの選択画面で選び、Pauselyがアプリの名前を知ることはありません。Appleからは非公開の"
         "コードだけが渡されます。Androidでは、スマートフォンのアプリ一覧から選びます。")
_replace("ja", "Pauselyは他のアプリでの操作を見ていますか？",
         "iPhoneとiPadでは見ていません。閲覧履歴やメッセージ、他のアプリの中身を見ることはありません。iOSが伝えるのは、"
         "選んだアプリが開いていた時間だけで、その時間はデバイスの中に保存されます。Androidでは、どのアプリが前面に"
         "あるかを知るためにユーザー補助サービスを使います。メッセージや入力内容を読むことはなく、代わりにタップや入力を"
         "することもありません。Chromeなど一部のブラウザでは、選んだサイトで一呼吸を置けるように、開いたサイトのアドレスも"
         "見ます。許可を求める前に、これらすべてを説明します。")
_replace("ja", "Pauselyは無料ですか？",
         "はい。無料版はお試しではなく、きちんと使える製品です。アプリ2つの保護、ルールひとつ、呼吸の一呼吸、記録の画面"
         "すべてが使えます。iPhoneとiPadでは、選んだアプリごとの今日の使用時間と、ロック画面とDynamic Islandの"
         "カウントダウンも使えます。")
_replace("ja", "どのデバイスで使えますか？",
         "iOS 17またはiPadOS 17以降のiPhoneかiPad、またはAndroid 8以降のAndroidスマートフォンです。Mac版はありません。")

# Footer: links to the company's other apps (28 Nov 2026).
T["de"].update({
    "Our other apps": "Unsere anderen Apps",
    "stop impulse buying": "weniger Impulskäufe",
    "period and pregnancy tracker": "Zyklus und Schwangerschaft im Blick",
})
T["es"].update({
    "Our other apps": "Nuestras otras apps",
    "stop impulse buying": "frena las compras por impulso",
    "period and pregnancy tracker": "seguimiento de periodo y embarazo",
})
T["ja"].update({
    "Our other apps": "ほかのアプリ",
    "stop impulse buying": "衝動買いを減らす",
    "period and pregnancy tracker": "生理と妊娠の記録",
})
