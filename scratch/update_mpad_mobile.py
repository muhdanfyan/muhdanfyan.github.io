
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

# Update mPaD
for project in portfolio:
    if project.get('slug') == 'mpad':
        project['highlights'] = [
            "Arsitektur Driver-Based (Scalable)",
            "Keamanan HMAC-SHA256 & JIT Calculation",
            "Integrasi Domain Pemerintahan (.go.id)",
            "Mobile App untuk Masyarakat & Petugas Lapangan",
            "Workflow DevOps dengan Expect Scripts"
        ]
        project['highlights_en'] = [
            "Driver-Based Architecture (Scalable)",
            "HMAC-SHA256 & JIT Calculation Security",
            "Government Domain Integration (.go.id)",
            "Mobile App for Citizens & Field Officers",
            "DevOps Workflow with Expect Scripts"
        ]
        project['full_description'] += " Ekosistem ini juga mencakup aplikasi mobile bagi masyarakat untuk kemudahan akses pembayaran dan pengecekan tagihan secara mandiri."
        project['full_description_en'] += " This ecosystem also includes a mobile application for citizens to easily access payments and check bills independently."

# Add QuranPWA if not exists
quran_exists = any(p.get('slug') == 'quranpwa' for p in portfolio)
if not quran_exists:
    quran = {
        "slug": "quranpwa",
        "title": "Quran PWA",
        "title_en": "Quran PWA",
        "year": "2026",
        "category": "PWA",
        "category_en": "PWA",
        "available_langs": ["id", "en"],
        "image": "https://quranpwa-gilt.vercel.app/icon-192.svg",
        "description": "Aplikasi Al-Qur'an digital berbasis PWA dengan fitur offline-first.",
        "description_en": "Digital Al-Qur'an application based on PWA with offline-first features.",
        "url": "https://quranpwa-gilt.vercel.app",
        "tech_stack": ["React", "TypeScript", "Vite", "PWA", "Tailwind CSS"],
        "project_type": "Personal/Research",
        "difficulty_level": "Intermediate",
        "difficulty_score": 82
    }
    portfolio.append(quran)

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Manifest updated with mPaD mobile and QuranPWA.")
