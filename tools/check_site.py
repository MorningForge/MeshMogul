#!/usr/bin/env python3
"""Dependency-free checks for the public site's files and project-path links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re
import argparse
import hashlib
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROJECT_BASE = '/MeshMogul/'
ORIGIN = 'https://morningforge.github.io'
STORE = 'https://create.roblox.com/store/asset/126445067739142'
PUBLIC_EMAIL = 'morningforge@proton.me'
GIT_EMAIL = '311570204+MorningForge@users.noreply.github.com'

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.headings, self.meta = [], set(), [], {}
        self.errors, self.title, self.language, self.main = [], False, False, False
        self.resources, self.canonical = [], None
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
        if 'src' in a: self.resources.append(a['src'])
        if tag == 'link' and a.get('rel') in ('stylesheet', 'icon', 'preload'):
            self.resources.append(a.get('href', ''))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-git-identity', action='store_true', help='Check effective author and committer identity immediately before committing')
    args = parser.parse_args()
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
        if name != '404.html' and (doc.canonical != ORIGIN + request or doc.meta.get('og:url') != ORIGIN + request):
            errors.append(name + ': canonical or Open Graph URL does not match route')
        if not any(ref.endswith('legal/') for ref in doc.links): errors.append(name + ': missing legal footer link')
        if STORE not in doc.links: errors.append(name + ': missing verified Creator Store CTA')
        for ref in doc.resources:
            if urlsplit(ref).scheme or urlsplit(ref).netloc: errors.append(name + ': external runtime resource')
        for ref in doc.links:
            link_count += 1
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                if ref == 'mailto:' + PUBLIC_EMAIL: continue
                if parsed.scheme != 'https': errors.append(name + ': unexpected external link scheme')
                if 'create.roblox.com/store/asset/' in ref and ref != STORE:
                    errors.append(name + ': unexpected Store asset destination')
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
            if p.suffix in ('.html', '.css', '.svg', '.md', '.yml', '.xml', '.txt'):
                emails = set(re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', content))
                if emails - {PUBLIC_EMAIL, GIT_EMAIL}: errors.append(name + ': unapproved email (value omitted)')
                if re.search(r'(?:[A-Z]:[\\/]|/(?:Users|home|workspace)/|docs/product-spec|Codex/Investigations)', content):
                    errors.append(name + ': private location or source reference (value omitted)')
                repositories = re.findall(r'MorningForge/([A-Za-z0-9_.-]+)', content)
                if any(repo != 'MeshMogul' for repo in repositories):
                    errors.append(name + ': unapproved repository reference (value omitted)')
            if p.suffix == '.html' and '1.1.0' in content and name != 'changelog/index.html':
                errors.append(name + ': stale version outside historical release notes')
    # The current release must be explicit; historical 1.1.1/1.1.0 notes remain valid.
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    changelog = (ROOT / 'changelog/index.html').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    if 'Founding · 1.2.0' not in home or 'changelog/#release-1-2-0' not in home:
        errors.append('index.html: missing current 1.2.0 identity or release link')
    if 'Current release: **Founding 1.2.0**' not in readme:
        errors.append('README.md: missing current 1.2.0 identity')
    for rel in ('index.html', 'changelog/index.html'):
        doc = documents[ROOT / rel]
        page_source = (ROOT / rel).read_text(encoding='utf-8')
        if (not re.search(r'<title>[^<]*1\.2\.0[^<]*</title>', page_source)
                or any('1.2.0' not in doc.meta.get(key, '') for key in ('og:title', 'description', 'og:description'))):
            errors.append(rel + ': title or metadata does not identify 1.2.0')
    sections = re.findall(r'<section id="release-(1-2-0|1-1-1|1-1-0)">(.*?)</section>', changelog, re.S)
    if [version for version, _ in sections] != ['1-2-0', '1-1-1', '1-1-0']:
        errors.append('changelog/index.html: current and historical releases must be newest first')
    elif 'Current release' not in sections[0][1] or 'Earlier release' not in sections[1][1] or 'Earlier notes' not in sections[2][1]:
        errors.append('changelog/index.html: incorrect current or historical release label')
    for path in documents:
        content = path.read_text(encoding='utf-8')
        if re.search(r'(?:provisional|proposed|upcoming|not yet released|not yet confirmed|candidate)[^<.]{0,120}1\.2\.0|1\.2\.0[^<.]{0,120}(?:provisional|proposed|upcoming|not yet released|not yet confirmed|candidate)', content, re.I):
            errors.append(path.relative_to(ROOT).as_posix() + ': 1.2.0 is described as unreleased')
    css = (ROOT / 'assets/site.css').read_text()
    if re.search(r'\.header-cta\s*\{[^}]*display\s*:\s*none', css): errors.append('Mobile acquisition CTA is hidden')
    if re.search(r'@import\b|url\(\s*[\'"]?(?:https?:)?//', css): errors.append('External CSS runtime dependency')
    legal = (ROOT / 'legal/index.html').read_text()
    notices = (ROOT / 'THIRD_PARTY_NOTICES.md').read_text()
    canonical_notice = '# MeshMogul — third-party software notices' + notices.split('# MeshMogul — third-party software notices', 1)[1]
    if hashlib.sha256(canonical_notice.encode()).hexdigest() != '3f230d0ab0c1c21eec8dc62e655149aea942cfe357032c8b25f5e5556b5e0cf6':
        errors.append('Release notice text differs from the approved full notice document')
    blocks = re.findall(r'```text\n(.*?)\n```', notices, re.S)
    rendered = re.findall(r'<pre class="license-text">(.*?)</pre>', legal, re.S)
    from html import unescape
    if len(blocks) != 3 or blocks != [unescape(block) for block in rendered]:
        errors.append('Legal page does not reproduce the three complete notice blocks')
    expected_notices = {'Copyright (c) 2025 EgoMoose', 'Copyright (c) 2026 EgoMoose', 'Copyright (c) 2025 RiskoZoSlovenska'}
    if {block.splitlines()[2] for block in blocks} != expected_notices:
        errors.append('Notice copyright identities or years differ')
    for block in blocks:
        if 'Permission is hereby granted' not in block or 'SOFTWARE.' not in block or 'THE SOFTWARE IS PROVIDED "AS IS"' not in block:
            errors.append('Incomplete MIT permission or disclaimer')
    workflow = (ROOT / '.github/workflows/pages.yml').read_text()
    if 'LICENSE.md THIRD_PARTY_NOTICES.md _site/' not in workflow or 'privacy legal _site/' not in workflow:
        errors.append('Pages staging omits legal documents or route')
    if 'cp -R . ' in workflow or 'cp -R *' in workflow: errors.append('Pages staging is too broad')
    if args.check_git_identity:
        for role in ('AUTHOR', 'COMMITTER'):
            ident = subprocess.check_output(['git', 'var', 'GIT_' + role + '_IDENT'], cwd=ROOT, text=True)
            if not ident.startswith('MorningForge <' + GIT_EMAIL + '> '):
                errors.append('Unapproved Git ' + role.lower() + ' identity (value omitted)')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(documents)} HTML pages, {link_count} links/assets, {len(urls)} sitemap entries; project-path, anchors, metadata, headings, alt attributes, release/legal/privacy/static-resource checks.')

if __name__ == '__main__': main()
