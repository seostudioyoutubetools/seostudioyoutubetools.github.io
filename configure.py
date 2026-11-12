#!/usr/bin/env python3
"""Set deployment URLs once; safe to run repeatedly on generated files."""
import argparse, re
from pathlib import Path
from urllib.parse import urlsplit
parser = argparse.ArgumentParser(description='Set canonical, Open Graph, sitemap and robots URLs.')
parser.add_argument('base_url', help='Full public site URL, e.g. https://USER.github.io/REPOSITORY/')
a = parser.parse_args(); parts=urlsplit(a.base_url)
if parts.scheme != 'https' or not parts.netloc or parts.query or parts.fragment or parts.username or parts.password:
    parser.error('Use a full HTTPS base URL without credentials, query or fragment.')
base=a.base_url.rstrip('/')+'/'
if any(c in base for c in ('"', "'", '<', '>', '&', ' ', '\\')):
    parser.error('Base URL contains an unsupported character.')
root=Path(__file__).resolve().parent
for f in root.glob('*.html'):
    text=f.read_text(encoding='utf-8'); suffix='' if f.name=='index.html' else f.name
    text=re.sub(r'(<link rel="canonical" href=")[^"]*(">)',lambda m:m[1]+base+suffix+m[2],text)
    text=re.sub(r'(<meta property="og:url" content=")[^"]*(">)',lambda m:m[1]+base+suffix+m[2],text)
    f.write_text(text,encoding='utf-8')
files=sorted(root.glob('*.html'),key=lambda f:(f.name!='index.html',f.name))
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{base}{"" if f.name=="index.html" else f.name}</loc></url>\n' for f in files)+'</urlset>\n'
(root/'sitemap.xml').write_text(xml,encoding='utf-8')
(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n',encoding='utf-8')
print('Configured',len(files),'pages for',base)
