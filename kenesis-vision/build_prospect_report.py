from pathlib import Path
import json
import re
import html
from collections import Counter

ROOT = Path(__file__).parent
esc = lambda v: html.escape(str(v or 'Not found'))

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

selection = read(ROOT / 'prospect_selection.json')
all_rows = []
for name in ['prospects_chennai_rubber.json', 'prospects_chennai_other.json', 'prospects_tn.json', 'prospects_south.json']:
    rows = read(ROOT / name)
    if isinstance(rows, dict):
        rows = rows.get('prospects', rows.get('companies', rows.get('candidates', [])))
    for row in rows:
        row['_source_file'] = name
        all_rows.append(row)
lookup = {r['name']: r for r in all_rows}
assert len(lookup) == len(all_rows), 'Duplicate company name'
dns_path = ROOT / 'prospect_mail_domains.json'
dns = read(dns_path) if dns_path.exists() else {}
if isinstance(dns, list):
    dns = {r['domain']: r for r in dns}
selected = []
for n, spec in enumerate(selection['selected'], 1):
    row = dict(lookup[spec['name']])
    row.update(spec)
    row['rank'] = n
    row['checked_date'] = '2026-09-15'
    row['email'] = row.get('email') or ''
    assert isinstance(row['email'], str), row['name']
    assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', row['email']), row['name']
    assert row.get('sources'), row['name']
    domain = row['email'].split('@')[-1].lower()
    row['mail_domain_check'] = dns.get(domain, {'status': 'Not checked'})
    selected.append(row)
assert len(selected) == 50
assert len({r['name'] for r in selected}) == 50
counts = Counter(r['geography'] for r in selected)
leader_count = sum(r['leader_grade'] != 'Unknown' for r in selected)
direct_count = sum(r['contact_grade'] == 'Leadership email' for r in selected)
export = {'checked_date': '2026-09-15', 'method': selection['method'], 'limits': selection['limits'], 'companies': selected,
          'reserves': [r for r in all_rows if r['name'] not in {s['name'] for s in selected}]}
(ROOT / 'Kenesis-50-Factory-Prospects.json').write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding='utf-8')

cards = []
for r in selected:
    sources = ''.join(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">{esc(s.get("claim", "Source"))}</a></li>' for s in r['sources'])
    mail_check = r['mail_domain_check']
    status = mail_check.get('status', 'Not checked') if isinstance(mail_check, dict) else str(mail_check)
    fields = [
      ('What they make', r.get('products')),
      ('Factory evidence', r.get('factory_evidence')),
      ('Leadership', r.get('leadership')),
      ('Leadership evidence', r.get('leadership_confidence')),
      ('Production contact', r.get('operational_contact') or 'No named production contact verified. Ask for the plant or production manager.'),
      ('Public business email', r['email']),
      ('Email source / recipient', r.get('email_type')),
      ('Mail-domain check', status + '. This does not verify the mailbox or guarantee delivery.'),
      ('Published business phone', r.get('phone')),
      ('Why shortlisted', r.get('fit_reason')),
      ('Discovery question — not confirmed pain', r.get('discovery_topic')),
      ('Check before drafting', r.get('caveat')),
    ]
    details = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k,v in fields)
    cards.append(f'''<article class="company" data-region="{esc(r['geography'])}" data-process="{esc(r['process_group'])}" data-leader="{esc(r['leader_grade'])}" data-contact="{esc(r['contact_grade'])}">
      <details id="company-{r['rank']}"><summary><span class="rank">{r['rank']:02}</span><span class="identity"><strong>{esc(r['name'])}</strong><span>{esc(r['city'])} · {esc(r['process_group'])}</span></span><span class="badge">{esc(r['contact_grade'])}</span></summary>
      <div class="body"><p class="reason">{esc(r['fit_reason'])}</p><dl>{details}</dl><h3>Evidence checked 15 September 2026</h3><ul class="sources">{sources}</ul><p class="small">Website: <a href="{esc(r['website'])}" target="_blank" rel="noopener noreferrer">{esc(r['website'])}</a></p></div></details></article>''')

def options(values):
    return ''.join(f'<option>{esc(v)}</option>' for v in values)

template = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kenesis · 50 factory prospects</title>
<style>
:root{--ink:#183830;--muted:#536760;--line:#d6e0d8;--bg:#f4f6f1;--accent:#176c4b}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 'Segoe UI',Arial,sans-serif}main{max-width:1120px;margin:auto;padding:40px 24px 80px}a{color:var(--accent);text-underline-offset:3px}.eyebrow{font-size:12px;letter-spacing:1.7px;font-weight:700;color:var(--accent)}h1{font-size:clamp(32px,5vw,54px);line-height:1.12;letter-spacing:-1.6px;margin:12px 0 20px}h2{font-size:22px;margin:0 0 12px}h3{font-size:17px}.lead{font-size:19px;color:var(--muted);max-width:780px}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:25px 0}.stat{background:white;border:1px solid var(--line);border-radius:10px;padding:18px}.stat strong{display:block;font-size:30px;line-height:1.1}.stat span{font-size:13px;color:var(--muted)}.note{background:#e5ede4;border-left:4px solid var(--accent);padding:18px 22px;border-radius:6px;margin:20px 0}.note p{margin:5px 0}.method{background:white;border:1px solid var(--line);border-radius:10px;margin:20px 0}.method summary{padding:16px 20px;font-weight:650}.method .body{padding-top:0}.filters{display:grid;grid-template-columns:2fr 1fr 1fr;gap:12px;margin-top:25px}label{font-size:12px;color:var(--muted);font-weight:600}input,select,button{font:inherit}input,select{display:block;width:100%;margin-top:5px;padding:11px;border:1px solid var(--line);border-radius:7px;background:white;color:var(--ink)}.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:16px 0}.row button{border:1px solid var(--line);border-radius:7px;padding:8px 12px;background:white;color:var(--ink);cursor:pointer}.row button.active{background:var(--ink);color:white}.count{margin-left:auto;color:var(--muted);font-size:14px}.company{margin:10px 0;background:white;border:1px solid var(--line);border-radius:10px;overflow:hidden}.company summary{display:flex;align-items:center;gap:16px;padding:18px;cursor:pointer;list-style:none}.company summary::-webkit-details-marker{display:none}.company summary:after{content:'+';margin-left:6px;font-size:24px;color:var(--accent)}.company details[open]>summary:after{content:'−'}.rank{font-size:19px;color:var(--accent);min-width:27px;font-weight:600}.identity{flex:1}.identity strong{display:block;font-size:17px}.identity>span{display:block;font-size:13px;color:var(--muted);margin-top:3px}.badge{border:1px solid var(--line);background:#f4f7f2;border-radius:5px;padding:4px 8px;font-size:11px;max-width:150px}.body{padding:12px 24px 24px}.reason{font-size:17px;max-width:850px}dl{display:grid;grid-template-columns:1fr 1fr;gap:0 28px}dl>div{padding:11px 0;border-bottom:1px solid var(--line);min-width:0}dt{font-size:12px;color:var(--muted);font-weight:650}dd{margin:5px 0 0;overflow-wrap:anywhere}.sources{padding-left:20px;font-size:14px}.sources li{margin:6px 0}.small,footer{font-size:13px;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:35px;padding-top:18px}.empty{padding:35px;background:white;border-radius:10px;text-align:center}[hidden]{display:none!important}:focus-visible{outline:3px solid #b0862c;outline-offset:3px}
@media(max-width:650px){main{padding:25px 15px}.stats{grid-template-columns:1fr 1fr}.filters{grid-template-columns:1fr}dl{grid-template-columns:1fr}.company summary{gap:10px;padding:15px}.badge{max-width:90px;font-size:10px}.body{padding:10px 18px 22px}.count{width:100%;margin:0}}
@media print{body{background:white}.filters,.row,.back{display:none!important}main{max-width:none;padding:0}.company{break-inside:avoid}.company[hidden]{display:block!important}.body{padding:5px 15px}.stats{grid-template-columns:repeat(4,1fr)}a{color:inherit}.company summary:after{display:none}}
</style></head><body><main>
<p class="eyebrow">KENESIS VISION · PROSPECT RESEARCH · 15 SEPTEMBER 2026</p>
<h1>50 factories.<br>Evidence before outreach.</h1>
<p class="lead">Chennai first. Public business emails, factory evidence and leadership clues—ready for your review before personalized drafts.</p>
<div class="stats"><div class="stat"><strong>__CHENNAI__</strong><span>Chennai & nearby industrial belt</span></div><div class="stat"><strong>__TN__</strong><span>Elsewhere in Tamil Nadu</span></div><div class="stat"><strong>__SOUTH__</strong><span>Elsewhere in South India</span></div><div class="stat"><strong>__DIRECT__</strong><span>Leadership email routes identified</span></div></div>
<div class="note"><p><strong>These are research prospects, not confirmed buyers.</strong></p><p>49 primary emails were published by the companies. Champion Plastics' email is corroborated by public corporate directories and should be confirmed by phone. No mailbox was tested by sending mail. Named leadership leads were found for __LEADERS__ companies, with source strength shown separately. A director's name does not establish owner control or quick purchasing.</p></div>
<details class="method"><summary>How the 50 were selected—and what remains unknown</summary><div class="body"><p>__METHOD__</p><p>__LIMITS__</p><p><strong>Read the badges:</strong> “Leadership email” means evidence connects the published address to a leader. “Named contact” means a person is named but their current authority is unconfirmed. “Company inbox” means a general business route. Full details retain the exact source and caveat.</p><p>Rubber and moulding are closest to the current pilot. Heat treatment is adjacent. Packaging and metalworking broaden requirement discovery. None is assumed compatible with Kenesis without seeing the machine and camera setup.</p><p><strong>First conversation:</strong> speak with the named leader and the production/plant manager. Establish the actual recurring loss, current workaround, camera visibility, budget owner and buying process. These facts cannot be established from a website alone.</p></div></details>
<div class="filters"><label>Search company, location, person or process<input id="search" type="search" placeholder="Try Ambattur, rubber or managing director"></label><label>Geography<select id="region"><option value="">All areas</option>__REGIONS__</select></label><label>Process group<select id="process"><option value="">All processes</option>__PROCESSES__</select></label></div>
<div class="row"><button id="leaders" type="button" aria-pressed="false">Strong leadership evidence</button><button id="direct" type="button" aria-pressed="false">Leadership emails</button><button id="reset" type="button">Reset</button><button id="print" type="button">Print / save PDF</button><span class="count" id="count" role="status" aria-live="polite">50 companies</span></div>
<div id="companies">__CARDS__</div><p id="empty" class="empty" hidden>No matches. Clear a filter to see more companies.</p>
<footer><p>No outreach or email drafts were created. Source-checked means the address was published in reviewed evidence. Mail-domain records only establish domain routing, not mailbox validity. Pages and job titles can be outdated.</p><p class="back"><a href="Kenesis-Vision-Research.html">Back to the market research</a> · <a href="Kenesis-50-Factory-Prospects.json" download>Download source-backed data</a></p></footer>
</main><script>
const cards=[...document.querySelectorAll('.company')];
const search=document.getElementById('search'),region=document.getElementById('region'),process=document.getElementById('process');
let leadersOnly=false,directOnly=false;
function filter(){const words=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;for(const card of cards){const text=card.textContent.toLowerCase();const match=words.every(w=>text.includes(w))&&(!region.value||card.dataset.region===region.value)&&(!process.value||card.dataset.process===process.value)&&(!leadersOnly||card.dataset.leader==='Strong')&&(!directOnly||card.dataset.contact==='Leadership email');card.hidden=!match;if(match)count++;}document.getElementById('count').textContent=count+' of 50 companies';document.getElementById('empty').hidden=count!==0;}
search.addEventListener('input',filter);region.addEventListener('change',filter);process.addEventListener('change',filter);
for(const id of ['leaders','direct'])document.getElementById(id).addEventListener('click',()=>{if(id==='leaders')leadersOnly=!leadersOnly;else directOnly=!directOnly;const on=id==='leaders'?leadersOnly:directOnly;document.getElementById(id).classList.toggle('active',on);document.getElementById(id).setAttribute('aria-pressed',String(on));filter();});
document.getElementById('reset').addEventListener('click',()=>{search.value='';region.value='';process.value='';leadersOnly=directOnly=false;for(const id of ['leaders','direct']){document.getElementById(id).classList.remove('active');document.getElementById(id).setAttribute('aria-pressed','false');}filter();});
let printState=[];window.addEventListener('beforeprint',()=>{printState=[...document.querySelectorAll('details')].map(d=>[d,d.open]);printState.forEach(([d])=>d.open=true)});window.addEventListener('afterprint',()=>printState.forEach(([d,open])=>d.open=open));document.getElementById('print').addEventListener('click',()=>window.print());
if(location.hash){const target=document.getElementById(location.hash.slice(1));if(target&&target.tagName==='DETAILS')target.open=true;}
</script></body></html>'''
replacements={'__CHENNAI__':str(counts['Chennai metro']),'__TN__':str(counts['Tamil Nadu — other']),'__SOUTH__':str(counts['South India — other']),'__DIRECT__':str(direct_count),'__LEADERS__':str(leader_count),'__METHOD__':esc(selection['method']),'__LIMITS__':esc(selection['limits']),'__REGIONS__':options(['Chennai metro','Tamil Nadu — other','South India — other']),'__PROCESSES__':options(sorted({r['process_group'] for r in selected})),'__CARDS__':''.join(cards)}
for key,value in replacements.items():
    template=template.replace(key,value)
assert not re.search(r'__[A-Z]+__',template)
(ROOT/'Kenesis-50-Factory-Prospects.html').write_text(template,encoding='utf-8')
script=re.search(r'<script>(.*?)</script>',template,re.S)[1]
(ROOT/'prospect_report_script_check.js').write_text(script,encoding='utf-8')
print(json.dumps({'selected':len(selected),'regions':dict(counts),'named_leaders':leader_count,'leadership_emails':direct_count,'reserve_count':len(export['reserves'])}))
