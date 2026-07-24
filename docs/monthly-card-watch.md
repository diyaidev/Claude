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

## Subscription baseline (updated 2026-07-23 from 19-month Apple Card export, Jan 2025–Jul 2026)

**Apple Card — active today:** Google Workspace $9.99/mo (since Mar 2025; verify not duplicating a business-paid plan); Google Cloud usage-based pennies; SunPass $30 auto-replenish (tolls, not a subscription).

**Apple Card — ended (history for comparison):**
- EQT*Ambetter insurance: $31.86/mo through Nov 2025 → **$1,511.31/mo Dec 2025–Apr 2026 (47× jump, 5 months, $7,556.55)** → all 5 refunded 2026-05-19 → Apple issued $5,763.12 credit-balance check 2026-06-25 (Ryan to confirm receipt). The canonical example of the failure mode this watch exists to catch.
- Spotify: $13.14/mo → $20.75/mo Mar 2026 (+58%, billing day moved) → no charges after May 2026 (confirm cancelled vs. moved cards).
- Audible: $0.99 promo → $14.95/mo → $9.99 → ended Aug 2025. Way.com WAY+ $2.95/mo ended Jul 2025. AAAaccelerator $197/mo Jan–Mar 2025, one month refunded, ended.

**Watch-style flags from history** (pattern examples): same-day same-amount pairs — American Airlines $302.33×2 (2025-04-17), $211.50×2 (2025-03-23), Blueprint $276.25×2 (2025-03-22), OpenAI $10×2 (2025-04-27).

The Amex / Chase ×2 / Wells Fargo rosters get added by the first complete monthly run from email + QuickBooks.

## Open items & verifications (checked 2026-07-23)

- ✅ **Ambetter refund check deposited**: WF mobile-deposit alert (found in Trash) confirms $5,763.12 deposited 2026-06-30 into WF account …0899. Note: …0899 ≠ …5623 (the account that funds Apple Card autopay) — Ryan has multiple WF accounts; only "Wells Fargo Operating" is in QBO.
- ✅ **Google Workspace $9.99 mystery**: two old-business Workspace subscriptions were canceled 2026-07-21 — **convoagent.co** (Business Standard) and **caisey.co** (Business Starter). The Apple Card's $9.99 monthly "GOOGLE *WORKSPACE" (last charged Jul 5) should stop; **Aug/Sep runs must confirm no further $9.99 Workspace charge on Apple Card** — if one appears, a third Workspace is still alive.
- ⏳ **Spotify**: left Apple Card after May 2026 ($20.75/mo at exit); Ryan believes it moved to Chase. No Spotify receipts in any connected inbox. Confirm via Chase transaction alerts (once enabled) or first run with Chase data.
- ⚠️ **Google Cloud billing card expiring**: Google Payments notice (2026-07-18, to ryan@accelerateyourmarketing.com): the Amex ••••1004 on "Google Cloud Platform & APIs" expires soon — update it before billing fails.
- ⏳ **QBO July posting**: still empty as of 2026-07-23 (bookkeeping cadence) — Aug run should treat July-$0 as posting lag per playbook.

## Operations

- **Change schedule / pause / delete:** ask Claude to `list_triggers`, then `update_trigger` / `delete_trigger` on `Monthly card & subscription watch`.
- **Why email + QuickBooks both:** issuer/receipt emails give merchant-level precision (and are the ONLY coverage for the personal Chase and Apple Card); QuickBooks gives complete, categorized coverage of the business accounts once each month is posted. Together they cover each other's blind spots.
