#!/usr/bin/env python3
"""Builds the static pages for bigrockco.com.

The site is plain HTML. This script stamps the shared header, footer, and quote
form into each page so they stay identical. Edit the content below, then run:

    python3 _src/build.py

Jekyll on GitHub Pages ignores this _src folder, so it is never published.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://bigrockco.com"
EMAIL = "BigRockLMTD@gmail.com"
LEGAL_NAME = "Big Rock Management LLC"
BROKERAGE = "Keller Williams Southern Arizona"
EFFECTIVE = "October 4, 2026"
NO_QUOTE = {"404.html", "privacy.html", "terms.html", "accessibility.html"}

# Equal Housing Opportunity mark (house with an equals sign), drawn as plain geometry
EHO = ('<svg class="eho" viewBox="0 0 40 40" role="img" aria-label="Equal Housing Opportunity">'
       '<path d="M20 3 2 15.5h4.5V37h27V15.5H38z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
       '<rect x="12" y="18" width="16" height="4" fill="currentColor"/><rect x="12" y="26" width="16" height="4" fill="currentColor"/></svg>')

# ---------- icons (Lucide, ISC license) ----------
def icon(name):
    paths = {
        "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
        "menu": '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
        "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
        "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
        "tag": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
        "calendar": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>',
        "key": '<path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/><path d="m21 2-9.6 9.6"/><circle cx="7.5" cy="15.5" r="5.5"/>',
        "sparkles": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/>',
        "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
        "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
        "sign": '<path d="M12 13v8"/><path d="M12 3v3"/><path d="M4 6a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h13a2 2 0 0 0 1.152-.365l3.424-2.317a1 1 0 0 0 0-1.635l-3.424-2.318A2 2 0 0 0 17 6z"/>',
    }
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')

# ---------- patches ----------
PATCHES = {
    "rentals": ("Rentals", "Short-term management", "rentals.html"),
    "cleaning": ("Cleaning", "Big Rock Service Solutions", "cleaning.html"),
    "hauling": ("Hauling", "Junk &amp; debris removal", "hauling.html"),
    "realty": ("Realty", "Buy &amp; sell", "realty.html"),
}

def patch(key, link=True, extra=""):
    name, sub, href = PATCHES[key]
    cls = f"patch patch--{key}"
    tag_open = f'<a class="{cls}" href="{href}"{extra}>' if link else f'<div class="{cls}" aria-hidden="true"{extra}>'
    tag_close = "</a>" if link else "</div>"
    return (f'{tag_open}<span class="patch__dome"><svg viewBox="0 0 200 200" aria-hidden="true">'
            f'<use href="assets/patches.svg#scene-{key}"/></svg></span>'
            f'<span class="patch__bar"><span class="patch__name">{name}</span>'
            f'<span class="patch__sub">{sub}</span></span>{tag_close}')

def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items) + "</ul>"

TAGS = (f'<ul class="tags" aria-label="Why Big Rock"><li>{icon("pin")}Locally owned in Tucson</li>'
        f'<li>{icon("tag")}Free quotes</li><li>{icon("calendar")}Same-week service</li></ul>')

# ---------- shell ----------
NAV = [("rentals.html", "Rentals"), ("cleaning.html", "Cleaning"), ("hauling.html", "Hauling"), ("realty.html", "Buy &amp; Sell")]

def header(current):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./" aria-label="Big Rock Management home">
      <img src="assets/img/logo-180.png" width="52" height="52" alt="">
      <span><b>Big Rock</b><small>Management</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{icon("menu")}</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn btn--small" href="#quote">Free quote</a>
    </nav>
  </div>
</header>'''

def quote(service=""):
    opts = [("rentals", "Short-term rental management"), ("cleaning", "Deep clean or reset (Big Rock Service Solutions)"),
            ("hauling", "Hauling &amp; debris removal"), ("realty", "Buying or selling a home"), ("other", "Not sure yet / more than one")]
    options = '<option value="" disabled selected>Choose one</option>' + "".join(
        f'<option value="{v}"{" selected" if v == service else ""}>{t}</option>' for v, t in opts)
    if service:
        options = options.replace(' disabled selected>Choose one', ' disabled>Choose one')
    areas = ["Tucson", "Oro Valley", "Marana", "Vail", "Sahuarita", "Somewhere else nearby"]
    area_opts = '<option value="" disabled selected>Choose one</option>' + "".join(f"<option>{a}</option>" for a in areas)
    return f'''<section class="quote" id="quote" aria-labelledby="quote-title">
  <div class="wrap">
    <div class="quote__side">
      <h2 id="quote-title">Tell us about the job. <em>The quote is free.</em></h2>
      <p>A few details is all it takes. We'll email you back with a plan and a price, and get you on the calendar, usually the same week.</p>
      <a class="quote__email" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>
      {TAGS}
    </div>
    <form class="form" action="mailto:{EMAIL}" method="POST" enctype="text/plain" novalidate>
      <div class="field">
        <label for="q-name">Your name</label>
        <input id="q-name" name="name" autocomplete="name" required>
        <span class="err">Please add your name.</span>
      </div>
      <div class="field">
        <label for="q-email">Email</label>
        <input id="q-email" name="email" type="email" autocomplete="email" required>
        <span class="err">Please add an email we can reply to.</span>
      </div>
      <div class="field">
        <label for="q-phone">Phone <small>(optional)</small></label>
        <input id="q-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="field">
        <label for="q-area">Where's the property?</label>
        <select id="q-area" name="area" required>{area_opts}</select>
        <span class="err">Please pick an area.</span>
      </div>
      <div class="field field--full">
        <label for="q-service">What do you need?</label>
        <select id="q-service" name="service" required>{options}</select>
        <span class="err">Please pick a service.</span>
      </div>
      <div class="field field--full">
        <label for="q-details">Details <small>(size of the place, what needs to go, dates)</small></label>
        <textarea id="q-details" name="details" placeholder="e.g. 3-bed casita in Oro Valley, want it listed on Airbnb by spring"></textarea>
      </div>
      <div class="hp" aria-hidden="true"><label for="q-gotcha">Leave this empty</label><input id="q-gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
      <p class="form__status" role="status" tabindex="-1"></p>
      <div class="form__foot">
        <button class="btn btn--gold" type="submit"><span>Send my quote request</span>{icon("arrow")}</button>
        <p class="form__note">We only use your details to reply to your request. See our <a href="privacy.html">privacy policy</a>.</p>
      </div>
    </form>
  </div>
</section>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer__brand">
      <img src="assets/img/logo-180.png" width="104" height="104" alt="Big Rock Management logo" loading="lazy">
      <p>Part of the Big Rock group of companies. Locally owned, serving the Tucson metro in Southern Arizona.</p>
    </div>
    <div>
      <h2>Services</h2>
      <ul>
        <li><a href="rentals.html">Short-term rental management</a></li>
        <li><a href="cleaning.html">Big Rock Service Solutions</a></li>
        <li><a href="hauling.html">Hauling &amp; debris removal</a></li>
        <li><a href="https://bigrockaz.com" target="_blank" rel="noopener">Big Rock Realty Group</a></li>
      </ul>
    </div>
    <div>
      <h2>Contact</h2>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Tucson metro, Southern Arizona</li>
        <li><a href="#quote">Request a free quote</a></li>
      </ul>
    </div>
    <div class="footer__broker">
      {EHO}
      <p>Real estate services are provided by Big Rock Realty Group, brokered by {BROKERAGE}. Each Keller Williams office is independently owned and operated. Equal Housing Opportunity.</p>
    </div>
    <div class="footer__legal">
      <span>&copy; 2026 {LEGAL_NAME}. All rights reserved.</span>
      <nav class="footer__links" aria-label="Legal"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="accessibility.html">Accessibility</a></nav>
      <span>Placeholder stock photography via Unsplash.</span>
    </div>
  </div>
</footer>
<script src="main.js" defer></script>'''

def page(file, title, desc, body_class, main, service="", current=None):
    url = SITE + "/" + ("" if file == "index.html" else file)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{'<base href="/">' if file == "404.html" else ""}
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#efe4cf">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/img/favicon-96.png">
<link rel="apple-touch-icon" href="assets/img/logo-180.png">
<link rel="preload" href="assets/fonts/AlfaSlabOne-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/Archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
{SCHEMA if file == "index.html" else ""}
</head>
<body class="{body_class}">
{header(current if current is not None else file)}
<main id="main">
{main}
</main>
{quote(service) if file not in NO_QUOTE else ""}
{FOOTER}
</body>
</html>
'''
    if file in NO_QUOTE:
        html = html.replace('href="#quote"', 'href="./#quote"')
    (ROOT / file).write_text(html)

SCHEMA = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Big Rock Management","url":"{SITE}/","email":"{EMAIL}","logo":"{SITE}/assets/img/logo-640.png","image":"{SITE}/assets/img/og-image.jpg","description":"Short-term rental management, deep cleaning, and hauling across the Tucson metro.","areaServed":["Tucson, AZ","Oro Valley, AZ","Marana, AZ","Vail, AZ","Sahuarita, AZ"],"address":{{"@type":"PostalAddress","addressLocality":"Tucson","addressRegion":"AZ","addressCountry":"US"}}}}
</script>'''

def page_hero(key, brand, h1, lede, primary_label, secondary=None):
    sec = ""
    if secondary:
        sec = f'<a class="link-arrow" href="{secondary[0]}">{secondary[1]}{icon("arrow")}</a>'
    return f'''<section class="page-hero">
  <div class="wrap">
    <div>
      <span class="page-hero__brand label">{brand}</span>
      <h1>{h1}</h1>
      <p class="page-hero__lede">{lede}</p>
      <div class="hero__actions">
        <a class="btn" href="#quote">{primary_label}{icon("arrow")}</a>
        {sec}
      </div>
    </div>
    {patch(key, link=False)}
  </div>
</section>'''

def faq(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q, a in items) + "</div>"

def family(exclude):
    keys = [k for k in PATCHES if k != exclude]
    return '<div class="family">' + "".join(patch(k) for k in keys) + "</div>"

# ================= HOME =================
home = f'''<section class="hero">
  <div class="wrap">
    <div class="hero__copy">
      <h1>One crew for the <em>whole</em> property.</h1>
      <p class="hero__lede">Buying and selling with Big Rock Realty Group, plus short-term rental management, deep cleans, and haul-offs across the Tucson metro. Pick your patch: it's all one family of companies.</p>
      <div class="hero__actions">
        <a class="btn" href="#quote">Get a free quote{icon("arrow")}</a>
        <a class="link-arrow" href="#services">See what we do{icon("arrow")}</a>
      </div>
      {TAGS}
    </div>
    <nav class="board" aria-label="Big Rock companies">
      {patch("rentals")}
      {patch("cleaning")}
      {patch("hauling")}
      {patch("realty")}
    </nav>
  </div>
</section>

<section class="section section--ink" aria-labelledby="loop-title">
  <div class="wrap">
    <div class="section__intro">
      <h2 id="loop-title">Buy it, reset it, rent it, clear it, sell it.</h2>
      <p>Most owners juggle a different company for every stage of a property. Big Rock covers every stage, so nothing falls between crews.</p>
    </div>
    <ol class="loop">
      <li><span class="loop__dot">{icon("sign")}</span><h3>Buy it</h3><p>Find the right place in Tucson.</p><span class="who label">Big Rock Realty Group</span></li>
      <li><span class="loop__dot">{icon("sparkles")}</span><h3>Reset it</h3><p>A deep clean so it starts fresh.</p><span class="who label">Service Solutions</span></li>
      <li><span class="loop__dot">{icon("key")}</span><h3>Rent it</h3><p>Listed, priced, and guest-ready.</p><span class="who label">Rental management</span></li>
      <li><span class="loop__dot">{icon("truck")}</span><h3>Clear it</h3><p>Old furniture and debris, gone.</p><span class="who label">Hauling</span></li>
      <li><span class="loop__dot">{icon("home")}</span><h3>Sell it</h3><p>Clean, empty, and ready to list.</p><span class="who label">Big Rock Realty Group</span></li>
    </ol>
  </div>
</section>

<section class="section" id="services" aria-labelledby="services-title">
  <div class="wrap">
    <div class="section__intro">
      <h2 id="services-title">What each patch handles</h2>
      <p>Four companies, one family, one email.</p>
    </div>

    <article class="service">
      <div class="service__media">
        <img src="assets/img/rentals-patio.jpg" width="1400" height="934" alt="Desert patio with shade sails, a water feature, and mountain views" loading="lazy">
        {patch("rentals", link=False)}
      </div>
      <div class="service__body">
        <span class="service__brand label">Big Rock Management</span>
        <h3>Short-term rental management</h3>
        <p>Own a casita or home you'd like on Airbnb or VRBO, without becoming a full-time host? We run it for you.</p>
        {ticks(["<b>Listing &amp; pricing:</b> setup, photos, and nightly rates that move with demand", "<b>Guests:</b> messaging, check-in, and reviews", "<b>Turnovers &amp; upkeep:</b> cleans between stays, restocking, and maintenance coordination"])}
        <a class="link-arrow" href="rentals.html">Rental management{icon("arrow")}</a>
      </div>
    </article>

    <article class="service service--flip">
      <div class="service__media">
        <img src="assets/img/cleaning-caddy.jpg" width="1400" height="934" alt="Cleaner carrying a caddy and broom up a tiled staircase" loading="lazy">
        {patch("cleaning", link=False)}
      </div>
      <div class="service__body">
        <span class="service__brand label">Big Rock Service Solutions</span>
        <h3>Deep cleans &amp; resets</h3>
        <p>For the cleans a weekly wipe-down doesn't touch: move-outs, between tenants, before listing, or after a long season of guests.</p>
        {ticks(["<b>Deep cleans:</b> kitchens, baths, baseboards, inside appliances", "<b>Resets:</b> move-in, move-out, and pre-listing", "<b>Rental-ready:</b> beds made, supplies stocked, photo-ready"])}
        <a class="link-arrow" href="cleaning.html">Cleaning &amp; resets{icon("arrow")}</a>
      </div>
    </article>

    <article class="service">
      <div class="service__media">
        <img src="assets/img/hauling-garage.jpg" width="1400" height="1010" alt="Garage packed with old equipment, tanks, and clutter" loading="lazy">
        {patch("hauling", link=False)}
      </div>
      <div class="service__body">
        <span class="service__brand label">Big Rock Management</span>
        <h3>Hauling &amp; bulk debris removal</h3>
        <p>Point at it, and it's gone. We load it, haul it, and leave the space swept.</p>
        {ticks(["<b>Junk &amp; furniture:</b> couches, mattresses, appliances, boxes", "<b>Yard &amp; construction:</b> brush, palm fronds, remodel leftovers", "<b>Cleanouts:</b> estates, move-outs, garages, and rentals"])}
        <a class="link-arrow" href="hauling.html">Hauling &amp; removal{icon("arrow")}</a>
      </div>
    </article>

    <article class="service service--flip">
      <div class="service__media">
        <img src="assets/img/realty-door.jpg" width="1400" height="982" alt="Blue adobe-style home with a red door and potted cactus" loading="lazy">
        {patch("realty", link=False)}
      </div>
      <div class="service__body">
        <span class="service__brand label">Big Rock Realty Group</span>
        <h3>Buying or selling a home</h3>
        <p>Big Rock Realty Group is the heart of the family: the team that helps Tucson buyers find a home and sellers get it sold. Everything else here grew up around it.</p>
        <a class="link-arrow" href="https://bigrockaz.com" target="_blank" rel="noopener">Visit bigrockaz.com{icon("arrow")}</a>
      </div>
    </article>
  </div>
</section>

<section class="section section--cream" aria-labelledby="area-title">
  <div class="wrap area">
    <img src="assets/img/tucson-view.jpg" width="1400" height="826" alt="Tucson foothills homes among saguaros, looking out over the city" loading="lazy">
    <div>
      <h2 id="area-title">Local to the Tucson metro</h2>
      <p>We're locally owned and work where we live: across the valley, from the foothills to the south side.</p>
      <ul class="towns"><li>Tucson</li><li>Oro Valley</li><li>Marana</li><li>Vail</li><li>Sahuarita</li></ul>
      <p>Somewhere just outside that? Ask anyway.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="how-title">How it works</h2></div>
    <ol class="steps">
      <li><h3>Tell us the job</h3><p>Use the form below or email us. Photos help if you have them.</p></li>
      <li><h3>Get a free quote</h3><p>We reply with a plan and a price. No charge, no pressure.</p></li>
      <li><h3>We show up</h3><p>Most cleans and hauls get scheduled the same week.</p></li>
    </ol>
  </div>
</section>

<section class="section section--cream" aria-labelledby="faq-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="faq-title">Questions we get</h2></div>
    {faq([
        ("Is it all one company?", "The Big Rock group is a family of companies. Buying and selling is Big Rock Realty Group (bigrockaz.com). Rental management and hauling are run by Big Rock Management. Cleaning runs as Big Rock Service Solutions."),
        ("How do quotes work?", "Tell us about the property and the job, and we'll email you a quote. It's free, and there's no obligation."),
        ("How soon can you come out?", "Most cleans and hauls are scheduled the same week you reach out."),
        ("Where do you work?", "Across the Tucson metro: Tucson, Oro Valley, Marana, Vail, and Sahuarita. If you're just outside that, ask."),
        ("Can I just call?", f"We handle everything by email so nothing gets lost. Write to {EMAIL} or use the quote form."),
    ])}
  </div>
</section>'''

page("index.html", "Big Rock Management | Rentals, Cleaning & Hauling in Tucson",
     "Short-term rental management, deep cleans and resets, and junk and debris hauling across the Tucson metro. Locally owned. Free quotes.",
     "page-home", home)

# ================= RENTALS =================
rentals = f'''{page_hero("rentals", "Big Rock Management", "Your Tucson rental, run for you.",
    "We set up the listing, price the nights, talk to the guests, and turn the place over between stays. You own it. We run it.",
    "Get a free quote", ("#included", "What's included"))}

<section class="section" id="included" aria-labelledby="inc-title">
  <div class="wrap">
    <div class="section__intro">
      <h2 id="inc-title">What we handle</h2>
      <p>Full-service management for short-term rentals on Airbnb and VRBO.</p>
    </div>
    <div class="included">
      <div>
        <h3>Listing &amp; pricing</h3>
        <p>A listing that earns the click.</p>
        {ticks(["Airbnb and VRBO listing setup", "Listing photos", "Nightly rates that move with the calendar and demand"])}
      </div>
      <div>
        <h3>Guest communication</h3>
        <p>Every message answered for you.</p>
        {ticks(["Questions before and during the stay", "Check-in instructions", "Reviews after checkout"])}
      </div>
      <div>
        <h3>Turnovers &amp; upkeep</h3>
        <p>Ready for the next guest, every time.</p>
        {ticks(["Cleans between stays", "Restocking supplies and linens", "Coordinating maintenance and repairs"])}
      </div>
    </div>
    <p class="not-offered"><b>Not included:</b> city and county permit filings and tax returns stay with the owner.</p>
  </div>
</section>

<section class="section section--cream" aria-labelledby="fit-title">
  <div class="wrap split split--tall">
    <img src="assets/img/rentals-bed.jpg" width="1120" height="1400" alt="Freshly made guest bed with rolled towels" loading="lazy">
    <div>
      <h2 id="fit-title">A good fit if you…</h2>
      {ticks(["Own a home, casita, or guest house in the Tucson metro", "Want rental income without hosting every stay yourself", "Already list a rental and want it handled better", "Want cleaning and hauling from the same team when you need it"])}
      <p>Every property is different, so pricing is quoted per property. The quote is free.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="rfaq-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="rfaq-title">Rental questions</h2></div>
    {faq([
        ("Which platforms do you list on?", "Airbnb and VRBO."),
        ("What does management cost?", "It depends on the property and how much you want handled. Tell us about your place and we'll send a free quote."),
        ("Do you handle permits and taxes?", "No. Short-term rental registration and tax filings stay in the owner's name and hands."),
        ("Who cleans between guests?", "Turnover cleans are part of what we manage, so you never schedule a cleaner."),
    ])}
    <div class="family-wrap"><h2 class="family-title">The rest of the family</h2>{family("rentals")}</div>
  </div>
</section>'''

page("rentals.html", "Short-Term Rental Management in Tucson | Big Rock Management",
     "Airbnb and VRBO management in the Tucson metro: listing setup, pricing, guest communication, and turnovers. Locally owned. Free quotes.",
     "page-rentals", rentals, service="rentals")

# ================= CLEANING =================
cleaning = f'''{page_hero("cleaning", "Big Rock Service Solutions", "Deep cleans and full resets.",
    "The clean you book when a place needs to start over: move-outs, between tenants, before listing, or after a long run of guests.",
    "Get a free quote", ("#included", "What's included"))}

<section class="section" id="included" aria-labelledby="inc-title">
  <div class="wrap">
    <div class="section__intro">
      <h2 id="inc-title">Two kinds of clean</h2>
      <p>Big Rock Service Solutions is the cleaning arm of the Big Rock group.</p>
    </div>
    <div class="included">
      <div>
        <h3>Deep clean</h3>
        <p>Top to bottom, inside and out.</p>
        {ticks(["Kitchens degreased, inside the oven and fridge", "Bathrooms scrubbed, hard-water spots and all", "Baseboards, doors, switches, and vents", "Desert dust off fans, blinds, and sills"])}
      </div>
      <div>
        <h3>Reset</h3>
        <p>Back to day one.</p>
        {ticks(["Move-out and move-in cleans", "Between-tenant turnovers", "Pre-listing cleans so photos shine", "Post-season resets for rentals"])}
      </div>
      <div>
        <h3>Rental-ready</h3>
        <p>For hosts and short-term rentals.</p>
        {ticks(["Beds made and linens swapped", "Supplies restocked", "Photo-ready staging touches"])}
      </div>
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="before-title">
  <div class="wrap split">
    <div class="photo-pair">
      <img src="assets/img/cleaning-empty-room.jpg" width="1400" height="934" alt="Empty, freshly cleaned room with wood floors and big windows" loading="lazy">
      <img src="assets/img/cleaning-caddy.jpg" width="1400" height="934" alt="Cleaner carrying supplies up the stairs" loading="lazy">
    </div>
    <div>
      <h2 id="before-title">Leaving, listing, or starting over?</h2>
      <p>If the reset turns up things that need to go (old furniture, boxes, a garage of leftovers), our hauling crew can take it on the same job.</p>
      <a class="link-arrow" href="hauling.html" style="margin-top:1.5rem">Add hauling{icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="cfaq-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="cfaq-title">Cleaning questions</h2></div>
    {faq([
        ("Why is it called Big Rock Service Solutions?", "It's the Big Rock group's cleaning company. Same family, same email, its own name."),
        ("How is a deep clean priced?", "By the size of the place and what it needs. Send us the details and we'll email a free quote."),
        ("How soon can you come?", "Most cleans are scheduled the same week."),
        ("Do I need to be there?", "Not necessarily. Tell us how to get in when we set up the job."),
    ])}
    <div class="family-wrap"><h2 class="family-title">The rest of the family</h2>{family("cleaning")}</div>
  </div>
</section>'''

page("cleaning.html", "Deep Cleaning & Resets in Tucson | Big Rock Service Solutions",
     "Deep cleans, move-out and pre-listing resets, and rental-ready cleaning across the Tucson metro from Big Rock Service Solutions. Free quotes.",
     "page-cleaning", cleaning, service="cleaning")

# ================= HAULING =================
hauling = f'''{page_hero("hauling", "Big Rock Management", "Point at it. It's gone.",
    "Junk, furniture, yard waste, and remodel debris, hauled away from homes and rentals across the Tucson metro. We load it, haul it, and sweep up.",
    "Get a free quote", ("#included", "What we haul"))}

<section class="section" id="included" aria-labelledby="inc-title">
  <div class="wrap">
    <div class="section__intro">
      <h2 id="inc-title">What we haul</h2>
      <p>Single items, a full trailer, or a whole house.</p>
    </div>
    <div class="included">
      <div>
        <h3>Junk &amp; furniture</h3>
        <p>The stuff that won't fit in the bin.</p>
        {ticks(["Couches, recliners, and mattresses", "Old appliances", "Boxes, shelving, and clutter"])}
      </div>
      <div>
        <h3>Yard &amp; construction</h3>
        <p>After the monsoon or the remodel.</p>
        {ticks(["Brush, branches, and palm fronds", "Remodel and demo leftovers", "Old fencing, pavers, and lumber"])}
      </div>
      <div>
        <h3>Cleanouts</h3>
        <p>When the whole place needs emptying.</p>
        {ticks(["Estate cleanouts", "Move-out and rental cleanouts", "Garages, sheds, and storage"])}
      </div>
    </div>
    <p class="not-offered"><b>Homes and rentals only:</b> we don't take commercial jobs.</p>
  </div>
</section>

<section class="section section--cream" aria-labelledby="curb-title">
  <div class="wrap split">
    <img src="assets/img/hauling-couch.jpg" width="1400" height="934" alt="Old gray couch left out by the curb" loading="lazy">
    <div>
      <h2 id="curb-title">Skip the trip to the dump.</h2>
      <p>No renting a trailer, no borrowing a truck, no second trip. Send a photo of the pile and we'll quote it.</p>
      <p>Emptying a place to sell or rent it? Pair the haul with a deep clean from Big Rock Service Solutions.</p>
      <a class="link-arrow" href="cleaning.html" style="margin-top:1.5rem">Add a deep clean{icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="hfaq-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="hfaq-title">Hauling questions</h2></div>
    {faq([
        ("How is hauling priced?", "By how much there is and what it is. A photo makes it easy: send one and we'll email a free quote."),
        ("Is there anything you can't take?", "Some items, like chemicals and other hazardous waste, need special disposal. Ask us about anything unusual."),
        ("Do you do commercial jobs?", "No. We haul for homeowners, landlords, and rental owners."),
        ("How fast can you come?", "Most hauls are scheduled the same week."),
    ])}
    <div class="family-wrap"><h2 class="family-title">The rest of the family</h2>{family("hauling")}</div>
  </div>
</section>'''

page("hauling.html", "Junk Removal & Debris Hauling in Tucson | Big Rock Management",
     "Junk and furniture removal, yard and construction debris hauling, and estate and move-out cleanouts across the Tucson metro. Free quotes.",
     "page-hauling", hauling, service="hauling")

# ================= REALTY =================
realty = f'''<section class="page-hero">
  <div class="wrap">
    <div>
      <span class="page-hero__brand label">Big Rock Realty Group</span>
      <h1>Buying or selling? That's Big Rock Realty Group.</h1>
      <p class="page-hero__lede">Real estate is the heart of the Big Rock family. Start buying or selling with the team at bigrockaz.com.</p>
      <div class="hero__actions">
        <a class="btn btn--light" href="https://bigrockaz.com" target="_blank" rel="noopener">Visit bigrockaz.com{icon("arrow")}</a>
        <a class="link-arrow" href="#sell-title" style="color:var(--cream)">Getting ready to sell?{icon("arrow")}</a>
      </div>
    </div>
    {patch("realty", link=False)}
  </div>
</section>

<section class="broker-strip" aria-label="Brokerage disclosure">
  <div class="wrap">
    {EHO}
    <p><b>Big Rock Realty Group</b> is a real estate team brokered by <b>{BROKERAGE}</b>. Each Keller Williams office is independently owned and operated. Equal Housing Opportunity.</p>
  </div>
</section>

<section class="section" aria-labelledby="sell-title">
  <div class="wrap split">
    <img src="assets/img/home-hillside.jpg" width="1400" height="934" alt="Home on a saguaro-covered hillside in the Tucson foothills" loading="lazy">
    <div>
      <h2 id="sell-title">Selling? Get it ready first.</h2>
      <p>Before a home hits the market, the rest of the family can clear it out and clean it top to bottom, so it photographs and shows at its best.</p>
      {ticks(["<b>Hauling:</b> empty the garage, the closets, the yard", "<b>Service Solutions:</b> a pre-listing deep clean", "<b>Rental management:</b> keeping it? Rent it out instead"])}
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="fam-title">
  <div class="wrap">
    <div class="section__intro"><h2 id="fam-title">The rest of the family</h2></div>
    {family("realty")}
  </div>
</section>'''

page("realty.html", "Buy or Sell a Home in Tucson | Big Rock Realty Group",
     "Buying or selling in the Tucson metro? Big Rock Realty Group is the real estate company at the heart of the Big Rock family. Visit bigrockaz.com.",
     "page-realty", realty, service="other")

# ================= 404 =================
lost = f'''<section class="section lost">
  <div class="wrap">
    <h1>This patch fell off.</h1>
    <p>The page you're looking for isn't here. Try one of these instead.</p>
    <div style="margin-top:2.5rem">{'<div class="family" style="max-width:56rem;grid-template-columns:repeat(4,minmax(0,1fr))">' + "".join(patch(k) for k in PATCHES) + "</div>"}</div>
    <a class="btn" href="./" style="margin-top:3rem">Back to home{icon("arrow")}</a>
  </div>
</section>'''
page("404.html", "Page not found | Big Rock Management", "That page isn't here.", "page-home", lost, current="")



# ================= LEGAL =================
def legal(file, title, desc, h1, intro, body):
    main = f'''<section class="section legal">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="legal__meta">Effective {EFFECTIVE}</p>
    <p class="legal__intro">{intro}</p>
    {body}
  </div>
</section>'''
    page(file, title, desc, "page-legal", main, current="")

legal("privacy.html", "Privacy Policy | Big Rock Management",
      "How Big Rock Management collects, uses, and protects the information you share with us.",
      "Privacy policy",
      f"{LEGAL_NAME} (&ldquo;Big Rock,&rdquo; &ldquo;we,&rdquo; &ldquo;us&rdquo;) runs bigrockco.com. This policy explains what we collect when you use the site or contact us, and what we do with it. The short version: we use your details only to answer your request, and we never sell them.",
      f'''<h2>What we collect</h2>
    <p>When you send a quote request or email us, we receive what you choose to give us:</p>
    <ul>
      <li>Your name and email address</li>
      <li>Your phone number, if you add it</li>
      <li>The general area of the property and the service you're interested in</li>
      <li>Anything you write in the details box, and any photos you email us</li>
    </ul>
    <p>We don't use cookies, analytics, advertising trackers, or tracking pixels on this site. Our host, GitHub Pages, may keep standard server logs (such as IP addresses) for security and to keep the site running. See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub's privacy statement</a>.</p>

    <h2>How we use it</h2>
    <ul>
      <li>To reply to you, prepare your free quote, and schedule the work</li>
      <li>To provide and follow up on services you ask us for</li>
      <li>To keep normal business records, and to meet legal or tax obligations</li>
    </ul>
    <p>We don't add you to marketing lists, and we don't send marketing texts. We contact you only about the request you sent.</p>

    <h2>Who we share it with</h2>
    <ul>
      <li><b>Our form service.</b> Quote requests are delivered to our inbox by a form-processing provider (Formspree), which handles the data only to deliver it to us.</li>
      <li><b>The Big Rock companies.</b> If your request is for a service run by another Big Rock company, such as cleaning by Big Rock Service Solutions or buying and selling with Big Rock Realty Group, we pass your request to that team so they can help you.</li>
      <li><b>When the law requires it.</b> If we're legally required to, or to protect our rights or someone's safety.</li>
    </ul>
    <p>We do not sell or rent your personal information, and we don't share it for advertising.</p>

    <h2>How long we keep it</h2>
    <p>We keep your messages as long as we need them to handle your request and keep reasonable business records, and then we delete them.</p>

    <h2>Your choices</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> anytime to ask what we have about you, to correct it, or to have it deleted. We'll answer promptly, unless we have to keep something to meet a legal obligation.</p>

    <h2>Security</h2>
    <p>The site runs over HTTPS, and we limit who can see your messages. No method of sending or storing data is perfectly secure, so please don't send sensitive information such as payment details or Social Security numbers through the form.</p>

    <h2>Children</h2>
    <p>This site is meant for adults. We don't knowingly collect information from children under 13.</p>

    <h2>Other websites</h2>
    <p>Links to other sites, including bigrockaz.com, are covered by those sites' own privacy policies.</p>

    <h2>Changes</h2>
    <p>If we update this policy, we'll post the new version here and change the effective date above.</p>

    <h2>Contact</h2>
    <p>{LEGAL_NAME}, Tucson, Arizona. <a href="mailto:{EMAIL}">{EMAIL}</a></p>''')

legal("terms.html", "Terms of Use | Big Rock Management",
      "The terms that apply when you use bigrockco.com.",
      "Terms of use",
      f"These terms apply to your use of bigrockco.com, which is run by {LEGAL_NAME}. By using the site, you agree to them.",
      f'''<h2>About the site</h2>
    <p>This site describes services from the Big Rock group of companies in the Tucson metro area: short-term rental management and hauling by {LEGAL_NAME}, cleaning by Big Rock Service Solutions, and real estate through Big Rock Realty Group, brokered by {BROKERAGE}.</p>

    <h2>Quotes</h2>
    <p>Quotes are free estimates based on the information you give us. A quote isn't a binding offer or contract. Prices and scope are confirmed in writing before any work begins, and they may change if the job differs from what was described.</p>

    <h2>Services</h2>
    <p>Any service you book is governed by the agreement or written confirmation for that job. Real estate services are provided only by licensed agents through {BROKERAGE}, and are subject to that brokerage's agreements and policies.</p>

    <h2>Photos and content</h2>
    <p>Some photos on this site are stock images used for illustration. They don't show our own work, properties, or staff. The site content, logo, and designs belong to {LEGAL_NAME} and may not be copied without permission.</p>

    <h2>No warranties</h2>
    <p>We try to keep this site accurate and available, but it's provided "as is," without warranties of any kind. Information here may change without notice.</p>

    <h2>Limitation of liability</h2>
    <p>To the extent the law allows, {LEGAL_NAME} isn't liable for any indirect or consequential damages arising from your use of this website.</p>

    <h2>Links</h2>
    <p>We link to other websites for convenience. We aren't responsible for their content or practices.</p>

    <h2>Governing law</h2>
    <p>These terms are governed by the laws of the State of Arizona.</p>

    <h2>Contact</h2>
    <p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a></p>''')

legal("accessibility.html", "Accessibility | Big Rock Management",
      "Our commitment to making bigrockco.com usable for everyone.",
      "Accessibility",
      "We want everyone to be able to use this site and reach us, including people who use screen readers, keyboard navigation, magnification, or other assistive technology.",
      f'''<h2>Our standard</h2>
    <p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA.</p>

    <h2>What we've done</h2>
    <ul>
      <li>Text and controls meet AA color-contrast levels</li>
      <li>Every page works with a keyboard, with visible focus outlines and a skip-to-content link</li>
      <li>Images have text descriptions, and decorative artwork is hidden from screen readers</li>
      <li>Form fields have labels, and errors are explained in text, not just color</li>
      <li>Animation is reduced for anyone who turns on "reduce motion"</li>
      <li>Layouts adapt to phones and to zoom up to 200%</li>
    </ul>

    <h2>Need help or found a problem?</h2>
    <p>If anything on this site is hard to use, email <a href="mailto:{EMAIL}">{EMAIL}</a> with the page and the problem. We'll fix it, and we'll help you get the information or the quote you need another way in the meantime.</p>''')

print("built:", ", ".join(p.name for p in sorted(ROOT.glob("*.html"))))
