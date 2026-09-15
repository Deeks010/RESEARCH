from pathlib import Path
from collections import Counter
import json, html, re
P=Path(__file__).parent
def read(n):return json.loads((P/n).read_text(encoding='utf-8-sig'))
def esc(v):
    if isinstance(v,list):v='; '.join(str(x) for x in v)
    if isinstance(v,dict):v='; '.join(f'{k}: {x}' for k,x in v.items())
    return html.escape(str(v or 'Not established'))
market=read('redesign_market.json')
rows=[]
for state in ['pa','nc','oh']:
    data=read('redesign_'+state+'.json')
    if isinstance(data,dict):data=data.get('companies',data.get('prospects',data.get('rows',[])))
    rows.extend(data)
assert len({r['name'] for r in rows})==len(rows)
for r in rows:
    r['selection_status']=r.get('selection_status','conditional').lower()
    if r['selection_status'] not in ['priority','conditional','reserve']:r['selection_status']='conditional'
    assert r['website'] and r['sources'] and r['issue_evidence']
    if r.get('email'):assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',r['email']),r['name']
    r['review_method']='Public page text and links. No visual, mobile or performance test.'
override_path=P/'redesign_review_overrides.json'
if override_path.exists():
    overrides=read(override_path.name)
    for r in rows:r.update(overrides.get(r['name'],{}))
order={'priority':0,'conditional':1,'reserve':2}
rows.sort(key=lambda r:(order[r['selection_status']],r['state'],r['name']))
for i,r in enumerate(rows,1):r['rank']=i
counts=Counter(r['selection_status'] for r in rows)
states=Counter(r['state'] for r in rows)
contact_types=Counter(r.get('email_type','unknown') for r in rows)
mail_path=P/'redesign_mail_domains.json'
mail=read(mail_path.name) if mail_path.exists() else []
mail_lookup={x['domain']:x for x in mail}
for r in rows:r['mail_domain_check']=mail_lookup.get(r.get('email','').split('@')[-1],{}).get('status','Not checked')
style='''body{margin:0;background:#f3f5f0;color:#163229;font:16px/1.6 system-ui}main{max-width:1100px;margin:auto;padding:30px}h1{font-size:42px;line-height:1.15;max-width:820px}h2{margin-top:30px}a{color:#146543}header,.box,article{background:white;border:1px solid #d8e2da;border-radius:14px;padding:24px;margin:16px 0}.stats{display:flex;gap:16px;flex-wrap:wrap}.stat{padding:12px;background:#edf4e9;border-radius:10px;min-width:150px}.stat strong{display:block;font-size:28px}summary{cursor:pointer;font-weight:700}.badge{display:inline-block;font-size:12px;padding:3px 8px;border-radius:8px;background:#edf4e9}dt{font-weight:700}dd{margin:0 0 14px}.muted{color:#52635b}input,select{padding:12px;border:1px solid #a4b3a8;border-radius:8px;margin:5px;font:inherit}table{width:100%;border-collapse:collapse}th,td{text-align:left;vertical-align:top;padding:12px;border-bottom:1px solid #ddd}.scroll{overflow:auto}ul{padding-left:22px}button{padding:9px 15px;border:0;border-radius:8px;background:#164b38;color:white;cursor:pointer}@media(max-width:650px){main{padding:12px}h1{font-size:30px}header,article,.box{padding:17px}}'''
parts=[f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Website redesign | US prospect research</title><style>{style}</style></head><body><main><header><p>SEPARATE SIDE PROJECT · RESEARCHED 15 SEPTEMBER 2026</p><h1>Sell a clearer path to booking.<br>Start with owner-run visitor farms.</h1><p>{esc(market["verdict"])}</p><div class="stats"><div class="stat"><strong>{len(rows)}</strong>businesses screened</div><div class="stat"><strong>{counts["priority"]}</strong>priority conversations</div><div class="stat"><strong>{sum(bool(r.get("email")) for r in rows)}</strong>published email routes</div><div class="stat"><strong>0</strong>confirmed buyers</div></div><p>Website links, ownership evidence, contact sources, observed issues and suggested fixes in one place. No designs or emails sent.</p></header>']
parts.append('<section class="box"><h2>Recommendation</h2><p>'+esc(market['recommendation'])+'</p><p>'+esc(market['geography'])+'</p><p><strong>Why this segment:</strong> visitors must decide when to come, what it costs and how to reserve. A clearer page can be tested against those tasks. Commodity-only farms may have little reason to buy a consumer website redesign. This is a hypothesis to test, not a claim that farms are the most profitable niche.</p><p><strong>What to sell first:</strong> a visit-planning or booking page with one clear action, verified current details and an easy seasonal update process. A full rebrand is a larger decision and is not justified by a typo or one outdated event.</p></section>')
parts.append('<details class="box"><summary>Market evidence and real competing offers</summary>')
for e in market['evidence']:parts.append(f'<p>{esc(e["claim"])} <a href="{esc(e["url"])}">{esc(e["type"])}</a></p>')
parts.append('<div class="scroll"><table><tr><th>Provider</th><th>Published offer</th><th>Meaning for this project</th></tr>')
for c in market['competition']:parts.append(f'<tr><td><a href="{esc(c["url"])}">{esc(c["name"])}</a></td><td>{esc(c["offer"])}<p>{esc(c["first_year_calculation"])}</p></td><td>{esc(c["meaning"])}</td></tr>')
parts.append('</table></div><p>These are advertised vendor prices, not verified customer invoices, market averages or suggested earnings.</p></details>')
parts.append('<details class="box"><summary>How to use the shortlist</summary><p><strong>Priority:</strong> stronger page-level evidence and an identifiable business offer. Start a qualification conversation; this does not mean the business needs a full redesign.</p><p><strong>Conditional:</strong> plausible improvement but facts, business impact, owner access or timing need checking.</p><p><strong>Reserve:</strong> functioning site, weak current need or material evidence gaps. Do not spend unpaid design time yet.</p><p>Email labels distinguish a named owner from a general business inbox. An address on the same page as an owner is not automatically owner-direct.</p><p>'+esc(market['limitations'])+'</p></details>')
parts.append('<h2>Companies and page evidence</h2><p>State counts: '+esc(dict(states))+'. The list is ordered by research priority, not projected sales value.</p><p><strong>Contact results:</strong> 9 owner-associated email routes; 18 general inboxes; 3 uncertain or restricted-purpose contacts. These include shared business addresses. All 13 primary email domains returned mail-routing records; individual inbox delivery is untested.</p><p>The sample also includes wholesale nursery, direct-food sales and garden-service businesses for comparison. Their buying tasks differ from visitor bookings.</p><input id="query" aria-label="Search prospects" placeholder="Company, county, owner, issue"><select id="state" aria-label="Filter by state"><option value="">All states</option>'+''.join(f'<option>{esc(s)}</option>' for s in sorted(states))+'</select><select id="status" aria-label="Filter by priority"><option value="">All priorities</option><option>priority</option><option>conditional</option><option>reserve</option></select><p id="shown"></p>')
for r in rows:
    fields=[('Owner / decision-maker',r.get('owner')),('Ownership evidence',r.get('owner_evidence')),('Public email',r.get('email')),('Email evidence type',r.get('email_type')),('Public phone',r.get('phone')),('What customers buy',r.get('offers')),('Operating / current-season evidence',r.get('active_evidence')),('Observed website issue',r.get('website_issue')),('Exact evidence and scope',r.get('issue_evidence')),('Suggested paid scope — hypothesis',r.get('proposed_fix')),('Why this business might buy',r.get('buyer_fit')),('Uncertainty / reason to hold',r.get('caveat')),('Research-priority rationale',r.get('rank_rationale') or r.get('selection_reason') or 'See issue evidence and caveat. No buying intent verified.')]
    fields.append(('Mail-domain check',r['mail_domain_check']+'; mailbox delivery untested.'))
    if r.get('alternate_email'):fields.append(('Other published contact',r['alternate_email']+' — '+r.get('alternate_email_note','Role not established')))
    sources=''.join(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s.get("claim","Source"))}</a></li>' for s in r['sources'])
    parts.append(f'<article class="prospect" data-state="{esc(r["state"])}" data-status="{esc(r["selection_status"])}"><details><summary>{r["rank"]:02}. {esc(r["name"])} <span class="badge">{esc(r["selection_status"])}</span><br><span class="muted">{esc(r["county"])} · {esc(r["state"])}</span></summary><p><a href="{esc(r["website"])}" target="_blank" rel="noopener">Open business website</a> · <a href="{esc(r["issue_url"])}" target="_blank" rel="noopener">Open reviewed page</a></p><dl>'+''.join(f'<dt>{esc(k)}</dt><dd>{esc(v)}</dd>' for k,v in fields)+'</dl><h3>Sources</h3><ul>'+sources+'</ul></details></article>')
parts.append('<section class="box"><h2>Test the business before building 30 free websites</h2><p>'+esc(market['test_plan'])+'</p><ol>'+''.join(f'<li>{esc(x)}</li>' for x in market['qualification'])+'</ol><details><summary>Time and money: planning example</summary><p>'+esc(market['economics'])+'</p></details><p>Seasonal timing matters: September can be peak preparation for fall attractions. Ask when they can discuss improvements; do not assume a live-season rebuild is welcome.</p></section>')
script="const q=document.getElementById('query'),s=document.getElementById('state'),t=document.getElementById('status'),a=[...document.querySelectorAll('.prospect')];function f(){let n=0;a.forEach(e=>{const ok=(!s.value||e.dataset.state===s.value)&&(!t.value||e.dataset.status===t.value)&&e.textContent.toLowerCase().includes(q.value.toLowerCase());e.hidden=!ok;if(ok)n++;});document.getElementById('shown').textContent=n+' businesses shown';}q.addEventListener('input',f);s.addEventListener('change',f);t.addEventListener('change',f);f();"
parts.append('<footer class="box"><p>This file opens offline. Source links require internet. Send the HTML attachment to share the report.</p><a href="Website-Redesign-Prospects.json" download>Download structured research</a></footer><script>'+script+'</script></main></body></html>')
(P/'Website-Redesign-Prospects.html').write_text(''.join(parts),encoding='utf-8')
(P/'Website-Redesign-Prospects.json').write_text(json.dumps(dict(market=market,counts=dict(counts),states=dict(states),contact_types=dict(contact_types),companies=rows),ensure_ascii=False,indent=2),encoding='utf-8')
(P/'redesign_script_check.js').write_text(script,encoding='utf-8')
print(json.dumps(dict(screened=len(rows),counts=dict(counts),contact_types=dict(contact_types))))
