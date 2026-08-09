# LSA → Performance Max Migration Playbook (LSA Command)

Built 2026-08-03. Grounded in what actually surfaced this week — not generic advice.

## Why this exists

Google announced July 20, 2026 that Local Services Ads is folding into Google Ads as a
specialized Performance Max campaign type ("PMax for leads"). Phase 1 of the migration
starts **this month (August 2026)** for a specific set of home-service verticals. LSA
Command's entire book is exactly that vertical list. This is the single biggest structural
change to the product LSA Command sells since Google Guaranteed → Google Verified last
October, and it's landing while Ryan is mid-onboarding a new white-label partner (Chris
Monkaitis / Monk Marketing, next call Aug 12). It's worth having the client story straight
before that call, not after clients start asking about it unprompted.

## What's actually changing

- Every existing Local Services Ads campaign converts into a Performance Max campaign
  built for pay-per-lead goals. Manual bidding ends.
- The standalone LSA dashboard goes away after an account migrates. Leads and campaign
  management move into the main Google Ads UI.
- **Historical performance reports do not carry over.** Anything Ryan or LSA Command
  needs for client reporting, case studies, or dispute history has to be exported before
  an account's transition date.
- Campaigns start pulling business name, address, hours, and photos live from Google
  Business Profile instead of separate manual entry in the LSA dashboard — so GBP hygiene
  now double-counts toward ad performance.
- What stays the same: pay-per-valid-lead pricing, Search/Maps-only placement, no
  keywords.

## Rollout timeline

| Phase | Who | When |
|---|---|---|
| 1 | Select US home & storefront service advertisers: plumbing, HVAC, electrical, appliance repair, house cleaning, lawn care, roofing, pest control, moving | August 2026 (now) |
| 2 | Broader advertiser groups, incl. service-area businesses without a storefront, custom bidding/booking accounts | Late 2026 |
| 3 | Non-US accounts, remaining categories | 2027 |

Phase 1's vertical list overlaps heavily with LSA Command's client base — this isn't a
"watch and wait" item.

## Internal checklist (LSA Command)

- [ ] Pull the full client roster and flag every account in a Phase 1 vertical
      (plumbing, HVAC, electrical, appliance repair, house cleaning, lawn care, roofing,
      pest control, moving). Those are candidates for migration this month.
- [ ] For each flagged account, export current LSA historical performance reports now,
      before any transition notice lands — this is the one irreversible loss if missed.
- [ ] Audit GBP profiles for those same clients (hours, photos, address accuracy) since
      PMax campaigns will now sync live from GBP instead of the LSA dashboard.
- [ ] Confirm whether LSA Command's own reporting/dashboard tooling reads from the LSA
      API or the Google Ads API — the standalone LSA dashboard's retirement may affect
      any internal tooling built against it.
- [ ] Decide on a standard client notice: proactive heads-up before Google's own
      migration email lands, or reactive only if a client asks. Proactive is the stronger
      trust play given LSA Command's positioning as the expert layer on top of Google.

## Client talking points (draft — not sent, for Ryan to use/edit)

Use when a client asks "why does my Local Services dashboard look different" or as a
proactive heads-up for Phase 1 vertical clients:

> Google is folding Local Services Ads into the main Google Ads platform this month as a
> new "Performance Max for leads" campaign type. You'll still only pay for valid leads —
> calls, messages, bookings — nothing changes there. What does change: the separate LSA
> dashboard goes away, and it now pulls your business hours/photos directly from your
> Google Business Profile, so keeping that current matters more than ever. We're already
> tracking which of your campaigns are affected and will flag anything that needs your
> input before it happens — you don't need to do anything right now.

## What this is not

This is not a finished client email — Ryan should decide proactive vs. reactive posture
and adjust tone before anything goes out. No client accounts were touched, queried, or
identified individually; the vertical list above is from Google's public rollout
announcement, not from LSA Command's actual roster (Claude doesn't have access to that
roster from Gmail/Calendar alone).

## Sources

- [Local Services Ads come to Google Ads via Performance Max — Search Engine Land](https://searchengineland.com/local-services-ads-come-to-google-ads-via-performance-max-482692)
- [Local Services Ads transition to Performance Max campaigns with pay-per-lead goals — Google Ads Help](https://support.google.com/google-ads/answer/17213585)
- [Google Kills LSA Dashboard, Forces Local Inventory Ads On — TechWyse](https://www.techwyse.com/news/platform-updates/google-local-services-ads-performance-max-migration-local-inventory-ads-default-2026)
- [Google Is Moving Local Services Ads to Performance Max: What Law Firms Need to Know — Justia (Jul 31, 2026)](https://onward.justia.com/google-is-moving-local-services-ads-to-performance-max-what-law-firms-need-to-know/)
- [Google Just Changed Local Services Ads — Cornerstone Advertising (Jul 29, 2026)](https://www.cornerstonead.com/2026/07/29/google-local-services-ads-update/)
