#!/usr/bin/env python3
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')

def fix_partial_pages():
    print("--- Fixing partial pages ---")
    
    # 1. 6 Race detail pages: orc, elf, nightborn, dullahan, seraph, celestine
    race_slugs = ['orc', 'elf', 'nightborn', 'dullahan', 'seraph', 'celestine']
    for r in race_slugs:
        p = os.path.join(BASE_DIR, f'src/pages/races/{r}.astro')
        with open(p, 'r') as f:
            content = f.read()
        
        # Replace container
        content = re.sub(
            r'<div class="container"[^>]*style="[^"]*max-width:\s*860px[^"]*"[^>]*>',
            '<div class="container container-guide" style="margin: 0 auto; padding: 40px 20px;">',
            content
        )
        
        # If not already containing article-layout
        if 'article-layout has-dual-sidebar' not in content:
            # Insert after </nav>
            nav_end = content.find('</nav>')
            if nav_end != -1:
                insert_pos = nav_end + len('</nav>')
                replacement = '\n\n    <div class="article-layout has-dual-sidebar">\n      <article class="article-main" style="line-height: 1.7; color: var(--ink);">'
                content = content[:insert_pos] + replacement + content[insert_pos:]
        
        with open(p, 'w') as f:
            f.write(content)
        print(f"Fixed race page: {r}.astro")

    # 2. classes/index.astro, tier-list/index.astro, classes/stats.astro, classes/super-classes.astro, traits/index.astro, codes/index.astro
    hub_files = [
        'src/pages/classes/index.astro',
        'src/pages/tier-list/index.astro',
        'src/pages/classes/stats.astro',
        'src/pages/classes/super-classes.astro',
        'src/pages/traits/index.astro',
        'src/pages/codes/index.astro',
    ]
    for rel_path in hub_files:
        p = os.path.join(BASE_DIR, rel_path)
        with open(p, 'r') as f:
            content = f.read()
        
        # If <div class="article-layout has-dual-sidebar"> is immediately followed by <header
        pattern = r'(<div class="article-layout has-dual-sidebar">\s*)(<header)'
        if re.search(pattern, content):
            content = re.sub(
                pattern,
                r'\1<article class="article-main" style="line-height: 1.7; color: var(--ink);">\n      \2',
                content,
                count=1
            )
            with open(p, 'w') as f:
                f.write(content)
            print(f"Fixed article-main open in: {rel_path}")

    # 3. races/best-races.astro
    best_races_path = os.path.join(BASE_DIR, 'src/pages/races/best-races.astro')
    with open(best_races_path, 'r') as f:
        br_content = f.read()
    if '<article class="article-main"' not in br_content:
        # Move header inside article-main and remove unclassed <article>
        br_content = br_content.replace(
            '<div class="article-layout has-dual-sidebar">\n    <header',
            '<div class="article-layout has-dual-sidebar">\n      <article class="article-main" style="line-height: 1.7; color: var(--ink);">\n        <header'
        )
        br_content = br_content.replace(
            '<article style="line-height: 1.7; color: var(--ink);">\n      <!-- Summary Callout -->',
            '<!-- Summary Callout -->'
        )
        with open(best_races_path, 'w') as f:
            f.write(br_content)
        print("Fixed races/best-races.astro")

    # 4. calculator/index.astro
    calc_path = os.path.join(BASE_DIR, 'src/pages/calculator/index.astro')
    with open(calc_path, 'r') as f:
        calc_content = f.read()
    if '<DualSidebar' not in calc_content:
        # Add <article class="article-main"> after <div class="article-layout has-dual-sidebar">
        calc_content = calc_content.replace(
            '<div class="article-layout has-dual-sidebar">\n    <header',
            '<div class="article-layout has-dual-sidebar">\n      <article class="article-main" style="line-height: 1.7; color: var(--ink);">\n        <header'
        )
        # Before cross-linking section end line 419:
        # </section>\n  </div>\n\n  <!-- Interactive Client-side Script -->
        closing_pattern = r'(</section>\s*</div>)(\s*<!-- Interactive Client-side Script -->)'
        calc_content = re.sub(
            closing_pattern,
            r'</section>\n      </article>\n\n      <!-- Dual Sidebar V3 (ON THIS PAGE + EXPLORE THE WIKI) -->\n      <DualSidebar tocHeadings={tocHeadings} currentUrl="/calculator/" />\n    </div>\n  </div>\2',
            calc_content,
            count=1
        )
        with open(calc_path, 'w') as f:
            f.write(calc_content)
        print("Fixed calculator/index.astro")

def apply_dual_sidebar_to_page(rel_path: str):
    p = os.path.join(BASE_DIR, rel_path)
    with open(p, 'r') as f:
        content = f.read()
    
    if '<DualSidebar' in content and 'article-layout has-dual-sidebar' in content and '<article class="article-main"' in content:
        print(f"Skipping already complete: {rel_path}")
        return

    # Extract canonical URL
    canon_match = re.search(r'canonical=["\']([^"\']+)["\']', content)
    if not canon_match:
        print(f"Error: No canonical found in {rel_path}")
        return
    canonical = canon_match.group(1)

    # Calculate relative imports
    depth = rel_path.count('/') - 1 # e.g. src/pages/gear/weapons.astro -> 3 - 1 = 2
    rel_prefix = '../' * depth

    # 1. Add frontmatter imports
    fm_pattern = r'^(---\s*[\s\S]*?)(---)'
    fm_match = re.search(fm_pattern, content)
    if not fm_match:
        print(f"Error: Frontmatter not found in {rel_path}")
        return
    
    fm_body = fm_match.group(1)
    if 'import DualSidebar' not in fm_body:
        import_stmt = f'\nimport DualSidebar from "{rel_prefix}components/DualSidebar.astro";\nimport {{ extractTocFromAstroUrl }} from "{rel_prefix}utils/toc";\n\nconst tocHeadings = extractTocFromAstroUrl(import.meta.url);\n'
        new_fm = fm_body + import_stmt + '---\n'
        content = content[:fm_match.start()] + new_fm + content[fm_match.end():]
    
    # 2. Ensure IDs on h2 and h3
    def add_heading_ids(body_text: str) -> str:
        def rep_h(m):
            tag = m.group(1)
            attrs = m.group(2) or ''
            inner = m.group(3)
            # check if id already exists
            if re.search(r'\bid=["\']', attrs):
                return m.group(0)
            clean_text = re.sub(r'<[^>]+>', '', inner).strip()
            if not clean_text:
                return m.group(0)
            slug = slugify(clean_text)
            return f'<{tag} id="{slug}"{attrs}>{inner}</{tag}>'
        
        return re.sub(r'<(h[23])(\s+[^>]*)?>(.*?)</\1>', rep_h, body_text, flags=re.IGNORECASE | re.DOTALL)

    # 3. Update HTML markup
    # Find container
    content = re.sub(
        r'<div class="container"[^>]*style="[^"]*"[^>]*>',
        '<div class="container container-guide" style="margin: 0 auto; padding: 40px 20px;">',
        content,
        count=1
    )

    # If <article> is already present
    if '<article' in content:
        # Check if breadcrumbs are outside or inside article
        # Usually:
        # <nav class="breadcrumbs" ...>...</nav>
        # <article style="...">...</article>
        # We transform to:
        # <div class="article-layout has-dual-sidebar">
        #   <article class="article-main" style="line-height: 1.7; color: var(--ink);">
        #     ...
        #   </article>
        #   <DualSidebar tocHeadings={tocHeadings} currentUrl="{canonical}" />
        # </div>
        
        # Replace opening article
        content = re.sub(
            r'<article(\s+style="[^"]*")?>',
            '<div class="article-layout has-dual-sidebar">\n      <article class="article-main" style="line-height: 1.7; color: var(--ink);">',
            content,
            count=1
        )
        
        # Replace closing </article>
        content = re.sub(
            r'</article>',
            f'</article>\n\n      <!-- Dual Sidebar V3 (ON THIS PAGE + EXPLORE THE WIKI) -->\n      <DualSidebar tocHeadings={{tocHeadings}} currentUrl="{canonical}" />\n    </div>',
            content,
            count=1
        )
    else:
        # Page without <article>, e.g. adventures/index.astro
        # Structure is usually:
        # <nav class="breadcrumbs" ...>...</nav>
        # <header ...>...</header>
        # ...
        # </div>
        # </BaseLayout>
        nav_pos = content.find('</nav>')
        if nav_pos != -1:
            split_pos = nav_pos + len('</nav>')
            top_part = content[:split_pos]
            rest = content[split_pos:]
            
            # Find the closing </div> of container before </BaseLayout>
            last_div_idx = rest.rfind('</div>')
            if last_div_idx != -1:
                inner_content = rest[:last_div_idx]
                bottom_part = rest[last_div_idx:]
                
                content = (
                    top_part +
                    '\n\n    <div class="article-layout has-dual-sidebar">\n' +
                    '      <article class="article-main" style="line-height: 1.7; color: var(--ink);">' +
                    inner_content +
                    '\n      </article>\n\n' +
                    f'      <!-- Dual Sidebar V3 (ON THIS PAGE + EXPLORE THE WIKI) -->\n' +
                    f'      <DualSidebar tocHeadings={{tocHeadings}} currentUrl="{canonical}" />\n' +
                    '    </div>' +
                    bottom_part
                )

    # Finally add heading IDs to all h2 / h3
    content = add_heading_ids(content)

    with open(p, 'w') as f:
        f.write(content)
    print(f"Applied DualSidebar to: {rel_path}")

def main():
    fix_partial_pages()

    target_pages = [
        'src/pages/adventures/difficulty.astro',
        'src/pages/adventures/index.astro',
        'src/pages/adventures/lineage-ranks.astro',
        'src/pages/adventures/torment.astro',
        'src/pages/codes/not-working.astro',
        'src/pages/codes/redeem.astro',
        'src/pages/combat/energy.astro',
        'src/pages/gear/armor-sets.astro',
        'src/pages/gear/index.astro',
        'src/pages/gear/legendary-powers.astro',
        'src/pages/gear/weapons.astro',
        'src/pages/guilds/arena.astro',
        'src/pages/guilds/castle-repair.astro',
        'src/pages/guilds/guild-raids.astro',
        'src/pages/guilds/index.astro',
        'src/pages/guilds/oaths.astro',
        'src/pages/races/index.astro',
        'src/pages/tier-list/class-tier-list.astro',
        'src/pages/tier-list/race-tier-list.astro',
        'src/pages/tier-list/talent-tier-list.astro',
        'src/pages/updates/index.astro',
        'src/pages/updates/patch-notes.astro',
    ]

    for p in target_pages:
        apply_dual_sidebar_to_page(p)

if __name__ == '__main__':
    main()
