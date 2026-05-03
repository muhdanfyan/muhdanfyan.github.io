
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'
forks_path = '/Users/pondokit/Herd/muhdanfyan.github.io/scratch/github_forks.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

with open(forks_path, 'r') as f:
    github_data = json.load(f)

fork_names = {repo['name'] for repo in github_data if repo['isFork']}

portfolio = data.get('portfolio', [])
original_count = len(portfolio)

# Filter out projects where slug or title matches a fork name
# We compare slug (lowercase) and title (converted to lowercase slug)
new_portfolio = []
for project in portfolio:
    slug = project.get('slug', '').lower()
    title_slug = project.get('title', '').lower().replace(' ', '-')
    
    is_fork = False
    for fork in fork_names:
        f_lower = fork.lower()
        if slug == f_lower or title_slug == f_lower or project.get('title', '').lower() == f_lower:
            is_fork = True
            break
    
    if not is_fork:
        new_portfolio.append(project)

data['portfolio'] = new_portfolio
removed_count = original_count - len(new_portfolio)

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Removed {removed_count} fork projects. Remaining: {len(new_portfolio)}")
if removed_count > 0:
    print("Removed projects:")
    for project in portfolio:
        if project not in new_portfolio:
            print(f"- {project.get('title')} ({project.get('slug')})")
