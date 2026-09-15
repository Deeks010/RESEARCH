from pathlib import Path
import re
import html
from markdown_it import MarkdownIt

ROOT = Path(__file__).parent
md = MarkdownIt('commonmark', {'html': False}).enable('table')
docs = [
 ('COMMERCIAL_COMPARISON.md', 'commercial', 'Customers, revenue & pricing', 'All 20 competitors, real prices and clearly labelled calculations.'),
 ('SOP_REDESIGN.md', 'redesign', 'Your curing-machine workflow', 'What to reuse when the next factory has different machines.'),
 ('global_commercial_scale.md', 'global-money', 'Global commercial evidence', 'Customer counts, money disclosures and estimate limitations.'),
 ('india_commercial_scale.md', 'india-money', 'Indian commercial evidence', 'Regional deployment counts and financial sources.'),
 ('sop_scale_and_specialist_commercials.md', 'specialist-money', 'How specialists deliver', 'Process teaching, installation work and delivery economics.'),
 ('guardex_profile.md', 'guardex', 'Guardex.ai deep dive', 'A close Indian competitor: products, pilots and evidence gaps.'),
 ('YOUR_SIX_USE_CASES.md', 'features', 'Your six features', 'Choose what to test first.'),
 ('india_competitors.md', 'india', 'India & regional competitors', 'The closest regional alternatives.'),
 ('global_competitors.md', 'global', 'Global competitors', 'Established industrial AI platforms.'),
 ('operations_competitors.md', 'operations', 'Production specialists', 'Alternatives focused on factory operations.'),
 ('market_validation.md', 'market', 'Market & evidence', 'Demand, pricing assumptions and practical limits.'),
 ('validation_and_research_playbook.md', 'plan', 'Your validation plan', 'Turn pilot interest into a buying decision.'),
 ('KENESIS_MARKET_REPORT.md', 'report', 'Full assessment', 'The complete market assessment and research index.'),
]
file_ids = {x[0]:x[1] for x in docs}

def slug(s):
    s = re.sub(r'[^\w\s-]', '', s.lower())
    return re.sub(r'\s', '-', s)

def render(s, docid):
    result = md.render(s)
    def link(m):
        dest=m.group(1)
        f, _, anchor=dest.partition('#')
        if f in file_ids:
            return 'href="#'+file_ids[f]+ ('--'+anchor if anchor else '')+'"'
        if dest.startswith('https://') or dest.startswith('http://'):
            return 'href="'+dest+'" target="_blank" rel="noopener noreferrer"'
        return m.group(0)
    result=re.sub(r'href="([^"]+)"',link,result)
    result=re.sub(r'<h([1-6])>(.*?)</h\1>',lambda m: '<h'+m[1]+' id="'+docid+'--'+slug(re.sub('<[^>]+>','',html.unescape(m[2])))+'">'+m[2]+'</h'+m[1]+'>', result)
    return result.replace('<table>', '<div class="table-wrap" role="region" aria-label="Comparison table" tabindex="0"><table>').replace('</table>', '</table></div>')

panels=[]
for filename, docid, title, desc in docs:
    source=(ROOT/filename).read_text(encoding='utf-8-sig')
    parts=re.split(r'^## (.+)$', source, flags=re.M)
    intro=re.sub(r'^# .+\n', '', parts[0], count=1).strip()
    sections=[]
    for i in range(1,len(parts),2):
        heading=parts[i]
        sections.append(f'<details class="research-section" id="{docid}--{slug(heading)}"><summary>{html.escape(heading)}</summary><div class="detail-body">{render(parts[i+1],docid)}</div></details>')
    panels.append(f'<section class="page" id="{docid}" hidden aria-labelledby="title-{docid}"><header class="page-heading"><p class="eyebrow">RESEARCH LIBRARY</p><h1 id="title-{docid}">{title}</h1><p>{desc}</p></header><details class="research-section intro" id="{docid}--context"><summary>Context and key conclusion</summary><div class="detail-body">{render(intro,docid)}</div></details>{"".join(sections)}</section>')

nav=''.join(f'<a href="#{id}">{title}</a>' for _,id,title,_ in docs)
template='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kenesis Vision — Market research</title>
<style>
:root{color-scheme:light;--ink:#172f35;--muted:#52676b;--line:#d8e3e1;--paper:#f5f7f4;--green:#126351;--light:#e4f2eb;--amber:#80501c}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 'Segoe UI',Arial,sans-serif}a{color:var(--green);text-underline-offset:3px}button,input{font:inherit}button,a,input,summary{-webkit-tap-highlight-color:transparent}:focus-visible{outline:3px solid #d19238;outline-offset:4px}button{cursor:pointer}.layout{display:grid;grid-template-columns:265px minmax(0,1fr);min-height:100vh}.sidebar{padding:32px 24px;border-right:1px solid var(--line);background:#fff;position:sticky;top:0;height:100vh;overflow:auto}.brand{font-size:24px;font-weight:750;letter-spacing:-1px}.brand span{color:var(--green)}.edition{font-size:12px;letter-spacing:1.4px;color:var(--muted);margin:3px 0 32px}.sidebar nav{display:grid;gap:5px}.sidebar nav a{font-size:14px;text-decoration:none;padding:11px 12px;border-radius:8px;color:var(--muted)}.sidebar nav a.active{background:var(--light);color:var(--green);font-weight:650}.side-note{font-size:12px;color:var(--muted);margin-top:30px;border-top:1px solid var(--line);padding-top:18px}.main{min-width:0;padding:25px clamp(22px,4vw,70px) 70px;max-width:1450px;width:100%}.toolbar{display:flex;gap:16px;justify-content:space-between;align-items:center;padding-bottom:24px;border-bottom:1px solid var(--line);margin-bottom:40px}.search-label{flex:1;max-width:470px}.search-label span{display:block;font-size:12px;color:var(--muted);margin-bottom:5px}input[type=search]{width:100%;border:1px solid var(--line);padding:10px 14px;border-radius:8px;background:#fff;min-width:0}.print{background:#fff;color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:10px 16px;font-size:13px;white-space:nowrap}.eyebrow{font-size:12px;font-weight:700;letter-spacing:1.7px;color:var(--green);margin:0 0 12px}h1{font-size:clamp(30px,4vw,48px);line-height:1.13;letter-spacing:-1.7px;max-width:850px;margin:0 0 19px}h2{font-size:25px;letter-spacing:-.5px;line-height:1.3;margin:34px 0 17px}h3{font-size:20px;line-height:1.4}p{margin:0 0 17px}.lead{max-width:720px;color:var(--muted);font-size:19px}.status{display:flex;gap:10px;flex-wrap:wrap;margin:23px 0}.tag{padding:5px 10px;font-size:12px;border:1px solid var(--line);border-radius:5px;background:#fff}.recommendation{background:var(--ink);color:#fff;padding:30px;border-radius:14px;margin:28px 0}.recommendation .eyebrow{color:#a5dac2}.recommendation h2{margin:0 0 12px;font-size:28px;max-width:750px}.recommendation p{color:#dce8e5;max-width:700px;margin-bottom:20px}.recommendation a{color:#fff;font-size:14px}.choices{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.choice{background:#fff;border:1px solid var(--line);border-radius:12px;padding:23px;text-decoration:none;color:var(--ink);display:block}.choice:hover{border-color:var(--green)}.choice .decision{font-size:11px;letter-spacing:1px;font-weight:700;color:var(--green);text-transform:uppercase}.choice h3{margin:10px 0}.choice p{font-size:15px;color:var(--muted);margin:0}.choice .more{display:block;font-size:13px;color:var(--green);margin-top:16px}.next{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;border-top:1px solid var(--line);padding-top:20px}.next .num{font-size:13px;color:var(--green);font-weight:700}.next h3{font-size:18px;margin:8px 0}.next p{font-size:15px;color:var(--muted)}.callout{border-left:3px solid #b68b43;padding:8px 0 8px 20px;margin:25px 0;font-size:15px;color:var(--muted)}.page-heading{margin-bottom:30px}.page-heading>p:last-child{color:var(--muted)}.research-section{margin:12px 0;border:1px solid var(--line);border-radius:10px;background:#fff;scroll-margin-top:20px}.research-section summary{padding:20px 24px;font-size:18px;font-weight:600;cursor:pointer}.research-section[open] summary{border-bottom:1px solid var(--line);color:var(--green)}.detail-body{padding:24px 28px;max-width:100%;overflow-wrap:anywhere}.detail-body p,.detail-body li{max-width:85ch}.detail-body h1{font-size:25px}.detail-body h2{font-size:23px}.detail-body h3{font-size:19px}.detail-body a{font-size:.94em}.detail-body li{margin-bottom:9px}.table-wrap{overflow:auto;width:100%;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.6;text-align:left}th{background:#edf3ef;font-weight:650;color:var(--ink)}th,td{padding:14px;vertical-align:top;border-bottom:1px solid var(--line);min-width:140px}tbody tr:nth-child(even){background:#fafbf9}.research-section code{background:#f0f3ef;padding:2px 4px}.result{display:block;background:#fff;border:1px solid var(--line);padding:18px 22px;border-radius:9px;margin:12px 0;text-decoration:none}.result strong{display:block}.result span{font-size:14px;color:var(--muted)}.search-count{color:var(--muted)}footer{font-size:12px;color:var(--muted);border-top:1px solid var(--line);margin-top:45px;padding-top:18px}[hidden]{display:none!important}
@media(max-width:850px){.layout{grid-template-columns:1fr}.sidebar{position:static;height:auto;padding:20px;border-right:0;border-bottom:1px solid var(--line)}.edition{margin-bottom:15px}.sidebar nav{display:flex;overflow:auto;gap:5px}.sidebar nav a{white-space:nowrap}.side-note{display:none}.main{padding:22px}.toolbar{margin-bottom:28px}.choices{grid-template-columns:1fr 1fr}.next{grid-template-columns:1fr}.detail-body{padding:20px}}
@media(max-width:500px){.choices{grid-template-columns:1fr}.toolbar{align-items:end;gap:10px}.print{padding:10px;font-size:12px}.recommendation{padding:23px}.recommendation h2{font-size:25px}h1{letter-spacing:-1px}.research-section summary{padding:17px;font-size:17px}body{font-size:16px}}
@media print{body{background:white;font-size:11pt}.layout{display:block}.sidebar,.toolbar,#search-results,.more{display:none!important}.main{padding:0;max-width:none}.page{display:block!important;break-before:page}.page-heading h1{font-size:25pt}.choices{display:block}.choice{break-inside:avoid;margin:12px 0}.recommendation{background:#edf3ef;color:#172f35}.recommendation p,.recommendation .eyebrow,.recommendation a{color:#172f35}.research-section{border:0}.research-section summary{padding:10px 0}.detail-body{padding:5px 0}table{font-size:9pt}.table-wrap{overflow:visible}th,td{min-width:0;padding:6px}a{color:#126351}footer{break-before:avoid}}
</style></head><body><div class="layout"><aside class="sidebar"><div class="brand">kenesis<span>.</span></div><p class="edition">VISION / MARKET RESEARCH</p><nav aria-label="Research sections"><a href="#overview" class="active">Start here</a>__NAV__</nav><div class="side-note">Research checked<br><strong>15 September 2026</strong><br><br>India first · Unpaid pilots<br><br>Vendor claims and our recommendations are kept distinct. All original evidence remains available.</div></aside>
<main class="main"><div class="toolbar"><label class="search-label"><span>FIND A COMPANY, FEATURE OR TOPIC</span><input type="search" id="search" placeholder="Try “Visionify”, “pricing” or “SOP”…"></label><button type="button" class="print" id="print">Print / Save PDF</button></div>
<section class="page" id="overview"><p class="eyebrow">THE RESEARCH, MADE READABLE</p><h1>A real market.<br>A buying reason still to prove.</h1><p class="lead">Factories already use AI on CCTV. Kenesis now needs to prove which problem an Indian factory will pay it to solve.</p><div class="status"><span class="tag">India first</span><span class="tag">Unpaid pilots</span><span class="tag">20 vendor offerings reviewed</span></div>
<div class="recommendation"><p class="eyebrow">UPDATED WITH YOUR RUBBER-CURING PILOT</p><h2>Reuse the unloading-delay workflow. Qualify each machine's signals.</h2><p>The timer and reports can stay shared. Different machines need a tested way to identify readiness and removal. Start with supported machine families and measure setup effort.</p><a href="#redesign--your-rubber-curing-example-what-to-keep-and-what-to-replace">Your machine-specific redesign →</a><br><a href="#commercial">All 20 competitors: customers, money and calculated prices →</a></div>
<p class="callout"><strong>New: 50 factory prospects.</strong> Chennai-first company research with leadership evidence, published business emails and production contacts. <a href="Kenesis-50-Factory-Prospects.html">Open the searchable shortlist →</a></p>
<p class="callout"><strong>New: owners first, across industries.</strong> A separate set of 50 factories across eight sectors. Ranked by ownership evidence, contact access and production fit. <a href="Kenesis-Owner-Led-50.html">Open the owner-led shortlist →</a></p>
<h2>Your six requests, at a glance</h2><div class="choices">
<a class="choice" href="#features--1-workstation-absence-useful-only-with-operational-context"><span class="decision">Test first</span><h3>Workstation absence</h3><p>Measure avoidable delay. Absence alone does not prove lost productivity.</p><span class="more">Evidence & next test →</span></a>
<a class="choice" href="#features--2-chitchatting-the-requested-label-is-unreliable"><span class="decision">Do not lead with this</span><h3>Chitchatting</h3><p>People gathering together does not establish whether a conversation is useful.</p><span class="more">What the camera can prove →</span></a>
<a class="choice" href="#features--3-sop-validation-your-scalability-concern-is-partly-right"><span class="decision">Keep it narrow</span><h3>SOP validation</h3><p>Repeated visible rules can scale. New detailed checks for every process are harder.</p><span class="more">See scalable vs custom checks →</span></a>
<a class="choice" href="#features--4-restricted-area-entry-define-unauthorized"><span class="decision">Possible add-on</span><h3>Restricted-area entry</h3><p>Zone entry is easy to define. Knowing who has permission needs more context.</p><span class="more">Compare the two problems →</span></a>
<a class="choice" href="#features--5-cctv-intelligence-chatbot-useful-interface-not-complete-knowledge"><span class="decision">Build on trusted data</span><h3>CCTV chatbot</h3><p>Useful for finding events. It cannot know what was never captured or detected.</p><span class="more">See the three possible offers →</span></a>
<a class="choice" href="#features--6-fall-detection-sell-response-improvement-carefully"><span class="decision">Targeted safety add-on</span><h3>Fall detection</h3><p>Focus on faster response where a safety team can act. Validate missed events.</p><span class="more">Evidence & practical limits →</span></a></div>
<p class="callout">These are research recommendations. None of the six features is established as a unique Kenesis advantage. Competitor claims are not proof of performance at your factories.</p>
<h2>What to do next</h2><div class="next"><div><span class="num">01 / CONFIRM THE LOSS</span><h3>Choose one pilot station</h3><p>Ask the production manager to verify the delay and its actual cost.</p></div><div><span class="num">02 / TEST PAYMENT</span><h3>Offer a paid extension</h3><p>Agree a fixed scope, end date and success conditions before adding features.</p></div><div><span class="num">03 / TEST REPEATABILITY</span><h3>Try the same offer elsewhere</h3><p>After one paid commitment, test two comparable factories.</p></div></div><a href="#plan">Open the full validation plan →</a>
</section>__PANELS__<section id="search-results" class="page" hidden><p class="eyebrow">SEARCH THE RESEARCH</p><h1>Results</h1><p id="search-count" class="search-count" role="status" aria-live="polite"></p><div id="results-list"></div></section><footer>Kenesis Vision · Research dated 15 September 2026 · Public-source assessment. No vendor outreach or independent product testing was performed.</footer></main></div>
<script>
const pages=[...document.querySelectorAll('.page')];
const search=document.getElementById('search');
const links=[...document.querySelectorAll('.sidebar nav a')];
const index=[...document.querySelectorAll('.research-section')].map(d=>({id:d.id,title:d.querySelector('summary').textContent,text:d.textContent.toLowerCase(),page:d.closest('.page').querySelector('h1').textContent,description:d.querySelector('.detail-body').textContent.trim().replace(/\\s+/g,' ').slice(0,170)}));
let current='overview';
function show(id){const page=document.getElementById(id);if(!page||!page.classList.contains('page'))return;pages.forEach(p=>p.hidden=p!==page);links.forEach(a=>{const on=a.hash==='#'+id;a.classList.toggle('active',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});current=id;}
function route(){const hash=decodeURIComponent(location.hash.slice(1))||'overview';const target=document.getElementById(hash);if(!target)return;search.value='';const page=target.classList.contains('page')?target:target.closest('.page');if(!page)return;show(page.id);let el=target;while(el&&el!==page){if(el.tagName==='DETAILS')el.open=true;el=el.parentElement;}requestAnimationFrame(()=>{if(target===page)window.scrollTo(0,0);else target.scrollIntoView({block:'start'});});}
window.addEventListener('hashchange',route);
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(a&&a.hash===location.hash){e.preventDefault();route();}});
search.addEventListener('input',()=>{const q=search.value.trim().toLowerCase();if(!q){route();return;}show('search-results');const matches=index.filter(d=>q.split(/\\s+/).every(w=>d.text.includes(w)));document.getElementById('search-count').textContent=matches.length+' matching sections';const list=document.getElementById('results-list');list.replaceChildren();for(const m of matches){const a=document.createElement('a');a.className='result';a.href='#'+m.id;const title=document.createElement('strong');title.textContent=m.title;const desc=document.createElement('span');desc.textContent=m.page+' · '+m.description+'…';a.append(title,desc);a.addEventListener('click',()=>{search.value='';if(location.hash===a.hash)route();});list.append(a);}});
let printState=[];window.addEventListener('beforeprint',()=>{printState=[...document.querySelectorAll('details')].map(d=>[d,d.open]);printState.forEach(([d])=>d.open=true)});window.addEventListener('afterprint',()=>printState.forEach(([d,open])=>d.open=open));document.getElementById('print').addEventListener('click',()=>window.print());route();
</script></body></html>'''
output=template.replace('__NAV__',nav).replace('__PANELS__',''.join(panels))
seen_ids={}
def unique_id(match):
    value=match[1]
    seen_ids[value]=seen_ids.get(value,0)+1
    return 'id="'+value+('' if seen_ids[value]==1 else '-'+str(seen_ids[value]))+'"'
output=re.sub(r'\bid="([^"]+)"',unique_id,output)
(ROOT/'Kenesis-Vision-Research.html').write_text(output,encoding='utf-8')
ids=set(re.findall(r'\bid="([^"]+)"',output))
targets=set(re.findall(r'href="#([^"]+)"',output))
missing=targets-ids
print(f'Created readable report: {len(output):,} characters; {len(panels)} full research chapters')
print('Missing internal anchors:',sorted(missing))
if missing: raise SystemExit(1)
