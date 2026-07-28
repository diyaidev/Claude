# lsacommand.com — Notification comparison section

Side-by-side marketing section: **Google's default LSA notification vs. the LSA Command
alert**, using real (redacted) screenshots from July 2026. Built from the Jul 28 meeting
with Nate and Alex — action item "[Alex] Compare Notifications: provide a visual side by
side comparison … to demonstrate value."

**Status: preview only — NOT live.** Ryan approves first (his explicit instruction).

## Files

| File | Purpose |
|---|---|
| `section.html` | The drop-in fragment. Self-contained: styles scoped under `.lsa-nc`, brand tokens as CSS variables at the top. |
| `index.html` | Standalone preview page (generated from `section.html` — edit `section.html`, not this). |
| `assets/` | Redacted web-sized screenshots (760px wide) + `archivo.woff2` (latin subset, variable weight). |

## What was redacted (and why)

From the raw phone screenshots, blurred before any use:

- Customer's phone number, full name, and street address (lead PII)
- The live conversation-takeover link (`lsa.ravu.me/tconv?…` — a working session link)
- The Google Ads customer ID

Left visible deliberately (easy to blur on request): client first name "Hunter",
"Crystal Cove Pool and Spa", and the "Sky Media Ventures LLC" white-label header —
the fine print uses the white-label header as a selling point.

## Before it ships

1. **CTA href** — `#book-a-demo` is a placeholder; point it at the real booking/demo URL.
2. **Hosting** — lsacommand.com resolves to Vercel (`cname.vercel-dns.com`), but the
   project isn't in the DIYAi Vercel team this workspace can reach; it's presumably under
   Alex's account. Go-live paths: Alex pastes `section.html` + `assets/` into the site
   repo, or this workspace gets access to that repo/Vercel project.
3. **Brand match** — tokens (`--nc-acc`, `--nc-bg`, fonts) are guesses at a clean default;
   adjust to the site's real palette in one place at the top of `section.html`.
4. Section defaults light and auto-adapts to a dark host page; delete the
   `prefers-color-scheme` block to pin it light.
