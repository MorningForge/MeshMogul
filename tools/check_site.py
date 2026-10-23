#!/usr/bin/env python3
"""Dependency-free checks for the public site's files and project-path links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROJECT_BASE = '/MeshMogul/'
ORIGIN = 'https://morningforge.github.io'

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.headings, self.meta = [], set(), [], {}
        self.errors, self.title, self.language, self.main = [], False, False, False
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.language = a.get('lang') == 'en'
        if tag == 'title': self.title = True
        if tag == 'main': self.main = True
        if tag == 'meta': self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        if re.fullmatch('h[1-6]', tag): self.headings.append(int(tag[1]))
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('Duplicate ID: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'img' and 'alt' not in a: self.errors.append('Image missing alt attribute')
        if tag == 'script': self.errors.append('Unexpected JavaScript; this site is script-free')
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])


def main():
    errors = []
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in p.relative_to(ROOT).parts for x in ('.git', '.local', '_site', '__pycache__')))
    documents = {p: Document(p.read_text()) for p in files if p.suffix == '.html'}
    link_count = 0
    for path, doc in documents.items():
        name = path.relative_to(ROOT).as_posix()
        errors.extend(name + ': ' + e for e in doc.errors)
        if not (doc.title and doc.language and doc.main): errors.append(name + ': missing title, language, or main')
        for key in ('description', 'viewport', 'og:title', 'og:description', 'og:type'):
            if not doc.meta.get(key): errors.append(name + ': missing ' + key)
        if doc.headings.count(1) != 1 or not doc.headings or doc.headings[0] != 1: errors.append(name + ': expected one leading H1')
        for prev, current in zip(doc.headings, doc.headings[1:]):
            if current > prev + 1: errors.append(name + ': skipped heading level')
        request = PROJECT_BASE + (name[:-10] if name.endswith('index.html') else name)
        for ref in doc.links:
            link_count += 1
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme != 'https': errors.append(name + ': unexpected external link scheme')
                continue
            url = urlsplit(urljoin(ORIGIN + request, ref))
            if not url.path.startswith(PROJECT_BASE):
                errors.append(name + ': link escapes project path: ' + ref); continue
            target = ROOT / unquote(url.path[len(PROJECT_BASE):])
            if target.is_dir(): target /= 'index.html'
            if not target.is_file(): errors.append(name + ': missing local target: ' + ref)
            elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
                errors.append(name + ': missing anchor: ' + ref)
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = {n.text for n in ET.parse(ROOT / 'sitemap.xml').findall('s:url/s:loc', ns)}
    expected = {ORIGIN + PROJECT_BASE + (p.relative_to(ROOT).as_posix()[:-10] if p.name == 'index.html' else p.relative_to(ROOT).as_posix()) for p in documents if p.name != '404.html'}
    if urls != expected: errors.append('Sitemap does not match indexable HTML pages')
    for p in files:
        name = p.relative_to(ROOT).as_posix()
        if p.is_symlink(): errors.append(name + ': unexpected symlink')
        if p.suffix.lower() in ('.luau', '.lua', '.rbxl', '.rbxmx', '.rbxm', '.pem', '.key'):
            errors.append(name + ': non-marketing file type')
        if p.suffix in ('.html', '.css', '.svg', '.md', '.yml', '.xml', '.txt', '.py'):
            content = p.read_text()
            if re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----', content):
                errors.append(name + ': possible credential')
            if p.suffix == '.html' and re.search(r'/workspace/|[A-Z]:\\|docs/product-spec|Codex/Investigations|MeshLab[A-Z]', content):
                errors.append(name + ': private implementation reference')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(documents)} HTML pages, {link_count} links/assets, {len(urls)} sitemap entries; project-path, anchors, metadata, headings, alt attributes, and public-file checks.')

if __name__ == '__main__': main()
