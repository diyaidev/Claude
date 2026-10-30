"""Weekly LSA blog posts. The weekly routine appends one post() call here per week.
Copy the post() pattern from blog2.py; keep DATE in template.py in mind (set date per post)."""
from blog2 import post as _post, POSTS as _ALL  # noqa: F401
from template import page, FEATURES

POSTS = []


def post(path, h1, title, desc, cat, minutes, card, lede, sections, faqs, related, date):
    import template
    old = template.DATE
    template.DATE = date
    try:
        POSTS.append(dict(path=path, eyebrow=cat, minutes=minutes, h1=h1, card=card, date=date, html=page(
            path, title, h1, desc, cat, [("Blog", "/blog/")], sections, faqs=faqs,
            kind="BlogPosting", related=related, lede=lede)))
    finally:
        template.DATE = old

# --- weekly posts below (newest last) ---
