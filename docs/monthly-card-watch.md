# Monthly Card & Subscription Watch

A recurring monthly review of Ryan's spending across **Chase credit card, Apple Card, American Express, and Wells Fargo debit**, designed to catch **new or unusual subscriptions** (the #1 goal — no more paying for a mystery subscription for months) plus possible fraud: unfamiliar merchants, duplicate charges, out-of-pattern amounts, strings of small "test" charges.

- **Schedule:** 1st of each month, ~8:07 AM Pacific (cron `7 15 1 * *` UTC)
- **Delivery:** run summary to Ryan via push notification + email (the Routine's built-in completion notification — no external sends)
- **Run mode:** fresh Claude session per run, in this workspace environment
- **On-demand:** in any Claude session, say *"run the monthly card watch now"* — follow the playbook below

## Coverage map (verified 2026-07-22)

| Account | QuickBooks (business books) | Email | Notes |
|---|---|---|---|
| Wells Fargo debit ("Wells Fargo Operating") | ✅ posted on bookkeeping cadence | ✅ Real-time alerts (Zelle, transactions) → ryansteinolfson@gmail.com — **currently auto-trashed**; Gmail purges Trash after ~30 days | QB authoritative once posted; fix the trash filter to keep full-month email coverage |
| Amex …23000 | ✅ ("American Express 23000") | ✅ rich — lands in ryan@accelerateyourmarketing.com | Best-covered account |
| Chase Business Card …1811 | ❌ not in the books today | ✅ Paperless statements/notices → ryan@accelerateyourmarketing.com (enabled 2026-07-23) | Optional: per-transaction Account Alerts to email for merchant-level detail |
| Chase personal card …3413 | ❌ personal card | ✅ Statement emails confirmed arriving in ryansteinolfson@gmail.com (verified: Jul 14 statement, balance $3,422.55); paperless re-confirmed 2026-07-23 | Optional: per-transaction Account Alerts to email for merchant-level detail |
| Apple Card | ❌ personal card | ❌ No email path — Apple ID is goryan@me.com (iCloud), not a connected inbox | Automated option: forward iCloud Mail → gmail. Manual path (proven 2026-07-23): export transactions CSV from Wallet and upload to a session. Autopay pulls from WF account …5623 |
| PayPal | ✅ ("Paypal Bank") | Receipt emails | Secondary |

## Data sources

| Source | Status | Role |
|---|---|---|
| Composio Gmail — ryan@accelerateyourmarketing.com (`gmail_smur-howard`) | **Verified working** — ~200 bank-domain emails per 45 days | **Primary**; most card email lands here |
| Composio Gmail — ryansteinolfson@gmail.com (`gmail_spire-rosier`) | Verified working (light bank traffic today) | Primary for personal-card alerts once issuer emails are enabled |
| Composio Gmail — ryan@diyai.ai (`gmail_equity-pig`) | Verified working | Supplemental; also reachable via native claude.ai Gmail connector |
| Intuit QuickBooks — company "Accelerate Marketing" | **Verified working** — P&L + balance sheet return full data; books complete through Jun 2026, current month posts later (bookkeeping cadence) | Co-primary for WF/Amex/PayPal; includes a "Dues & Subscriptions" expense line to track month-over-month |
| Zapier Gmail (12 actions enabled) | Enabled; used for outbound sends elsewhere | Not needed by this watch |

Notes: Ryan's business domain is **accelerateyourmarketing.com** (not acceleratemarketing.com). A QuickBooks month showing $0 usually means "not posted yet by the bookkeeper," not "no data" — report it as a posting lag, and re-query before concluding the connection is broken (one earlier empty-file reading in this workspace proved transient).

## Ryan's remaining setup items (recommended)

1. **Apple Card**: Apple mail routes to the Apple ID goryan@me.com (iCloud), so for automated coverage set up iCloud Mail forwarding → ryansteinolfson@gmail.com. Until then, the manual path works: Wallet → Apple Card → monthly statement → Export Transactions (CSV) and upload it to a session (Ryan did this for July 2026 on 2026-07-23).
2. **Chase (optional sharpening)**: paperless statements/notices were enabled 2026-07-23 for both cards (…1811 business, …3413 personal). For merchant-level, same-day signal, also enable per-transaction Account Alerts delivered to email (Chase: Profile & Settings → Alerts).

## Activation

The Routine is created from a Claude session with the parameters above (name `Monthly card & subscription watch`, cron `7 15 1 * *` UTC, new session per fire, notifications push + email, prompt = the playbook below). If it is ever missing (check via `list_triggers`), recreate it by saying **"Create the monthly card watch Routine exactly as specified in docs/monthly-card-watch.md"** and approving the permission prompt.

## Playbook (the Routine prompt)

> MONTHLY CARD & SUBSCRIPTION WATCH — automated monthly spend review for Ryan Steinolfson.
>
> Mission: review Ryan's card/bank spending for the calendar month that just ended — Chase credit card, Apple Card, American Express, and Wells Fargo debit — and flag anything strange. The #1 priority is catching NEW, changed, or unusual subscriptions/recurring charges quickly. Also flag possible fraud: unfamiliar merchants, duplicate charges, out-of-pattern amounts, strings of small "test" charges.
>
> Procedure:
> 1. Target month = the full calendar month immediately before today. Baseline = the 3 months before that.
> 2. Gather data from EVERY source below. If a source is unavailable or errors, note the gap and continue — never fail silently, and never stop at the first source that works.
>    a. Composio Gmail (`COMPOSIO_MULTI_EXECUTE_TOOL` → tool_slug `GMAIL_FETCH_EMAILS`), against each account: `gmail_smur-howard` (ryan@accelerateyourmarketing.com — most card email), `gmail_spire-rosier` (ryansteinolfson@gmail.com — personal-card alerts), `gmail_equity-pig` (ryan@diyai.ai). Queries scoped to the target month (`after:YYYY/MM/DD before:YYYY/MM/DD`) and ALWAYS prefixed with `in:anywhere` — issuer emails have been found in Spam and Trash (Wells Fargo alerts get auto-trashed, and Gmail purges Trash after ~30 days, so early-month alerts may be gone by run day; note this in the report if WF email coverage looks thin): `in:anywhere {from:chase.com from:americanexpress.com from:aexp.com from:wellsfargo.com from:apple.com}`; `in:anywhere subject:(receipt OR subscription OR renewal OR trial OR "price increase")`; `in:anywhere {from:stripe.com from:paypal.com}`. Extract merchant, amount, date, and account hints ("account ending …").
>    b. Intuit QuickBooks: `company_info`, then `profit_loss_quickbooks_account` covering baseline start through target-month end — watch "Dues & Subscriptions" and every expense category for new lines or jumps >~25% / ~$50 vs. baseline. Covers Wells Fargo Operating, Amex …23000, PayPal (Chase and Apple Card are NOT in QuickBooks). If the target month shows $0 across the board, report "books not yet posted for <month>" (bookkeeping lag — books post on a cadence), fall back to comparing the most recent posted months, and re-query rather than declaring the connection broken.
>    c. BACKUP — native claude.ai Gmail connector (ryan@diyai.ai): `search_threads` with the same queries if Composio is unavailable.
> 3. Build a merchant-level list of charges and recurring items. Compare against baseline months; classify each: NEW subscription, price change, duplicate charge, unfamiliar/out-of-pattern charge, or known-recurring (fine).
> 4. The FINAL message is what gets pushed/emailed to Ryan — make it self-sufficient:
>    - Line 1 verdict: "Card watch <Month YYYY>: N items need your attention" (or "all clear"), naming any data-source gaps in the same line.
>    - Flagged items: merchant — amount — date — source/account — why flagged — suggested action (cancel / dispute / verify).
>    - Current subscription roster with amounts and estimated monthly total.
>    - One line: sources checked vs. unavailable (including "QB books posted through <month>").
> 5. Do NOT send emails or external messages, and do not modify the repository. The Routine's built-in completion notification delivers the summary to Ryan by push + email.

## Subscription baseline (seed — the watch updates this picture each run)

| Merchant | Amount | Cadence | Card | First confirmed |
|---|---|---|---|---|
| Google Workspace | $9.99 | Monthly | Apple Card | Jul 5, 2026 (CSV) — verify it isn't duplicating a business-paid Workspace plan |
| Google Cloud | ~$0.35 | Monthly (usage-based) | Apple Card | Jul 1, 2026 (CSV) |

The full roster (Amex, Chase ×2, WF) gets built on the first complete monthly run from email + QuickBooks and should replace this seed table.

## Operations

- **Change schedule / pause / delete:** ask Claude to `list_triggers`, then `update_trigger` / `delete_trigger` on `Monthly card & subscription watch`.
- **Why email + QuickBooks both:** issuer/receipt emails give merchant-level precision (and are the ONLY coverage for the personal Chase and Apple Card); QuickBooks gives complete, categorized coverage of the business accounts once each month is posted. Together they cover each other's blind spots.
