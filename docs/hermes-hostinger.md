# Hermes Agent on Hostinger — ChatGPT-Subscription Build

**Status:** ✅ LIVE (2026-08-05). Hermes v0.20.0 on srv1837504, engine GPT-5.6 Sol via ChatGPT-subscription Codex OAuth, reasoning medium, Telegram gateway restored, all services boot-persistent. Verified end-to-end (test message delivered + live `ENGINE-OK` inference).
**Last updated:** 2026-08-05
**Owner:** Ryan · maintained in the Claude workspace

## What was actually found (major correction to earlier assumption)

Hermes was **already installed on this VPS since 2026-07-17** (not a fresh box): full config, SOUL.md ("one of Ryan's three agents"), credential store, and Telegram wiring. Timeline reconstructed from the box: gateway systemd unit crashed **Jul 27** (exit 1, never restarted — unit was not boot-enabled), Telegram keys were disabled **Jul 29** (`DISABLED_20260729_*` prefixes), and the main model had been switched to grok-4.5/xAI after the Anthropic API credential exhausted (the "$200/day" burn). The box also runs live business crons (AgentOps outreach runner, reply triage, Gmail brain) — untouched by this work.

## Live account survey (2026-08-05, via Hostinger API)

- **VPS:** `srv1837504.hstgr.cloud` (id 1837504) — KVM 2, 2 vCPU / 8 GB RAM / 100 GB disk, IPv4 31.97.14.109, **running**, created 2026-07-17
- **OS:** plain Ubuntu 24.04 LTS (template 1077) — no agent stack installed yet
- **Subscription:** KVM 2 active, $203.88/yr, renews 2027-07-03 — no purchase needed
- **Template catalog:** all 93 checked — **no Hermes Agent one-click template exists in this account's API catalog** (closest: NemoClaw, n8n, Claude Code, Codex). Decision: install Hermes directly on the running Ubuntu 24.04 with the official installer — avoids wiping the box and skips the template dependency entirely.
- Composio's Hostinger toolkit is read-only for VPS ops (list/inspect); OS-level work happens in hPanel's Browser Terminal.

---

## The decision (recorded so we don't relitigate it)

**Hermes Agent's engine = Ryan's ChatGPT subscription, via the OpenAI Codex provider. No OpenAI API key, no per-token billing.**

Verified against Nous Research's official docs (not just the video):

- Hermes's OpenAI Codex provider authenticates with **ChatGPT OAuth device-code login** — you open a URL, enter a code, done. Credentials live in `~/.hermes/auth.json` on the VPS. No Codex CLI install required. Works on a headless server (device-code flow needs no browser on the VPS itself).
- Model access follows the ChatGPT plan: **GPT-5.6 Sol / Terra / Luna** are available through Codex on paid ChatGPT plans (Sol is the flagship).
- By contrast, Hermes's **Anthropic path requires Claude Max *plus extra usage credits*** — the base Max allowance is not usable inside Hermes. So running Claude inside Hermes would cost extra money for no benefit.

**Division of labor:**

| Layer | Engine | Billing |
|---|---|---|
| Hermes Agent (Hostinger VPS, 24/7) | GPT-5.6 via ChatGPT subscription (Codex OAuth) | Flat ChatGPT plan — $0 marginal |
| Claude workspace (this repo, email, books, YouTube ops) | Claude via Ryan's Claude subscription | Flat — unchanged, nothing to set up |

Reference point from the source video: the creator was spending ~$200/day on Claude Opus API inside Hermes before switching to GPT-5.6 on a ChatGPT subscription.

## Model settings (from the video, cross-checked)

- **Main model:** GPT-5.6 **Sol** (top pick on Pro/$100/$200 plans). On the $20 Plus plan, Sol works but **Terra or Luna** stretches the usage allowance further.
- **Reasoning level:** `/reasoning medium` sent in the chat channel after setup. Medium beats high/ultra for instruction-following; `low` is the runner-up if speed matters or the plan is Plus.
- Set the model either in the terminal wizard (`hermes model` → type "codex" → OpenAI Codex → GPT-5.6 Sol) or the web dashboard (`hermes dashboard` → Models).

## Setup runbook

### As-built record (all executed 2026-08-05 by Claude over SSH)

1. **Access:** Hostinger API token connected via Composio (Composio org "Enhanced Controls" had to be disabled for tool execution). SSH: ed25519 key `claude-ryan-workspace` (registered on the Hostinger account, id 553217) authorized on the VPS by Ryan via Browser Terminal; private key lives in the Composio sandbox (`/mnt/files/keys/`).
2. **Update:** official installer re-run over the existing install → Hermes v0.20.0. Log: `/root/hermes-install.log`.
3. **Engine switch** in `/root/.hermes/config.yaml`: `model.provider: xai-oauth → openai-codex`, `model.default: grok-4.5 → gpt-5.6-sol`, removed stale `base_url: https://api.x.ai/v1`, `agent.reasoning_effort: xhigh → medium`. **No ChatGPT sign-in was needed — a valid Codex OAuth credential already existed** (`hermes auth status openai-codex` → logged in). If it ever expires: `hermes auth add openai-codex` (device code).
4. **Telegram restored** in `/root/.hermes/.env`: stripped `DISABLED_20260729_` off `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, `TELEGRAM_HOME_CHANNEL` (same bot/token Ryan supplied — they matched). Old `claude-telegram-listener` unit confirmed dead (disabled, script gone) → no getUpdates conflict.
5. **Services:** `hermes gateway restart` (auto-refreshed the outdated unit), `systemctl --user restart hermes-serve hermes-dashboard`; **`hermes-gateway` was boot-disabled — now enabled** (root cause of the July outage persisting). All three active + enabled, `Linger=yes`.
6. **Verification:** `hermes status` → Model `gpt-5.6-sol`, Provider `OpenAI Codex`; `hermes send -t telegram …` delivered to home channel (chat 6767234485); one-shot inference `hermes chat -q` returned `ENGINE-OK` in 7s through the subscription.

Config backups on the VPS: `/root/.hermes/config.yaml.bak-claude-*`, `/root/.hermes/.env.bak-claude-*`.

### Open items / ops notes
- **Pending kernel reboot** ("System restart required" MOTD). Everything is boot-persistent now; reboot at a quiet hour (avoid weekday 10:00 UTC outreach run and :11/:41 triage slots). ~1 min downtime.
- Hermes MCP server `linear` fails OAuth in background context (pre-existing, harmless warning). Fix only if needed: `hermes mcp login linear` in an interactive SSH session.
- Anthropic credentials in Hermes remain exhausted/stale — irrelevant now (fallback chain: codex/gpt-5.5 → anthropic → nous). Consider pruning the fallback chain later.
- Dashboard stays bound to 127.0.0.1:9120, serve on 127.0.0.1:9119 — not publicly exposed; keep it that way.
- On the $20 Plus plan, if Sol rate-limits: drop to `gpt-5.6-terra` or reasoning `low` (one-line config change).

## Use-case backlog (post-setup)

From the video, adapted to Ryan's world:
1. **Website/price watchers** — cron jobs that watch pages for changes and text Ryan on hits (video example: RTX 5090 price drops at Micro Center; ours: competitor offers, client-site changes, tool pricing pages).
2. **Home AI lab** — Hermes inventories a machine's hardware, finds the best local models on Hugging Face for it, and reports use cases. Prompt from the video: *"Check out the hardware and specs on my computer, then go through Hugging Face and find the best local AI model I can run on it, then list the use cases I can do with that model."*
3. **Unity game studio** — Hermes drives Unity end-to-end (assets, characters, lighting) if Ryan ever wants to play with this.

## Checklist — final state

- [x] Hostinger connected via Composio (2026-08-05)
- [x] SSH access authorized (key paste by Ryan)
- [x] Hermes updated + engine switched to GPT-5.6 Sol on ChatGPT subscription (no sign-in needed — existing valid Codex OAuth)
- [x] Telegram re-enabled with Ryan's existing bot; test message delivered
- [x] Services active + boot-enabled
- [x] ChatGPT plan: **Pro ($100)** (upgraded 2026-08-05) — Sol primary is the right call; fallback chain leads with `gpt-5.6-terra` (`gpt-5.6-sol-pro` exists in the catalog if Ryan ever wants max-compute mode; slower per turn)
- [x] Rebooted 2026-08-05 19:48 UTC — new kernel 6.8.0-136, reboot-required cleared, all three services auto-started (persistence fix proven)
- [ ] Build first cron use cases (site/price watchers) — next session

## Sources

- Source video: <https://youtu.be/eHZ14afnDZ0> (transcript pulled 2026-08-04)
- Hermes AI providers (Codex OAuth, Anthropic Max+credits caveat): <https://hermes-agent.nousresearch.com/docs/integrations/providers>
- Hermes quickstart & install: <https://hermes-agent.nousresearch.com/docs/getting-started/quickstart>
- Hostinger one-click template: <https://www.hostinger.com/applications/hermes-agent>
- GPT-5.6 announcement (Sol/Terra/Luna, July 9 2026): <https://openai.com/index/gpt-5-6/>
