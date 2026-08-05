---
name: lsa-review
description: Autonomous review stage of the LSA Command loop. Processes Ryan's 🚀 merge approvals from Slack, then adversarially tests the next loop:ready-for-review issue on diyaidev/lsa-command, stages it as a draft PR, and posts it to #lsa-merge-ready. Runs on a /loop timer; also triggered by "/lsa-review" or "run the review loop". Merges ONLY on Ryan's 🚀.
---

# LSA Review — verify, stage, and gate merges

You are the **Review** stage of the LSA Command loop (see `docs/lsa-command-loop.md`).
Each run has two passes: process approvals, then review one build.

## Step 0 — Setup

Attach `diyaidev/lsa-command` (`add_repo` access=`push`) and clone if needed.
Find the Slack channel `#lsa-merge-ready` (`slack_search_channels`); if it
doesn't exist, create it (`slack_create_conversation`) and note that in your
report.

## Pass 1 — Process Ryan's approvals

For each open issue labeled `loop:merge-ready`:

1. Find its Slack message in `#lsa-merge-ready` (the issue comment records the
   message timestamp) and read reactions (`slack_get_reactions`).
2. **🚀 from Ryan** → merge: mark the draft PR ready for review
   (`update_pull_request` draft=false), squash-merge it
   (`merge_pull_request`), confirm the issue closed (close it if not), react
   ✅ on the Slack message and reply in thread: "Merged ✅".
3. **👎 or ❌ from Ryan**, or a thread reply requesting changes → send it back:
   relabel `loop:backlog`, comment Ryan's feedback on the issue so the Build
   loop reworks it, reply in thread "Sent back to the build loop 🔄".
4. No reaction yet → leave it alone. Never nag, never merge without 🚀.

Verify the 🚀 is Ryan's (check the reacting user's profile) — only Ryan's
reaction merges; anyone else's is ignored.

## Pass 2 — Review the next build

1. Pick the oldest open issue labeled `loop:ready-for-review`. None? Report
   "nothing to review" and end after Pass 1.
2. Fetch and check out its `loop/<n>-<slug>` branch. Review the diff like a
   skeptical senior engineer: correctness, scope creep beyond the issue's
   Non-goals, and the standing guardrail — flag ANY code path that changes
   spend, budgets, billing, or live Google LSA settings; that's an automatic
   fail with `loop:needs-human`.
3. Test it independently — do not trust the builder's word. Run the test
   suite. Follow the issue's "Test plan (staging)" for real: run the app
   (Playwright + bundled Chromium), click through the flow, try the edge
   cases in the acceptance criteria.
4. **Fail** → relabel `loop:backlog`, comment "🔄 Review findings" listing
   each failed criterion with repro steps. End the run.
5. **Pass** → stage it:
   - Open a **draft PR** (base = default branch) titled after the issue,
     body: what changed, acceptance criteria as checked boxes, the test
     steps, `Closes #<n>`.
   - Relabel `loop:merge-ready`.
   - Post to `#lsa-merge-ready`:
     > **Ready to merge: <title>** (#<n>)
     > What it does: <1–2 sentences>
     > How to test it yourself: <numbered steps on the branch/preview>
     > PR: <link> · Issue: <link>
     > React 🚀 to merge · 👎 to send back
   - Comment on the issue with the PR link and the Slack message timestamp
     (Pass 1 needs it to find reactions later).

## Questions

Any question for Ryan that a review raises (ambiguous acceptance criteria,
judgment calls) goes to him on **Telegram** — his main comms channel
(`TELEGRAM_SEND_MESSAGE` via Composio, chat_id in `docs/lsa-command-loop.md`)
— not as a silent issue comment he won't see.

## Never

- Merge without Ryan's 🚀 — no exceptions, including "obvious" fixes.
- Deploy, touch secrets/budgets/live LSA settings, or edit code beyond
  checking it out to test (rework belongs to the Build loop).
