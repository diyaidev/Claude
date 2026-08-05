# Hermes Agent on Hostinger — ChatGPT-Subscription Build

**Status:** Hostinger connected & account surveyed (2026-08-05). Target VPS identified — install proceeds on the existing OS, no reinstall. Next: Ryan's ~10-minute terminal session (Phases 2–3).
**Last updated:** 2026-08-05
**Owner:** Ryan · maintained in the Claude workspace

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

### Phase 0 — Access ✅ done 2026-08-05
Hostinger API token connected via Composio (account `hostinger_suid-hamose`; Composio "Enhanced Controls" had to be disabled in the Composio org settings for tool execution to work). Still open: confirm ChatGPT plan tier (Plus $20 / Pro) — decides Sol vs Terra/Luna default above.

### Phase 1 — Hermes install on the existing VPS (no reinstall)
Run in hPanel → VPS → srv1837504 → **Browser Terminal** (logs in as root; no SSH setup needed). The one-click template route was dropped — no Hermes template exists in this account's catalog, and installing on the running OS avoids a wipe.

```bash
apt update && apt install -y git curl xz-utils
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### Phase 2 — Engine auth (ChatGPT subscription)
```bash
hermes model          # → type "codex" → OpenAI Codex → GPT-5.6 Sol
```
Device-code flow: Hermes prints a URL + code; Ryan opens it on his phone/laptop, signs in with the ChatGPT account, enters the code. ~2 minutes, one time. If auth ever expires: `hermes auth add openai-codex`.

### Phase 3 — Always-on + Telegram
```bash
hermes gateway setup  # connect Telegram (also supports Discord, Slack, WhatsApp, Signal, email)
```
Telegram needs a bot token from @BotFather (60-second job). Then send `/reasoning medium` in the Telegram chat.

### Phase 4 — Hardening & ops
- SSH key auth only (register keys via Hostinger API once connected); disable password login.
- Keep `hermes dashboard` bound to localhost — access via SSH tunnel, never exposed publicly.
- `hermes update` periodically; credentials persist in `~/.hermes/`.

## Use-case backlog (post-setup)

From the video, adapted to Ryan's world:
1. **Website/price watchers** — cron jobs that watch pages for changes and text Ryan on hits (video example: RTX 5090 price drops at Micro Center; ours: competitor offers, client-site changes, tool pricing pages).
2. **Home AI lab** — Hermes inventories a machine's hardware, finds the best local models on Hugging Face for it, and reports use cases. Prompt from the video: *"Check out the hardware and specs on my computer, then go through Hugging Face and find the best local AI model I can run on it, then list the use cases I can do with that model."*
3. **Unity game studio** — Hermes drives Unity end-to-end (assets, characters, lighting) if Ryan ever wants to play with this.

## What Claude still needs from Ryan

- [x] Hostinger connected via Composio (2026-08-05)
- [ ] ChatGPT plan tier confirmation (Plus vs Pro)
- [ ] ~10-minute Browser Terminal session: paste Phase 1 commands, then device-code sign-in (Phase 2)
- [ ] Telegram bot token from @BotFather (or 60 seconds to create one together)

## Sources

- Source video: <https://youtu.be/eHZ14afnDZ0> (transcript pulled 2026-08-04)
- Hermes AI providers (Codex OAuth, Anthropic Max+credits caveat): <https://hermes-agent.nousresearch.com/docs/integrations/providers>
- Hermes quickstart & install: <https://hermes-agent.nousresearch.com/docs/getting-started/quickstart>
- Hostinger one-click template: <https://www.hostinger.com/applications/hermes-agent>
- GPT-5.6 announcement (Sol/Terra/Luna, July 9 2026): <https://openai.com/index/gpt-5-6/>
