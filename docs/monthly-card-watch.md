# Monthly Card & Subscription Watch

A recurring monthly review of Ryan's spending across **Chase credit card, Apple Card, American Express, and Wells Fargo debit**, designed to catch **new or unusual subscriptions** (the #1 goal — no more paying for a mystery subscription for months) plus possible fraud: unfamiliar merchants, duplicate charges, out-of-pattern amounts, strings of small "test" charges.

- **Schedule:** 1st of each month, ~8:07 AM Pacific (cron `7 15 1 * *` UTC)
- **Delivery:** run summary to Ryan via push notification + email (the Routine's built-in completion notification — no external sends)
- **Run mode:** fresh Claude session per run, in this workspace environment
- **On-demand:** in any Claude session, say *"run the monthly card watch now"* — follow the playbook below

## Data sources (verified 2026-07-22)

| Source | Status | Role |
|---|---|---|
| Composio Gmail — ryan@accelerateyourmarketing.com (`gmail_smur-howard`) | **Verified working** — ~200 bank-domain emails per 45 days; Amex (acct …023000) confirmed live | **Primary** — most card email lands here |
| Composio Gmail — ryansteinolfson@gmail.com (`gmail_spire-rosier`) | Verified working — but only 2 bank-domain emails in 45 days | Primary (light traffic today; grows if Ryan enables issuer alerts) |
| Composio Gmail — ryan@diyai.ai (`gmail_equity-pig`) | Verified working | Supplemental; also reachable via the native claude.ai Gmail connector |
| Intuit QuickBooks (company "Accelerate Marketing") | Connected, but **zero transactions Jul 2025–Jun 2026** (`hasTransactions: false`) | Secondary once fixed — likely the connector is signed into an empty/wrong company file, or bank feeds were never set up in it |
| Zapier Gmail (12 actions enabled) | Enabled; used for outbound email sends elsewhere in the workspace | Not needed by this watch |

Note: Ryan's business domain is **accelerateyourmarketing.com** (not acceleratemarketing.com).

## Ryan's remaining setup items (optional but recommended)

1. **QuickBooks**: verify the Claude QuickBooks connector is signed into the company file that actually holds your books, and that bank feeds for the four accounts are connected there (QBO → Banking: https://qbo.intuit.com/app/banking). Until then the watch runs on email data alone.
2. **Issuer alert emails**: turn on per-transaction or daily alert emails at Chase, Wells Fargo, and Apple Card (Amex already emails ryan@accelerateyourmarketing.com). Merchant-level alerts make "what exactly is this new $14.99 charge" answerable.

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
>    a. PRIMARY — Composio Gmail (`COMPOSIO_MULTI_EXECUTE_TOOL` → tool_slug `GMAIL_FETCH_EMAILS`), against each account: `gmail_smur-howard` (ryan@accelerateyourmarketing.com — most card email), `gmail_spire-rosier` (ryansteinolfson@gmail.com), `gmail_equity-pig` (ryan@diyai.ai). Queries scoped to the target month (`after:YYYY/MM/DD before:YYYY/MM/DD`): `{from:chase.com from:americanexpress.com from:aexp.com from:wellsfargo.com from:apple.com}`; `subject:(receipt OR subscription OR renewal OR trial OR "price increase")`; `{from:stripe.com from:paypal.com}`. Extract merchant, amount, date, and account hints (e.g., "account ending …") from each alert/receipt/statement email.
>    b. SECONDARY — Intuit QuickBooks connector: `company_info`, then `profit_loss_quickbooks_account` covering baseline start through target-month end. Compare expense accounts month-over-month; flag new categories or jumps >~25% / ~$50. If `hasTransactions: false` (the state as of 2026-07-22), add one action-item line to the report: "QuickBooks still has no bank-feed data."
>    c. BACKUP — native claude.ai Gmail connector (ryan@diyai.ai): `search_threads` with the same queries if Composio is unavailable.
> 3. Build a merchant-level list of charges and recurring items. Compare against baseline months; classify each: NEW subscription, price change, duplicate charge, unfamiliar/out-of-pattern charge, or known-recurring (fine).
> 4. The FINAL message is what gets pushed/emailed to Ryan — make it self-sufficient:
>    - Line 1 verdict: "Card watch <Month YYYY>: N items need your attention" (or "all clear"), naming any data-source gaps in the same line.
>    - Flagged items: merchant — amount — date — source/account — why flagged — suggested action (cancel / dispute / verify).
>    - Current subscription roster with amounts and estimated monthly total.
>    - One line: sources checked vs. unavailable.
> 5. Do NOT send emails or external messages, and do not modify the repository. The Routine's built-in completion notification delivers the summary to Ryan by push + email.

## Operations

- **Change schedule / pause / delete:** ask Claude to `list_triggers`, then `update_trigger` / `delete_trigger` on `Monthly card & subscription watch`.
- **Why email + QuickBooks both:** issuer/receipt emails give merchant-level precision for naming the exact subscription; QuickBooks (once its company file has bank feeds) gives complete category-level coverage as a cross-check. Together they cover each other's blind spots.
