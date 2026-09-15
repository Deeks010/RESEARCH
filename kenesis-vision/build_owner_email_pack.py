from pathlib import Path
import json,html,re
from collections import Counter
P=Path(__file__).parent
def read(n):return json.loads((P/n).read_text(encoding='utf-8-sig'))
def esc(x):return html.escape(str(x or 'Not verified'))
rows=read('Kenesis-Owner-Led-50.json')['companies']
local=[r for r in rows if r['geography']=='Chennai metro'][13:]
extra={
'J-Tech Instruments':('https://www.jtechinstruments.in/contact','General company contact. Institutional syllabus independently names J. John Wesily as proprietor; no separately assigned owner email established.'),
'Saravana Bhava Fabricators (SB Fabricators)':('https://sbfabs.com/','Official general inbox; proprietor named separately.'),
'Sriram Industries':('https://www.sriram-industries.com/contact.htm','Published email belongs to finance/commercial head M. Rajendran, not proprietor M. Nagarajan. Useful route, not owner-direct.'),
'Dhruv Comfort Seating':('https://www.dhruvcomfortseating.net/','Founder Sunil Arya and general business inbox published; no owner-specific assignment.'),
'Ford Packaging':('https://www.fordpackaging.co.in/about.html','Proprietor named in profile; email is general business contact.'),
'R S Manufacturing':('https://sites.google.com/rsmanufacturing.in/rsmanufacturing/about-us','Siva is explicitly assigned this email. Prose links supervision and proprietor experience ambiguously; legal ownership remains uncertain.'),
'VRM Polymers':('https://www.vrmpolymers.com/','Official business inbox; no separate owner mailbox established.'),
'Shahi Foods':('https://www.shahifoodproducts.com/contact-us.html','Three general inboxes published. Factory address now verified: Plot 16, K.R.C. Nagar, Uthukottai 602026. No owner-specific email found.'),
'Base Electrical Engineering':('https://www.baseelectricalengg.com/about.html','Magudapathi P named as proprietor; email is shared business contact.'),
'JP Electricals':('https://jpelectricals.co.in/','General business contact; no separate A. Anthony address established.'),
'Paramasivam Kitchen Equipments':('https://www.paramasivamkitchenequipments.com/contact-us/','Official proprietor Babu and business email route; mailbox assignment not explicit. Address differs in secondary GST listing; confirm before visit.'),
'CHIK / Designs Factory':('https://mychik.co.in/pages/about-us','Founders publish this address beneath their signed message. Treated as founder-associated shared business inbox, not individually verified owner mailbox. Page claims 2–3 daily orders; wholesale/total factory volume unknown.'),
'Harshal Printing & Packaging':('https://gurunanakcollege.edu.in/files-new/dvv/criterion-1/1.3.4-projects-commerce.pdf','2021 company letterhead signed by proprietor gives general email. Current owner mailbox not found. Similar HPPL interview not merged without entity linkage.')}
localout=[]
for r in local:
    url,evidence=extra[r['name']]
    localout.append(dict(name=r['name'],email=r['email'],person=r['leadership'],role='See named leader; mailbox ownership unconfirmed',classification='association_uncertain' if r['name'] in ['R S Manufacturing','CHIK / Designs Factory'] else 'general_only',source_urls=[url],evidence=evidence,checked_date='2026-09-15'))
(P/'owner_email_enrichment_chennai_b.json').write_text(json.dumps(localout,ensure_ascii=False,indent=2),encoding='utf-8')

examples=[
dict(company='Thirumala Press Components',subject='A question about TPC’s press and welding work',source='https://www.tpcpltd.com/about',basis='Official profile documents presses, fabrication and robotic welding. Client logos include TAFE and Rane; logos are company claims, not independently confirmed current contracts.',body='Hi Sharath,\n\nI saw that TPC combines press work, fabrication and robotic welding for tractor and automotive components.\n\nI’m building Kenesis Vision. We’re testing whether existing CCTV can help explain production delays that are difficult to reconstruct afterwards.\n\nWhen a batch waits between operations, how does your team work out what held it up? Or is that already covered by your production records?\n\nWe’re choosing our first repeatable product. A brief reply about one gap would help us decide what is worth building.\n\n[Your name]\nKenesis Vision'),
dict(company='Varna Print Factory',subject='How does Varna review interruptions across shifts?',source='https://varnaprintfactory.com/about-us',basis='Official page states digital printing on woven/knit fabrics, three shifts and Ranganath’s operational role. Companies in his biography are former employers, not established Varna clients.',body='Hi Ranganath,\n\nI read that Varna prints both woven and knit fabrics and runs three shifts. Your site says you oversee operations.\n\nWhen output is below plan, can you trace the interruption across those shifts from your current records?\n\nAt Kenesis Vision, we’re testing AI on existing CCTV to make visible production events easier to review. We’re still deciding which factory problem to build a repeatable product around.\n\nWhat, if anything, is hard to reconstruct at Varna today? A short reply is enough.\n\n[Your name]\nKenesis Vision'),
dict(company='Shahi Foods',subject='A question about Shahi’s Uthukottai factory',source='https://www.shahifoodproducts.com/contact-us.html',basis='Official contact page separates the Uthukottai factory from Koyambedu office. Product range is appalam/pappadum. No unverified named client is used.',body='Hello Shahi Foods team,\n\nCould you pass this to the owner or production manager? I saw that your factory is in Uthukottai and your office is in Koyambedu.\n\nI’m building Kenesis Vision. We’re testing whether existing CCTV can help answer production questions without someone replaying hours of footage.\n\nIs there a recurring factory issue that your team currently has to visit or phone the floor to understand?\n\nWe’re choosing our first repeatable product. One example would help us judge whether video could be useful.\n\n[Your name]\nKenesis Vision')]

files=['owner_email_enrichment_chennai_a.json','owner_email_enrichment_chennai_b.json','owner_email_enrichment_tn.json','owner_email_enrichment_south.json']
if not all((P/f).exists() for f in files):
    print('Local enrichment saved. Waiting for remaining regional research.');raise SystemExit
contacts=[]
for f in files:
    part=read(f)
    if isinstance(part,dict):part=part.get('companies',part.get('results',part.get('contacts',[])))
    contacts.extend(part)
assert len(contacts)==50 and len({r['name'] for r in contacts})==50
lookup={r['name']:r for r in contacts}
counts=Counter(r['classification'] for r in contacts)
style='body{font:17px/1.6 system-ui;background:#f4f6fa;color:#172338;max-width:1050px;margin:auto;padding:30px}h1{font-size:38px;line-height:1.2}h2{margin-top:36px}article,.panel{background:white;padding:24px;border-radius:14px;margin:16px 0;border:1px solid #dce2eb}summary{cursor:pointer;font-weight:700}a{color:#0759ad}pre{font:inherit;white-space:pre-wrap}input,select{padding:12px;border:1px solid #aaa;border-radius:8px;margin:5px}small,.muted{color:#526174}dt{font-weight:700}dd{margin:0 0 13px} .pill{font-size:13px;background:#eaf1fa;padding:4px 8px;border-radius:8px}'
parts=[f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kenesis | Owner contacts and personal outreach</title><style>{style}</style><h1>Make the question specific.<br>Keep the introduction honest.</h1><p>Research checked 15 September 2026 · Latest owner-led shortlist: 50 companies · Nothing sent</p>']
parts.append('<div class="panel"><h2>The wording I recommend</h2><p><strong>One verified detail → one relevant question → an honest Kenesis introduction → one easy reply.</strong></p><p>Use a plain production-related subject. Avoid false “Re:” threads, invented urgency, or claiming this is purely academic research. We are building a commercial product and learning which problem to solve.</p><p>Do not ask the owner to design an AI solution. Ask what happened last time, how they discovered it and whether the current workaround is enough. No promised savings or compatibility before seeing the camera view.</p><p>Client names belong in the research notes only when supported. Mention them in an email only if they make the question more useful. A logo, former employer or industry served does not establish a current customer contract.</p><p>These are recommended starting drafts, not proven high-response wording. Judge responses by actual problem descriptions and relevant conversations, not just opens.</p></div>')
parts.append('<h2>Three worked examples</h2><p>Drafts for review. Replace the sender name before use. A request for a call can follow once someone identifies a real problem.</p>')
for e in examples:parts.append(f'<article><h3>{esc(e["company"])}</h3><p><strong>Subject: {esc(e["subject"])}</strong></p><pre>{esc(e["body"])}</pre><details><summary>Why this wording is specific</summary><p>{esc(e["basis"])}</p><a href="{esc(e["source"])}">Company evidence</a></details></article>')
parts.append(f'<h2>Owner email search: 50 companies</h2><p>{counts["direct_verified"]} direct addresses verified against a named leader; {counts["association_uncertain"]} associated but not confirmed owner-specific; {counts["general_only"]} general/company routes. “Direct” means publicly assigned to the person, not proof that they personally read it. No mailbox deliverability test.</p><p>Existing confirmed direct addresses are included in this total. It is not a count of newly discovered emails. Generic Gmail addresses can be legitimate business routes but are not automatically owner-direct.</p><input id="search" placeholder="Search company, owner or process" aria-label="Search companies"><select id="kind" aria-label="Contact type"><option value="">All contact types</option><option value="direct_verified">Verified named leader email</option><option value="association_uncertain">Association needs checking</option><option value="general_only">General business route</option></select><p id="count"></p>')
out=[]
for r in rows:
    c=lookup[r['name']]
    if r['name']=='Shahi Foods':
        r=dict(r,factory_evidence='Official contact page lists factory at Plot 16, K.R.C. Nagar, Uthukottai Post & Taluk, Tiruvallur 602026. Koyambedu is the separate office.',caveat='Factory address now verified in contact-page research. Founder-name variants and current decision authority still need checking; no CCTV or buying intent confirmed.')
    urls=c.get('source_urls',[])
    if isinstance(urls,str):urls=[urls]
    links=' · '.join(f'<a href="{esc(u)}">Contact source {i+1}</a>' for i,u in enumerate(urls))
    facts=' · '.join(f'<a href="{esc(s["url"])}">Company source {i+1}</a>' for i,s in enumerate(r['sources']))
    client='Named current clients not verified in this research. Do not invent them.'
    if r['name'].startswith('Thirumala'):client=examples[0]['basis']
    if r['name']=='Varna Print Factory':client=examples[1]['basis']
    if r['name']=='MG Knit Garments':
        client='Official about page names ElevenParis, Gertrude Gaston and Ba&sh as customers. Company-reported relationship, not independently verified current contracts.'
        facts+=' · <a href="https://www.mgknitgarments.com/about">Published customer claims</a>'
    parts.append(f'<article class="contact" data-kind="{esc(c["classification"])}"><details><summary>{r["rank"]}. {esc(r["name"])} <span class="pill">{esc(c["classification"].replace("_"," "))}</span></summary><dl><dt>Named leader</dt><dd>{esc(c.get("person") or r["leadership"])}</dd><dt>Best published route from this search</dt><dd>{esc(c.get("email"))}</dd><dt>What the evidence establishes</dt><dd>{esc(c.get("evidence"))}</dd><dt>What they make</dt><dd>{esc(r["products"])}</dd><dt>Documented production facts</dt><dd>{esc(r["factory_evidence"])}</dd><dt>Clients: claim boundary</dt><dd>{esc(client)}</dd><dt>Question to explore, not a diagnosed problem</dt><dd>{esc(r["discovery_topic"])}</dd><dt>What still needs checking</dt><dd>{esc(r["caveat"])}</dd></dl><p>{links}</p><p>{facts}</p></details></article>')
    out.append(dict(company=r['name'],contact=c,products=r['products'],production_evidence=r['factory_evidence'],client_evidence=client,discovery_question=r['discovery_topic'],company_sources=r['sources']))
    additional=c.get('additional_contacts',[])
    if additional:
        extras=''.join(f'<li>{esc(x.get("person"))} — {esc(x.get("role"))}: {esc(x.get("email"))}</li>' for x in additional)
        parts[-1]=parts[-1].replace('</details></article>','<h3>Additional published contacts</h3><ul>'+extras+'</ul></details></article>')
script="const q=document.getElementById('search'),k=document.getElementById('kind'),cards=[...document.querySelectorAll('.contact')];function filter(){let n=0;cards.forEach(c=>{const ok=(!k.value||c.dataset.kind===k.value)&&c.textContent.toLowerCase().includes(q.value.toLowerCase());c.hidden=!ok;if(ok)n++;});document.getElementById('count').textContent=n+' companies shown';}q.addEventListener('input',filter);k.addEventListener('change',filter);filter();"
parts.append('<p><a href="Kenesis-Owner-Led-50.html">Back to the factory shortlist</a> · <a href="Kenesis-Owner-Email-Pack.json" download>Download research data</a></p><script>'+script+'</script></html>')
(P/'Kenesis-Owner-Email-Pack.html').write_text(''.join(parts),encoding='utf-8')
(P/'Kenesis-Owner-Email-Pack.json').write_text(json.dumps(dict(scope='Latest owner-led 50; not all 91',counts=dict(counts),examples=examples,companies=out),ensure_ascii=False,indent=2),encoding='utf-8')
(P/'owner_email_pack_check.js').write_text(script,encoding='utf-8')
print(dict(counts))
