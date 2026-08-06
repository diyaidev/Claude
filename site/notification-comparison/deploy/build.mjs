import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const esc = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');

// Build the section: swap the repo section's <img> shots for scaled live-HTML email replicas
const googleFrame = `<div class="nc-frame" data-nat-h="1051">
                                <iframe title="Google's actual LSA notification email" srcdoc="__GOOGLE_EMAIL__"
                                    style="width:860px;height:1051px;border:0;transform-origin:top left;display:block;pointer-events:none"
                                    scrolling="no"></iframe>
                            </div>`;
const lsaFrame = `<div class="nc-frame" data-nat-h="1466">
                                <iframe title="The actual LSA Command lead alert email" srcdoc="__LSA_EMAIL__"
                                    style="width:860px;height:1466px;border:0;transform-origin:top left;display:block;pointer-events:none"
                                    scrolling="no"></iframe>
                            </div>`;
const scaler = `        <script>
            (function () {
                function fitNotificationFrames() {
                    document.querySelectorAll('.nc-frame').forEach(function (f) {
                        var s = f.clientWidth / 860;
                        var i = f.querySelector('iframe');
                        if (!i) return;
                        i.style.transform = 'scale(' + s + ')';
                        f.style.height = (parseFloat(f.dataset.natH) * s) + 'px';
                    });
                }
                window.addEventListener('resize', fitNotificationFrames);
                window.addEventListener('load', fitNotificationFrames);
                fitNotificationFrames();
            })();
        </script>`;

let section = readFileSync('section-lsacommand.html', 'utf8')
  .replace(/<img src="notification-google-alert\.png"[\s\S]*?>/, () => googleFrame)
  .replace(/<img src="notification-lsacommand-alert\.png"[\s\S]*?>/, () => lsaFrame)
  .replace('</section>', () => scaler + '\n        </section>')
  .replace('__GOOGLE_EMAIL__', () => esc(readFileSync('email-google.html', 'utf8')))
  .replace('__LSA_EMAIL__', () => esc(readFileSync('email-lsa.html', 'utf8')));

let page;
try {
  let live;
  if (process.env.TEST_LIVE) {
    live = readFileSync(process.env.TEST_LIVE, 'utf8');
  } else {
    const res = await fetch('https://www.lsacommand.com/', { headers: { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36' } });
    if (!res.ok) throw new Error('fetch ' + res.status);
    live = await res.text();
  }
  const anchor = '<!-- Refund Engine Section -->';
  if (!live.includes(anchor)) throw new Error('anchor missing');
  live = live.replace(anchor, () => section + '\n        ' + anchor);
  // point the replica's relative assets at the real domain; keep hashes/schemes intact
  page = live.replace(/\b(src|href)="([^"]+)"/g, (m, a, v) =>
    /^(https?:|#|mailto:|tel:|sms:|data:|\/\/)/.test(v) ? m : `${a}="https://lsacommand.com/${v}"`);
  page = page.replace('</title>', () => '</title>\n    <meta name="robots" content="noindex">');
  // mirror the site's own assets into this deployment so the copy is complete
  mkdirSync('public', { recursive: true });
  const rels = new Set();
  for (const m of page.matchAll(/\b(?:src|href)="https:\/\/lsacommand\.com\/([^"/]+)"/g)) rels.add(m[1]);
  for (const name of rels) {
    try {
      const r = await fetch('https://lsacommand.com/' + name);
      if (!r.ok) throw new Error('HTTP ' + r.status);
      writeFileSync('public/' + name, Buffer.from(await r.arrayBuffer()));
      page = page.replaceAll('https://lsacommand.com/' + name, name);
      console.log('mirrored', name);
    } catch (e) { console.error('asset skipped (stays absolute):', name, e.message); }
  }
} catch (e) {
  console.error('live splice failed, using standalone fallback:', e.message);
  page = [
    '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width,initial-scale=1">',
    '<meta name="robots" content="noindex">',
    '<title>LSA Command | Notification Comparison (preview)</title>',
    '<script src="https://cdn.tailwindcss.com"><\/script>',
    "<script>tailwind.config={theme:{extend:{colors:{midnight:'#050505',electric:'#00F5D4',space:'#0a0a0a'}}}}<\/script>",
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">',
    "<style>body{background:#050505;color:#fff;font-family:'Inter',sans-serif}h1,h2,h3,h4{font-family:'Outfit',sans-serif}",
    '.glass{background:rgba(28,37,65,.4);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.1)}',
    '.text-neon{color:#00F5D4}.bg-neon{background-color:#00F5D4}</style></head><body>',
    section,
    '</body></html>',
  ].join('\n');
}

mkdirSync('public', { recursive: true });
writeFileSync('public/index.html', page);
console.log('built public/index.html', page.length, 'bytes');
