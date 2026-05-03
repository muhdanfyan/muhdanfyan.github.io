
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

# List of identified forks based on user request and GitHub data
forks_to_remove = [
    'merchap', 'merch_ap', 'ladziiz', 'ladziidz-catering', 
    'afbarbershop', 'strix', 'simrs-api', 'retribusi-pos', 
    'whatsapp-bot', 'tpasaas', 'AutoPentestX', 'siakad',
    'some-investment-books', 'buku-masjid', 'app-mod-workshop',
    'floating-awesome-button', 'wp-calo'
]

new_portfolio = []
for project in portfolio:
    slug = str(project.get('slug', '')).lower()
    title = str(project.get('title', '')).lower()
    
    is_fork = False
    for fork in forks_to_remove:
        if fork in slug or fork in title or slug in fork or title in fork:
            # Special check for short names to avoid false positives
            if len(fork) > 3:
                is_fork = True
                break
    
    if not is_fork:
        new_portfolio.append(project)
    else:
        print(f"Removing fork: {project.get('title')} ({project.get('slug')})")

data['portfolio'] = new_portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Cleanup complete. Remaining: {len(new_portfolio)}")
