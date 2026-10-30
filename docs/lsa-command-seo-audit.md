# lsacommand.com — SEO Keyword Review (2026-10-30)

Source: live production HTML (Vercel project `lsa-command`), robots.txt, sitemap.xml.

## What's working
- Title `LSA Command | Speed-to-Lead for Google Local Services Ads` (55 chars, good)
- Meta description, canonical, OG/Twitter tags, OG image all present
- One H1, 4,600 words of copy, all 13 images have alt text
- robots.txt allows all; sitemap exists; blog has started (2 posts, agency-focused)
- YouTube embed is lazy-loaded with a keyword-rich title

## The core problem
The site is written in **brand language**, while buyers search with **problem language**.
Times each phrase appears in the homepage copy:

| Phrase buyers search | On page |
|---|---|
| "Google Local Services Ads" / "local services ads" | 1 |
| "LSA leads" | 0 |
| "LSA management" / "Local Services Ads management" | 0 |
| "Google Guaranteed" / "Google Screened" | 0 |
| "dispute LSA leads" / "lead credit" | 3 (dispute) |
| "answering service" / "AI receptionist" / "missed calls" | 0 / 0 / 2 |
| "LSA ranking" / "responsiveness" | 10 / ~0 |
| Trades: plumber, HVAC, roofer, electrician | 0 — only "pool" (8) |
| "Performance Max" / "PMax" (Google is moving LSA into PMax) | 0 |

The headings ("The 30-Second Strike", "The Command ROI", "Mastering The 4 R's") contain no search terms.
Google weights H2s heavily.

## Priority keyword targets
**Tier 1 (high intent, aim the homepage and core pages here)**
- google local services ads software / LSA software
- LSA lead management / google LSA leads
- dispute google LSA leads / LSA lead refund / LSA lead credits
- how to rank higher in google local services ads / LSA ranking factors
- LSA responsiveness / LSA answer rate / missed calls local services ads
- AI answering service for google local services ads

**Tier 2 (trade-specific landing pages; these are low competition)**
- google local services ads for {plumbers, HVAC, roofers, electricians, pool contractors, garage door, pest control}

**Tier 3 (timely; few people own these yet)**
- local services ads performance max / LSA PMax transition
- LSA reviews / how to get more google LSA reviews
- LSA service area settings / zip code targeting

## Fixes, in priority order
1. **Rewrite H2s to keyword + benefit.** For example:
   - "The Call Flow Engine" → "AI Answering for Google LSA Calls: 100% Answered"
   - "The Automated Refund Engine" → "Automatic LSA Lead Disputes & Refunds"
   - "Command Your Service Area" → "LSA Service Area Targeting by City & Zip"
   - "The 30-Second Strike…" → "Protect Your LSA Responsiveness & 'Replies in Minutes' Badge"
   - "Review Gathering Taken To A Whole New Level" → "Get More Google LSA Reviews Automatically"
2. **H1:** "Capture Every Google LSA Lead…" → "Google Local Services Ads Software That Answers Every Lead". Keep the current line as the subhead.
3. **Build separate URLs.** Today it's one page, and the sitemap has no feature pages. Add `/lsa-lead-disputes`, `/lsa-ai-answering`, `/lsa-service-area`, `/lsa-reviews`, `/lsa-ranking`, and one page per trade. Each page gets one of the videos below.
4. **Schema:** add `SoftwareApplication` (with offers), `FAQPage` (add an FAQ block), and `VideoObject` for each embedded video. Right now only Organization/WebSite exist.
5. **Add an FAQ section** using real queries: "How do I dispute an LSA lead?", "Does missing calls hurt LSA ranking?", "What happens to LSA with Performance Max?", "How do LSA reviews work?"
6. **Blog:** current posts target agencies. Add contractor-intent posts: LSA → PMax transition, LSA ranking factors, LSA lead credits under Google's automated system.
7. **Trade coverage:** testimonials are all pool contractors. Add at least HVAC/plumbing/roofing proof or copy.
8. Minor: legal links are relative (`privacy-policy.html`); `/affiliate/signup` is in the sitemap and doesn't need to be indexed.

## Video ↔ keyword map (new clips, 16:9, 12s, Higgsfield)
| Clip | Site section | Target page / YouTube title |
|---|---|---|
| 1 Call Flow | Call Flow Engine | "AI Answering Service for Google Local Services Ads" |
| 2 Refunds | Automated Refund Engine | "How to Dispute Google LSA Leads (Automatically)" |
| 3 Service Area | Command Your Service Area | "Google LSA Service Area Targeting by Zip Code" |
| 4 Reviews | Review Gathering | "How to Get More Google LSA Reviews" |
| 5 Messages | LSA API Fallback | "Never Miss a Google LSA Message Lead" |

Self-host these as `<video autoplay muted loop playsinline>` with a poster image, plus `VideoObject` schema. Also upload each one to YouTube under the title above, so it can rank in video results.
