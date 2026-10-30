from template import page, VIDEOS, FEATURES, INDUSTRIES

PMAX = '<a href="/blog/google-local-services-ads-performance-max/">LSA’s move into Performance Max</a>'
RANK = '<a href="/blog/how-to-rank-higher-google-local-services-ads/">how LSA ranking works</a>'


def others(path):
    return [f for f in FEATURES if f[0] != path][:3] + [INDUSTRIES[0], INDUSTRIES[1]]


PAGES = []

# ---------------------------------------------------------------- AI answering
p = "/lsa-ai-call-answering/"
PAGES.append((p, page(
    p,
    "AI Answering Service for Google Local Services Ads | LSA Command",
    "AI Answering Service for Google Local Services Ads",
    "Answer 100% of your Google LSA calls. Your team rings first, and AI picks up at 15 seconds to qualify, book, and alert you with the recording, summary, and transcript.",
    "AI call answering",
    [],
    [
        ("Why missed LSA calls cost more than one job", """
<p>Every Google Local Services Ads call is a lead you paid for. When nobody picks up, you lose that customer, and you also hurt the <strong>responsiveness</strong> signal Google uses to rank LSA advertisers. Google says plainly that missed calls can hurt responsiveness.</p>
<p>Contractors miss calls for normal reasons: the crew is on a roof, the office is on another line, or it’s 9 PM on a Sunday. A generic answering service or voicemail doesn’t fix the ranking problem. It also doesn’t give you what you need to call the customer back quickly.</p>
<p>The stakes are going up. As LSA moves into Google Ads, industry reports say a missed call during your business hours can now be charged as a lead if the caller stays on the line long enough. Read our guide to """ + PMAX + """ for details.</p>"""),
        ("How LSA Command answers every call: humans first, AI always", """
<ol>
<li><strong>0–15 seconds: your team gets first shot.</strong> Every LSA call rings your phones first. If someone answers, it’s a normal call and the AI stays out of the way.</li>
<li><strong>At 15 seconds: AI picks up.</strong> If nobody answers (busy, on a job, after hours), the LSA Command AI answers on the spot. It qualifies the caller, captures the job details, and books the job or warm-transfers a hot lead to your phone while the caller is still on the line.</li>
<li><strong>Inside 30 seconds: Google sees the call answered.</strong> Every call is answered inside Google’s 30-second window, so your response rate stays at 100%.</li>
<li><strong>Instantly: you get the full picture.</strong> A text and an email hit your phone with the caller’s number, the call recording, a five-second AI summary, and the full transcript. Google’s own alert for a phone lead is just an email with no recording or transcript.</li>
</ol>"""),
        ("Robocalls never reach your phone", """
<p>Paid LSA numbers attract spam. LSA Command runs a three-layer defense that stops robocalls before your phone rings and counts every block in your dashboard. Your team spends its time on real customers.</p>"""),
        ("Open 24 hours, without a night shift", """
<p>Because every call and message is answered, you can list your business as <strong>Open 24 Hours</strong> in LSA. Being “open now” when competitors are closed earns you placement at nights, on weekends and on holidays. Those are often the searches where homeowners have an urgent problem and will book whoever answers.</p>"""),
    ],
    faqs=[
        ("Will the AI answer calls my team could have taken?", "No. Every call rings your team first for 15 seconds. The AI only answers when no one picks up."),
        ("Does answering every call improve my Google LSA ranking?", "Responsiveness is one of the factors Google uses to rank Local Services Ads, and Google says missed calls can hurt it. Answering every call within 30 seconds protects that signal. Ranking also depends on proximity, reviews, and business hours, so no tool can promise a specific position."),
        ("What do I receive after the AI handles a call?", "A text and an email with the caller’s number, the call recording, an AI summary, and the full transcript, so you can call back already knowing what the customer needs."),
        ("Can the AI transfer a hot lead to me?", "Yes. Qualified callers can be warm-transferred straight to your phone while they’re still on the line."),
    ],
    video=VIDEOS["answering"], video_name="LSA Command AI call answering for Google Local Services Ads",
    related=others(p),
    lede="Your team rings first. If nobody picks up in 15 seconds, AI answers, qualifies the caller, and texts you the recording, summary, and transcript, so every paid LSA call is answered inside Google’s 30-second window.",
)))

# ---------------------------------------------------------------- Message leads
p = "/lsa-message-leads/"
PAGES.append((p, page(
    p,
    "Never Miss a Google LSA Message Lead | LSA Command",
    "Answer 100% of Your Google LSA Message Leads",
    "10–15% of replies to Google Local Services message leads never reach the customer. LSA Command verifies every reply through the LSA API and re-sends anything that drops.",
    "Message lead response",
    [],
    [
        ("The hidden problem with LSA message leads", """
<p>When a homeowner messages you through Google Local Services Ads, your reply goes back to Google over SMS. Your phone, or any off-the-shelf AI agent, shows the reply as “delivered.”</p>
<p>But in the accounts we audit, <strong>10–15% of those replies never land in the LSA lead thread</strong> and never reach the customer. This happens to replies from people and from generic AI bots alike. The only way to see it is to log into LSA and open each lead, so most businesses never find out.</p>
<p>Every dropped reply is a paid lead that went cold. It also counts against your responsiveness, which is part of """ + RANK + """.</p>"""),
        ("How the LSA API fallback works", """
<ol>
<li><strong>Reply fast.</strong> LSA Command’s AI answers new message leads in under 30 seconds, day or night. You can also reply yourself; you’re backed up either way.</li>
<li><strong>Verify the thread.</strong> Because LSA Command is built on the LSA API, it checks the actual lead thread after every reply, not just the SMS delivery receipt.</li>
<li><strong>Force it through.</strong> If a reply hasn’t landed within minutes, LSA Command pushes it into the thread through the API.</li>
<li><strong>Count it.</strong> Every recovered message appears in your dashboard as an exact count, not an estimate.</li>
</ol>"""),
        ("Protect the “replies in minutes” badge", """
<p>Fast, consistent replies help earn Google’s <em>“typically replies in minutes”</em> label on your listing. Slow ones can show customers that you reply in hours instead. A 90% response rate and a 100% response rate look similar on paper, but the gap is real paid leads that never got a reply.</p>"""),
    ],
    faqs=[
        ("Why would a reply to an LSA message lead not be delivered?", "Replies travel back to Google over an SMS bridge. A share of them never reach the LSA thread even though your phone shows them as delivered. Without checking the thread through the LSA API, there’s no way to know."),
        ("Do I have to let the AI answer my messages?", "No. You can answer messages yourself and LSA Command will still verify that every reply reached the customer, re-sending any that drop."),
        ("How fast does LSA Command reply to a new message lead?", "The AI replies in under 30 seconds, 24 hours a day."),
    ],
    video=VIDEOS["messages"], video_name="LSA Command message lead fallback for Google Local Services Ads",
    related=others(p),
    lede="Your phone says “delivered,” but 10–15% of replies to LSA message leads never reach the customer. LSA Command checks every thread through the LSA API and re-sends anything that drops.",
)))

# ---------------------------------------------------------------- Disputes
p = "/lsa-lead-disputes/"
PAGES.append((p, page(
    p,
    "How to Dispute Google LSA Leads & Get Credits | LSA Command",
    "Google LSA Lead Disputes, Credits, and Lead Feedback on Autopilot",
    "Stop paying for spam and wrong-number LSA leads. LSA Command scores every lead, sends lead feedback to Google, and tracks every credit so you can see what you got back.",
    "Lead disputes & credits",
    [],
    [
        ("How LSA lead credits work now", """
<p>Google used to let advertisers dispute charged leads by hand. It has since moved most of that to an <strong>automated lead-credit system</strong>. Google reviews leads itself and credits the ones it decides are invalid. Advertisers are asked to rate every lead through lead feedback.</p>
<p>Two things matter for contractors:</p>
<ul>
<li><strong>Not every bad lead qualifies for a credit.</strong> Google’s current guidance says it no longer gives credits for “job type not serviced” or “geo not serviced” leads, and it lists category and regional exclusions. A lead can be a poor fit and still be billable. <a href="https://support.google.com/localservices/answer/15100654?hl=en">Read Google’s lead-credit guidance</a>.</li>
<li><strong>Feedback trains the system.</strong> The ratings you send back help Google learn which leads you actually want, so the more consistently you rate leads, the better.</li>
</ul>"""),
        ("What LSA Command does with every lead", """
<ol>
<li><strong>Reviews every call and message.</strong> The AI listens to each call and reads each message, then scores lead quality from 1 to 5.</li>
<li><strong>Flags credit-eligible leads.</strong> Spam, robocalls, wrong numbers and other leads that fit Google’s credit rules are flagged automatically.</li>
<li><strong>Sends lead feedback to Google.</strong> Every lead gets rated back to Google, so it can send you more of the jobs you want.</li>
<li><strong>Tracks credits, not guesses.</strong> Your dashboard keeps three things separate: our assessment, the feedback that was submitted, and the credit Google actually recorded. A credit only counts once Google records it.</li>
</ol>
<p>On the homepage you can see a real month from our dashboard: 206 leads monitored and $110.64 refunded. Your numbers will depend on your trade, market and lead mix.</p>"""),
        ("Fewer bad leads in the first place", """
<p>Credits fix past charges; a tighter setup prevents future ones. LSA Command pairs lead feedback with <a href="/lsa-service-area/">service area targeting</a>, so you stop showing up in zip codes and job types you don’t serve.</p>"""),
    ],
    faqs=[
        ("Can I still dispute a Google LSA lead manually?", "Google has moved most lead disputes to an automated credit system and asks advertisers to rate leads through lead feedback. Check your account’s current options, since Google has changed this process several times."),
        ("Which LSA leads qualify for a credit?", "Generally spam, robocalls, and other invalid leads under Google’s policy. Google’s current guidance says it no longer credits “job type not serviced” or “geo not serviced” leads, so a poor-fit lead isn’t always refundable."),
        ("How does LSA Command know which leads are bad?", "The AI reviews every call recording and message, scores lead quality from 1 to 5, and flags leads that match Google’s credit rules."),
        ("Will LSA Command show credits that Google hasn’t approved?", "No. Credits are tracked separately from our assessment and from submitted feedback. A credit appears as recovered only once Google records it."),
    ],
    video=VIDEOS["disputes"], video_name="LSA Command automated lead disputes and credits",
    related=others(p),
    lede="LSA Command reviews every Google Local Services lead, flags the ones that qualify for a credit, rates every lead back to Google, and tracks what you actually get refunded.",
)))

# ---------------------------------------------------------------- Service area
p = "/lsa-service-area/"
PAGES.append((p, page(
    p,
    "Google LSA Service Area Targeting by City & Zip Code | LSA Command",
    "Google LSA Service Area Targeting by City, County & Zip Code",
    "Choose every profitable city, county, and zip code for your Google Local Services Ads, push it to LSA in seconds, and track your live LSA rank on every city you serve.",
    "Service area targeting",
    [],
    [
        ("Why your LSA service area decides your lead quality", """
<p>Google shows Local Services Ads to people searching inside the areas you choose, and closeness to the customer is one of the main ranking factors. If your area is too small, you miss profitable jobs. If it’s too loose, you pay for leads 50 minutes away.</p>
<p>Setting it up by hand in the LSA dashboard is slow, especially for contractors who serve dozens of towns. Many accounts end up with duplicate areas, missing suburbs, or old zones nobody remembers adding.</p>"""),
        ("Build the exact footprint you want", """
<ul>
<li><strong>Find every profitable area.</strong> The Radius tool lists every city, county, and zip code in your region so you can include the ones you want and exclude the ones you don’t.</li>
<li><strong>Clean up duplicates.</strong> Overlapping and duplicate areas are found and removed in one click.</li>
<li><strong>Push it to LSA instantly.</strong> No manual entry. Your finished service area uploads straight to your Google LSA account through the API.</li>
<li><strong>See what each change produced.</strong> Every radius change is logged and compared against lead volume, so you know whether an expansion actually paid off.</li>
</ul>"""),
        ("Your real LSA rank on every city you serve", """
<p>The LSA Command Rank Tracker drops a numbered pin on each city in your service area, showing your live Local Services position there for your main keyword. Your home base is tracked weekly and your whole area monthly. Rank-over-time charts show whether faster response and more reviews are moving you up.</p>"""),
    ],
    faqs=[
        ("Can I target specific zip codes in Google Local Services Ads?", "Yes. LSA lets you choose service areas by city, county, and zip code. LSA Command makes it fast to build that list and push it to your account."),
        ("Will a bigger service area get me more LSA leads?", "It can, but proximity is a ranking factor, so far-away areas usually rank lower and may bring poorer-fit jobs. The goal is the most profitable footprint, not the biggest one."),
        ("How do I know where I rank in each city?", "The LSA Command Rank Tracker shows your live LSA position on every city in your service area, tracked on your main keyword."),
    ],
    video=VIDEOS["area"], video_name="LSA Command service area targeting for Google Local Services Ads",
    related=others(p),
    lede="Pick every profitable city, county, and zip code, push it to Google Local Services Ads in seconds, and see your live LSA rank pinned on every city you serve.",
)))

# ---------------------------------------------------------------- Reviews
p = "/lsa-reviews/"
PAGES.append((p, page(
    p,
    "How to Get More Google LSA Reviews Automatically | LSA Command",
    "Get More Google LSA Reviews, Automatically",
    "Reviews are a Google Local Services Ads ranking factor. LSA Command follows up after every job by call or text, helps customers write the review, and answers every review for you.",
    "Review generation",
    [],
    [
        ("Why reviews matter so much in LSA", """
<p>Your review rating and review count are among the main things Google uses to rank Local Services Ads, alongside proximity, responsiveness, and business hours. They’re also what homeowners compare first when three providers show up side by side.</p>
<p>Most contractors know this and still don’t ask consistently. The crew forgets, the office is busy, and a generic review-request blast gets ignored.</p>"""),
        ("A real conversation, not a review blast", """
<ol>
<li><strong>AI follows up after the job</strong> by phone call or text and asks how it went, like a good office manager would.</li>
<li><strong>It drafts the review with the customer.</strong> Based on what they said, the AI suggests a review they can post as-is or edit.</li>
<li><strong>It sends the link while they’re still engaged.</strong> The suggested review and your Google review link arrive by text during the conversation.</li>
<li><strong>Unhappy customers go to the owner.</strong> If someone had a bad experience, the conversation is routed to you for a personal fix before it turns into a public review.</li>
</ol>"""),
        ("Every review answered for you", """
<p>When reviews come in, LSA Command replies to each one under your business name with a quick, professional response. That shows future customers you’re paying attention and keeps your profile active.</p>"""),
    ],
    faqs=[
        ("Do reviews affect Google LSA ranking?", "Yes. Google lists review score and the number of reviews among the factors that affect Local Services Ads ranking."),
        ("Is it OK for the AI to suggest review text?", "The AI drafts a review based on what the customer actually said, and the customer decides whether to post it, edit it, or write their own."),
        ("What happens if a customer is unhappy?", "The conversation is routed to the owner so the problem can be fixed personally."),
    ],
    video=VIDEOS["reviews"], video_name="LSA Command automated Google LSA review generation",
    related=others(p),
    lede="LSA Command follows up after every job by call or text, helps customers write a review while the job is fresh, sends your Google link, and answers every review for you.",
)))
