
import json
import os

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

# 1. Update existing projects with categories and difficulty
for project in portfolio:
    slug = project.get('slug', project.get('title', '').lower().replace(' ', ''))
    
    # Defaults
    if 'project_type' not in project:
        if any(kw in slug for kw in ['retribusi', 'simpad', 'baubau', 'lurah']):
            project['project_type'] = 'Government'
        elif any(kw in slug for kw in ['onecreative', 'kassa', 'umkm', 'barber']):
            project['project_type'] = 'UMKM'
        elif any(kw in slug for kw in ['mbg', 'siakad', 'simrs']):
            project['project_type'] = 'Corporate'
        elif any(kw in slug for kw in ['aindea', 'quranta', 'strix', 'bot']):
            project['project_type'] = 'Personal/Research'
        else:
            project['project_type'] = 'Personal/Education'

    if 'difficulty_level' not in project:
        if project['project_type'] in ['Government', 'Corporate']:
            project['difficulty_level'] = 'Expert'
            project['difficulty_score'] = 95
        elif any(kw in slug for kw in ['aindea', 'kassa', 'security']):
            project['difficulty_level'] = 'Advanced'
            project['difficulty_score'] = 90
        else:
            project['difficulty_level'] = 'Intermediate'
            project['difficulty_score'] = 80

# 2. Add mPaD if not exists
mpad_exists = any(p.get('slug') == 'mpad' for p in portfolio)
if not mpad_exists:
    mpad = {
        "slug": "mpad",
        "title": "mPaD (Mitrapad Ecosystem)",
        "title_en": "mPaD (Mitrapad Ecosystem)",
        "year": "2026",
        "category": "Financial System",
        "category_en": "Financial System",
        "available_langs": ["id", "en"],
        "image": "img/screenshots/mpad.png",
        "description": "Ekosistem integrasi pendapatan daerah dan pembayaran multi-bank (H2H).",
        "description_en": "Regional revenue integration ecosystem and multi-bank payment (H2H).",
        "url": "https://github.com/muhdanfyan/launch-mpad",
        "full_description": "mPaD adalah platform middleware finansial yang menghubungkan sistem pemerintah daerah dengan berbagai bank mitra. Menggunakan arsitektur Driver-Based Manager untuk skalabilitas integrasi bank baru secara instan.",
        "full_description_en": "mPaD is a financial middleware platform that connects local government systems with various partner banks. Utilizing a Driver-Based Manager architecture for instant scalability of new bank integrations.",
        "tech_stack": ["PHP", "Laravel", "MySQL", "HMAC-SHA256", "Redis"],
        "impact": "Mempercepat proses integrasi bank dari mingguan menjadi harian, memastikan akurasi data denda JIT (Just-In-Time), dan meningkatkan transparansi PAD.",
        "impact_en": "Accelerating bank integration processes from weeks to days, ensuring JIT (Just-In-Time) penalty data accuracy, and increasing regional revenue transparency.",
        "tech_rationale": "Arsitektur Driver-Based dipilih untuk memisahkan logika spesifik bank (Inquiry/Notify) dari core system. HMAC-SHA256 digunakan untuk menjamin integritas data antar sistem finansial.",
        "tech_rationale_en": "Driver-Based architecture was chosen to separate bank-specific logic (Inquiry/Notify) from the core system. HMAC-SHA256 is used to guarantee data integrity between financial systems.",
        "project_type": "Government",
        "difficulty_level": "Expert",
        "difficulty_score": 98,
        "is_featured": True
    }
    # Insert at the top
    portfolio.insert(0, mpad)

# 3. Ensure MBG and Aindea are featured
for project in portfolio:
    if project.get('slug') in ['mbgone', 'aindea', 'onecreative']:
        project['is_featured'] = True

data['portfolio'] = portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Manifest updated successfully.")
