from pathlib import Path
import ast
import html
import json
import re
from collections import Counter

ROOT = Path(__file__).parent
def read(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
def esc(v):
    if isinstance(v, list):
        v = '; '.join(str(x) for x in v)
    if isinstance(v, dict):
        v = '; '.join(f'{k}: {value}' for k,value in v.items())
    return html.escape(str(v or 'Not verified'))

# Reuse the already checked offline report layout, without executing its builder.
tree = ast.parse((ROOT/'build_prospect_report.py').read_text(encoding='utf-8'))
template = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='template' for t in n.targets))
rows=[]
for f in ['owner_candidates_chennai.json','owner_candidates_tn.json','owner_candidates_south.json','owner_candidates_reused.json']:
    part=read(f)
    if isinstance(part,dict):
        part=part.get('companies',part.get('prospects',part.get('candidates',[])))
    rows.extend(part)
lookup={r['name']:r for r in rows}
assert len(lookup)==len(rows), 'Duplicate candidates'
for name,extra in read('owner_reuse_notes.json').items():
    lookup[name].update(extra)
    if extra.get('extra_source'):
        lookup[name]['sources'].append(extra['extra_source'])
sector_evidence=read('owner_sector_evidence.json')
selection=read('owner_selection.json')
old_names={r['name'] for r in read('Kenesis-50-Factory-Prospects.json')['companies']}
mail_path=ROOT/'owner_mail_domains.json'
mail_data=read('owner_mail_domains.json') if mail_path.exists() else []
if isinstance(mail_data,dict):
    mail_data=[mail_data]
mail={r['domain']:r for r in mail_data}
selected=[]
metric_names=['Ownership/control evidence','Direct decision-maker route','Local management and plant','Repeat visual workflow','Technology/readiness evidence']
metric_max=[3,2,2,2,1]
for spec in selection['selected']:
    r=dict(lookup[spec['name']])
    r.update(spec)
    r['checked_date']='2026-09-15'
    r['reused_from_first_list']=r['name'] in old_names
    points=r['metric_scores']
    assert len(points)==5 and all(isinstance(v,int) and 0<=v<=mx for v,mx in zip(points,metric_max)), r['name']
    r['priority_score']=sum(points)
    r['decision_access_score']=sum(points[:3])
    r['visual_fit_score']=sum(points[3:])
    r['sector_comparison']=sector_evidence[r['sector_group']]
    assert r['sources'] and r.get('ownership_evidence') and r.get('factory_evidence'), r['name']
    assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',r['email']), r['name']
    r['mail_domain_check']=mail.get(r['email'].split('@')[-1].lower(),{'status':'Not checked'})
    selected.append(r)
geo_order={'Chennai metro':0,'Tamil Nadu — other':1,'South India — other':2}
selected.sort(key=lambda r:(geo_order[r['geography']],-r['priority_score'],-r['decision_access_score'],r['name']))
assert len(selected)==50 and len({r['name'] for r in selected})==50
for i,r in enumerate(selected,1):r['rank']=i
counts=Counter(r['geography'] for r in selected)
sectors=Counter(r['sector_group'] for r in selected)
owner_count=sum(r['metric_scores'][0]==3 for r in selected)
direct_count=sum(r['metric_scores'][1]==2 for r in selected)
new_count=sum(not r['reused_from_first_list'] for r in selected)

cards=[]
for r in selected:
    scores=' · '.join(f'{name}: {v}/{mx}' for name,v,mx in zip(metric_names,r['metric_scores'],metric_max))
    fields=[('What they make',r['products']),('Factory evidence',r['factory_evidence']),('Leader to approach',r['leadership']),
      ('Ownership evidence',r['ownership_evidence']),('Evidence confidence',r['leadership_confidence']),
      ('Why decisions may be easier to reach — inference',r['decision_locality']),('Public business email',r['email']),('Email provenance',r['email_type']),
      ('Public business phone',r.get('phone')),('Production contact',r.get('operational_contact') or 'Request the production or plant manager; no named operational contact verified.'),
      ('Existing technology signals',r['adoption_signals']),('Potential visual use case — hypothesis',r['operational_usecase']),
      ('Discovery question',r['discovery_topic']),('Main qualification gap',r['caveat']),
      ('Score breakdown',scores),('Mail-domain check',r['mail_domain_check']['status']+'; mailbox deliverability not verified.')]
    dl=''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k,v in fields)
    sources=''.join(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">{esc(s.get("claim","Source"))}</a></li>' for s in r['sources'])
    analogy=r['sector_comparison']
    sector_id='sector-'+str(list(sector_evidence).index(r['sector_group']))
    label='Owner/family evidence' if r['metric_scores'][0]==3 else ('Founder / qualified owner evidence' if r['metric_scores'][0]==2 else 'Decision-access candidate')
    prior='Reused from first list' if r['reused_from_first_list'] else 'New prospect'
    cards.append(f'''<article class="company" data-region="{esc(r['geography'])}" data-process="{esc(r['sector_group'])}" data-leader="{'Strong' if r['metric_scores'][0]==3 else 'Qualified'}" data-contact="{'Leadership email' if r['metric_scores'][1]==2 else 'Company inbox'}"><details id="company-{r['rank']}"><summary><span class="rank">{r['rank']:02}</span><span class="identity"><strong>{esc(r['name'])}</strong><span>{esc(r['city'])} · {esc(r['sector_group'])} · {prior}</span></span><span class="badge">{r['priority_score']}/10 priority<br>{label}</span></summary><div class="body"><p class="reason">{esc(r['fit_reason'])}</p><dl>{dl}</dl><p><a href="#{sector_id}">See the AI-vision comparison for this industry</a></p><h3>Company evidence</h3><ul class="sources">{sources}</ul></div></details></article>''')

template=template.replace('Kenesis · 50 factory prospects','Kenesis · 50 owner-led factory prospects')
template=template.replace('50 factories.<br>Evidence before outreach.','50 factories.<br>Owners first. Across industries.')
template=template.replace('Chennai first. Public business emails, factory evidence and leadership clues—ready for your review before personalized drafts.','Chennai first. A separate shortlist ranked by access to decision-makers and plausible visual workflows—not rubber-product similarity.')
template=template.replace('Leadership email routes identified','Direct leadership contact routes')
template=template.replace('Strong leadership evidence','Explicit owner/family evidence').replace('>Leadership emails<','>Direct leadership routes<')
note=f'''<div class="note"><p><strong>{new_count} new prospects · {50-new_count} reused · {len(sectors)} sector groups.</strong></p><p>{owner_count} have explicit owner/family/partner evidence in company or institutional sources. Other candidates have founder-led or qualified ownership evidence, identified individually. All 50 have a published business email.</p><p><strong>No confirmed buying intent or sales-cycle data.</strong> Scores rank research evidence. They are not probabilities of purchase, promised approval times or proof that existing CCTV is suitable.</p></div>'''
template=re.sub(r'<div class="note">.*?</div>\s*<details class="method">',lambda m:note+'<details class="method">',template,count=1,flags=re.S)
method='''<details class="method"><summary>How ranking works: five signals, 10 points</summary><div class="body"><p>Geography takes priority: Chennai and its industrial belt, then the rest of Tamil Nadu, then other South Indian states. Within each tier, higher evidence scores come first. Sector variety is deliberate. This is a researched sample, not an exhaustive ranking of all factories.</p><dl><div><dt>Ownership/control · 0–3</dt><dd>3: explicit proprietor, family-owned or partner evidence in a company/institutional source. 2: active founder or qualified secondary/historical owner evidence. 1: executive title only. 0: unknown. No shareholding percentage is invented.</dd></div><div><dt>Contact access · 0–2</dt><dd>2: published leader-associated email or direct phone. 1: general company email/phone. 0: only an indirect or unverified route. A published number may still be answered by staff.</dd></div><div><dt>Local management · 0–2</dt><dd>2: local leader/contact and operating production location align. 1: plant exists but approval location is unclear. 0: only an office or unknown factory. These are access proxies, not authority confirmations.</dd></div><div><dt>Visual workflow · 0–2</dt><dd>2: documented repeated production/handling stages. 1: production exists but work is bespoke or poorly described. 0: no supported factory use case. Camera coverage remains untested.</dd></div><div><dt>Readiness · 0–1</dt><dd>1: specific production technology, formal quality systems or similar investment evidence. 0: no concrete signal found. Existing automation can also make extra monitoring unnecessary.</dd></div></dl><p><strong>Why not predict days to close?</strong> Owner control can shorten access, but budgets, existing systems and procurement rules remain unknown. The scores are judgment-based prioritization with visible inputs; they have not been calibrated against actual sales.</p><p><strong>Similarity is a hypothesis:</strong> competitor examples identify plausible use cases, not problems at these prospects. First validate recurring loss, camera visibility, a responsible manager and an actual paid-pilot budget. General CCTV is not a substitute for microscopic inspection, temperature measurement or process-quality testing.</p><p>Company pages may be undated. Founder status does not prove present ownership; secondary and historical sources are qualified. Every contact is publicly published. No mailbox was probed and no message or draft was created.</p></div></details>'''
template=re.sub(r'<details class="method">.*?</details>',lambda m:method,template,count=1,flags=re.S)
template=template.replace('Try Ambattur, rubber or managing director','Try food, founder, garments or Ambattur')
template=template.replace('Back to the market research','Back to the market research')
template=template.replace('Kenesis-50-Factory-Prospects.json','Kenesis-Owner-Led-50.json')
template=template.replace('Download source-backed data','Download source-backed data')
template=template.replace('<p class="back">','<p class="back"><a href="Kenesis-50-Factory-Prospects.html">Earlier factory shortlist</a> · ')
comparisons='<section><h2>Industry comparisons: why these factories are worth interviewing</h2><p>These examples support discovery questions. They do not establish needs at the companies above.</p>'
for i,(sector,ev) in enumerate(sector_evidence.items()):
    comparisons+=f'<article id="sector-{i}" class="note"><h3>{esc(sector)} · {sectors[sector]} prospects</h3><p>{esc(ev["analogy"])}</p><p>{esc(ev["limit"])}</p><a href="{esc(ev["source"])}" target="_blank" rel="noopener noreferrer">Read comparison source</a></article>'
comparisons+='</section>'
template=template.replace('<footer>',comparisons+'<footer>')
template=template.replace('<h1>','<p><a href="Kenesis-Owner-Email-Pack.html">Updated owner email search and company-specific draft examples →</a></p><h1>',1)
template=template.replace('All 50 have a published business email.','All 50 have a published business email. Sri Hanuma Rice Mills needs phone-first verification: its published email domain returned no MX mail-routing record. The other 49 primary email domains returned MX records; individual mailboxes remain unverified.')
replacements={'__CHENNAI__':str(counts['Chennai metro']),'__TN__':str(counts['Tamil Nadu — other']),'__SOUTH__':str(counts['South India — other']),'__DIRECT__':str(direct_count),'__REGIONS__':''.join(f'<option>{esc(x)}</option>' for x in geo_order),'__PROCESSES__':''.join(f'<option>{esc(x)}</option>' for x in sorted(sectors)),'__CARDS__':''.join(cards)}
for key,value in replacements.items():template=template.replace(key,value)
assert not re.search(r'__[A-Z]+__',template)
(ROOT/'Kenesis-Owner-Led-50.html').write_text(template,encoding='utf-8')
(ROOT/'owner_report_script_check.js').write_text(re.search(r'<script>(.*?)</script>',template,re.S)[1],encoding='utf-8')
output={'checked_date':'2026-09-15','scoring':'Ownership 3 + direct access 2 + local management 2 + visual workflow 2 + readiness 1; evidence priority, not conversion probability.',
 'counts':{'geography':dict(counts),'sectors':dict(sectors),'explicit_owner_evidence':owner_count,'direct_leadership_routes':direct_count,'new':new_count,'reused':50-new_count},
 'companies':selected,'reserves':[r for r in rows if r['name'] not in {s['name'] for s in selected}]}
(ROOT/'Kenesis-Owner-Led-50.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(output['counts'],ensure_ascii=True))
