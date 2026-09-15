import json
from pathlib import Path
P=Path(__file__).parent
def read(n): return json.loads((P/n).read_text(encoding='utf-8-sig'))
groups=['Metalworking and machinery','Food processing','Garments and textiles','Electrical and electronics','Packaging and printing','Plastics','Furniture and wood','Heat treatment']
# Manually assessed evidence scores: control, contact, locality, workflow, readiness.
ch=[(0,[3,1,2,2,1]),(0,[3,2,1,1,0]),(0,[3,1,2,1,0]),(0,[3,2,2,1,1]),(1,[3,1,2,2,0]),(2,[2,1,1,2,0]),(2,[3,1,2,1,0]),(3,[3,1,1,1,0]),(3,[3,1,2,1,0]),(4,[2,1,2,2,0]),(3,[3,1,1,1,0]),(0,[3,1,2,2,1]),(5,[3,1,1,2,0]),(0,[3,1,2,2,1]),(0,[3,1,1,1,0]),(6,[2,1,2,2,0]),(1,[2,1,1,2,1]),(4,[2,1,1,2,0]),(3,[3,1,2,2,1]),(3,[3,2,2,2,1])]
tn={0:(0,[3,2,2,2,1]),1:(0,[3,2,2,2,1]),2:(0,[3,1,2,2,1]),4:(2,[2,2,2,2,1]),5:(2,[2,1,2,2,1]),6:(2,[2,1,2,2,1]),7:(2,[3,1,1,2,1]),8:(4,[2,1,1,2,1]),9:(2,[2,2,2,2,1]),10:(2,[3,1,1,2,0]),12:(1,[3,2,1,2,1]),15:(5,[3,2,2,2,1]),16:(7,[2,1,2,2,1]),17:(7,[2,1,2,2,1])}
south={'Varna Print Factory':(2,[2,2,2,2,1]),'Ajay Sensors & Instruments':(3,[3,2,2,1,1]),'BVN Modulars':(6,[2,1,2,2,1]),'Nice Global Food Products':(1,[2,1,1,2,1]),'Altom Foods':(1,[2,2,2,2,0]),'Ganesh Metal Products':(0,[3,1,2,2,1]),'Team D':(0,[2,1,2,2,1]),'Syno Pack India':(0,[3,2,2,1,0]),'The Green Wrap':(4,[3,1,1,2,1]),'Sri Hanuma Rice Mills':(1,[3,1,2,2,1])}
selected=[]
def add(r,g,s,geo): selected.append(dict(name=r['name'],metric_scores=s,sector_group=groups[g],geography=geo))
for r,(g,s) in zip(read('owner_candidates_chennai.json'),ch): add(r,g,s,'Chennai metro')
for i,r in enumerate(read('owner_candidates_tn.json')):
    if i in tn: add(r,*tn[i],'Tamil Nadu — other')
for r in read('owner_candidates_south.json'):
    if r['name'] in south: add(r,*south[r['name']],'South India — other')
notes=read('owner_reuse_notes.json')
for r,g in zip(read('owner_candidates_reused.json'),[0,4,4,4,7,0]): add(r,g,notes[r['name']]['metric_scores'],'Chennai metro')
assert len(selected)==50
(P/'owner_selection.json').write_text(json.dumps({'selected':selected},ensure_ascii=False,indent=2),encoding='utf-8')
dns=(P/'check_prospect_mail_domains.ps1').read_text()
dns=dns.replace("'prospects_chennai_rubber.json', 'prospects_chennai_other.json', 'prospects_tn.json', 'prospects_south.json'","'owner_candidates_chennai.json', 'owner_candidates_tn.json', 'owner_candidates_south.json', 'owner_candidates_reused.json'").replace("'prospect_mail_domains.json'","'owner_mail_domains.json'")
(P/'check_owner_mail_domains.ps1').write_text(dns,encoding='utf-8')
