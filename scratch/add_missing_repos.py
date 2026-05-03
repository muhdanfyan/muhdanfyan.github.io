
import json
import os

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'
github_repos_path = '/Users/pondokit/Herd/muhdanfyan.github.io/scratch/github_repos_full.json'
forks_path = '/Users/pondokit/Herd/muhdanfyan.github.io/scratch/github_forks.json'

with open(manifest_path, 'r') as f:
    manifest_data = json.load(f)

with open(github_repos_path, 'r') as f:
    github_repos = json.load(f)

with open(forks_path, 'r') as f:
    forks_data = json.load(f)

fork_names = {repo['name'] for repo in forks_data if repo['isFork']}
manifest_slugs = {str(p.get('slug') or '').lower() for p in manifest_data['portfolio']}
manifest_titles = {str(p.get('title') or '').lower() for p in manifest_data['portfolio']}

added_count = 0
portfolio = manifest_data['portfolio']

for repo in github_repos:
    name = repo['name']
    name_lower = name.lower()
    
    # Skip forks
    if name in fork_names:
        continue
        
    # Skip if already in manifest
    if name_lower in manifest_slugs or name_lower in manifest_titles:
        continue
    
    # Categorize
    slug = name_lower
    project_type = 'Personal/Education'
    difficulty_level = 'Intermediate'
    difficulty_score = 80
    
    if any(kw in slug for kw in ['retribusi', 'simpad', 'baubau', 'lurah', 'pajak']):
        project_type = 'Government'
        difficulty_level = 'Expert'
        difficulty_score = 95
    elif any(kw in slug for kw in ['onecreative', 'kassa', 'umkm', 'barber', 'fnb']):
        project_type = 'UMKM'
        difficulty_level = 'Advanced'
        difficulty_score = 88
    elif any(kw in slug for kw in ['mbg', 'siakad', 'simrs', 'hospital', 'clinic', 'hrd']):
        project_type = 'Corporate'
        difficulty_level = 'Advanced'
        difficulty_score = 90
    elif any(kw in slug for kw in ['aindea', 'ai', 'bot', 'security', 'pentest', 'research']):
        project_type = 'Personal/Research'
        difficulty_level = 'Advanced'
        difficulty_score = 92

    # Prepare entry
    new_project = {
        "slug": slug,
        "title": name.replace('-', ' ').title(),
        "title_en": name.replace('-', ' ').title(),
        "year": repo['updatedAt'][:4],
        "category": "Repository",
        "category_en": "Repository",
        "available_langs": ["id", "en"],
        "image": None,
        "description": repo.get('description') or f"Digital project: {name}.",
        "description_en": repo.get('description') or f"Digital project: {name}.",
        "url": repo.get('homepageUrl') or repo['url'],
        "project_type": project_type,
        "difficulty_level": difficulty_level,
        "difficulty_score": difficulty_score
    }
    
    portfolio.append(new_project)
    added_count += 1

manifest_data['portfolio'] = portfolio

with open(manifest_path, 'w') as f:
    json.dump(manifest_data, f, indent=2)

print(f"Added {added_count} missing projects to manifest.")
