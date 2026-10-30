from template import page, FEATURES

POSTS = []


def post(path, h1, title, desc, cat, minutes, card, lede, sections, faqs, related):
    POSTS.append(dict(path=path, eyebrow=cat, minutes=minutes, h1=h1, card=card, html=page(
        path, title, h1, desc, cat, [("Blog", "/blog/")], sections, faqs=faqs,
        kind="BlogPosting", related=related, lede=lede)))


RANK = ("/blog/how-to-rank-higher-google-local-services-ads/", "How to rank higher in Google Local Services Ads")
PMAX = ("/blog/google-local-services-ads-performance-max/", "LSA is moving to Performance Max: what to do now")

post("/blog/google-local-services-ads-cost/",
     "How Much Do Google Local Services Ads Cost?",
     "How Much Do Google Local Services Ads Cost? (2026 Guide) | LSA Command",
     "What Google Local Services Ads cost per lead in 2026, what drives the price up or down, and why cost per booked job is the number contractors should track.",
     "Contractor guides", 6,
     "LSA charges per lead, not per click. Here’s what drives the price, what recent benchmarks show by trade, and the number that matters more than cost per lead.",
     "You pay per lead, not per click, but the price per lead varies widely by trade and market. Here’s what drives it and how to judge whether LSA is working.",
     [
         ("How LSA pricing works", """
<p>Google Local Services Ads charge per lead: a call, message, or booking request from a potential customer that’s related to your services. You don’t pay for clicks or impressions. You set a budget, and Google decides how many leads you get within it.</p>
<p>Google doesn’t publish a price list. Lead cost depends on your trade, your location, the type of job, the lead type, and how many other businesses are competing in your area. As LSA moves into Performance Max, bidding shifts to a campaign-level target cost per lead. <a href="/blog/google-local-services-ads-performance-max/">See what’s changing</a>.</p>"""),
         ("What recent benchmarks show", """
<p>Industry studies put the average home-services LSA lead somewhere around <strong>$50–$65</strong> in 2026. One study of roughly 1,000 home-services businesses reported about $63 per unique lead. Trade ranges reported by agencies look roughly like this:</p>
<ul>
<li><strong>Plumbing:</strong> often among the priciest of the everyday trades, around $35–$70 per lead</li>
<li><strong>HVAC:</strong> around $30–$70 per lead</li>
<li><strong>Electrical:</strong> around $40–$75 per lead</li>
<li><strong>Roofing and remodeling:</strong> much higher, often in the hundreds per lead</li>
</ul>
<p>Treat these as directional. They come from agencies and vendors with different samples and methods, and your market can be well above or below them. Sources: <a href="https://thevalleymarketinggroup.com/blog/google-local-services-ads-cost-per-lead-2026/">Valley Marketing Group</a>, <a href="https://www.webfx.com/blog/ppc/google-lsa-cost/">WebFX</a>.</p>"""),
         ("Track cost per booked job, not cost per lead", """
<p>A cheap lead nobody answers is expensive. A $60 lead that books 40% of the time costs $150 per booked job; the same lead booking 20% of the time costs $300. That’s why the biggest levers on LSA cost are usually <em>after</em> the lead arrives:</p>
<ul>
<li><strong>Answer every call and message.</strong> Unanswered leads are pure waste, and as LSA moves into Google Ads, some missed calls during business hours may be billed. <a href="/lsa-ai-call-answering/">AI call answering</a> closes that gap.</li>
<li><strong>Get credits for invalid leads.</strong> Spam and other invalid leads can be credited back. <a href="/lsa-lead-disputes/">See how lead credits work now</a>.</li>
<li><strong>Rate every lead.</strong> Lead feedback teaches Google which leads you want.</li>
<li><strong>Tighten your service area and job types</strong> so you aren’t paying for work you don’t want. See <a href="/lsa-service-area/">service area targeting</a>.</li>
</ul>"""),
     ],
     [("How much does a Google LSA lead cost?", "It varies by trade and market. Recent industry benchmarks put the average home-services lead around $50–$65, with roofing and remodeling much higher. Google doesn’t publish fixed prices."),
      ("Do I pay for clicks on Local Services Ads?", "No. LSA charges per lead (a call, message, or booking request related to your services), not per click."),
      ("Can I get money back for bad LSA leads?", "Invalid leads such as spam can be credited under Google’s lead-credit rules. Poor-fit leads aren’t always eligible.")],
     [FEATURES[2], FEATURES[0], RANK])

post("/blog/google-verified-badge/",
     "Google Verified Badge: What Replaced Google Guaranteed on Local Services Ads",
     "Google Verified Badge: What Replaced Google Guaranteed | LSA Command",
     "Google Guaranteed and Google Screened were folded into one Google Verified badge on Local Services Ads. What changed, what’s required, and what contractors should update.",
     "LSA updates", 4,
     "Google Guaranteed, Google Screened, and License Verified became one Google Verified badge, and the money-back guarantee ended. Here’s what that means for your LSA listing.",
     "The Google Guaranteed and Google Screened badges are gone. Local Services Ads now show a single Google Verified badge, and the customer money-back guarantee has ended.",
     [
         ("What changed", """
<p>Starting in October 2025, Google consolidated its Local Services Ads badges, <strong>Google Guaranteed</strong>, <strong>Google Screened</strong>, and <strong>License Verified by Google</strong>, into one badge: <strong>Google Verified</strong>. <a href="https://www.searchenginejournal.com/google-confirms-new-google-verified-badge-for-local-services-ads/554360/">Search Engine Journal covered the announcement</a>.</p>
<p>The biggest practical change: the <strong>Google Guarantee money-back program ended</strong>. Reports say customers could only claim for jobs booked through LSA before December 7, 2025. Google has said the change doesn’t affect LSA ranking.</p>"""),
         ("What it takes to get the badge", """
<p>The badge shows that a business completed Google’s verification checks for its category and location. Depending on your trade and area, those can include background checks, license verification, and insurance. Businesses that already completed verification received the badge automatically; new advertisers get it once verification is complete.</p>
<p>Keep your documents current. Expired licenses or insurance can cost you the badge and your eligibility to run LSA.</p>"""),
         ("What contractors should update", """
<ul>
<li><strong>Your marketing.</strong> Remove “Google Guaranteed” or “Google Screened” claims from your website, trucks, and ads, and don’t promise customers Google’s money-back guarantee.</li>
<li><strong>Your verification documents.</strong> Set reminders before licenses and insurance expire.</li>
<li><strong>What actually ranks you.</strong> The badge gets you in. Responsiveness, reviews, proximity, and hours decide where you show. <a href="/blog/how-to-rank-higher-google-local-services-ads/">Here’s how ranking works</a>.</li>
</ul>"""),
     ],
     [("Is Google Guaranteed still available?", "No. Google Guaranteed, Google Screened, and License Verified by Google were consolidated into the Google Verified badge starting in October 2025, and the money-back guarantee ended."),
      ("Does the Google Verified badge affect LSA ranking?", "Google has said the badge change doesn’t affect ranking. Ranking still depends on proximity, reviews, responsiveness, business hours, and complaints."),
      ("How do I get the Google Verified badge?", "Complete Google’s LSA verification for your category and location, which can include background checks, license verification, and insurance.")],
     [RANK, PMAX, FEATURES[4]])

post("/blog/local-services-ads-vs-google-ads/",
     "Local Services Ads vs. Google Search Ads: Which Should Contractors Use?",
     "Local Services Ads vs. Google Ads for Contractors | LSA Command",
     "Google Local Services Ads vs. Google Search Ads for contractors: how pricing, placement, control, and lead handling compare, and when to run both.",
     "Contractor guides", 5,
     "Pay per lead or pay per click? A plain-English comparison of LSA and Google Search Ads for home service businesses, and when running both makes sense.",
     "Both put you at the top of Google, but they work very differently. Here’s how Local Services Ads and Google Search Ads compare for home service businesses.",
     [
         ("The short version", """
<table class="compare"><thead><tr><th></th><th>Local Services Ads</th><th>Google Search Ads</th></tr></thead><tbody>
<tr><td>You pay for</td><td>Leads (calls, messages, bookings)</td><td>Clicks</td></tr>
<tr><td>Placement</td><td>Very top of results, with the Google Verified badge</td><td>Top and bottom of results</td></tr>
<tr><td>Targeting</td><td>Categories, job types, service area; no keywords</td><td>Keywords, locations, audiences</td></tr>
<tr><td>Landing page</td><td>Your LSA profile</td><td>Your website</td></tr>
<tr><td>Ranking signals</td><td>Proximity, reviews, responsiveness, hours, budget</td><td>Bid, ad and landing-page quality</td></tr>
</tbody></table>"""),
         ("When LSA wins", """
<p>LSA usually wins for urgent, local, phone-first jobs such as a broken AC, a burst pipe, or a roof leak. The homeowner sees reviews and the Google Verified badge, then calls directly. You only pay when a lead comes in, and invalid leads can be credited.</p>
<p>The catch: you have less control. You can’t pick keywords or write ad copy, and ranking depends heavily on how fast you answer. Businesses that miss calls slide down. <a href="/blog/how-to-rank-higher-google-local-services-ads/">See how LSA ranking works</a>.</p>"""),
         ("When Search Ads win", """
<p>Search Ads give you control: specific keywords, custom landing pages, and your own messaging. They’re useful for high-ticket planned projects, services LSA doesn’t cover, and capturing searches outside your LSA categories. You pay for every click, though, whether or not it turns into a lead.</p>"""),
         ("Most contractors should run both, and answer everything", """
<p>LSA and Search Ads cover different parts of the same search results page. Running both lets you appear twice. Either way, the money is made or lost when the lead arrives. Every unanswered call or slow text reply wastes spend on either channel. LSA Command makes sure <a href="/lsa-ai-call-answering/">every LSA call</a> and <a href="/lsa-message-leads/">every message</a> gets answered.</p>"""),
     ],
     [("Are Local Services Ads cheaper than Google Ads?", "It depends on your trade and market. LSA charges per lead instead of per click, which often makes lead cost more predictable, but the real comparison is cost per booked job."),
      ("Can I run Local Services Ads and Google Ads at the same time?", "Yes. They appear in different places on the results page, and many contractors run both. LSA is also moving into Google Ads as a Performance Max campaign type."),
      ("Do Local Services Ads use keywords?", "No. LSA matches you to searches based on your business category, job types, and service area.")],
     [PMAX, FEATURES[0], ("/blog/google-local-services-ads-cost/", "How much do Google Local Services Ads cost?")])

post("/blog/lsa-lead-notifications/",
     "How to Get Google LSA Lead Notifications (Now That the App Is Gone)",
     "How to Get Google LSA Lead Notifications by Text | LSA Command",
     "Google retired the Local Services Ads app, and phone-lead alerts now come by email only. How to get instant LSA lead alerts by text with the recording, summary, and transcript.",
     "Contractor guides", 4,
     "With the LSA app retired, Google’s alert for a phone lead is an email. Here’s why that costs jobs and how to get instant text alerts with the full call details.",
     "Google retired the Local Services Ads mobile app in January 2025. For a phone lead, its only alert now is an email. Here’s why that’s a problem and how to fix it.",
     [
         ("What Google sends you today", """
<p>Since the LSA app was retired in January 2025, Google’s notification for a phone lead is an email. There’s no text message, no call recording, no summary, and no transcript. To see details, you log into the dashboard.</p>
<p>Email is a leaky channel. Industry benchmarks suggest roughly one in six legitimate emails never reaches the inbox, and a contractor on a job site isn’t watching email anyway. In the LSA accounts we audit, <strong>10–15% of paid leads routinely show no owner response at all</strong>, usually because the only alert was an email nobody saw.</p>"""),
         ("What a useful lead alert includes", """
<ul>
<li><strong>A text message,</strong> the same second the lead comes in, to you and anyone on your team</li>
<li><strong>The customer’s number,</strong> one tap to call back (including the extension Google assigns on message leads)</li>
<li><strong>The call recording,</strong> so you hear exactly what was said</li>
<li><strong>A short AI summary</strong> of what the customer wants, plus the full transcript</li>
<li><strong>A takeover link</strong> to jump into a live message conversation yourself</li>
</ul>
<p>That’s what LSA Command sends on every call, message, and web-chat lead. You call back in minutes, already knowing the job.</p>"""),
         ("Faster callbacks, better ranking", """
<p>Speed matters twice in LSA: the first business to respond usually wins the job, and responsiveness is a ranking factor. Pair instant alerts with <a href="/lsa-ai-call-answering/">AI call answering</a> so leads are handled even when nobody can pick up.</p>"""),
     ],
     [("Is there still a Google Local Services Ads app?", "Google retired the standalone LSA mobile app in January 2025. Phone-lead notifications now come by email."),
      ("Can I get LSA lead alerts by text message?", "Not from Google directly for phone leads. LSA Command texts and emails you instantly for every lead, with the caller’s number, recording, AI summary, and transcript.")],
     [FEATURES[0], FEATURES[1], RANK])

post("/blog/bad-google-lsa-leads/",
     "Why You’re Getting Bad Google LSA Leads (and How to Fix It)",
     "Why You’re Getting Bad Google LSA Leads and How to Fix It | LSA Command",
     "Spam, wrong numbers, out-of-area calls, and jobs you don’t do: the common causes of bad Google Local Services Ads leads and the fixes that actually work.",
     "Contractor guides", 5,
     "Spam, wrong numbers, jobs you don’t do, and calls from 50 miles away. The usual causes of bad LSA leads, which ones Google will credit, and how to prevent the rest.",
     "Most bad LSA leads come from a handful of fixable causes. Here’s how to find yours, which ones Google will credit, and how to stop paying for the rest.",
     [
         ("The usual suspects", """
<ul>
<li><strong>Spam and robocalls.</strong> Paid numbers attract them. These are typically eligible for a credit.</li>
<li><strong>Wrong job types.</strong> If your profile lists services you don’t want, Google sends those leads. Google’s current guidance says it no longer credits “job type not serviced” leads, so fix this in your settings.</li>
<li><strong>Too-wide service area.</strong> Leads from towns you won’t drive to. Google also no longer credits “geo not serviced” leads.</li>
<li><strong>Price shoppers and tire-kickers.</strong> Real leads, poor fit. Not refundable, but lead feedback helps Google send fewer.</li>
</ul>
<p>Source: <a href="https://support.google.com/localservices/answer/15100654?hl=en">Google’s lead-credit guidance</a>.</p>"""),
         ("Fix the settings first", """
<ol>
<li><strong>Audit your job types.</strong> Turn off every service you don’t want more of.</li>
<li><strong>Rebuild your service area</strong> around the cities and zip codes where you’re profitable. <a href="/lsa-service-area/">LSA Command’s Radius tool</a> does this and pushes it to LSA.</li>
<li><strong>Block robocalls</strong> before they reach your phone. LSA Command uses a three-layer filter.</li>
</ol>"""),
         ("Then train Google with feedback", """
<p>Rate every lead. Feedback is how Google learns which leads you want. LSA Command <a href="/lsa-lead-disputes/">scores every lead 1–5, rates it back to Google, and flags credit-eligible leads</a>, then tracks the credits Google actually records.</p>"""),
         ("Don’t mistake a missed lead for a bad lead", """
<p>Some leads look bad because nobody answered them in time. The customer called someone else. Check your answer rate before blaming lead quality. <a href="/lsa-ai-call-answering/">Answering every call</a> often improves your “lead quality” overnight.</p>"""),
     ],
     [("Does Google refund bad LSA leads?", "Google credits invalid leads, such as spam, under its lead-credit rules. Its current guidance says it no longer credits “job type not serviced” or “geo not serviced” leads, so fix those in your settings."),
      ("How do I stop getting LSA leads outside my area?", "Tighten your service area to the cities and zip codes you actually serve. Proximity is also a ranking factor, so a focused area usually ranks better.")],
     [FEATURES[2], FEATURES[3], ("/blog/google-local-services-ads-cost/", "How much do Google Local Services Ads cost?")])

post("/blog/respond-to-google-lsa-message-leads/",
     "How to Respond to Google LSA Message Leads (and Make Sure the Reply Arrives)",
     "How to Respond to Google LSA Message Leads | LSA Command",
     "Best practices for Google Local Services Ads message leads: reply speed, what to say, earning the replies-in-minutes badge, and why some replies never reach the customer.",
     "Contractor guides", 4,
     "Message leads are a growing share of LSA volume. Here’s how fast to reply, what to say, and how to catch the replies that silently never arrive.",
     "Message leads are a growing share of LSA volume, and they’re judged on speed. Here’s how to reply, and how to make sure your reply actually reaches the customer.",
     [
         ("Reply in minutes, not hours", """
<p>Homeowners message several businesses at once. The first useful reply usually wins. Fast replies also help earn Google’s “typically replies in minutes” label and protect your responsiveness score, which is part of <a href="/blog/how-to-rank-higher-google-local-services-ads/">how LSA ranks you</a>.</p>"""),
         ("What a good first reply includes", """
<ol>
<li>Thank them and confirm the job (“Sounds like your AC is blowing warm air”).</li>
<li>Ask the one or two questions you need to quote or schedule.</li>
<li>Offer a specific next step: a call, a time slot, or a visit.</li>
<li>Include a direct number to reach you.</li>
</ol>"""),
         ("The problem nobody sees: replies that never arrive", """
<p>LSA message replies travel back to Google over SMS. Your phone shows them as delivered, but in the accounts we audit, <strong>10–15% never land in the LSA thread</strong>. The customer never sees them and assumes you ignored them. The only way to catch this is to check each lead thread.</p>
<p>LSA Command <a href="/lsa-message-leads/">replies in under 30 seconds and verifies every reply through the LSA API</a>, re-sending any that drop, whether the AI or your team wrote it.</p>"""),
     ],
     [("How fast should I reply to an LSA message lead?", "Within minutes. Homeowners message several providers at once, and responsiveness is an LSA ranking factor."),
      ("Why didn’t my customer get my LSA message reply?", "Replies travel back to Google over SMS, and a share of them never reach the LSA thread even when your phone shows them as delivered. Check the thread in LSA, or use a tool that verifies delivery through the LSA API.")],
     [FEATURES[1], FEATURES[0], ("/blog/lsa-lead-notifications/", "How to get Google LSA lead notifications")])
