
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'
forks_path = '/Users/pondokit/Herd/muhdanfyan.github.io/scratch/github_forks.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

with open(forks_path, 'r') as f:
    github_data = json.load(f)

# Create a set of fork names in various formats
fork_names = set()
for repo in github_data:
    if repo['isFork']:
        name = repo['name'].lower()
        fork_names.add(name)
        fork_names.add(name.replace('-', ''))
        fork_names.add(name.replace('-', ' '))

portfolio = data.get('portfolio', [])
original_count = len(portfolio)

new_portfolio = []
removed_projects = []

for project in portfolio:
    slug = project.get('slug', '').lower()
    title = project.get('title', '').lower()
    title_slug = title.replace(' ', '-')
    title_compact = title.replace(' ', '')
    
    is_fork = False
    for fork in fork_names:
        if slug == fork or title == fork or title_slug == fork or title_compact == fork:
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
