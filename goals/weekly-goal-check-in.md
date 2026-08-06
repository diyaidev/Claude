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

**Current focus (v1.2, updated 2026-07-23):** primary focus is now the **Pay-Per-Call lead
brokering opportunity with Daniel Foster** (sellyourcalls.vercel.app — recruiting and vetting
call sellers, brokering calls to buyers like pool contractors; sub-affiliate agreement and
first-20 seller review in motion). Agent Operations outbound keeps running in the background
via Ryan's automated sequence (see Week 2 evaluation); LSACommand keeps converting on its own
momentum; DIY AI remains the conversational-AI component inside LSACommand.

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
5. Each Thursday, also refresh `pay-per-call/launch-tracker.md` (open-items status + the weekly
   scoreboard row: applications, screened, live sellers, calls, payouts) and
   `agent-operations/outbound-scoreboard.md` (sends / replies / meetings per vertical) from
   Gmail and calendar data before writing the question — questions should cite these numbers.

## Question log

### Week 1 — 2026-07-16

**Q1:** Of your three AI offers — LSACommand.com, DIY AI, and Agent Operations AI — how many
paying customers did each one add in the last 30 days, and which ONE offer would you pick to
push hard if the other two had to wait 90 days?

**A (2026-07-19, answered in session):** LSACommand added a couple of new clients in the last 30 days; Agent
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

**Round 2 (2026-07-19):** Ryan reviewed v1 — copy direction approved, but he prefers the
current live site's more modern look, so **do not ship**. His edits, now applied in v2: case
study anonymized to "a pest control company based out of Ohio"; no 15-minute event type exists,
so buttons read "Book a walkthrough" (pointing at the 30-minute discovery link) while the
15-minute promise stays in the closing headline. v2 also got a design pass (Manrope type,
glass sticky nav, gradient hero with a live "digital employee" conversation mockup, elevated
cards). Still blocked from seeing the current live design: Ryan to either allow
agentoperationsai.com in the environment network settings or paste a screenshot of the current
homepage so the design language can be matched before any production deploy.

### Week 2 — 2026-07-23

**Week in review:** the Agent Operations push went live — at least 8 personalized cold emails
to Atlanta pest control companies on Jul 22 (PestNation, Kuma, Got-Bugs, Peachtree, North
Fulton, Anthem, BREDA, Bizzy Bee) and 5 to DFW restoration companies on Jul 21, plus a
referral-partner recap to Nate (Sky Media). No pest control walkthroughs on the calendar yet.
New this week: a Pay-Per-Call project with Daniel (sellyourcalls.vercel.app) and an
A Building Co AI walkthrough. The homepage rewrite is still parked in preview awaiting Ryan's
design input.

**Q2:** This week you put real outbound behind Agent Operations — 13+ personalized emails in
two days across pest control and restoration — but every one of them lands on a homepage still
selling the old message, and the rewrite is sitting in preview waiting on you. Which do you
pick by Friday: give me the current site's design reference (allow agentoperationsai.com in
the environment network settings, or paste a screenshot here) so the new page ships before
your next batch — or ship the v2 preview as-is and iterate on the live site?

**A (2026-07-23, in session):** Ryan redirected rather than answering directly: he asked for an
evaluation of the Agent Operations outbound to date, clarified that Claude is not the sender
(his own automated sequence is), and declared a focus shift — the Daniel Foster Pay-Per-Call
lead brokering opportunity is now the primary push. Website ship decision remains open; v2
stays parked in preview.

**Outbound evaluation (as of 2026-07-23):** ~50 unique prospects contacted since Jul 7 in a
3-touch sequence (personalized opener → "floating back" bump → breakup note pointing at
agentoperationsai.com), rotating one metro/vertical per day: Charlotte trades (8), Nashville
family/injury law (8), Orlando HVAC (1+), Phoenix roofing (6), DFW restoration (8), Atlanta
pest control (8), Denver garage doors (4+, sent the morning of Jul 23). **Prospect replies: 0.
Meetings booked: 0.** Read: copy is strong and personalization is real, but ~8 sends per
vertical is too small a sample to judge any vertical, and total volume (~3/day) is an order of
magnitude below what cold-email reply rates (1–5%) need to produce meetings. The engine works;
the aim scatters daily and never accumulates evidence in one vertical.

### Week 3 — 2026-07-30

**Week in review:** the Daniel Foster deal moved fast — the affiliate agreement went through
two negotiated redrafts (Ryan's "five things before I sign" Jul 27; "two fixes and I'm
signing" Jul 28 — entity + Section 5 cure window, with the 90/10 item resolved better than
asked and categories opening after one completed pay cycle), and Daniel's final version
landed Jul 29 at 9:34pm — **unsigned as of this check-in**. Seller recruiting started 1:1:
Ippei, Jesse/RankExpand (+follow-up), Jacky/Indexsy, Nick/DigitalLandlords — 0 replies yet;
the Skool post still isn't live; no seller or Dalton meetings on the calendar. Ryan reported
himself green-lit after talking to Aranza (Jul 23) and sent Daniel a supply-lanes memo. The
background Agent Operations sequence added four more one-day verticals (~67 prospects total)
and produced its first-ever reply — an opt-out from Phoenix Roofing — plus one bounce. Also
closed this week: the Avanta partnership wind-down (charges confirmed stopped) and a
make-right note to Josh on the $200/$300 pricing miss.

**Q3:** Daniel's final agreement — with both of your edits in it — has been sitting in your
inbox since last night, while four seller conversations warm up with nothing signed behind
them. What day do you sign, and how many completed seller applications will exist at
sellyourcalls.vercel.app by next Thursday's check-in?

**A:** _(not answered in session — observed from the week's data instead: the agreement was
still unsigned as of 2026-08-06; Daniel nudged "Are we good to go?" on Jul 30 with no visible
reply; completed seller applications visible: 0.)_

### Week 4 — 2026-08-06

**Week in review:** the deal is stalled at the finish line — Daniel's final agreement (both of
Ryan's edits in) has now sat unsigned for 8 days, and his Jul 30 "Are we good to go?" nudge has
gone 7 days without a visible reply. Real motion did happen: a pay-per-call conversation with
Direct Phone Calls on Aug 4 (directphonecalls@gmail.com + anemeshsharma9@gmail.com), and a
"Call Nate" partner touch Aug 5. But the four seller 1:1s got no replies and no new ones went
out; the Skool post is still not live; no Dalton or seller meetings are booked. The background
sequence added four more verticals — Las Vegas–area pools, Chicago appliance repair, Nashville
fencing, Minneapolis chimney (~83 prospects total) — still one reply ever (an opt-out).
Notable: the sequence is now cold-emailing pool companies as Agent Operations prospects while
pool contractors are the candidate buyer network for pay-per-call; the two motions are touching
the same pond from opposite ends.

**Q4:** Daniel asked "Are we good to go?" seven days ago and hasn't heard back — after you
negotiated hard and won both edits. What is actually stopping the signature — name the specific
blocker out loud — and if there isn't one, does the signed copy go back to Daniel today?

**A:** _(pending)_
