import json

def migrate():
    with open('all_sites_raw.json', 'r') as f:
        raw_sites = json.load(f)
    
    with open('data/manifest.json', 'r') as f:
        manifest = json.load(f)
    
    # Existing titles to avoid duplicates
    existing_urls = {p['url'].rstrip('/') for p in manifest['portfolio']}
    
    new_portfolios = []
    for site in raw_sites:
        url = site.get('ssl_url') or site.get('url')
        if not url: continue
        
        clean_url = url.rstrip('/')
        if clean_url in existing_urls: continue
        
        # Format the name
        name = site.get('name', 'Project').replace('-', ' ').title()
        
        new_portfolios.append({
            "title": name,
            "title_en": name,
            "category": "Web App",
            "image": site.get('screenshot_url', 'img/screenshots/default.png'),
            "url": url,
            "description": f"Digital project: {name}. Deployed via Netlify.",
            "description_en": f"Digital project: {name}. Deployed via Netlify.",
            "available_langs": ["id", "en"]
        })
        existing_urls.add(clean_url)
    
    manifest['portfolio'].extend(new_portfolios)
    
    with open('data/manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Successfully migrated {len(new_portfolios)} new projects. Total projects: {len(manifest['portfolio'])}")

if __name__ == "__main__":
    migrate()
