#!/usr/bin/env python3
"""
build_teaching.py — Generate halaman /mengajar/ dari content/teaching/*/index.mdoc

Menghasilkan:
  dist/mengajar/index.html          — daftar semua pengalaman mengajar
  dist/mengajar/<slug>/index.html   — halaman detail per entri
  mengajar/...                      — mirror di root (untuk kompatibilitas)

Sumber kebenaran: content/teaching/<slug>/index.mdoc (YAML frontmatter + markdown body)

Usage: python3 scripts/build_teaching.py
"""
import html
import json
import os
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CONTENT = BASE / "content" / "teaching"
DIST = BASE / "dist" / "mengajar"
ROOT = BASE / "mengajar"

# ----------------------------------------------------------------------------
# Frontmatter & markdown helpers
# ----------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML-ish frontmatter (key: "value" sederhana) + body."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")

    data = {}
    for line in raw.split("\n"):
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        if val in ("true", "True"):
            data[key] = True
        elif val in ("false", "False"):
            data[key] = False
        elif val.isdigit():
            data[key] = int(val)
        else:
            data[key] = val
    return data, body


def md_to_html(md: str) -> str:
    """Konversi markdown sederhana → HTML (paragraf, list, bold, italic, link, img)."""
    lines = md.split("\n")
    out, buf, in_ul = [], [], False

    def flush_par():
        if buf:
            out.append("<p>" + inline(" ".join(buf).strip()) + "</p>")
            buf.clear()

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_par()
            close_ul()
            continue
        img = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if img:
            flush_par(); close_ul()
            out.append(f'<p><img src="{img.group(2)}" alt="{html.escape(img.group(1))}"></p>')
            continue
        li = re.match(r"^[-*]\s+(.*)$", line.strip())
        if li:
            flush_par()
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append("<li>" + inline(li.group(1)) + "</li>")
            continue
        flush_par(); close_ul()
        buf.append(line.strip())

    flush_par(); close_ul()
    return "\n".join(out)


def inline(t: str) -> str:
    """Inline markdown: escape dulu, lalu terapkan penanda."""
    # simpan link & gambar agar tidak ter-escape
    t = re.sub(r"\[(.+?)\]\((.+?)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


# ----------------------------------------------------------------------------
# HTML shell
# ----------------------------------------------------------------------------

LINKS_CSS = """
:root{--indigo:#4f46e5;--slate:#0f172a}
*{box-sizing:border-box}
body{margin:0;font-family:Inter,-apple-system,Segoe UI,Roboto,sans-serif;background:#fff;color:#0f172a;line-height:1.65}
a{color:var(--indigo);text-decoration:none}
nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-bottom:1px solid #f1f5f9}
nav .wrap{max-width:1120px;margin:0 auto;padding:16px 24px;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:900;font-size:1.4rem;background:linear-gradient(90deg,#4f46e5,#9333ea);-webkit-background-clip:text;background-clip:text;color:transparent}
nav .links a{margin-left:24px;font-weight:700;font-size:.9rem;color:#475569}
nav .links a:hover{color:var(--indigo)}
main{max-width:1120px;margin:0 auto;padding:56px 24px 96px}
h1{font-size:2.4rem;font-weight:800;margin:0 0 12px}
.lead{color:#64748b;margin-bottom:48px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:28px}
.card{border:1px solid #f1f5f9;border-radius:20px;overflow:hidden;background:#fff;transition:.3s;display:flex;flex-direction:column}
.card:hover{box-shadow:0 20px 40px -12px rgba(15,23,42,.18);transform:translateY(-4px)}
.card img{width:100%;height:200px;object-fit:cover;display:block}
.card .body{padding:22px;flex:1;display:flex;flex-direction:column}
.badge{display:inline-block;font-size:.68rem;font-weight:900;letter-spacing:.05em;text-transform:uppercase;color:var(--indigo);background:#eef2ff;padding:4px 10px;border-radius:999px;margin-bottom:12px}
.card h3{margin:0 0 8px;font-size:1.15rem}
.topic{color:#64748b;font-style:italic;font-size:.9rem;margin:0 0 14px}
.desc{color:#475569;font-size:.9rem;margin:0}
.more{margin-top:auto;padding-top:18px;border-top:1px solid #f8fafc;color:var(--indigo);font-weight:700;font-size:.85rem}
.detail-head{max-width:820px;margin:0 auto 40px;text-align:center}
.detail-head .meta{color:#94a3b8;font-weight:700;font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:14px}
.detail-head h1{font-size:2rem}
.detail-hero{max-width:900px;margin:0 auto 44px}
.detail-hero img{width:100%;border-radius:24px;box-shadow:0 24px 48px -16px rgba(15,23,42,.25)}
.content{max-width:820px;margin:0 auto;color:#334155}
.content h2{font-size:1.4rem;border-bottom:1px solid #f1f5f9;padding-bottom:8px;margin-top:40px}
.content h3{font-size:1.15rem;margin-top:28px}
.content ul{padding-left:22px}
.content li{margin-bottom:8px}
.content img{width:100%;border-radius:20px;margin:28px 0}
.content strong{color:#0f172a}
.back{max-width:820px;margin:56px auto 0;padding-top:24px;border-top:1px solid #f1f5f9}
.back a{font-weight:700}
footer{max-width:1120px;margin:0 auto;padding:32px 24px;color:#94a3b8;font-size:.85rem;border-top:1px solid #f1f5f9}
"""


def shell(title: str, desc: str, canonical: str, body: str, image: str = "") -> str:
    og_img = image or "/img/screenshots/default.png"
    if og_img.startswith("/"):
        og_img = "https://muhdanfyan.github.io" + og_img
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta name="author" content="Muhdan Fyan Syah Sofian">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Muhdan Fyan Portfolio">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@muhdanfyan">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>{LINKS_CSS}</style>
</head>
<body>
<nav><div class="wrap">
<a class="logo" href="/">MUHDAN FYAN</a>
<div class="links">
<a href="/#portfolio">Portofolio</a>
<a href="/#writing">Tulisan</a>
<a href="/mengajar/">Mengajar</a>
</div>
</div></nav>
<main>
{body}
</main>
<footer>
&copy; {__import__('datetime').datetime.now().year} Muhdan Fyan Syah Sofian &middot; Pengalaman Mengajar &amp; Materi
</footer>
</body>
</html>
"""


# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------

def load_entries() -> list[dict]:
    entries = []
    if not CONTENT.exists():
        return entries
    for d in sorted(CONTENT.iterdir()):
        f = d / "index.mdoc"
        if not (d.is_dir() and f.exists()):
            continue
        fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        if not fm.get("slug"):
            fm["slug"] = d.name
        fm["_body_html"] = md_to_html(body)
        fm["_body_md"] = body
        entries.append(fm)
    entries.sort(key=lambda e: (e.get("order", 999), str(e.get("period", ""))))
    return entries


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""), quote=True)


def build_index(entries: list[dict]) -> str:
    cards = []
    for e in entries:
        slug = e["slug"]
        img = e.get("image", "")
        period = e.get("period", "")
        event = e.get("event", slug)
        topic = e.get("topic", "")
        desc = e.get("summary") or e.get("summary_en") or ""
        cards.append(f"""<a class="card" href="/mengajar/{esc(slug)}/">
<img src="{esc(img)}" alt="{esc(event)}" loading="lazy">
<div class="body">
<span class="badge">{esc(period)}</span>
<h3>{esc(event)}</h3>
<p class="topic">&ldquo;{esc(topic)}&rdquo;</p>
<p class="desc">{esc(desc[:180])}{'&hellip;' if len(desc) > 180 else ''}</p>
<span class="more">Lihat Detail &rarr;</span>
</div>
</a>""")
    body = f"""<h1>Pengalaman Mengajar &amp; Materi</h1>
<p class="lead">Kelas, webinar, dan forum tempat saya berbagi ilmu — dari teknologi, AI, hingga literasi digital.</p>
<div class="grid">
{chr(10).join(cards)}
</div>"""
    return shell("Pengalaman Mengajar &amp; Materi | Muhdan Fyan",
                 "Kumpulan pengalaman mengajar, menjadi narasumber, dan pemateri kelas teknologi serta AI.",
                 "https://muhdanfyan.github.io/mengajar/", body)


def build_detail(e: dict) -> str:
    slug = e["slug"]
    event = e.get("event", slug)
    topic = e.get("topic", "")
    period = e.get("period", "")
    img = e.get("image", "")
    link = e.get("link", "")
    body_html = e.get("_body_html", "")

    cta = ""
    if link:
        cta = f"""<div style="max-width:820px;margin:48px auto 0;padding:28px;background:#f8fafc;border:1px solid #f1f5f9;border-radius:20px;display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center">
<div><strong style="display:block;margin-bottom:4px">Ingin melihat lebih lanjut?</strong>
<span style="color:#64748b;font-size:.9rem">Dokumentasi resmi dan materi tersedia di link berikut.</span></div>
<a href="{esc(link)}" target="_blank" rel="noopener" style="background:#4f46e5;color:#fff;padding:12px 28px;border-radius:12px;font-weight:700">Kunjungi Link</a>
</div>"""

    body = f"""<div class="detail-head">
<div class="meta">{esc(period)} &middot; {esc(event)}</div>
<h1>{esc(topic)}</h1>
</div>
<div class="detail-hero"><img src="{esc(img)}" alt="{esc(event)}"></div>
<div class="content">
{body_html}
</div>
{cta}
<div class="back"><a href="/mengajar/">&larr; Kembali ke Pengalaman Mengajar</a></div>"""

    return shell(f"{topic} | Pengalaman Mengajar",
                 e.get("summary", "")[:200] or event,
                 f"https://muhdanfyan.github.io/mengajar/{slug}/",
                 body, img)


def main():
    entries = load_entries()
    if not entries:
        print("⚠️  Tidak ada entri di content/teaching/")
        return

    for target in (DIST, ROOT):
        (target).mkdir(parents=True, exist_ok=True)

    idx = build_index(entries)
    (DIST / "index.html").write_text(idx, encoding="utf-8")
    (ROOT / "index.html").write_text(idx, encoding="utf-8")

    for e in entries:
        page = build_detail(e)
        for target in (DIST / e["slug"], ROOT / e["slug"]):
            target.mkdir(parents=True, exist_ok=True)
            (target / "index.html").write_text(page, encoding="utf-8")

    # Sinkronkan aset gambar teaching
    src_img = BASE / "public" / "img" / "teaching"
    if src_img.exists():
        for target in (BASE / "img" / "teaching", BASE / "dist" / "img" / "teaching"):
            target.mkdir(parents=True, exist_ok=True)
            for f in src_img.iterdir():
                if f.is_file():
                    shutil.copy2(f, target / f.name)

    # Update sitemap
    for sm in (BASE / "dist" / "sitemap-0.xml", BASE / "garden-sitemap.xml"):
        if not sm.exists():
            continue
        x = sm.read_text(encoding="utf-8")
        for e in entries:
            url = f"https://muhdanfyan.github.io/mengajar/{e['slug']}/"
            if url in x:
                continue
            x = x.replace("</urlset>",
                          f"<url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url></urlset>")
        sm.write_text(x, encoding="utf-8")

    print(f"✅ mengajar: {len(entries)} halaman + index → dist/mengajar/ & mengajar/")
    for e in entries:
        print(f"   • {e['slug']}")


if __name__ == "__main__":
    main()
