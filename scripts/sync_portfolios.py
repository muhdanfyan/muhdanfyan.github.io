import json
import subprocess
import os

def get_netlify_sites():
    print("Fetching sites from Netlify...")
    try:
        # We already have a cached version from previous step, but let's try to get fresh if possible
        # result = subprocess.run(['netlify', 'sites:list', '--json'], capture_output=True, text=True)
        # if result.returncode == 0:
        #    return json.loads(result.stdout)
        
        # Fallback to the file we just created if it exists
        if os.path.exists('scratch/netlify_sites.json'):
            with open('scratch/netlify_sites.json', 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error fetching Netlify sites: {e}")
    return []

def get_vercel_sites():
    print("Fetching sites from Vercel (limited support)...")
    # Vercel CLI is harder to parse without --json, but we can try to get the list
    # For now, let's look for existing vercel_sites.json or skip
    if os.path.exists('scratch/vercel_sites.json'):
        try:
            with open('scratch/vercel_sites.json', 'r') as f:
                return json.load(f)
        except:
            pass
    return []

def sync():
    netlify_sites = get_netlify_sites()
    vercel_sites = get_vercel_sites()
    
    with open('data/manifest.json', 'r') as f:
        manifest = json.load(f)
    
    existing_urls = {p['url'].rstrip('/') for p in manifest['portfolio']}
    new_count = 0
    
    # Process Netlify
    for site in netlify_sites:
        url = site.get('ssl_url') or site.get('url')
        if not url: continue
        
        clean_url = url.rstrip('/')
        if clean_url in existing_urls: continue
        
        name = site.get('name', 'Project').replace('-', ' ').title()
        manifest['portfolio'].append({
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
        new_count += 1

    # Save manifest
    with open('data/manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Sync complete! Added {new_count} new projects. Total: {len(manifest['portfolio'])}")

if __name__ == "__main__":
    sync()
