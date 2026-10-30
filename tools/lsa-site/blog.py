from template import page, FEATURES, INDUSTRIES

POSTS = []

p = "/blog/google-local-services-ads-performance-max/"
POSTS.append(dict(
    path=p, eyebrow="LSA updates", minutes=6,
    h1="Google Local Services Ads Are Moving to Performance Max: What Contractors Should Do Now",
    card="Google is folding LSA into Google Ads as a Performance Max campaign type. Here’s what stays the same, what changes, and the checklist to work through before your account moves.",
    html=page(
        p,
        "LSA Moving to Performance Max: What Contractors Should Do | LSA Command",
        "Google Local Services Ads Are Moving to Performance Max: What Contractors Should Do Now",
        "Google is moving Local Services Ads into Google Ads as a Performance Max campaign type. What stays the same, what changes for bidding and missed calls, and a checklist for contractors.",
        "LSA updates",
        [("Blog", "/blog/")],
        [
            ("What’s happening", """
<p>Google is moving Local Services Ads out of its standalone dashboard and into Google Ads, where LSA becomes a <strong>Performance Max campaign type with a pay-per-lead goal</strong>. Industry coverage says the rollout started in August 2026 with select U.S. advertisers and will expand through 2027. <a href="https://www.invoca.com/blog/googles-local-services-ads-moving-to-performance-max-heres-everything-you-need-to-know">Invoca has a detailed rundown</a>.</p>
<p>Google’s official migration notice in your account is the final word on your timing. Watch for it, and don’t make changes based on rumors.</p>"""),
            ("What stays the same", """
<ul>
<li><strong>You still pay per lead,</strong> not per click.</li>
<li><strong>Ads still show on Search and Maps.</strong> Reports say these campaigns will not expand to YouTube, Gmail, or Display the way standard Performance Max does.</li>
<li><strong>No keywords.</strong> Google still matches you to searches based on your categories, job types, and service area.</li>
<li><strong>Your Google Verified badge carries over.</strong></li>
</ul>"""),
            ("What changes", """
<ul>
<li><strong>Where you manage it.</strong> The standalone LSA dashboard goes away and campaigns are run inside Google Ads.</li>
<li><strong>Bidding.</strong> Manual max-per-lead bids are reported to be replaced by a single campaign-level target cost per lead (Target CPA). You lose fine-grained bid control, so the data you feed Google matters more.</li>
<li><strong>Budgets.</strong> Reports say your historical weekly budget will be converted to a daily average.</li>
<li><strong>Missed calls.</strong> Industry reports say that from October 1, 2026, a missed call during your stated business hours can be charged as a lead if the caller stays on the line for about 20 seconds or more. If that applies to your account, every unanswered call costs you money as well as the job.</li>
<li><strong>Reporting history.</strong> Sources disagree on how much LSA history carries into Google Ads. Export your reports before you migrate.</li>
</ul>"""),
            ("A checklist for contractors", """
<ol>
<li><strong>Export your LSA history now:</strong> leads, charges, credits, and call recordings you rely on.</li>
<li><strong>Answer every call.</strong> If missed calls can be billed, an answering gap becomes a direct cost. LSA Command’s <a href="/lsa-ai-call-answering/">AI call answering</a> rings your team first and picks up at 15 seconds.</li>
<li><strong>Answer every message, and confirm it was delivered.</strong> See how <a href="/lsa-message-leads/">message lead verification</a> catches replies that never reach the customer.</li>
<li><strong>Rate every lead.</strong> With automated bidding, lead feedback is one of the clearest ways to tell Google what a good lead looks like. LSA Command <a href="/lsa-lead-disputes/">rates every lead back to Google</a>.</li>
<li><strong>Track booked jobs, not just leads.</strong> A target cost per lead says nothing about whether the leads became paid work. Measure cost per booked job.</li>
<li><strong>Tighten your service area</strong> before the move, so automated bidding starts from a clean footprint. See <a href="/lsa-service-area/">service area targeting</a>.</li>
</ol>"""),
        ],
        faqs=[
            ("Are Google Local Services Ads going away?", "No. LSA is moving into Google Ads as a Performance Max campaign type. You still pay per lead, and ads still appear on Search and Maps."),
            ("When will my LSA account move to Performance Max?", "Industry reports say the rollout began in August 2026 for select U.S. advertisers and will expand through 2027. Google notifies each advertiser before migrating their account."),
            ("Will I be charged for missed calls?", "Industry reports say that from October 1, 2026, a missed call during stated business hours can be charged as a lead if the caller stays on the line for about 20 seconds or more. Check your account’s current terms."),
        ],
        kind="BlogPosting",
        related=[FEATURES[0], FEATURES[2], ("/blog/how-to-rank-higher-google-local-services-ads/", "How to rank higher in Google Local Services Ads")],
        lede="Google is folding Local Services Ads into Google Ads as a Performance Max campaign type. Here’s what stays the same, what changes, and what to do before your account moves.",
    ),
))

p = "/blog/how-to-rank-higher-google-local-services-ads/"
POSTS.append(dict(
    path=p, eyebrow="LSA ranking", minutes=6,
    h1="How to Rank Higher in Google Local Services Ads",
    card="Google ranks LSA advertisers on proximity, reviews, responsiveness, business hours, and complaints. Here’s what each one means and what you can actually control.",
    html=page(
        p,
        "How to Rank Higher in Google Local Services Ads (2026) | LSA Command",
        "How to Rank Higher in Google Local Services Ads",
        "The Google Local Services Ads ranking factors explained: proximity, reviews, responsiveness, business hours, and complaints, plus what contractors can do to move up.",
        "LSA ranking",
        [("Blog", "/blog/")],
        [
            ("What Google uses to rank LSA advertisers", """
<p>Local Services Ads don’t use keywords or bids per click. Google decides which providers to show, and in what order, using a small set of signals. Its help center lists these as the main ranking factors:</p>
<ul>
<li><strong>Proximity</strong> to the person searching</li>
<li><strong>Review score and number of reviews</strong></li>
<li><strong>Responsiveness</strong> to calls and messages</li>
<li><strong>Business hours</strong></li>
<li><strong>Serious or repeated complaints</strong> about the business</li>
</ul>
<p>Your budget and bid also determine how often you appear. Google’s own <a href="https://support.google.com/localservices/answer/12492201?hl=en">guide to improving LSA performance</a> adds practical tips such as photos and selecting every job type you offer.</p>"""),
            ("1. Responsiveness: the factor you control most", """
<p>Responsiveness is the factor contractors can change fastest. Google says missed calls can hurt it, and slow message replies count too.</p>
<ul>
<li>Answer calls inside 30 seconds, every time. LSA Command’s <a href="/lsa-ai-call-answering/">AI call answering</a> rings your team first and picks up at 15 seconds if nobody answers.</li>
<li>Reply to message leads within minutes, and confirm the reply arrived. <a href="/lsa-message-leads/">10–15% of message replies can silently fail</a>.</li>
<li>Watch your responsiveness score in the dashboard. It’s based on recent performance, so improvements show up quickly.</li>
</ul>"""),
            ("2. Reviews: rating and volume", """
<p>Both your average rating and your review count matter, and homeowners compare them side by side. The fix is consistency: ask after every job, make posting easy, and reply to every review. See how <a href="/lsa-reviews/">automated review follow-up</a> works.</p>"""),
            ("3. Business hours", """
<p>Being open when the customer searches matters. If you can genuinely answer around the clock, listing 24-hour availability lets you appear for night, weekend, and holiday searches when competitors are closed.</p>"""),
            ("4. Proximity and your service area", """
<p>You can’t move your shop, but you can choose where you show up. A focused <a href="/lsa-service-area/">service area</a> keeps your budget on the cities and zip codes where you rank well and win profitable jobs. A rank tracker shows where you actually appear in each city.</p>"""),
            ("5. Lead feedback and complaints", """
<p>Rating every lead tells Google which leads you want. Fixing unhappy customers before they become complaints protects your standing. LSA Command <a href="/lsa-lead-disputes/">rates every lead back to Google</a> and routes unhappy customers to the owner.</p>"""),
        ],
        faqs=[
            ("What is the most important Google LSA ranking factor?", "Google doesn’t publish weights. Proximity, reviews, responsiveness, and business hours all matter. Responsiveness is usually the one a contractor can improve fastest."),
            ("Does answering calls faster improve LSA ranking?", "Google lists responsiveness as a ranking factor and says missed calls can hurt it. Answering every call and message quickly protects that signal."),
            ("Can I pay to rank #1 in Local Services Ads?", "Budget and bid affect how often you appear, but ranking also depends on proximity, reviews, responsiveness, and hours. No one can guarantee the top spot."),
        ],
        kind="BlogPosting",
        related=[FEATURES[0], FEATURES[4], ("/blog/google-local-services-ads-performance-max/", "LSA is moving to Performance Max: what to do now")],
        lede="Google ranks Local Services Ads on a handful of signals. Here’s what each one means, which ones you control, and how to move up.",
    ),
))
