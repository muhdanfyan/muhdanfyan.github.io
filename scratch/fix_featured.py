
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

# Re-add mPaD consolidated project
mpad_project = {
  "slug": "mpad",
  "title": "mPaD (Mitrapad Ecosystem)",
  "title_en": "mPaD (Mitrapad Ecosystem)",
  "year": "2025",
  "category": "Product Suite",
  "category_en": "Product Suite",
  "available_langs": ["id", "en"],
  "image": "img/screenshots/e-retribusi.png",
  "description": "Ekosistem digital terpadu untuk pengelolaan pajak dan retribusi daerah secara real-time.",
  "description_en": "Integrated digital ecosystem for real-time local tax and retribution management.",
  "url": "https://adminwiyasa.site",
  "full_description": "mPaD (Mitrapad) adalah solusi Enterprise Resource Planning (ERP) untuk pemerintah daerah yang mencakup modul Admin, API Gateway (H2H Multi-bank), serta aplikasi mobile untuk petugas lapangan dan masyarakat.",
  "full_description_en": "mPaD (Mitrapad) is an Enterprise Resource Planning (ERP) solution for local governments including Admin modules, API Gateway (H2H Multi-bank), and mobile applications for field officers and citizens.",
  "tech_stack": ["Laravel", "PostgreSQL", "React Native", "Redis", "Docker"],
  "highlights": ["Multi-tenant Architecture", "H2H Banking Integration", "Offline-first Mobile Sync"],
  "highlights_en": ["Multi-tenant Architecture", "H2H Banking Integration", "Offline-first Mobile Sync"],
  "project_type": "Government",
  "difficulty_level": "Expert",
  "difficulty_score": 98,
  "is_featured": True
}

# Remove any existing mpad/launch-mpad that might conflict or be duplicates if desired, 
# but user just said "pindahkan" and "mpad disimpan di halaman utama".
# I'll replace the one with slug 'mpad' if exists, else append.

portfolio = data.get('portfolio', [])
new_portfolio = [p for p in portfolio if p.get('slug') != 'mpad']
new_portfolio.insert(0, mpad_project)

# Ensure quranpwa is NOT featured
for p in new_portfolio:
    if p.get('slug') == 'quranpwa':
        p['is_featured'] = False
        
# Sort: Featured first, then year desc
new_portfolio.sort(key=lambda x: (not x.get('is_featured', False), -(int(x.get('year', '0') if str(x.get('year')).isdigit() else '0'))))

data['portfolio'] = new_portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print('mPaD added as featured, QuranPWA removed from featured.')
