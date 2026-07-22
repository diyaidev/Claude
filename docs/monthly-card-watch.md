# Monthly Card & Subscription Watch

A recurring monthly review of Ryan's spending across **Chase credit card, Apple Card, American Express, and Wells Fargo debit**, designed to catch **new or unusual subscriptions** (the #1 goal — no more paying for a mystery subscription for months) plus possible fraud: unfamiliar merchants, duplicate charges, out-of-pattern amounts, strings of small "test" charges.

- **Schedule:** 1st of each month, ~8:07 AM Pacific (cron `7 15 1 * *` UTC)
- **Delivery:** run summary to Ryan via push notification + email (the Routine's built-in completion notification — no external sends)
- **Run mode:** fresh Claude session per run, in this workspace environment
- **On-demand:** in any Claude session, say *"run the monthly card watch now"* — follow the playbook below

## Status (as of 2026-07-22 setup session)

| Piece | Status |
|---|---|
| Scheduled Routine | **Pending activation** — the `create_trigger` call was declined by the session permission layer; needs Ryan's one-time approval (see Activation below) |
| QuickBooks connector | Connected (Accelerate Marketing), but **no transaction data** for Apr–Jun 2026 (`hasTransactions: false`) — QBO bank feeds appear stale/disconnected |
| Gmail connector (ryan@diyai.ai) | Working, but inbox contains **zero** emails from chase.com / americanexpress.com / wellsfargo.com / apple.com in the last 90 days — bank email lands elsewhere |
| Personal Gmail (ryansteinolfson@gmail.com) | Not directly reachable — Composio/Zapier tool calls were declined during setup |
| ryan@acceleratemarketing.com | Not connected to any available tool |

## Ryan's setup checklist (makes the watch actually see data)

1. **Reconnect QBO bank feeds** — in QuickBooks Online go to **Banking** (https://qbo.intuit.com/app/banking) and re-authorize the Chase, Apple Card, Amex, and Wells Fargo feeds so transactions flow again.
2. **Route bank email into a readable inbox** — in ryansteinolfson@gmail.com (and ryan@acceleratemarketing.com), create a filter: `from:(chase.com OR americanexpress.com OR aexp.com OR wellsfargo.com OR apple.com)` → **forward to ryan@diyai.ai** (Gmail: Settings → Forwarding → add forwarding address, then create the filter). Alternatively, approve Claude's Composio Gmail access for the personal account.
3. **Turn on transaction alert emails** at each issuer (Chase, Amex, Wells Fargo, Apple Card all support per-transaction or daily alert emails) — merchant-level alerts make subscription detection far more precise than statements alone.

## Activation

The Routine could not be created from the setup session (permission declined). To activate: in a Claude session, say **"Create the monthly card watch Routine exactly as specified in docs/monthly-card-watch.md"** and **approve the `create_trigger` permission prompt** when it appears. Parameters: name `Monthly card & subscription watch`, cron `7 15 1 * *` (UTC), new session per fire, notifications push + email, prompt = the playbook below.

## Playbook (the Routine prompt)

> MONTHLY CARD & SUBSCRIPTION WATCH — automated monthly spend review for Ryan Steinolfson.
>
> Mission: review Ryan's card/bank spending for the calendar month that just ended — Chase credit card, Apple Card, American Express, and Wells Fargo debit — and flag anything strange. The #1 priority is catching NEW, changed, or unusual subscriptions/recurring charges quickly. Also flag possible fraud: unfamiliar merchants, duplicate charges, out-of-pattern amounts, strings of small "test" charges.
>
> Procedure:
> 1. Target month = the full calendar month immediately before today. Baseline = the 3 months before that.
> 2. Gather data from EVERY source below. If a source is unavailable or errors, note the gap and continue — never fail silently, and never stop at the first source that works.
>    a. Intuit QuickBooks connector: call `company_info`, then `profit_loss_quickbooks_account` covering baseline start through target-month end (returns monthly columns). Compare expense accounts month-over-month; flag categories that are new or jumped more than ~25% or ~$50. If it returns `hasTransactions: false`, report "QuickBooks bank feeds are not syncing" as an action item for Ryan.
>    b. Gmail connector (ryan@diyai.ai): `search_threads` for the target month with queries such as `{from:chase.com from:americanexpress.com from:aexp.com from:wellsfargo.com from:apple.com}`, `subject:(statement OR receipt OR subscription OR renewal OR trial OR "price increase")`, `{from:stripe.com from:paypal.com}`. Open promising threads with `get_thread`; extract merchant, amount, date — including messages auto-forwarded from Ryan's other mailboxes.
>    c. Composio Gmail tools (`COMPOSIO_SEARCH_TOOLS` → `GMAIL_FETCH_EMAILS`), if available — may reach ryansteinolfson@gmail.com where most bank/card email lands. Same searches.
> 3. Build a merchant-level list of charges and recurring items. Compare against baseline months; classify each: NEW subscription, price change, duplicate charge, unfamiliar/out-of-pattern charge, or known-recurring (fine).
> 4. The FINAL message is what gets pushed/emailed to Ryan — make it self-sufficient:
>    - Line 1 verdict: "Card watch <Month YYYY>: N items need your attention" (or "all clear"), naming any data-source gaps in the same line.
>    - Flagged items: merchant — amount — date — source/account — why flagged — suggested action (cancel / dispute / verify).
>    - Current subscription roster with amounts and estimated monthly total.
>    - One line: sources checked vs. unavailable.
> 5. Do NOT send emails or external messages, and do not modify the repository. The Routine's built-in completion notification delivers the summary to Ryan by push + email.

## Operations

- **Change schedule / pause / delete:** ask Claude to `list_triggers`, then `update_trigger` / `delete_trigger` on `Monthly card & subscription watch` (requires approving the permission prompt).
- **Why email + QuickBooks both:** QuickBooks (once feeds sync) gives complete category-level coverage; issuer/receipt emails give merchant-level precision for naming the exact subscription. Together they cover each other's blind spots.
