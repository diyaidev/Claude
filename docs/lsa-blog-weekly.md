# LSA Command — Weekly Blog Post Playbook

A scheduled routine runs this once a week. It drafts **one** new post for lsacommand.com/blog and opens it as a **draft PR**. Nothing goes live until Ryan merges it.

## Repos
- Website: `diyaidev/LSACommand.com` (static HTML on Vercel; merge to `main` = live)
- Generator + this playbook: `diyaidev/claude` → `tools/lsa-site/`

## Steps
1. Attach and clone both repos (`add_repo` with push access for the website).
2. **Pick the topic:** take the first topic in the backlog below whose slug does not already exist under `blog/` on the website's `main` branch or any open PR branch.
3. **Pick the base:** if PR #3 (`seo/keyword-pages`) is still unmerged, branch from it; otherwise branch from `main`. Name the branch `blog/<slug>`.
4. **Research (required):** run 2–3 web searches for current facts. Prefer Google's own help pages and Search Engine Land / Search Engine Journal / PPC Land. Never invent statistics. Phrase third-party numbers as "industry reports say" and link them. Product claims must match the current homepage (`index.html`).
5. **Write:** append one `post(...)` call to `tools/lsa-site/weekly.py`, following the pattern in `blog2.py`:
   - 3–5 sections, 2–3 FAQs, today's date, category "Contractor guides" / "LSA updates" / "Agency guides"
   - Link to at least 2 relevant feature pages and 1 existing post
   - Plain language in Ryan's voice: short sections, no hype
6. **Build:** `python3 tools/lsa-site/build_blog.py <website-clone>`. Do not pass `--force`. Without it, only new posts are written; the index and sitemap are refreshed. Confirm `git diff --stat` touches only the new post, `blog/index.html` and `sitemap.xml`. Validate the JSON-LD parses, and screenshot the post at 390px and 1280px with Playwright (no horizontal scroll).
7. **Ship:** commit `weekly.py` to `diyaidev/claude` (draft PR). Open a draft PR on the website with the post title and a "Sources" list. Then message Ryan on Telegram (see `docs/lsa-command-loop.md`, alias `ryan-loop`) with the PR link and a one-line summary.

## Hard rules
- Never push to `main` and never merge. Draft PRs only.
- One post per run. If research can't verify the core facts for a topic, skip it, take the next one, and mention the skip in the PR.
- Nothing about ad spend changes or billing advice beyond what Google publishes.

## Topic backlog (in order)
| Slug | Working title | Category |
|---|---|---|
| lsa-job-types-settings | How to Choose Your Google LSA Job Types (and Stop Paying for Jobs You Don't Want) | Contractor guides |
| lsa-budget-weekly | How to Set Your Google Local Services Ads Budget | Contractor guides |
| lsa-photos | Do Photos Help Your Google LSA Ranking? | Contractor guides |
| lsa-24-hour-hours | Should You List Your Business as Open 24 Hours on LSA? | Contractor guides |
| lsa-lead-feedback | Google LSA Lead Feedback: How Rating Leads Trains Google | LSA updates |
| lsa-booked-jobs-tracking | How to Track Cost per Booked Job from Google LSA | Contractor guides |
| lsa-missed-call-charges | Are You Being Charged for Missed LSA Calls? | LSA updates |
| lsa-not-showing | Why Isn't My Google Local Services Ad Showing? | Contractor guides |
| lsa-for-agencies-white-label | White-Label LSA Software for Marketing Agencies | Agency guides |
| lsa-review-responses | How to Respond to Google LSA Reviews (Templates) | Contractor guides |
| lsa-suspension | Google LSA Account Suspended? Common Causes and Fixes | Contractor guides |
| lsa-vs-angi-thumbtack | Google LSA vs. Angi vs. Thumbtack for Contractors | Contractor guides |

Add new topics to the bottom. Ryan can reorder the list at any time.
