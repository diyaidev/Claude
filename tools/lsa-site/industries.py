from template import page, VIDEOS, FEATURES, INDUSTRIES


def features_block():
    return """
<ul>
<li><a href="/lsa-ai-call-answering/"><strong>AI call answering</strong></a>: your team rings first, and AI picks up at 15 seconds so every call is answered inside Google’s 30-second window.</li>
<li><a href="/lsa-message-leads/"><strong>Message lead response</strong></a>: replies in under 30 seconds, verified through the LSA API so none silently drop.</li>
<li><a href="/lsa-lead-disputes/"><strong>Lead feedback and credits</strong></a>: every lead scored and rated back to Google; spam and invalid leads flagged for credit.</li>
<li><a href="/lsa-service-area/"><strong>Service area targeting</strong></a>: the exact cities and zip codes you want, pushed to LSA in seconds, with your live rank on each one.</li>
<li><a href="/lsa-reviews/"><strong>Review generation</strong></a>: AI follow-up after every job and a reply to every review.</li>
</ul>"""


TRADES = [
    dict(
        path="/industries/hvac/", name="HVAC", plural="HVAC companies", video="answering",
        title="Google Local Services Ads for HVAC Companies | LSA Command",
        h1="Google Local Services Ads for HVAC Companies",
        desc="Win more AC and furnace repair jobs from Google Local Services Ads. LSA Command answers every HVAC lead in under 30 seconds, 24/7, and keeps your LSA ranking strong through heat waves and cold snaps.",
        lede="When the AC dies in July, the homeowner books the first HVAC company that answers. LSA Command makes sure that’s you, day or night, at peak season and at 2 AM.",
        problem="""
<p>HVAC demand comes in spikes. The first real heat wave or cold snap floods every LSA account in your market at once. Those are the days your techs are busiest and your phones are hardest to answer.</p>
<p>Missed calls on those days cost twice: you lose jobs worth hundreds or thousands of dollars, and your responsiveness drops just as Google is deciding who to show first. Emergency no-heat and no-cool calls also come in at night and on weekends, when most offices are closed.</p>""",
        jobs="AC repair, furnace and heat pump repair, new system installs, maintenance plans, and duct work",
        faq_extra=("Should my HVAC company list itself as open 24 hours on LSA?", "If every call and message gets answered, yes. LSA Command’s AI answers nights and weekends, so you can list 24-hour availability and show up for emergency no-heat and no-cool searches when competitors are closed."),
    ),
    dict(
        path="/industries/plumbers/", name="plumbing", plural="plumbers", video="answering",
        title="Google Local Services Ads for Plumbers | LSA Command",
        h1="Google Local Services Ads for Plumbers",
        desc="Turn more Google Local Services Ads leads into plumbing jobs. LSA Command answers every emergency call 24/7, texts you the recording and summary, and flags spam leads for credit.",
        lede="Burst pipes and backed-up drains don’t wait for business hours. LSA Command answers every plumbing lead in under 30 seconds and puts the caller’s details in your hand before you call back.",
        problem="""
<p>Plumbing leads are urgent. A homeowner with water on the floor calls the first two or three listings and books whoever answers. If your crew is under a sink and the call goes to voicemail, that job is gone in minutes.</p>
<p>Plumbers also see plenty of low-value LSA traffic: wrong numbers, sales calls, and spam. Paying for those leads and never rating them back to Google teaches the system nothing.</p>""",
        jobs="emergency leak repair, drain cleaning, water heater repair and replacement, sewer line work, and fixture installs",
        faq_extra=("Can LSA Command tell an emergency plumbing call from a routine one?", "The AI qualifies every caller and captures the problem, address, and urgency. Your alert includes a short summary, so you can see right away whether it’s a burst pipe or a quote request. Hot leads can be warm-transferred to your phone while the caller is still on the line."),
    ),
    dict(
        path="/industries/roofers/", name="roofing", plural="roofers", video="area",
        title="Google Local Services Ads for Roofers | LSA Command",
        h1="Google Local Services Ads for Roofing Contractors",
        desc="Get more roofing jobs from Google Local Services Ads. LSA Command answers every lead while your crews are on roofs, targets the zip codes worth chasing, and builds the reviews homeowners compare.",
        lede="Your crews are on roofs, not by the phone. LSA Command answers every roofing lead, tightens your service area to the neighborhoods worth chasing, and builds the reviews homeowners compare before they call.",
        problem="""
<p>Roofing jobs are high-ticket, so every lost LSA lead hurts. Yet roofing crews are among the hardest to reach: on a roof, on a ladder, or across town doing an inspection.</p>
<p>After a storm, LSA demand jumps across a wide area. Without a deliberate service area, roofers end up paying for leads far outside the neighborhoods they actually want to work. Homeowners comparing roofers also lean heavily on reviews, since they’re trusting someone with a big job.</p>""",
        jobs="roof repair, roof replacement, storm and hail damage inspections, leak repair, and gutter work",
        faq_extra=("How should roofers set their LSA service area?", "Start with the cities and zip codes where your jobs are most profitable and where you can show up for inspections quickly. Proximity is an LSA ranking factor, so far-away areas usually rank lower. LSA Command’s Radius tool builds that list and pushes it to LSA, and the Rank Tracker shows where you appear in each city."),
    ),
    dict(
        path="/industries/electricians/", name="electrical", plural="electricians", video="messages",
        title="Google Local Services Ads for Electricians | LSA Command",
        h1="Google Local Services Ads for Electricians",
        desc="Win more electrical jobs from Google Local Services Ads. LSA Command answers every call and message lead in under 30 seconds, qualifies the job, and keeps your LSA responsiveness at 100%.",
        lede="Electricians get a mix of urgent calls and big planned projects through LSA. LSA Command answers both in under 30 seconds and tells you which is which before you call back.",
        problem="""
<p>Electrical LSA leads range from “half my house has no power” to panel upgrades and EV charger installs. Many homeowners send a message instead of calling, especially for planned work. If those replies are slow, or silently fail to reach them, they move on to the next listing.</p>
<p>Electricians also work in attics, crawlspaces, and on commercial jobs where answering the phone isn’t realistic. That’s where responsiveness slips.</p>""",
        jobs="power outages and troubleshooting, panel upgrades, EV charger installation, lighting, and wiring repairs",
        faq_extra=("Do message leads matter for electricians on LSA?", "Yes, especially for planned projects like panel upgrades and EV chargers, where homeowners often message instead of calling. LSA Command replies in under 30 seconds and checks through the LSA API that each reply actually reached the customer."),
    ),
    dict(
        path="/industries/pool-contractors/", name="pool", plural="pool contractors", video="reviews",
        title="Google Local Services Ads for Pool Contractors | LSA Command",
        h1="Google Local Services Ads for Pool Contractors",
        desc="Proven with real pool companies: LSA Command helps pool builders and pool service companies answer every Google Local Services lead, improve lead quality, and climb the LSA rankings.",
        lede="LSA Command was proven with real pool companies. Advantage Pools, Champion Pools, and Edgewater Pools use it to answer every LSA lead and tighten lead quality.",
        problem="""
<p>Pool leads cover very different jobs: weekly cleaning, green-pool cleanups, equipment repair, and new pool construction worth tens of thousands of dollars. Answering each one quickly, and telling Google which jobs you actually want, decides whether your LSA budget fills the schedule with builds or with one-off cleanings.</p>
<p>Pool demand is also seasonal. The spring opening rush hits every pool company in your area at once.</p>""",
        jobs="pool construction, pool cleaning and maintenance, green-pool cleanups, equipment and pump repair, and resurfacing",
        faq_extra=("Has LSA Command been used by pool companies?", "Yes. Our case studies come from pool contractors, including Advantage Pools, Champion Pools, and Edgewater Pools. <a href=\"/#everything\">See the results on our homepage</a>."),
    ),
]

PAGES = []
for t in TRADES:
    others = [i for i in INDUSTRIES if i[0] != t["path"]]
    sections = [
        (f"Why {t['plural']} lose Google LSA leads", t["problem"]),
        (f"What LSA Command does for {t['plural']}", f"""
<p>LSA Command handles the LSA leads for {t['jobs']}. You get the same system on every lead:</p>
{features_block()}"""),
        ("What you get on every lead", """
<p>Within seconds of every call or message, you get a text and an email with the customer’s number, the call recording, a short AI summary, and the full transcript. Google’s own alert for a phone lead is just an email. You call back already knowing what the job is.</p>"""),
    ]
    faqs = [
        (f"Are Google Local Services Ads worth it for {t['plural']}?", f"LSA puts {t['plural']} at the very top of Google with the Google Verified badge, and you pay per lead instead of per click. It pays off when you answer every lead fast, rate leads back to Google, and keep your service area tight. Those are the areas LSA Command handles."),
        t["faq_extra"],
        ("Is LSA changing in 2026?", "Yes. Google is moving Local Services Ads into Google Ads as a Performance Max campaign type. <a href=\"/blog/google-local-services-ads-performance-max/\">Read what contractors should do now</a>."),
    ]
    PAGES.append((t["path"], page(
        t["path"], t["title"], t["h1"], t["desc"], f"LSA for {t['plural']}",
        [],
        sections, faqs=faqs, video=VIDEOS[t["video"]],
        video_name=f"LSA Command for {t['plural']}",
        related=others[:3] + [FEATURES[0], FEATURES[2]], lede=t["lede"],
    )))
