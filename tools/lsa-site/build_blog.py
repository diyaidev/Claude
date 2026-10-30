import os, sys
from template import write
import blog, blog2, weekly, blogindex
root = sys.argv[1]
force = "--force" in sys.argv
# Only create posts that don't exist yet, so hand edits on the live site are never overwritten.
for p in blog.POSTS + blog2.POSTS + weekly.POSTS:
    if force or not os.path.exists(os.path.join(root, p["path"].strip("/"), "index.html")):
        print(write(root, p["path"], p["html"]))
cat = {"/blog/google-local-services-ads-performance-max/": "LSA updates", "/blog/how-to-rank-higher-google-local-services-ads/": "Contractor guides"}
posts = []
for p in weekly.POSTS[::-1] + blog.POSTS + blog2.POSTS:
    posts.append(dict(path=p["path"], h1=p["h1"], card=p["card"], minutes=p["minutes"], cat=cat.get(p["path"], p["eyebrow"]), date=p.get("date", "2026-10-30"), date_label=__import__("datetime").date.fromisoformat(p.get("date", "2026-10-30")).strftime("%B %-d, %Y")))
posts += [
 dict(path="/blog/lsa-reporting-software-agencies/", h1="How to Choose LSA Reporting Software for Agencies", cat="Agency guides", minutes=5, date="2026-10-26", date_label="October 26, 2026",
      card="An agency report should explain what happened after the lead arrived. Use this checklist to evaluate the numbers, outcomes, and feedback behind the dashboard."),
 dict(path="/blog/multi-account-lsa-software-agencies/", h1="How to Choose LSA Software for Multiple Client Accounts", cat="Agency guides", minutes=5, date="2026-10-26", date_label="October 26, 2026",
      card="A successful single-account demo does not prove a tool fits your agency portfolio. Test client separation, account mapping, and rollout controls before expanding."),
]
open(f"{root}/blog/index.html", "w").write(blogindex.build(posts, "/blog/google-local-services-ads-performance-max/"))
# sitemap additions
sm = open(f"{root}/sitemap.xml").read()
add = "".join(f'  <url><loc>https://lsacommand.com{p["path"]}</loc><lastmod>{p.get("date", "2026-10-30")}</lastmod></url>\n' for p in blog2.POSTS + weekly.POSTS if p["path"] not in sm)
sm = sm.replace('  <url><loc>https://lsacommand.com/blog/lsa-reporting-software-agencies/', add + '  <url><loc>https://lsacommand.com/blog/lsa-reporting-software-agencies/', 1)
open(f"{root}/sitemap.xml", "w").write(sm)
