#!/usr/bin/env python3
import os
import glob
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, 'src/pages')

exclude = ['404.astro', 'about/index.astro', 'contact/index.astro', 'privacy-policy/index.astro', 'index.astro']

all_astro = glob.glob(os.path.join(PAGES_DIR, '**/*.astro'), recursive=True)
content_pages = [p for p in all_astro if os.path.relpath(p, PAGES_DIR) not in exclude]

print(f"Total content pages to process for MobileToc: {len(content_pages)}")

for p in sorted(content_pages):
    with open(p, 'r') as f:
        content = f.read()

    rel_from_pages = os.path.relpath(p, PAGES_DIR)
    
    if '<MobileToc' in content:
        print(f"Skipping already present: {rel_from_pages}")
        continue

    depth = rel_from_pages.count('/') # e.g. classes/warrior.astro -> 1
    rel_prefix = '../' * (depth + 1) # e.g. ../../components/MobileToc.astro

    # 1. Add import in frontmatter
    fm_pattern = r'^(---\s*[\s\S]*?)(---)'
    fm_match = re.search(fm_pattern, content)
    if not fm_match:
        print(f"Warning: No frontmatter in {rel_from_pages}")
        continue
    
    fm_body = fm_match.group(1)
    if 'import MobileToc' not in fm_body:
        import_stmt = f'import MobileToc from "{rel_prefix}components/MobileToc.astro";\n'
        # Insert after import DualSidebar
        if 'import DualSidebar' in fm_body:
            fm_body = fm_body.replace('import DualSidebar', import_stmt + 'import DualSidebar')
        else:
            fm_body = fm_body + import_stmt
        content = fm_body + content[fm_match.end() - 3:]

    # 2. Insert <MobileToc tocHeadings={tocHeadings} /> right after </header> inside article-main
    mobile_toc_tag = '\n\n        <!-- Mobile Table of Contents (≤980px) -->\n        <MobileToc tocHeadings={tocHeadings} />'
    
    # Try after </header>
    header_end = content.find('</header>')
    if header_end != -1:
        insert_pos = header_end + len('</header>')
        content = content[:insert_pos] + mobile_toc_tag + content[insert_pos:]
    else:
        # If no </header>, insert right after <article class="article-main" ...>
        article_match = re.search(r'<article class="article-main"[^>]*>', content)
        if article_match:
            insert_pos = article_match.end()
            content = content[:insert_pos] + mobile_toc_tag + content[insert_pos:]
        else:
            print(f"Warning: neither header nor article-main found in {rel_from_pages}")
            continue

    with open(p, 'w') as f:
        f.write(content)
    print(f"Added MobileToc to: {rel_from_pages}")
