
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'
forks_path = '/Users/pondokit/Herd/muhdanfyan.github.io/scratch/github_forks.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

with open(forks_path, 'r') as f:
    github_data = json.load(f)

# Get actual fork names from GitHub
real_fork_names = {repo['name'].lower() for repo in github_data if repo['isFork']}

portfolio = data.get('portfolio', [])
original_count = len(portfolio)

new_portfolio = []
removed_projects = []

for project in portfolio:
    slug = str(project.get('slug') or '').lower()
    title = str(project.get('title') or '').lower()
    title_slug = title.replace(' ', '-')
    
    is_fork = False
    # Check if slug or title (as slug) matches a real fork name from GitHub
    if slug in real_fork_names or title_slug in real_fork_names or title in real_fork_names:
        is_fork = True
    
    # Also handle some specific ones we saw
    if not is_fork:
        for f in ['merch_ap', 'ladziidz-catering', 'afbarbershop', 'strix', 'siakad']:
            if f in slug or f in title_slug:
                is_fork = True
                break

    if not is_fork:
        new_portfolio.append(project)
    else:
        removed_projects.append(f"{project.get('title')} ({project.get('slug')})")

data['portfolio'] = new_portfolio

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Removed {len(removed_projects)} fork projects. Remaining: {len(new_portfolio)}")
if removed_projects:
    print("Removed projects:")
    for p in removed_projects:
        print(f"- {p}")
