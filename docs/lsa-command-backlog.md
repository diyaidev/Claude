# LSA Command — Loop Backlog (spec of record, 2026-08-05)

Spec'd with Ryan via the kickoff interview. **File these verbatim as GitHub
issues on `diyaidev/lsa-command` the moment the repo is attached** (label +
title as shown, body from each section). Until then this file is the backlog's
source of truth. After filing, the first `lsa-spec` session should also audit
the existing rankings feature in code and add polish issues for rough edges it
finds (Ryan: "smooth it out").

Ryan's verbatim priorities: **things breaking silently is what hurts most** —
clients find outages (phone calls not answered, features failing) before the
team does. Rankings-over-time is second. None of this touches budgets,
billing, or spend.

---

## Issue 1 — `[P1] Automated end-to-end health checks for critical client-facing flows`
Labels: `loop:backlog`

## Background
Things break and nobody knows when it happened; clients discover outages first
(e.g., inbound phone calls not being answered, features silently failing).
Ryan wants AI continually testing the software so the team finds breakage
before clients do. (Kickoff interview, 2026-08-05.)

## Scope
Enumerate the critical client-facing journeys from the codebase — at minimum:
inbound lead call handling/answering, dashboard loading with real data,
rankings results rendering, monthly report generation — and build an automated
end-to-end smoke suite (Playwright or the repo's existing framework) that
exercises each one against staging config, plus read-only checks against
production where safe. One command runs everything headless.

## Non-goals
Load/perf testing; alert delivery (Issue 2); any billing/spend/budget code paths.

## Acceptance criteria
- [ ] Single command runs the full suite headless.
- [ ] Every enumerated critical journey has at least one check.
- [ ] Each check reports pass/fail with a log/screenshot artifact.
- [ ] A deliberately broken flow in staging is caught by exactly the matching check.

## Test plan (staging)
Run the suite on the branch — all green. Introduce a controlled failure in
staging (e.g., stub the call-handling endpoint to error), re-run, verify that
journey fails with a useful artifact while others stay green. Revert the stub.

## Guardrails
Standard loop guardrails. Checks must be non-destructive; production checks
read-only.

---

## Issue 2 — `[P1] Run the health checks on a schedule and alert Ryan on failure`
Labels: `loop:backlog`

## Background
Detection can't depend on someone remembering to run tests. Ryan: "have the AI
continually test the software."

## Scope
Schedule Issue 1's suite via the repo's native infra (GitHub Actions schedule,
cron, or platform scheduler — whichever the codebase already uses). On failure,
alert Ryan on Telegram (his main comms channel — `ryan-loop` Composio
connection; chat_id in `docs/lsa-command-loop.md`) with journey name, error
summary, timestamp, and artifact link. Send a recovery notice when a failing
check goes green. Include a short daily morning summary.

**Assumptions for reviewer to surface in the merge-ready post:** 30-minute
cadence; failure + recovery alerts only, plus one morning summary. Ryan can
adjust with a reply.

## Non-goals
Paging/on-call tooling; client-visible status pages; new alert channels beyond
Telegram.

## Acceptance criteria
- [ ] Scheduled runs appear in run history at the configured cadence.
- [ ] A simulated failure produces a Telegram alert within one cycle.
- [ ] Recovery notice arrives on the next green run.
- [ ] Morning summary sends once daily.

## Test plan (staging)
Trigger the schedule (or shorten cadence temporarily in staging), simulate a
failure per Issue 1's test plan, observe alert → fix → recovery notice.

---

## Issue 3 — `[P2] Persist LSA ranking snapshots over time per business`
Labels: `loop:backlog`

## Background
The rankings feature identifies how a business currently ranks in Local
Services Ads, but keeps no history. Ryan wants ranking tracked over time;
it surfaces in results, the dashboard, and the monthly report.

## Scope
On each ranking check, persist a timestamped snapshot keyed by business (and
whatever market/keyword dimensions the feature already models). Add a
retrieval path returning a time series filtered by business + date range.
History starts at deploy; no backfill.

## Non-goals
Changing how rank is computed; new data sources; UI (Issues 4–5).

## Acceptance criteria
- [ ] Repeated ranking checks produce distinct timestamped rows.
- [ ] Series retrieval returns correct, ordered data per business/date range.
- [ ] Existing current-rank display unaffected.

## Test plan (staging)
Run ranking checks at least twice for a seeded business; query the series;
verify rows, ordering, and that the current-rank UI still works.

---

## Issue 4 — `[P2] Show ranking-over-time trend in results and dashboard`
Labels: `loop:backlog`

## Background
Trends belong wherever current rank shows today: the results view and the
dashboard.

## Scope
Trend visualization (line chart) of rank history per business in both spots,
using Issue 3's series. Rank 1 renders as best (top). Sensible empty state
until enough history exists.

## Non-goals
Monthly report (Issue 5); changing rank computation.

## Acceptance criteria
- [ ] Chart renders with seeded history in results view and dashboard.
- [ ] Orientation correct (rank 1 best); axis labeled with dates.
- [ ] Empty state shows before ≥2 snapshots exist.

## Test plan (staging)
Seed multi-day history for a test business, open both views in the browser,
verify chart + empty state on a fresh business.

---

## Issue 5 — `[P2] Add ranking trend section to the monthly report`
Labels: `loop:backlog`

## Background
The monthly report is the third surface where rankings appear.

## Scope
New report section: rank at start of month, end of month, net change, and a
compact trend chart/table consistent with the dashboard's data.

## Non-goals
Redesigning the rest of the report.

## Acceptance criteria
- [ ] Generated report for a seeded business shows the section with correct values.
- [ ] Businesses with no history get a clean "tracking started <date>" note.
- [ ] Report generation succeeds end-to-end (also covered by Issue 1's suite).

## Test plan (staging)
Generate the monthly report for seeded and fresh businesses; verify section
contents and overall generation.
