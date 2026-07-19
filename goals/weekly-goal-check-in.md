# Weekly Goal Check-in — Ryan Steinolfson

A living log for the weekly "Krone" (cron) coaching question. A scheduled Routine wakes the
Claude session every Thursday morning (~9am ET), reviews this file plus Ryan's recent activity,
asks ONE question that moves him toward the goal below, and logs it here.

## The goal (v1.1 — inferred 2026-07-16, focus set by Ryan 2026-07-19)

**Turn the AI-for-local-services business — DIY AI (diyai.ai), LSACommand.com, and Agent
Operations AI (agentoperationsai.com) — into a predictable, paying-customer revenue engine
that can stand on its own next to (and eventually beyond) the Accelerate Marketing agency.**

More concretely: convert the large audience-building effort Ryan already runs every week into
paying customers of a focused offer.

**Current focus (Ryan's call, from the Q1 answer):** push Agent Operations AI hard for the
next 90 days. LSACommand.com keeps running — it's converting (a couple of new clients in the
last 30 days) — and DIY AI is treated as the conversational-AI component inside LSACommand
rather than a separate offer.

### Evidence (from calendar, email, and business tools — July 2026)

- 30 of 68 calendar events between Jun 15 and Jul 31 are the LSACommand.com Mastermind
  (Mon/Wed/Fri 9–10am ET); another 14 are the weekly DIYAI Live Video Workshop (Tue 2pm) and
  Accelerate Marketing Live Workshop (Wed 2pm). Roughly two-thirds of scheduled time is
  top-of-funnel audience building.
- Cold outbound from ryan@diyai.ai to plumbing / HVAC / electrical / roofing owners pitching AI
  agents that "answer every call and web lead first-ring, book the job, and log it — priced like
  labor, not software" (Winn's Plumbing, City Air Experts, Patterson, Bradham Brothers, Acosta,
  Ewing Electric), backed by an email warm-up network across agentoperationsai.com /
  accelerateyourmarketing.com / diyai.ai.
- Pipeline activity: DIY AI discovery calls, LSACommand strategy sessions (64 Leads, Torres
  Roofing — demo no-show), Heavy Lifting Marketing onboarding plus three follow-up meetings,
  Gold Coast Podcast appearance.
- Infrastructure: new `diyai-crm` Supabase project (Jun 30), QuickBooks upgrade sessions with a
  bookkeeper (Jul 10 and 15), business loan agreement (Jul 6) — financial and ops rails for growth.

*If this reads wrong, Ryan corrects it in the check-in session and this section gets revised
(v2, v3, …) rather than replaced.*

## Ground rules for the weekly question

1. ONE question per week, asked Thursday morning. Short setup (two sentences max), then the question.
2. Never repeat a previous question; build on earlier answers and on what actually happened that
   week (email / calendar / CRM signals when available).
3. Favor questions that force a decision, a number, or a commitment — not reflection for its own sake.
4. Log every question here; log Ryan's answer when he gives one. Commit and push after each update.

## Question log

### Week 1 — 2026-07-16

**Q1:** Of your three AI offers — LSACommand.com, DIY AI, and Agent Operations AI — how many
paying customers did each one add in the last 30 days, and which ONE offer would you pick to
push hard if the other two had to wait 90 days?

**A (2026-07-19):** LSACommand added a couple of new clients in the last 30 days; Agent
Operations AI added zero. DIY AI is conversational AI and effectively already a component of
LSACommand, so it isn't a separate push. Ryan's pick: **Agent Operations AI**. Follow-up he
requested: a review of agentoperationsai.com for setup/conversion problems (delivered in
session 2026-07-19).

**Review outcome (2026-07-19):** infrastructure is healthy (domain + www attached to the
Vercel `agentic-ops` project, production deploy READY as of Jul 14), but the homepage leads
with "Agentic Ops | Autonomous Business Intelligence" — a message mismatch against the cold
emails that send trades owners there expecting "answer every call and web lead first-ring,
book the job, priced like labor, not software." Recommended: rewrite the homepage around the
missed-call promise for trades, unify the brand name (emails say Agent Operations AI, site
says Agentic Ops), and add an instant proof mechanism (live demo line / test-call widget).
Full page-by-page teardown pending Ryan allowing agentoperationsai.com in this environment's
network policy (direct fetch is currently egress-blocked).

**Follow-through (2026-07-19):** Ryan green-lit the rewrite with sharper positioning: one name —
**Agent Operations** (no "AI", no abbreviations); the product is a **digital employee** that runs
the whole loop (intake → customer creation → estimate → booking → agreement → follow-up →
review), not just call answering; lead with the pest control solution already implemented at
The Mole Hunter on **FieldRoutes** (platform confirmed via the Apr 7 meeting transcript with
Branden); name the trades (pest control first, then plumbing, HVAC, electrical, roofing); CTA
matched to the cold-email 15-minute ask; meta title/description carry the promise. New homepage
built at `agent-operations/homepage/index.html`, deployed to Vercel as a **preview** on the
agentic-ops project — production swap awaiting Ryan's approval.
