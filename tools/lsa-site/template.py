import json, html, os, re

SITE = "https://lsacommand.com"
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3FBaderAd23sqqiU6EqWQQkx6fA/"
VIDEOS = {
    "answering": CDN + "hf_20261030_154332_76864363-9746-4519-97cb-7e66e676f35d.mp4",
    "disputes": CDN + "hf_20261030_154332_02531c15-2c68-4010-9c81-c924a0284390.mp4",
    "area": CDN + "hf_20261030_154332_cb3e5992-b0cc-4938-b0b6-12eeccd3351e.mp4",
    "reviews": CDN + "hf_20261030_154333_147bf738-47d1-498c-b15e-2f56850b7e7f.mp4",
    "messages": CDN + "hf_20261030_154332_c594f400-88e4-4ce4-bceb-2af28f855915.mp4",
}
WALKTHROUGH = "https://ryan.diyai.ai/30-min-discovery-call"
DATE = "2026-10-30"

FEATURES = [
    ("/lsa-ai-call-answering/", "AI call answering"),
    ("/lsa-message-leads/", "Message lead response"),
    ("/lsa-lead-disputes/", "Lead disputes & credits"),
    ("/lsa-service-area/", "Service area targeting"),
    ("/lsa-reviews/", "Review generation"),
]
INDUSTRIES = [
    ("/industries/hvac/", "HVAC"),
    ("/industries/plumbers/", "Plumbers"),
    ("/industries/roofers/", "Roofers"),
    ("/industries/electricians/", "Electricians"),
    ("/industries/pool-contractors/", "Pool contractors"),
]


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def strip(t):
    return html.unescape(re.sub(r"<[^>]+>", "", t)).strip()


def page(path, title, h1, description, eyebrow, crumbs, sections, faqs=(), video=None,
         video_name=None, kind="WebPage", related=(), lede=""):
    url = SITE + path
    toc = "".join(f'<li><a href="#{slug(h)}">{html.escape(h)}</a></li>' for h, _ in sections)
    if faqs:
        toc += '<li><a href="#faq">Frequently asked questions</a></li>'
    body = ""
    for h, content in sections:
        body += f'<h2 id="{slug(h)}">{html.escape(h)}</h2>\n{content}\n'
    if faqs:
        body += '<h2 id="faq">Frequently asked questions</h2>\n<div class="faq">'
        for q, a in faqs:
            body += f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>"
        body += "</div>\n"
    body += ('<section class="cta-box"><h2>See it on your own LSA account.</h2>'
             '<p>Call or text <a href="tel:+19897124370">989-712-4370</a>, or book a walkthrough and bring your '
             'current LSA dashboard. We will show you exactly where leads are slipping.</p>'
             f'<a class="button" href="{WALKTHROUGH}">Book a walkthrough</a></section>')
    if related:
        links = "".join(f'<li><a href="{p}">{html.escape(t)}</a></li>' for p, t in related)
        body += f'<aside class="related" aria-label="Related pages"><p class="eyebrow">Keep exploring</p><ul>{links}</ul></aside>'

    video_html = ""
    graph = [
        {"@type": "Organization", "@id": SITE + "/#organization", "name": "LSA Command",
         "url": SITE + "/", "logo": SITE + "/lsa-command-logo.svg"},
    ]
    main = {"@type": kind, "@id": url + "#main", "url": url, "name": strip(h1), "headline": strip(h1),
            "description": description, "inLanguage": "en",
            "publisher": {"@id": SITE + "/#organization"}}
    if kind == "BlogPosting":
        main.update({"datePublished": DATE, "dateModified": DATE, "author": {"@id": SITE + "/#organization"},
                     "mainEntityOfPage": {"@type": "WebPage", "@id": url}})
    graph.append(main)
    if video:
        video_html = (f'<figure class="video"><video src="{video}" controls muted playsinline preload="metadata" '
                      f'poster="/preview-stats.png" aria-label="{html.escape(video_name)}"></video>'
                      f'<figcaption>{html.escape(video_name)}</figcaption></figure>')
        graph.append({"@type": "VideoObject", "name": video_name, "description": description,
                      "thumbnailUrl": SITE + "/preview-stats.png", "uploadDate": DATE,
                      "duration": "PT12S", "contentUrl": video, "embedUrl": url})
    if faqs:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in faqs]})
    items = [("Home", SITE + "/")] + [(n, SITE + p) for n, p in crumbs] + [(strip(h1), url)]
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]})
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)

    crumb_html = '<li><a href="/">Home</a></li>' + "".join(
        f'<li><a href="{p}">{html.escape(n)}</a></li>' for n, p in crumbs) + \
        f'<li aria-current="page">{html.escape(strip(h1))}</li>'
    feature_links = "".join(f'<a href="{p}">{html.escape(t)}</a>' for p, t in FEATURES)
    industry_links = "".join(f'<a href="{p}">{html.escape(t)}</a>' for p, t in INDUSTRIES)
    meta_line = (f'<p class="article-meta">By <a href="/" rel="author">LSA Command</a> <span aria-hidden="true">·</span> '
                 f'<time datetime="{DATE}">{__import__("datetime").date.fromisoformat(DATE).strftime("%B %-d, %Y")}</time></p>') if kind == "BlogPosting" else ""
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    t = html.escape(title)
    d = html.escape(description)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index,follow">
  <meta property="og:type" content="{'article' if kind == 'BlogPosting' else 'website'}">
  <meta property="og:site_name" content="LSA Command">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/preview-stats.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{SITE}/preview-stats.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/blog/blog.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/" aria-label="LSA Command home"><img src="/lsa-command-logo.svg" alt="LSA Command" width="720" height="240"></a>
      <nav aria-label="Main navigation"><a href="/#everything">Features</a><a href="/blog/">Blog</a><a href="/support.html">Support</a><a class="button" href="{WALKTHROUGH}">Book a walkthrough</a></nav>
    </div>
  </header>
  <main id="main" class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{crumb_html}</ol></nav>
    <article>
      <header class="article-header">
        <p class="eyebrow">{html.escape(eyebrow)}</p>
        <h1>{h1}</h1>
        {lede_html}
        {meta_line}
      </header>
      <div class="article-layout">
        <aside class="contents" aria-label="On this page"><p class="contents-label">On this page</p><nav aria-label="Table of contents"><ol>{toc}</ol></nav></aside>
        <div class="article-body">
          {video_html}
          <div class="approved-copy">
{body}
          </div>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer"><div class="container">
    <nav aria-label="Features">{feature_links}</nav>
    <nav aria-label="Industries">{industry_links}</nav>
    <nav aria-label="Footer navigation"><a href="/">Home</a><a href="/blog/">Blog</a><a href="/support.html">Support</a><a href="/privacy-policy.html">Privacy Policy</a><a href="/terms-of-service.html">Terms of Service</a><a href="/cookie-policy.html">Cookie Policy</a><a href="/gdpr.html">GDPR</a><a href="/hipaa-compliance.html">HIPAA Compliance</a></nav>
    <p>© 2026 LSA Command. All rights reserved. Google and Google Local Service Ads are trademarks of Google LLC. We are not affiliated with Google.</p>
  </div></footer>
</body>
</html>
"""


def write(root, path, content):
    out = os.path.join(root, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(content)
    return out
