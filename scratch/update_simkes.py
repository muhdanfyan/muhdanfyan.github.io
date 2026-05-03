
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

# Find and update the detailed Simkes project
# And filter out the duplicate short Simkes project
new_portfolio = []
simkes_found = False

for project in portfolio:
    title = str(project.get('title') or '')
    slug = str(project.get('slug') or '')
    url = str(project.get('url') or '')
    
    if title == 'Simkes':
        if slug == 'simkes':
            # This is the detailed one
            project['url'] = 'https://simkes-seven.vercel.app/'
            project['image'] = 'img/screenshots/simkes.png'
            project['title'] = 'SIMKES Dinkes Baubau'
            project['title_en'] = 'SIMKES Dinkes Baubau'
            project['description'] = 'Sistem Informasi Manajemen Kesehatan Dinas Kesehatan Kota Baubau.'
            project['description_en'] = 'Health Management Information System for Baubau Health Office.'
            project['full_description'] = 'SIMKES adalah sistem informasi terpadu untuk Dinas Kesehatan Kota Baubau yang mencakup visualisasi sebaran puskesmas, monitoring kasus P2P, kesehatan masyarakat, dan capaian program kesehatan secara real-time.'
            project['full_description_en'] = 'SIMKES is an integrated information system for the Baubau City Health Office that includes visualization of health center distribution, monitoring of infectious disease cases, public health, and real-time health program achievements.'
            project['tech_stack'] = ["Laravel", "Leaflet JS", "Tailwind CSS", "MySQL"]
            new_portfolio.append(project)
            simkes_found = True
        else:
            # This is the duplicate/short one, skip it
            continue
    else:
        new_portfolio.append(project)

data['portfolio'] = new_portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Simkes project updated and duplicates removed.")
