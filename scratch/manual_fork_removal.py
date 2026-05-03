
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

# Manually identified forks that might have different names
manual_forks = ['merchap', 'ladziiz', 'afbarbershop', 'strix', 'siakad', 'autopentestx']

new_portfolio = []
for project in portfolio:
    title = str(project.get('title') or '').lower()
    slug = str(project.get('slug') or '').lower()
    
    is_fork = False
    for f in manual_forks:
        if f in title or f in slug:
            is_fork = True
            break
            
    if not is_fork:
        new_portfolio.append(project)
    else:
        print(f"Manually removing fork: {project.get('title')}")

data['portfolio'] = new_portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Final count: {len(new_portfolio)}")
