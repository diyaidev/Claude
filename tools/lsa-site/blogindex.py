import html
from template import WALKTHROUGH

CATS = ["Contractor guides", "LSA updates", "Agency guides"]

def build(posts, featured_path):
    feat = next(p for p in posts if p["path"] == featured_path)
    rest = [p for p in posts if p is not feat]
    def card(p):
        c = html.escape(p["cat"])
        return (f'<article class="post-card" data-cat="{c}"><p class="tag">{c}</p>'
                f'<h3><a href="{p["path"]}">{html.escape(p["h1"])}</a></h3><p>{html.escape(p["card"])}</p>'
                f'<p class="card-meta"><time datetime="{p["date"]}">{p["date_label"]}</time> · {p["minutes"]} min read</p></article>')
    chips = '<button class="chip active" data-filter="all" aria-pressed="true">All guides</button>' + "".join(
        f'<button class="chip" data-filter="{c}" aria-pressed="false">{c}</button>' for c in CATS)
    cards = "\n".join(card(p) for p in rest)
    items = ",".join(f'{{"@type":"ListItem","position":{i+1},"url":"https://lsacommand.com{p["path"]}","name":{html.escape(p["h1"]) and __import__("json").dumps(p["h1"])}}}' for i, p in enumerate(posts))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Local Services Ads Blog: Guides for Contractors & Agencies | LSA Command</title>
  <meta name="description" content="Practical Google Local Services Ads guides: LSA ranking, lead costs, bad leads, the Google Verified badge, the move to Performance Max, and choosing LSA software.">
  <link rel="canonical" href="https://lsacommand.com/blog/">
  <meta name="robots" content="index,follow">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="LSA Command">
  <meta property="og:title" content="The LSA Command Blog: Google Local Services Ads Guides">
  <meta property="og:description" content="Practical Google Local Services Ads guides for contractors and agencies.">
  <meta property="og:url" content="https://lsacommand.com/blog/">
  <meta property="og:image" content="https://lsacommand.com/preview-stats.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/blog/blog.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@graph":[{{"@type":"Organization","@id":"https://lsacommand.com/#organization","name":"LSA Command","url":"https://lsacommand.com/","logo":"https://lsacommand.com/lsa-command-logo.svg"}},{{"@type":"Blog","@id":"https://lsacommand.com/blog/#blog","url":"https://lsacommand.com/blog/","name":"The LSA Command Blog","publisher":{{"@id":"https://lsacommand.com/#organization"}}}},{{"@type":"ItemList","itemListElement":[{items}]}},{{"@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://lsacommand.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://lsacommand.com/blog/"}}]}}]}}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/" aria-label="LSA Command home"><img src="/lsa-command-logo.svg" alt="LSA Command" width="720" height="240"></a>
      <nav aria-label="Main navigation"><a href="/#everything">Features</a><a href="/blog/">Blog</a><a href="/support.html">Support</a><a class="button" href="{WALKTHROUGH}">Book a walkthrough</a></nav>
    </div>
  </header>
  <section class="blog-hero"><div class="container">
    <p class="eyebrow">The LSA Command Blog</p>
    <h1>Win more jobs from <span>Google Local Services Ads.</span></h1>
    <p>Practical, no-fluff guides for contractors and agencies: LSA ranking, lead costs, lead quality, Google’s latest changes, and the software that ties it together.</p>
  </div></section>
  <main id="main" class="container blog-index">
    <article class="featured-post">
      <div><p class="tag">Featured · {html.escape(feat["cat"])}</p>
      <h2><a href="{feat["path"]}">{html.escape(feat["h1"])}</a></h2>
      <p>{html.escape(feat["card"])}</p>
      <p class="card-meta"><time datetime="{feat["date"]}">{feat["date_label"]}</time> · {feat["minutes"]} min read</p>
      <a class="button" href="{feat["path"]}">Read the guide</a></div>
    </article>
    <div class="chips" role="group" aria-label="Filter guides by topic">{chips}</div>
    <section class="post-grid" aria-label="All guides">
{cards}
    </section>
    <section class="walkthrough"><div><h2>See where your LSA leads are slipping.</h2><p>Bring your LSA dashboard. We’ll show you your answer rate, lead quality, and the credits you’re leaving on the table.</p></div><a class="button" href="{WALKTHROUGH}">Book a walkthrough</a></section>
  </main>
  <footer class="site-footer"><div class="container">
    <nav aria-label="Features"><a href="/lsa-ai-call-answering/">AI call answering</a><a href="/lsa-message-leads/">Message lead response</a><a href="/lsa-lead-disputes/">Lead disputes &amp; credits</a><a href="/lsa-service-area/">Service area targeting</a><a href="/lsa-reviews/">Review generation</a></nav>
    <nav aria-label="Industries"><a href="/industries/hvac/">HVAC</a><a href="/industries/plumbers/">Plumbers</a><a href="/industries/roofers/">Roofers</a><a href="/industries/electricians/">Electricians</a><a href="/industries/pool-contractors/">Pool contractors</a></nav>
    <nav aria-label="Footer navigation"><a href="/">Home</a><a href="/blog/">Blog</a><a href="/support.html">Support</a><a href="/privacy-policy.html">Privacy Policy</a><a href="/terms-of-service.html">Terms of Service</a><a href="/cookie-policy.html">Cookie Policy</a><a href="/gdpr.html">GDPR</a><a href="/hipaa-compliance.html">HIPAA Compliance</a></nav>
    <p>© 2026 LSA Command. All rights reserved. Google and Google Local Service Ads are trademarks of Google LLC. We are not affiliated with Google.</p>
  </div></footer>
  <script>
  document.querySelectorAll('.chip').forEach(function (b) {{
    b.addEventListener('click', function () {{
      var f = b.dataset.filter;
      document.querySelectorAll('.chip').forEach(function (c) {{ var on = c === b; c.classList.toggle('active', on); c.setAttribute('aria-pressed', on); }});
      document.querySelectorAll('.post-card').forEach(function (c) {{ c.hidden = f !== 'all' && c.dataset.cat !== f; }});
    }});
  }});
  </script>
</body>
</html>
"""
