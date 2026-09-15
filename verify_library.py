"""Check the portable library without fetching websites or rewriting research."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import ast
import json
import re

root = Path(__file__).parent
missing = []

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                url = urlsplit(value)
                if not url.scheme and not url.netloc and url.path:
                    if not (self.base / unquote(url.path)).exists():
                        missing.append((str(self.base), value))

reports = [root/'index.html', *root.glob('kenesis-vision/Kenesis-*.html'),
           *root.glob('website-redesign/Website-*.html')]
for report in reports:
    parser = Links()
    parser.base = report.parent
    parser.feed(report.read_text(encoding='utf-8'))
for path in root.rglob('*.json'):
    if '.git' not in path.parts:
        json.loads(path.read_text(encoding='utf-8-sig'))
for path in root.rglob('*.py'):
    ast.parse(path.read_text(encoding='utf-8-sig'))
for path in [root/'README.md', root/'kenesis-vision/README.md', root/'website-redesign/README.md']:
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if not urlsplit(target).scheme:
            assert (path.parent/target).exists(), (path, target)
assert not missing, missing
def read(relative):
    return json.loads((root/relative).read_text(encoding='utf-8-sig'))
first = read('kenesis-vision/Kenesis-50-Factory-Prospects.json')['companies']
second = read('kenesis-vision/Kenesis-Owner-Led-50.json')['companies']
assert len(first) == len(second) == 50
assert len({r['name'] for r in first+second}) == 91
assert len(read('kenesis-vision/Kenesis-Owner-Email-Pack.json')['companies']) == 50
assert len(read('website-redesign/Website-Redesign-Prospects.json')['companies']) == 30
print(f'Passed: {len(reports)} HTML reports, local guide links, JSON/Python syntax and prospect counts.')
