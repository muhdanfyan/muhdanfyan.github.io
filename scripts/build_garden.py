#!/usr/bin/env python3
"""
build_garden.py — Convert .md files to .html for Digital Garden
Background putih bersih, responsive, minimalis.
Usage: python3 scripts/build_garden.py
"""

import os
import re
import json
import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
OUTPUT_DIR = BASE_DIR  # Output di root biar akses via muhdanfyan.github.io/catatan/

SECTIONS = {
    "catatan": {"title": "Catatan", "icon": "📝", "desc": "Pemikiran, diskusi, dan refleksi"},
    "laporan": {"title": "Laporan", "icon": "📅", "desc": "Schedule dan laporan harian"},
    "project": {"title": "Proyek", "icon": "📄", "desc": "Dokumentasi proyek"},
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Muhdan Fyan</title>
    <meta name="description" content="{desc}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background: #ffffff;
            color: #1e293b;
            line-height: 1.8;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 0 24px; }}
        
        /* Nav */
        nav {{
            position: fixed; top: 0; width: 100%; z-index: 50;
            background: rgba(255,255,255,0.9); backdrop-filter: blur(12px);
            border-bottom: 1px solid #f1f5f9;
        }}
        nav .container {{
            display: flex; justify-content: space-between; align-items: center;
            padding-top: 16px; padding-bottom: 16px;
        }}
        nav .logo {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800; font-size: 1.25rem;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-decoration: none;
        }}
        nav .links {{ display: flex; gap: 20px; align-items: center; }}
        nav .links a {{
            color: #64748b; text-decoration: none; font-size: 0.875rem; font-weight: 600;
            transition: color 0.2s;
        }}
        nav .links a:hover {{ color: #6366f1; }}
        nav .links .back-btn {{
            padding: 6px 14px; background: #f8fafc; border-radius: 8px;
            border: 1px solid #e2e8f0; font-size: 0.8rem; font-weight: 600;
            color: #475569; text-decoration: none; transition: all 0.2s;
        }}
        nav .links .back-btn:hover {{ border-color: #6366f1; color: #6366f1; }}

        main {{ padding-top: 80px; padding-bottom: 60px; }}
        
        /* Header */
        .page-header {{ padding: 40px 0 32px; }}
        .page-header .icon {{ font-size: 2rem; margin-bottom: 8px; }}
        .page-header h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2rem; font-weight: 800; color: #0f172a;
            margin-bottom: 8px;
        }}
        .page-header p {{ color: #64748b; font-size: 1rem; }}

        /* List */
        .list {{ display: flex; flex-direction: column; gap: 12px; }}
        .list-item {{
            display: block; padding: 20px 24px;
            background: #f8fafc; border: 1px solid #e2e8f0;
            border-radius: 12px; text-decoration: none;
            color: inherit; transition: all 0.2s;
        }}
        .list-item:hover {{
            border-color: #6366f1; background: #f1f5ff;
            transform: translateY(-1px); box-shadow: 0 4px 12px rgba(99,102,241,0.1);
        }}
        .list-item .title {{
            font-weight: 600; font-size: 1.05rem; color: #0f172a;
            margin-bottom: 4px;
        }}
        .list-item .meta {{
            font-size: 0.8rem; color: #94a3b8; display: flex; gap: 12px;
        }}
        .list-item .meta .tag {{
            padding: 2px 8px; background: #eef2ff; color: #6366f1;
            border-radius: 4px; font-size: 0.7rem; font-weight: 500;
        }}
        .list-item .excerpt {{
            font-size: 0.9rem; color: #64748b; margin-top: 6px;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }}

        /* Article */
        article {{ padding: 24px 0; }}
        article h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2rem; font-weight: 800; color: #0f172a;
            margin-bottom: 8px; line-height: 1.3;
        }}
        article .article-meta {{
            font-size: 0.85rem; color: #94a3b8; margin-bottom: 32px;
            padding-bottom: 24px; border-bottom: 1px solid #f1f5f9;
            display: flex; gap: 16px; flex-wrap: wrap;
        }}
        article .article-meta .tag {{
            padding: 2px 10px; background: #eef2ff; color: #6366f1;
            border-radius: 4px; font-size: 0.75rem; font-weight: 500;
        }}
        article h2 {{ font-size: 1.4rem; font-weight: 700; margin: 28px 0 12px; color: #0f172a; }}
        article h3 {{ font-size: 1.15rem; font-weight: 600; margin: 24px 0 8px; color: #1e293b; }}
        article p {{ margin-bottom: 16px; color: #334155; }}
        article ul, article ol {{ margin-bottom: 16px; padding-left: 24px; }}
        article li {{ margin-bottom: 6px; color: #334155; }}
        article blockquote {{
            border-left: 4px solid #6366f1; background: #f8fafc;
            padding: 16px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;
            color: #475569; font-style: italic;
        }}
        article code {{
            background: #f1f5f9; padding: 2px 6px; border-radius: 4px;
            font-size: 0.85em; color: #6366f1;
        }}
        article pre {{
            background: #0f172a; color: #e2e8f0; padding: 20px; border-radius: 12px;
            overflow-x: auto; margin: 20px 0; font-size: 0.85rem; line-height: 1.6;
        }}
        article pre code {{ background: none; color: inherit; padding: 0; }}
        article img {{ max-width: 100%; border-radius: 12px; margin: 20px 0; border: 1px solid #f1f5f9; }}
        article a {{ color: #6366f1; text-decoration: underline; text-underline-offset: 2px; }}
        article hr {{ border: none; border-top: 1px solid #e2e8f0; margin: 32px 0; }}
        article table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        article th, article td {{ padding: 10px 14px; border: 1px solid #e2e8f0; text-align: left; font-size: 0.9rem; }}
        article th {{ background: #f8fafc; font-weight: 600; }}

        /* Footer */
        footer {{
            text-align: center; padding: 40px 0; font-size: 0.8rem; color: #94a3b8;
            border-top: 1px solid #f1f5f9;
        }}

        @media (max-width: 640px) {{
            .page-header h1 {{ font-size: 1.6rem; }}
            article h1 {{ font-size: 1.5rem; }}
            nav .links .desktop-only {{ display: none; }}
        }}
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">MUHDAN FYAN</a>
            <div class="links">
                <a href="/" class="desktop-only">Beranda</a>
                {nav_links}
                <a href="/" class="back-btn">← Kembali</a>
            </div>
        </div>
    </nav>
    <main>
        <div class="container">
            {content}
        </div>
    </main>
    <footer>
        <div class="container">
            © {year} Muhdan Fyan Syah Sofian
        </div>
    </footer>
</body>
</html>"""


def parse_frontmatter(text):
    """Parse YAML-like frontmatter from markdown."""
    fm = {"title": "", "date": "", "tags": [], "status": "published"}
    rest = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip().lower()
                    val = val.strip().strip('"').strip("'")
                    if key == "tags":
                        fm["tags"] = [t.strip().strip('"').strip("'") for t in val.split(",") if t.strip()]
                    else:
                        fm[key] = val
            rest = parts[2].strip()
    return fm, rest


def md_to_html(text):
    """Simple markdown to HTML converter."""
    html = ""
    in_code = False
    in_list = False
    list_type = None
    in_blockquote = False
    
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Code block
        if line.strip().startswith("```"):
            if in_code:
                html += "</code></pre>\n"
                in_code = False
            else:
                lang = line.strip().replace("```", "").strip()
                html += f'<pre><code class="language-{lang}">'
                in_code = True
            i += 1
            continue
        
        if in_code:
            html += line + "\n"
            i += 1
            continue
        
        # Close list if needed
        if in_list and not line.strip():
            if list_type == "ul":
                html += "</ul>\n"
            else:
                html += "</ol>\n"
            in_list = False
            list_type = None
            i += 1
            continue
        
        # Headers
        if line.startswith("## "):
            html += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("### "):
            html += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("# "):
            # Skip H1 (used as title from frontmatter)
            pass
        # Horizontal rule
        elif line.strip() in ("---", "***", "___"):
            html += "<hr>\n"
        # Blockquote
        elif line.startswith("> "):
            html += f"<blockquote><p>{line[2:]}</p></blockquote>\n"
        # Unordered list
        elif line.strip().startswith("- ") or line.strip().startswith("* "):
            if not in_list or list_type != "ul":
                if in_list:
                    html += "</ul>\n"
                html += "<ul>\n"
                in_list = True
                list_type = "ul"
            content = line.strip()[2:]
            html += f"<li>{content}</li>\n"
        # Ordered list
        elif re.match(r'^\d+[.)]\s', line.strip()):
            if not in_list or list_type != "ol":
                if in_list:
                    html += "</ol>\n"
                html += "<ol>\n"
                in_list = True
                list_type = "ol"
            content = re.sub(r'^\d+[.)]\s', '', line.strip())
            html += f"<li>{content}</li>\n"
        # Empty line
        elif not line.strip():
            if in_list:
                continue
            html += "<br>\n"
        # Paragraph (fallback)
        else:
            # Inline formatting
            content = line
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
            content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
            # Links
            content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', content)
            # Images
            content = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1">', content)
            html += f"<p>{content}</p>\n"
        i += 1
    
    if in_list:
        html += "</ul>\n" if list_type == "ul" else "</ol>\n"
    if in_code:
        html += "</code></pre>\n"
    
    return html


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def format_date(date_str):
    """Format date string to Indonesian format."""
    if not date_str:
        return ""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        months = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
        return f"{d.day} {months[d.month-1]} {d.year}"
    except:
        return date_str


def build_section(section_name):
    """Build HTML pages for a section (catatan/laporan/project)."""
    info = SECTIONS[section_name]
    src_dir = CONTENT_DIR / section_name
    dst_dir = OUTPUT_DIR / section_name
    
    # Create output directory
    dst_dir.mkdir(parents=True, exist_ok=True)
    
    # Collect all markdown files
    articles = []
    for f in sorted(src_dir.glob("*.md"), reverse=True):
        fm, content = parse_frontmatter(f.read_text(encoding="utf-8"))
        title = fm.get("title", f.stem.replace("-", " ").title())
        date = fm.get("date", "")
        tags = fm.get("tags", [])
        excerpt = content.strip()[:200].replace("\n", " ")
        slug = f.stem
        
        articles.append({
            "title": title,
            "date": date,
            "tags": tags,
            "slug": slug,
            "excerpt": excerpt,
            "fm": fm,
            "content": content,
        })
    
    # Build index page
    list_items = []
    for a in articles:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in a["tags"])
        date_str = format_date(a["date"])
        excerpt = a["excerpt"][:200] + ("..." if len(a["excerpt"]) > 200 else "")
        list_items.append(f"""
        <a href="/{section_name}/{a["slug"]}.html" class="list-item">
            <div class="title">{a["title"]}</div>
            <div class="meta">{date_str} {tags_html}</div>
            <div class="excerpt">{excerpt}</div>
        </a>""")
    
    nav_links = "".join(f'<a href="/{s}/">{SECTIONS[s]["title"]}</a>' 
                        for s in SECTIONS if s != section_name)
    
    index_content = f"""
    <div class="page-header">
        <div class="icon">{info["icon"]}</div>
        <h1>{info["title"]}</h1>
        <p>{info["desc"]}</p>
    </div>
    <div class="list">
        {"".join(list_items) if list_items else '<p style="color: #94a3b8; padding: 20px;">Belum ada konten.</p>'}
    </div>"""
    
    # Write index
    index_html = HTML_TEMPLATE.format(
        title=info["title"],
        desc=info["desc"],
        nav_links=nav_links,
        year=datetime.now().year,
        content=index_content,
    )
    (dst_dir / "index.html").write_text(index_html, encoding="utf-8")
    
    # Build individual article pages
    all_nav = "".join(f'<a href="/{s}/" class="desktop-only">{SECTIONS[s]["title"]}</a>' 
                      for s in SECTIONS)
    
    for a in articles:
        content_html = md_to_html(a["content"])
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in a["tags"])
        date_str = format_date(a["date"])
        
        article_content = f"""
        <article>
            <h1>{a["title"]}</h1>
            <div class="article-meta">
                <span>{date_str}</span>
                {tags_html}
            </div>
            {content_html}
        </article>"""
        
        article_html = HTML_TEMPLATE.format(
            title=f'{a["title"]} — Muhdan Fyan',
            desc=a["excerpt"][:160],
            nav_links=all_nav,
            year=datetime.now().year,
            content=article_content,
        )
        
        (dst_dir / f'{a["slug"]}.html').write_text(article_html, encoding="utf-8")
    
    return len(articles)


def build_sitemap():
    """Generate sitemap.xml for all garden pages."""
    urls = ["https://muhdanfyan.github.io/"]
    
    for section in SECTIONS:
        urls.append(f"https://muhdanfyan.github.io/{section}/")
        src_dir = CONTENT_DIR / section
        for f in src_dir.glob("*.md"):
            urls.append(f"https://muhdanfyan.github.io/{section}/{f.stem}.html")
    
    today = datetime.now().strftime("%Y-%m-%d")
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for url in urls:
        xml += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
  </url>
"""
    xml += "</urlset>"
    
    (OUTPUT_DIR / "garden-sitemap.xml").write_text(xml, encoding="utf-8")
    print(f"  ✅ Sitemap: {len(urls)} URLs")


def main():
    print("🌱 Membangun Digital Garden...\n")
    
    total = 0
    for section in SECTIONS:
        count = build_section(section)
        total += count
        print(f"  📁 {section}/ → {count} artikel")
    
    build_sitemap()
    
    print(f"\n✅ Selesai! Total {total} halaman terbit.")
    print(f"   📍 https://muhdanfyan.github.io/catatan/")
    print(f"   📍 https://muhdanfyan.github.io/laporan/")
    print(f"   📍 https://muhdanfyan.github.io/project/")


if __name__ == "__main__":
    main()
