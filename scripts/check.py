from pathlib import Path
import re

for page in Path('.').rglob('*.md'):
    text = page.read_text()
    links = re.findall(r'\]\(([^\s)]+)\)', text)
    links += re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', text, re.I)
    for link in links:
        path = link.split('#', 1)[0]
        if path and not re.match(r'[a-z][a-z0-9+.-]*:', path, re.I):
            assert (page.parent / path).exists(), f'{page}: missing {path}'
print('Documentation links passed')
