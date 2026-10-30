import sys, re
from template import write
import features, industries, blog
root = sys.argv[1]
for path, html in features.PAGES + industries.PAGES:
    print(write(root, path, html))
for p in blog.POSTS:
    print(write(root, p["path"], p["html"]))

# blog index cards (newest first)
idx = open(f"{root}/blog/index.html").read()
cards = ""
for p in blog.POSTS:
    cards += (f'<article class="guide-card"><p class="eyebrow">{p["eyebrow"]}</p><h2><a href="{p["path"]}">{p["h1"]}</a></h2>'
              f'<p>{p["card"]}</p><p class="card-meta"><time datetime="2026-10-30">October 30, 2026</time> · {p["minutes"]} min read</p>'
              f'<a class="read-link" href="{p["path"]}">Read the guide <span aria-hidden="true">→</span><span class="sr-only">: {p["h1"]}</span></a></article>\n')
if blog.POSTS[0]["path"] not in idx:
    idx = idx.replace('<section class="guide-grid" aria-label="Agency guides">', '<section class="guide-grid" aria-label="LSA guides">' + cards, 1)
    idx = idx.replace("Better questions.<br>Better agency decisions.", "Google Local Services Ads guides.")
    idx = idx.replace("Practical guides for agencies evaluating Google Local Services Ads software, reporting, and multi-client workflows.",
                      "Practical guides for contractors and agencies on Google Local Services Ads: ranking, lead quality, the move to Performance Max, and choosing LSA software.")
    open(f"{root}/blog/index.html", "w").write(idx)

# sitemap
urls = ["/", "/lsa-ai-call-answering/", "/lsa-message-leads/", "/lsa-lead-disputes/", "/lsa-service-area/", "/lsa-reviews/",
        "/industries/hvac/", "/industries/plumbers/", "/industries/roofers/", "/industries/electricians/", "/industries/pool-contractors/",
        "/blog/", "/blog/google-local-services-ads-performance-max/", "/blog/how-to-rank-higher-google-local-services-ads/",
        "/blog/lsa-reporting-software-agencies/", "/blog/multi-account-lsa-software-agencies/",
        "/support.html", "/privacy-policy.html", "/terms-of-service.html", "/cookie-policy.html", "/gdpr.html", "/hipaa-compliance.html"]
old = {"/blog/lsa-reporting-software-agencies/", "/blog/multi-account-lsa-software-agencies/"}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    lm = "2026-10-26" if u in old else ("2026-10-30" if not u.endswith(".html") else None)
    sm += f'  <url><loc>https://lsacommand.com{u}</loc>' + (f'<lastmod>{lm}</lastmod>' if lm else '') + '</url>\n'
open(f"{root}/sitemap.xml", "w").write(sm + "</urlset>\n")
