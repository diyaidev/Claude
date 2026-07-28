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
| `assets/` | Web-sized email images (760px wide, retina sources rendered at 2x) + `archivo.woff2` (latin subset, variable weight). |

## About the email images (v2)

Ryan's second set of screenshots (full desktop emails) arrived as chat images rather
than files, so both emails were rebuilt as pixel-faithful HTML replicas and rendered
with headless Chromium — visually identical to the originals, crisper than the phone
screenshots, with **partial blurs per Ryan's spec**: you can tell there's a real phone
number / name / email, but can't read the whole thing.

- Phone number: `+1360` visible, remaining digits blurred
- Lead name: "Vincent" visible, last name blurred (both mentions)
- Street address blurred; "Henderson Nv" visible, ZIP blurred
- Takeover link: `lsa.ravu.me/tconv?i=` visible, token blurred
- Google customer ID: `568-` visible, rest blurred; recipient email `skym…@gmail.com` middle blurred

The blurred spans contain **scrambled substitute text underneath**, so the real values
are unrecoverable even if the blur were reversed. Replica sources:
`scratchpad/email-lsa.html` + `email-google.html` (session scratchpad; not committed).

Left visible deliberately: "Hunter", "Crystal Cove Pool and Spa", and the
"Sky Media Ventures LLC" white-label header — the fine print uses white-labeling as a
selling point.

## Before it ships

1. **Placement** — Ryan wants this in/next to the **response rate** section of
   lsacommand.com: the speed-to-lead framing feeds directly into response-rate proof.
2. **CTA href** — `#book-a-demo` is a placeholder; point it at the real booking/demo URL.
2. **Hosting** — lsacommand.com resolves to Vercel (`cname.vercel-dns.com`), but the
   project isn't in the DIYAi Vercel team this workspace can reach; it's presumably under
   Alex's account. Go-live paths: Alex pastes `section.html` + `assets/` into the site
   repo, or this workspace gets access to that repo/Vercel project.
3. **Brand match** — tokens (`--nc-acc`, `--nc-bg`, fonts) are guesses at a clean default;
   adjust to the site's real palette in one place at the top of `section.html`.
4. Section defaults light and auto-adapts to a dark host page; delete the
   `prefers-color-scheme` block to pin it light.
