# Claude Workspace — Standing Instructions

## Email & communications preferences (Ryan)

- **Always CC Alex Contes (alex@diyai.ai)** on all client/partner email communications sent on Ryan's behalf — meeting recaps, follow-ups, onboarding emails, and similar outbound messages.
- Ryan sends email as **ryan@diyai.ai**. Draft in Ryan's voice: casual-professional ("Hey <name>," openers, short sections, plain language).
- Before sending any follow-up/recap, check `in:sent` to avoid duplicate sends.

## Key contacts

- **Alex Contes** — alex@diyai.ai (DIYAI team; CC on all client communications)
- **Chris Monkaitis ("Chris M")** — chris@monk-marketing.com (Monk Marketing; white-label partner being onboarded; recurring calls Wednesdays 11 AM ET)

## LSA Command Loop

- Autonomous spec → build → review loop for the LSA command software (`diyaidev/lsa-command`), modeled on Finn's "Fin Loop". Full playbook: `docs/lsa-command-loop.md`. Skills: `lsa-spec` (morning interview → GitHub issues), `lsa-build` (builds next backlog issue on a `loop/` branch), `lsa-review` (independently tests, stages a **draft PR**, posts to `#lsa-merge-ready` in Slack).
- **Hard rules:** the live platform (default branch) never changes without Ryan's 🚀 reaction in Slack; anything touching ad spend, budgets, or billing is never built autonomously (`loop:needs-human`).
- Morning kickoff: Ryan runs `/lsa-spec` with his ideas, then starts `/loop 30m run the lsa-build skill, then the lsa-review skill`. Evening: Ryan reacts 🚀 (merge) or 👎 (send back) in `#lsa-merge-ready`. "Process the LSA approvals" = run `lsa-review` Pass 1 immediately.
- **All loop questions to Ryan go via Telegram** (his main comms channel): Composio → `TELEGRAM_SEND_MESSAGE` / poll `TELEGRAM_GET_UPDATES`, connection `telegram_remble-hooper`; chat_id + mechanics in `docs/lsa-command-loop.md`. Fall back to in-session questions only if Telegram is unreachable.

## Scheduled jobs

- **Monthly card & subscription watch** — 1st of each month (~8 AM PT): reviews prior-month spend across Chase credit card, Apple Card, Amex, and Wells Fargo debit; flags new/changed subscriptions and odd charges; notifies Ryan via push + email. Playbook and current status: `docs/monthly-card-watch.md`. If Ryan says "run the card watch now", follow that playbook immediately.

## Tooling notes

- Meeting content sources, in order of reliability from this environment: Gmail "Notes: …" emails from gemini-notes@google.com (Google Meet/Gemini recaps land in ryan@diyai.ai's inbox shortly after each meeting), then Granola/Google Drive (both may require connector re-approval).
- Sending email: the Gmail connector is draft/read-only; actual sends go through the Zapier Gmail "Send Email" action.
- Reading email: Composio holds active Gmail connections for all four mailboxes — ryansteinolfson@gmail.com (`gmail_spire-rosier`), ryan@accelerateyourmarketing.com (`gmail_smur-howard`; most bank/card email lands here), ryan@diyai.ai (`gmail_equity-pig`), max@diyai.ai (`gmail_rail-mider`, default). Use `COMPOSIO_MULTI_EXECUTE_TOOL` → `GMAIL_FETCH_EMAILS` with the account alias. Ryan's business domain is accelerateyourmarketing.com (not acceleratemarketing.com).
- Intuit QuickBooks connector reaches company "Accelerate Marketing" (business books). Data posts on a bookkeeping cadence (Sandy): as of 2026-07-22, complete through June; current month typically empty until reconciled — a recent month showing $0 usually means "not posted yet", not "no data" (an earlier empty-file reading in this workspace was itself transient, so re-query before concluding anything is broken). Accounts in the file: Wells Fargo Operating (the WF debit), Amex …23000, PayPal. Chase credit card and Apple Card are personal cards NOT in QuickBooks — their coverage comes from issuer emails.
