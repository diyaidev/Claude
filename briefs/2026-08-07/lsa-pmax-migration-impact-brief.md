# LSA Command — Impact Brief: Local Services Ads Moving Into Performance Max

*Drafted 2026-08-07 by the morning operator brief, for discussion at today's
9am LSACommand.com Mastermind. Research-only — no code changes, no client
outreach. Sourced from public reporting (links at bottom); no access to
Google's internal rollout comms or the `lsa-command` codebase from this
session.*

## What's happening

Google announced on **July 20, 2026** that Local Services Ads are being
folded into Google Ads as a new **Performance Max for pay-per-lead**
campaign type. The **first rollout wave is early August 2026** — i.e. now —
covering home and storefront service categories in the US: plumbing, HVAC,
electrical, appliance repair, house cleaning, lawn care, roofing, pest
control, and moving. Broader advertiser groups (service-area businesses
without a storefront, accounts with custom bidding/booking configs) follow
in "late 2026," with the full migration continuing in phases through 2027.
Google says affected advertisers get advance notice before their specific
campaigns migrate.

## What changes

- The **standalone LSA dashboard goes away** for migrated advertisers —
  campaign management and lead response move into the regular Google Ads
  interface.
- Campaigns become **Performance Max, pay-per-lead** campaigns instead of
  the keywordless LSA product advertisers know today.
- **Real-time sync with Google Business Profile** becomes the source of
  truth for business name, address, hours, and photos — no more separate
  manual entry in the LSA dashboard.
- **Historical performance reports do not migrate** — whatever exists in
  the old LSA dashboard's history stays behind.
- Existing budgets, settings, and creative assets transfer automatically
  for migrated accounts.

## What stays the same

Ads still appear only on Search and Maps. Campaigns are still built off
Google Business Profile data. Advertisers still pay only for valid leads
(calls, messages, bookings) — not clicks.

## Why this matters for LSA Command specifically

LSA Command's current product surfaces — rankings tracking, the client
dashboard, health monitoring, monthly reports, the phone/chat lead-capture
widget — are all built assuming the standalone LSA dashboard and its data
model exist. Three concrete risk areas to name in the Mastermind:

1. **Rankings tracking (P2 backlog, Issues 3–5).** If ranking data is
   currently pulled from the LSA dashboard/API, migrated accounts may
   expose that data differently (or not at all) once they move into
   Google Ads / Performance Max. Worth checking whether the ranking
   source is the LSA-specific surface or the general Google Ads API
   before more UI work (Issues 4–5) is built on top of it.
2. **Health monitoring (P1 backlog, Issues 1–2).** The in-flight "catch
   breakage before clients do" work should explicitly include a check for
   "has this client's account been migrated to Performance Max" — a
   silent platform migration is exactly the kind of breakage Ryan said
   hurts most, and it's about to happen to some client base, on Google's
   timeline, not LSA Command's.
3. **Client-facing history and reporting.** Because historical performance
   doesn't migrate, any client who gets moved this wave will see a gap or
   reset in their reporting unless LSA Command is already snapshotting
   that data independently (which is exactly what Issue 3 does going
   forward — but anything before today isn't backfilled either way).

## Which clients are exposed first

The first wave is scoped to specific verticals: plumbing, HVAC, electrical,
appliance repair, house cleaning, lawn care, roofing, pest control, moving.
Any LSA Command client in those categories is a candidate for early
migration and should be the first place to look for symptoms (dashboard
data source changing, a client asking "why does my LSA login look
different").

## Suggested next steps (for Ryan / the Mastermind, not autonomously built)

- Confirm with the team whether LSA Command pulls its data from the LSA
  dashboard/API surface or the general Google Ads API — that answer
  determines whether this is a non-event or a rebuild.
  - Sky Media Ventures / Champion Pools is a house-service-adjacent
    account already in the partnership pipeline (agreement signed
    2026-08-06) — a plausible early candidate to watch once client
    accounts start migrating.
- If exposed: decide whether the migration should become a
  `loop:needs-human` issue (it likely touches how leads/spend surface,
  which is explicitly off-limits for autonomous builds) filed via
  `/lsa-spec` once the technical exposure is confirmed.
- Consider proactive client messaging for accounts in the first-wave
  verticals, so they hear about the dashboard change from LSA Command
  before they hear it from Google.

## Sources

- [Local Services Ads come to Google Ads via Performance Max — Search Engine Land](https://searchengineland.com/local-services-ads-come-to-google-ads-via-performance-max-482692)
- [Google Local Services Ads Meet PMax: What You Need to Know — WordStream](https://www.wordstream.com/blog/google-ads-lsa-pmax-update)
- [Google Is Bringing Local Services Ads Into Google Ads — Search Engine Journal](https://www.searchenginejournal.com/google-is-bringing-local-services-ads-into-google-ads/582816/)
- [Local Services Ads transition to Performance Max campaigns with pay-per-lead goals — Google Ads Help](https://support.google.com/google-ads/answer/17213585)
- [Google Kills LSA Dashboard, Forces Local Inventory Ads On — TechWyse](https://www.techwyse.com/news/platform-updates/google-local-services-ads-performance-max-migration-local-inventory-ads-default-2026)
