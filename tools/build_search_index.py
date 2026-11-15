#!/usr/bin/env python3
"""Generate the same-origin search index from the published articles, without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]


class ArticleText(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.active = False
        self.parts = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            self.active = True

    def handle_endtag(self, tag):
        if tag == 'article':
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)


def build_index():
    catalog = json.loads((ROOT / 'assets/foundations-catalog.json').read_text())
    entries = []
    for guide in catalog['guides']:
        source = (ROOT / 'guides' / guide['slug'] / 'index.html').read_text()
        text = re.sub(r'\s+', ' ', ' '.join(ArticleText(source).parts)).strip()
        entries.append({**{key: guide[key] for key in (
            'slug', 'title', 'track', 'difficulty', 'summary', 'symptoms', 'tags')}, 'content': text})
    return json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    path = ROOT / 'assets/foundations-search-index.json'
    generated = build_index()
    if args.check:
        if not path.is_file() or path.read_text() != generated:
            raise SystemExit('Search index is stale; run python3 tools/build_search_index.py')
        print('PASS: full-text search index matches all published articles and catalog metadata.')
    else:
        path.write_text(generated, encoding='utf-8')
        print('Generated static Foundations search index.')


if __name__ == '__main__':
    main()
