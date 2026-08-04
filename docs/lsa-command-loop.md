# LSA Command Loop

An autonomous build loop for the LSA command software (`diyaidev/lsa-command`),
modeled on Finn's "Fin Loop" (spec → build → review, YouTube FRGLToHAtgc) and
configured from Ryan's interview answers on 2026-08-04.

**The deal:** Ryan spends a few minutes in the morning answering spec questions.
The loop builds, tests, and stages work all day on its own. Ryan approves
merges with a 🚀 in Slack at the end of the day. Nothing ever changes on the
live platform without that 🚀.

## Architecture

Three project skills in `.claude/skills/`, one shared pipeline on GitHub Issues:

| Stage | Skill | What it does |
|---|---|---|
| Spec | `lsa-spec` | Interviews Ryan until confident, files detailed issues with acceptance criteria into the backlog |
| Build | `lsa-build` | Picks the next backlog issue, builds it on a `loop/<n>-<slug>` branch, verifies, hands to review |
| Review | `lsa-review` | Independently tests the build, stages it as a **draft PR**, posts to Slack; merges only on Ryan's 🚀 |

### Issue pipeline (labels on `diyaidev/lsa-command`)

```
loop:backlog → loop:building → loop:ready-for-review → loop:merge-ready → merged (issue closed)
     ↑______________ review fail / 👎 sends it back ______________|

Side tracks: loop:blocked (builder stuck — needs Ryan's input)
             loop:needs-human (touches money/live LSA — never built autonomously)
```

### Staging model (per Ryan: branch + draft PR, like this workspace's PRs #3/#4)

- All work on `loop/` feature branches; the default branch is the live platform
  and is never pushed directly.
- Review stages each finished issue as a **draft PR** — that draft PR *is* the
  staging section. Ryan's 🚀 flips it to ready and merges it. 👎 sends it back
  to the build queue with his feedback.

### Approvals (Slack)

Channel: `#lsa-merge-ready` (created on first review run if missing). Each
staged change is posted with a plain-language summary, self-test steps, and
PR/issue links. Reactions — **from Ryan only**:

- 🚀 → merge it (squash), close the issue, ✅ confirmation in thread
- 👎 / ❌ → back to the build loop with his feedback

## Daily rhythm (morning kickoff, all-day loop)

1. **Morning (~5 min):** Ryan opens a session and says `/lsa-spec` plus
   whatever's on his mind ("fix X, polish Y"). Answers the interview
   questions. Issues get filed.
2. **All day (hands-off):** in that session Ryan starts the loop:

   ```
   /loop 30m run the lsa-build skill, then the lsa-review skill
   ```

   Every ~30 minutes the session builds the next issue, then reviews/stages
   the previous one. (Finn's original two-terminal variant also works:
   `/loop 30m /lsa-build` in one session and `/loop 30m /lsa-review` in
   another — the labels keep them from colliding.)
3. **Evening (~5 min):** Ryan opens `#lsa-merge-ready`, self-tests anything he
   wants, taps 🚀 (or 👎). The next review cycle performs the merges — or he
   tells any session "process the LSA approvals" to do it immediately.

## Guardrails (from Ryan's interview, non-negotiable)

1. **Live platform untouched without 🚀** — staging is branches + draft PRs;
   merge requires Ryan's rocket, verified to be from Ryan.
2. **No spend or budget changes, ever, autonomously** — any issue or code path
   touching ad budgets, billing, payments, or money movement gets
   `loop:needs-human` and stops.
3. **One issue per build cycle** — no batching, no scope creep past an issue's
   Non-goals.
4. **Review trusts nothing** — it re-runs tests and walks the test plan itself
   before anything is staged.

## First-run setup checklist (needs Ryan present once, to approve connector prompts)

- [ ] Merge this PR so the skills land on `main` and load in future sessions.
- [ ] First `/lsa-spec` run: approve the `add_repo` prompt for
      `diyaidev/lsa-command` (push access) — subsequent sessions reuse it.
- [ ] Same run creates the six `loop:*` labels on the repo.
- [ ] First `/lsa-review` run: approve Slack channel creation for
      `#lsa-merge-ready`.
- [ ] Optional: invite Alex to `#lsa-merge-ready` (visibility only — his
      reactions don't merge).

## Current status

- **2026-08-04** — Loop designed from the video transcript + Ryan's interview
  (repo: `diyaidev/lsa-command` · tracker: GitHub Issues · staging: draft PRs ·
  approvals: Slack 🚀 · cadence: morning kickoff + all-day 30m loop · first
  focus: bug fixes & polish). Skills staged for review; nothing run against
  the live repo yet.
